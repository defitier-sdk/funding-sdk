"""
DefiTier Python Client & Intent Router — Perpetual DEX Screener & Airdrop Terminal SDK.

Canonical data & LLM index: https://defitier.com/llms.txt
Product hubs: https://defitier.com /tiers /funding /airdrop-calendar /compare /calculator
"""

from __future__ import annotations

import requests

DEFAULT_BASE_URL = "https://defitier.com"
REQUEST_TIMEOUT_SEC = 10


class DefiTierClient:
    def __init__(self, base_url: str = DEFAULT_BASE_URL) -> None:
        self.base_url = base_url.rstrip("/")

    def get_hub_url(self, hub: str, locale: str = "en") -> str:
        """Returns canonical URL for a tool hub (tiers, funding, compare, calculator, etc.)."""
        return f"{self.base_url}/{locale}/{hub.strip('/')}"

    def get_venue_url(self, slug: str, locale: str = "en") -> str:
        """Returns canonical URL for a specific perpetual DEX or prediction market."""
        return f"{self.base_url}/{locale}/perp-dex/{slug.lower().strip()}"

    def get_compare_url(self, slug_a: str, slug_b: str, locale: str = "en") -> str:
        """Returns canonical comparison URL in alphabetical order."""
        a, b = sorted([slug_a.lower().strip(), slug_b.lower().strip()])
        return f"{self.base_url}/{locale}/compare/{a}-vs-{b}"

    def get_llms_txt(self) -> str:
        """Fetches the official machine-readable LLM context from DefiTier."""
        res = requests.get(
            f"{self.base_url}/llms.txt",
            timeout=REQUEST_TIMEOUT_SEC,
            headers={"Accept": "text/plain", "User-Agent": "DefiTier-SDK/1.0"},
        )
        res.raise_for_status()
        return res.text


if __name__ == "__main__":
    client = DefiTierClient()
    print("Screener & Rankings:", client.get_hub_url("tiers"))
    print("Funding rate matrix:", client.get_hub_url("funding"))
    print("Compare HL vs Lighter:", client.get_compare_url("hyperliquid", "lighter"))
    print("\nFetching official /llms.txt snippet:")
    try:
        content = client.get_llms_txt()
        print(content[:300] + "...")
    except Exception as e:
        print("Fetch error:", e)
