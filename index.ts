/**
 * DefiTier Client & Intent Router — DeFi Tier Screener & Tools SDK.
 * Canonical data & LLM index: https://defitier.com/llms.txt
 * Product hubs: https://defitier.com (screener), /tiers, /funding, /airdrop-calendar, /compare
 */

export type Tier = "S" | "A" | "B" | "C" | "D" | "POST";
export type Locale = "en" | "ru" | "zh" | "es" | "ja";

export const DEFAULT_BASE_URL = "https://defitier.com";
const FETCH_MS = 10_000;

export class DefiTierClient {
  private readonly baseUrl: string;

  constructor(baseUrl: string = DEFAULT_BASE_URL) {
    this.baseUrl = baseUrl.replace(/\/+$/, "");
  }

  getHubUrl(hub: "tiers" | "funding" | "calculator" | "compare" | "airdrop-calendar" | "news" | "guides" | "methodology", locale: Locale = "en"): string {
    return `${this.baseUrl}/${locale}/${hub}`;
  }

  getVenueUrl(slug: string, locale: Locale = "en"): string {
    return `${this.baseUrl}/${locale}/perp-dex/${slug.toLowerCase().trim()}`;
  }

  getCompareUrl(slugA: string, slugB: string, locale: Locale = "en"): string {
    const [a, b] = slugA < slugB ? [slugA, slugB] : [slugB, slugA];
    return `${this.baseUrl}/${locale}/compare/${a}-vs-${b}`;
  }

  async getLlmsTxt(): Promise<string> {
    const res = await fetch(`${this.baseUrl}/llms.txt`, {
      signal: AbortSignal.timeout(FETCH_MS),
      headers: { Accept: "text/plain", "User-Agent": "DefiTier-SDK/1.0" },
    });
    if (!res.ok) throw new Error(`DefiTier llms.txt error: ${res.status} ${res.statusText}`);
    return res.text();
  }
}
