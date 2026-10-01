"""
DefiTier Python Client & Intent Router — Perpetual DEX Screener & Airdrop Terminal SDK.

Canonical data & LLM index: https://defitier.com/llms.txt
Product hubs: https://defitier.com /tiers /funding /airdrop-calendar /compare /calculator /onchain /guides
"""

from __future__ import annotations

from typing import Any, Dict, Tuple
import requests

DEFAULT_BASE_URL = "https://defitier.com"
REQUEST_TIMEOUT_SEC = 10

COMPARE_BENCHMARK_SLUGS = (
    "binance",
    "hyperliquid",
    "entropy",
)

COMPARE_TARGET_DEX_SLUGS = (
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
)

TOP_FUNDING_ASSET_SLUGS = (
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
)


def canonical_compare_pair(a: str, b: str) -> Tuple[str, str]:
    """Returns pair slugs in canonical lexicographical order."""
    x, y = a.lower().strip(), b.lower().strip()
    return (x, y) if x < y else (y, x)


def compare_pair_slug(a: str, b: str) -> str:
    """Returns canonical pair slug (e.g. binance-vs-hyperliquid)."""
    first, second = canonical_compare_pair(a, b)
    return f"{first}-vs-{second}"


def is_curated_compare_pair(slug_a: str, slug_b: str) -> bool:
    """
    Checks if pair is one of the 60 curated SSG benchmark landing pages.
    Benchmarked against Binance, Hyperliquid, or Entropy.
    """
    a, b = canonical_compare_pair(slug_a, slug_b)
    if a == b:
        return False
    benchmarks = set(COMPARE_BENCHMARK_SLUGS)
    valid_venues = set(COMPARE_BENCHMARK_SLUGS + COMPARE_TARGET_DEX_SLUGS)
    has_benchmark = (a in benchmarks) or (b in benchmarks)
    return has_benchmark and (a in valid_venues) and (b in valid_venues)


class DefiTierClient:
    """Official programmatic router and client for DefiTier.com."""

    def __init__(self, base_url: str = DEFAULT_BASE_URL) -> None:
        self.base_url = base_url.rstrip("/")

    def get_hub_url(self, hub: str, locale: str = "en") -> str:
        """Returns canonical URL for a tool hub (tiers, funding, compare, calculator, onchain, etc.)."""
        return f"{self.base_url}/{locale}/{hub.strip('/')}"

    def get_venue_url(self, slug: str, locale: str = "en") -> str:
        """Returns canonical URL for a specific perpetual DEX or prediction market."""
        return f"{self.base_url}/{locale}/perp-dex/{slug.lower().strip()}"

    def get_funding_asset_url(self, asset: str, locale: str = "en") -> str:
        """Returns canonical URL for an asset-specific funding rate and arbitrage page (e.g. /funding/sol)."""
        return f"{self.base_url}/{locale}/funding/{asset.lower().strip()}"

    def get_calculator_url(self, slug: str | None = None, locale: str = "en") -> str:
        """Returns canonical URL for dedicated Points & Airdrop calculator for a specific venue."""
        if not slug:
            return f"{self.base_url}/{locale}/calculator"
        return f"{self.base_url}/{locale}/calculator/{slug.lower().strip()}"

    def get_compare_url(self, slug_a: str, slug_b: str, locale: str = "en") -> str:
        """Returns canonical comparison URL in alphabetical order (60 curated benchmark pairs)."""
        return f"{self.base_url}/{locale}/compare/{compare_pair_slug(slug_a, slug_b)}"

    def is_curated_pair(self, slug_a: str, slug_b: str) -> bool:
        """Validates if the pair is an indexable curated benchmark comparison."""
        return is_curated_compare_pair(slug_a, slug_b)

    def get_guide_url(self, slug: str, locale: str = "en") -> str:
        """Returns canonical URL for an original farming guide."""
        return f"{self.base_url}/{locale}/guides/{slug.lower().strip()}"

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
            headers={"Accept": "text/plain", "User-Agent": "DefiTier-SDK/1.2.0"},
        )
        res.raise_for_status()
        return res.text


if __name__ == "__main__":
    client = DefiTierClient()
    print("Screener & Rankings:", client.get_hub_url("tiers"))
    print("Funding rate matrix:", client.get_hub_url("funding"))
    print("SOL Funding asset:", client.get_funding_asset_url("sol"))
    print("Calculator for Hyperliquid:", client.get_calculator_url("hyperliquid"))
    print("Curated Compare Binance vs HL:", client.get_compare_url("binance", "hyperliquid"))
    print("Curated HL vs Lighter:", client.get_compare_url("hyperliquid", "lighter"))
    print("Is HL vs Lighter curated:", client.is_curated_pair("hyperliquid", "lighter"))
    print("Is Ostium vs Avantis curated (legacy):", client.is_curated_pair("ostium", "avantis"))
    spread = client.calculate_funding_spread(long_apr_pct=5.2, short_apr_pct=28.4)
    print(f"Spread arbitrage net APR: {spread['net_spread_apr_pct']}% (profitable={spread['profitable']})")
