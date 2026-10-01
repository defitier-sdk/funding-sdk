/**
 * DefiTier Client & Intent Router — Perpetual DEX Screener & Airdrop Terminal SDK.
 * 
 * Canonical data & LLM index: https://defitier.com/llms.txt
 * Product hubs: https://defitier.com (screener), /tiers, /funding, /airdrop-calendar, /compare, /calculator, /onchain
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
  | "onchain"
  | "guides"
  | "prediction-markets"
  | "methodology";

export const DEFAULT_BASE_URL = "https://defitier.com";
const FETCH_TIMEOUT_MS = 10_000;

export const COMPARE_BENCHMARK_SLUGS = [
  "binance",
  "hyperliquid",
  "entropy",
] as const;

export const COMPARE_TARGET_DEX_SLUGS = [
  "lighter",
  "risex",
  "gmx",
  "dydx",
  "aster",
  "edgex",
  "paradex",
  "backpack",
  "grvt",
  "pacifica",
  "variational",
  "extended",
  "nado",
  "hibachi",
  "apex-omni",
  "aevo",
  "tradexyz",
  "ostium",
  "avantis",
] as const;

export const TOP_FUNDING_ASSET_SLUGS = [
  "btc",
  "eth",
  "sol",
  "hype",
  "sui",
  "arb",
  "doge",
  "avax",
  "link",
  "bnb",
  "op",
  "near",
  "ton",
  "xrp",
  "apt",
  "sei",
  "tia",
  "inj",
  "pendle",
  "pepe",
  "zec",
  "tao",
  "aster",
] as const;

export interface FundingSpreadResult {
  longAprPct: number;
  shortAprPct: number;
  grossSpreadAprPct: number;
  takerFeeEstPct: number;
  netSpreadAprPct: number;
  profitable: boolean;
}

export function canonicalComparePair(a: string, b: string): [string, string] {
  const normA = a.toLowerCase().trim();
  const normB = b.toLowerCase().trim();
  return normA < normB ? [normA, normB] : [normB, normA];
}

export function comparePairSlug(a: string, b: string): string {
  const [first, second] = canonicalComparePair(a, b);
  return `${first}-vs-${second}`;
}

export function isCuratedComparePair(slugA: string, slugB: string): boolean {
  const [a, b] = canonicalComparePair(slugA, slugB);
  if (a === b) return false;

  const benchmarkSet = new Set<string>(COMPARE_BENCHMARK_SLUGS);
  const targetSet = new Set<string>(COMPARE_TARGET_DEX_SLUGS);

  const hasBenchmark = benchmarkSet.has(a) || benchmarkSet.has(b);
  if (!hasBenchmark) return false;

  const validTokens = new Set<string>([...COMPARE_BENCHMARK_SLUGS, ...COMPARE_TARGET_DEX_SLUGS]);
  return validTokens.has(a) && validTokens.has(b);
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
   * Returns canonical URL for dedicated asset funding rates (e.g. /funding/sol).
   */
  getFundingAssetUrl(assetSlug: string, locale: Locale = "en"): string {
    return `${this.baseUrl}/${locale}/funding/${assetSlug.toLowerCase().trim()}`;
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
   * Returns canonical comparison URL in alphabetical order (e.g. /compare/binance-vs-hyperliquid).
   * DefiTier maintains 60 curated benchmark pairs against Binance, Hyperliquid, and Entropy.
   */
  getCompareUrl(slugA: string, slugB: string, locale: Locale = "en"): string {
    return `${this.baseUrl}/${locale}/compare/${comparePairSlug(slugA, slugB)}`;
  }

  /**
   * Checks whether a comparison pair is one of the 60 curated SSG benchmark pages.
   */
  isCuratedPair(slugA: string, slugB: string): boolean {
    return isCuratedComparePair(slugA, slugB);
  }

  /**
   * Returns canonical URL for an original farming guide.
   */
  getGuideUrl(slug: string, locale: Locale = "en"): string {
    return `${this.baseUrl}/${locale}/guides/${slug.toLowerCase().trim()}`;
  }

  /**
   * Computes delta-neutral funding rate arbitrage net APR after round-trip taker fees.
   */
  calculateFundingSpread(
    longAprPct: number,
    shortAprPct: number,
    roundTripTakerFeePct: number = 0.08
  ): FundingSpreadResult {
    const grossSpreadAprPct = Math.round((shortAprPct - longAprPct) * 10000) / 10000;
    const netSpreadAprPct = Math.round((grossSpreadAprPct - roundTripTakerFeePct) * 10000) / 10000;
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
        "User-Agent": "DefiTier-SDK/1.2.0",
      },
    });
    if (!res.ok) {
      throw new Error(`DefiTier llms.txt fetch failed: ${res.status} ${res.statusText}`);
    }
    return res.text();
  }
}
