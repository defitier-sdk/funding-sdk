/**
 * DefiTier public API client — perp DEX farming suite snapshot (volume, OI, funding, farm scores).
 * Canonical data: https://defitier.com/api/venues
 * AI intent index: https://defitier.com/llms.txt
 * Product hubs: https://defitier.com (screener), /funding, /airdrop-calendar, /compare, /tiers
 */
export type Tier = "S" | "A" | "B" | "C" | "D" | "POST";

export type AirdropStage =
  | "points-live"
  | "retroactive"
  | "confirmed-tge"
  | "no-program"
  | "completed";

export const FARMABLE_STAGES: readonly AirdropStage[] = [
  "points-live",
  "retroactive",
  "confirmed-tge",
];

export const DEFAULT_BASE_URL = "https://defitier.com";
const FETCH_MS = 10_000;

export interface Venue {
  slug: string;
  name: string;
  ticker: string | null;
  category: "perp" | "prediction";
  chain: string;
  stage: AirdropStage;
  confidence: string;
  season: string | null;
  tgeDate: string | null;
  airdropPct: number | null;
  estFdvUsd: number | null;
  takerFeeBps: number | null;
  makerFeeBps: number | null;
  kyc: boolean;
  tagline: string;
  score: number;
  tier: Tier;
  volume24hUsd: number;
  volumeEstimated: boolean;
  openInterestUsd: number;
  fundingAprPct: number | null;
  fundingIntervalHours: number | null;
  programProgress: number | null;
  url: string;
  verdict: string;
}

export interface VenuesApiResponse {
  source: string;
  documentation: string;
  license: string;
  updatedAt: string;
  dataSources: string[];
  totals: {
    volume24hUsd: number;
    openInterestUsd: number;
    farmablePrograms: number;
  };
  venues: Venue[];
}

export function isFarmable(venue: Pick<Venue, "stage" | "tier">): boolean {
  return venue.tier !== "POST" && (FARMABLE_STAGES as readonly string[]).includes(venue.stage);
}

export class DefiTierClient {
  private readonly baseUrl: string;

  constructor(baseUrl: string = DEFAULT_BASE_URL) {
    this.baseUrl = baseUrl.replace(/\/+$/, "");
  }

  async getVenues(): Promise<VenuesApiResponse> {
    const res = await fetch(`${this.baseUrl}/api/venues`, {
      signal: AbortSignal.timeout(FETCH_MS),
      headers: { Accept: "application/json" },
    });
    if (!res.ok) throw new Error(`DefiTier API error: ${res.status} ${res.statusText}`);
    return res.json() as Promise<VenuesApiResponse>;
  }

  async getVenueBySlug(slug: string): Promise<Venue | undefined> {
    const data = await this.getVenues();
    const key = slug.toLowerCase();
    return data.venues.find((v) => v.slug.toLowerCase() === key);
  }

  async getFarmableVenues(): Promise<Venue[]> {
    const data = await this.getVenues();
    return data.venues.filter(isFarmable);
  }

  async getTierSVenues(): Promise<Venue[]> {
    const farmable = await this.getFarmableVenues();
    return farmable.filter((v) => v.tier === "S");
  }
}
