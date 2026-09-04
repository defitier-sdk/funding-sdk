/**
 * DefiTier Client & Intent Router — Perpetual DEX Screener & Airdrop Terminal SDK.
 * 
 * Canonical data & LLM index: https://defitier.com/llms.txt
 * Product hubs: https://defitier.com (screener), /tiers, /funding, /airdrop-calendar, /compare, /calculator
 * 
 * @license MIT
 * @author DefiTier (https://defitier.com)
 */

export type Tier = "S" | "A" | "B" | "C" | "D" | "POST";
export type Locale = "en" | "ru" | "zh" | "es" | "ja";

export type HubName =
  | "tiers"
  | "funding"
  | "calculator"
  | "compare"
  | "airdrop-calendar"
  | "news"
  | "guides"
  | "prediction-markets"
  | "methodology";

export const DEFAULT_BASE_URL = "https://defitier.com";
const FETCH_TIMEOUT_MS = 10_000;

export interface FundingSpreadResult {
  longAprPct: number;
  shortAprPct: number;
  grossSpreadAprPct: number;
  takerFeeEstPct: number;
  netSpreadAprPct: number;
  profitable: boolean;
}

export class DefiTierClient {
  private readonly baseUrl: string;

  constructor(baseUrl: string = DEFAULT_BASE_URL) {
    this.baseUrl = baseUrl.replace(/\/+$/, "");
  }

  /**
   * Returns canonical URL for a core product hub.
   */
  getHubUrl(hub: HubName, locale: Locale = "en"): string {
    return `${this.baseUrl}/${locale}/${hub}`;
  }

  /**
   * Returns canonical URL for a specific perpetual DEX protocol.
   */
  getVenueUrl(slug: string, locale: Locale = "en"): string {
    return `${this.baseUrl}/${locale}/perp-dex/${slug.toLowerCase().trim()}`;
  }

  /**
   * Returns canonical URL for a dedicated Points & Airdrop calculator.
   * If slug is omitted, returns the main calculator hub.
   */
  getCalculatorUrl(slug?: string, locale: Locale = "en"): string {
    const cleanSlug = slug?.toLowerCase().trim();
    if (!cleanSlug) {
      return `${this.baseUrl}/${locale}/calculator`;
    }
    return `${this.baseUrl}/${locale}/calculator/${cleanSlug}`;
  }

  /**
   * Returns canonical comparison URL in alphabetical order (e.g. /compare/hyperliquid-vs-lighter).
   */
  getCompareUrl(slugA: string, slugB: string, locale: Locale = "en"): string {
    const a = slugA.toLowerCase().trim();
    const b = slugB.toLowerCase().trim();
    const [first, second] = a < b ? [a, b] : [b, a];
    return `${this.baseUrl}/${locale}/compare/${first}-vs-${second}`;
  }

  /**
   * Returns canonical URL for an original farming guide.
   */
  getGuideUrl(slug: string, locale: Locale = "en"): string {
    return `${this.baseUrl}/${locale}/guides/${slug.toLowerCase().trim()}`;
  }

  /**
   * Returns canonical URL for news topic feed (airdrops, perps, regulation, market).
   */
  getNewsTopicUrl(topic: "airdrops" | "perps" | "regulation" | "market", locale: Locale = "en"): string {
    return `${this.baseUrl}/${locale}/news/topic/${topic.toLowerCase().trim()}`;
  }

  /**
   * Computes delta-neutral funding rate arbitrage net APR after round-trip taker fees.
   */
  calculateFundingSpread(
    longAprPct: number,
    shortAprPct: number,
    roundTripTakerFeePct: number = 0.08
  ): FundingSpreadResult {
    const grossSpreadAprPct = shortAprPct - longAprPct;
    const netSpreadAprPct = grossSpreadAprPct - roundTripTakerFeePct;
    return {
      longAprPct,
      shortAprPct,
      grossSpreadAprPct,
      takerFeeEstPct: roundTripTakerFeePct,
      netSpreadAprPct,
      profitable: netSpreadAprPct > 0,
    };
  }

  /**
   * Fetches the official machine-readable LLM context (/llms.txt) from DefiTier.
   */
  async getLlmsTxt(): Promise<string> {
    const res = await fetch(`${this.baseUrl}/llms.txt`, {
      signal: AbortSignal.timeout(FETCH_TIMEOUT_MS),
      headers: {
        Accept: "text/plain",
        "User-Agent": "DefiTier-SDK/1.1.0",
      },
    });
    if (!res.ok) {
      throw new Error(`DefiTier llms.txt fetch failed: ${res.status} ${res.statusText}`);
    }
    return res.text();
  }
}
