"""
DefiTier Python Client & Intent Router — Perpetual DEX Screener & Airdrop Terminal SDK.

Canonical data & LLM index: https://defitier.com/llms.txt
Product hubs: https://defitier.com /tiers /funding /airdrop-calendar /compare /calculator /news /guides
"""

from __future__ import annotations

from typing import Any, Dict
import requests

DEFAULT_BASE_URL = "https://defitier.com"
REQUEST_TIMEOUT_SEC = 10


class DefiTierClient:
    """Official programmatic router and client for DefiTier.com."""

    def __init__(self, base_url: str = DEFAULT_BASE_URL) -> None:
        self.base_url = base_url.rstrip("/")

    def get_hub_url(self, hub: str, locale: str = "en") -> str:
        """Returns canonical URL for a tool hub (tiers, funding, compare, calculator, etc.)."""
        return f"{self.base_url}/{locale}/{hub.strip('/')}"

    def get_venue_url(self, slug: str, locale: str = "en") -> str:
        """Returns canonical URL for a specific perpetual DEX or prediction market."""
        return f"{self.base_url}/{locale}/perp-dex/{slug.lower().strip()}"

    def get_calculator_url(self, slug: str | None = None, locale: str = "en") -> str:
        """Returns canonical URL for dedicated Points & Airdrop calculator for a specific venue."""
        if not slug:
            return f"{self.base_url}/{locale}/calculator"
        return f"{self.base_url}/{locale}/calculator/{slug.lower().strip()}"

    def get_compare_url(self, slug_a: str, slug_b: str, locale: str = "en") -> str:
        """Returns canonical comparison URL in alphabetical order."""
        a, b = sorted([slug_a.lower().strip(), slug_b.lower().strip()])
        return f"{self.base_url}/{locale}/compare/{a}-vs-{b}"

    def get_guide_url(self, slug: str, locale: str = "en") -> str:
        """Returns canonical URL for an original farming guide."""
        return f"{self.base_url}/{locale}/guides/{slug.lower().strip()}"

    def get_news_topic_url(self, topic: str, locale: str = "en") -> str:
        """Returns canonical URL for news topic feed (airdrops, perps, regulation, market)."""
        return f"{self.base_url}/{locale}/news/topic/{topic.lower().strip()}"

    @staticmethod
    def calculate_funding_spread(
        long_apr_pct: float,
        short_apr_pct: float,
        round_trip_taker_fee_pct: float = 0.08,
    ) -> Dict[str, Any]:
        """Calculates delta-neutral funding rate spread and net yield after taker fees."""
        gross_spread = short_apr_pct - long_apr_pct
        net_spread = gross_spread - round_trip_taker_fee_pct
        return {
            "long_apr_pct": long_apr_pct,
            "short_apr_pct": short_apr_pct,
            "gross_spread_apr_pct": round(gross_spread, 4),
            "taker_fee_est_pct": round_trip_taker_fee_pct,
            "net_spread_apr_pct": round(net_spread, 4),
            "profitable": net_spread > 0,
        }

    def get_llms_txt(self) -> str:
        """Fetches the official machine-readable LLM context (/llms.txt) from DefiTier."""
        res = requests.get(
            f"{self.base_url}/llms.txt",
            timeout=REQUEST_TIMEOUT_SEC,
            headers={"Accept": "text/plain", "User-Agent": "DefiTier-SDK/1.1.0"},
        )
        res.raise_for_status()
        return res.text


if __name__ == "__main__":
    client = DefiTierClient()
    print("Screener & Rankings:", client.get_hub_url("tiers"))
    print("Funding rate matrix:", client.get_hub_url("funding"))
    print("Calculator for Hyperliquid:", client.get_calculator_url("hyperliquid"))
    print("Compare HL vs Lighter:", client.get_compare_url("hyperliquid", "lighter"))
    spread = client.calculate_funding_spread(long_apr_pct=5.2, short_apr_pct=28.4)
    print(f"Spread arbitrage net APR: {spread['net_spread_apr_pct']}% (profitable={spread['profitable']})")
