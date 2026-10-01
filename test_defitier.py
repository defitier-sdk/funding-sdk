import unittest
from defitier import (
    DefiTierClient,
    canonical_compare_pair,
    compare_pair_slug,
    is_curated_compare_pair,
    COMPARE_BENCHMARK_SLUGS,
    COMPARE_TARGET_DEX_SLUGS,
    TOP_FUNDING_ASSET_SLUGS,
)


class DefiTierClientTests(unittest.TestCase):
    def setUp(self):
        self.client = DefiTierClient()

    def test_canonical_hubs(self):
        self.assertEqual(self.client.get_hub_url("tiers"), "https://defitier.com/en/tiers")
        self.assertEqual(self.client.get_hub_url("funding"), "https://defitier.com/en/funding")
        self.assertEqual(self.client.get_hub_url("compare"), "https://defitier.com/en/compare")
        self.assertEqual(self.client.get_hub_url("calculator"), "https://defitier.com/en/calculator")
        self.assertEqual(self.client.get_hub_url("airdrop-calendar"), "https://defitier.com/en/airdrop-calendar")
        self.assertEqual(self.client.get_hub_url("onchain"), "https://defitier.com/en/onchain")
        self.assertEqual(self.client.get_hub_url("guides"), "https://defitier.com/en/guides")

    def test_localized_routes(self):
        self.assertEqual(self.client.get_hub_url("tiers", "ru"), "https://defitier.com/ru/tiers")
        self.assertEqual(self.client.get_hub_url("funding", "zh"), "https://defitier.com/zh/funding")
        self.assertEqual(self.client.get_hub_url("compare", "es"), "https://defitier.com/es/compare")
        self.assertEqual(self.client.get_hub_url("calculator", "ja"), "https://defitier.com/ja/calculator")

    def test_funding_asset_urls(self):
        self.assertEqual(self.client.get_funding_asset_url("sol"), "https://defitier.com/en/funding/sol")
        self.assertEqual(self.client.get_funding_asset_url("BTC"), "https://defitier.com/en/funding/btc")
        self.assertEqual(self.client.get_funding_asset_url("hype", "ru"), "https://defitier.com/ru/funding/hype")
        self.assertIn("sol", TOP_FUNDING_ASSET_SLUGS)
        self.assertIn("btc", TOP_FUNDING_ASSET_SLUGS)
        self.assertEqual(len(TOP_FUNDING_ASSET_SLUGS), 23)

    def test_compare_canonical_slugs(self):
        self.assertEqual(canonical_compare_pair("hyperliquid", "binance"), ("binance", "hyperliquid"))
        self.assertEqual(compare_pair_slug("lighter", "hyperliquid"), "hyperliquid-vs-lighter")
        self.assertEqual(
            self.client.get_compare_url("lighter", "hyperliquid"),
            "https://defitier.com/en/compare/hyperliquid-vs-lighter",
        )

    def test_curated_compare_matrix(self):
        # Benchmark vs benchmark
        self.assertTrue(is_curated_compare_pair("binance", "hyperliquid"))
        self.assertTrue(is_curated_compare_pair("binance", "entropy"))
        self.assertTrue(is_curated_compare_pair("entropy", "hyperliquid"))

        # Benchmark vs Target DEX
        self.assertTrue(is_curated_compare_pair("binance", "lighter"))
        self.assertTrue(is_curated_compare_pair("hyperliquid", "aster"))
        self.assertTrue(is_curated_compare_pair("entropy", "pacifica"))
        self.assertTrue(is_curated_compare_pair("hyperliquid", "variational"))

        # Non-benchmark pairs should be False (these 308-redirect to /compare/)
        self.assertFalse(is_curated_compare_pair("ostium", "avantis"))
        self.assertFalse(is_curated_compare_pair("dydx", "gmx"))
        self.assertFalse(is_curated_compare_pair("lighter", "aster"))

        # Identical venues
        self.assertFalse(is_curated_compare_pair("hyperliquid", "hyperliquid"))

    def test_funding_spread_calculation(self):
        res = self.client.calculate_funding_spread(long_apr_pct=5.0, short_apr_pct=25.0, round_trip_taker_fee_pct=0.1)
        self.assertEqual(res["long_apr_pct"], 5.0)
        self.assertEqual(res["short_apr_pct"], 25.0)
        self.assertEqual(res["gross_spread_apr_pct"], 20.0)
        self.assertEqual(res["net_spread_apr_pct"], 19.9)
        self.assertTrue(res["profitable"])

        # Unprofitable case
        neg = self.client.calculate_funding_spread(long_apr_pct=20.0, short_apr_pct=10.0)
        self.assertFalse(neg["profitable"])
        self.assertLess(neg["net_spread_apr_pct"], 0)


if __name__ == "__main__":
    unittest.main()
