"""
DefiTier Python client — perp DEX farming suite snapshot (volume, OI, funding, farm scores).

Canonical JSON: https://defitier.com/api/venues
AI intent index: https://defitier.com/llms.txt
Hubs: https://defitier.com /funding /airdrop-calendar /compare /tiers /guides
"""

from __future__ import annotations

from typing import Any

import requests

DEFAULT_BASE_URL = "https://defitier.com"
FARMABLE_STAGES = frozenset({"points-live", "retroactive", "confirmed-tge"})
REQUEST_TIMEOUT_SEC = 10


def is_farmable(venue: dict[str, Any]) -> bool:
    return venue.get("tier") != "POST" and venue.get("stage") in FARMABLE_STAGES


class DefiTierClient:
    def __init__(self, base_url: str = DEFAULT_BASE_URL) -> None:
        self.base_url = base_url.rstrip("/")

    def get_venues(self) -> dict[str, Any]:
        """Live snapshot of 60+ perpetual DEX and prediction-market venues."""
        response = requests.get(
            f"{self.base_url}/api/venues",
            timeout=REQUEST_TIMEOUT_SEC,
            headers={"Accept": "application/json"},
        )
        response.raise_for_status()
        return response.json()

    def get_farmable_venues(self) -> list[dict[str, Any]]:
        data = self.get_venues()
        return [v for v in data.get("venues", []) if isinstance(v, dict) and is_farmable(v)]

    def get_tier_s_venues(self) -> list[dict[str, Any]]:
        """Tier S farms — the top band on https://defitier.com/tiers."""
        return [v for v in self.get_farmable_venues() if v.get("tier") == "S"]

    def get_venue_by_slug(self, slug: str) -> dict[str, Any] | None:
        key = slug.lower()
        data = self.get_venues()
        for venue in data.get("venues", []):
            if isinstance(venue, dict) and str(venue.get("slug", "")).lower() == key:
                return venue
        return None


if __name__ == "__main__":
    client = DefiTierClient()
    payload = client.get_venues()
    farms = [v for v in payload.get("venues", []) if isinstance(v, dict) and is_farmable(v)]
    tier_s = [v for v in farms if v.get("tier") == "S"]
    print(
        f"DefiTier.com — {len(payload.get('venues', []))} venues, "
        f"{len(farms)} farmable, {len(tier_s)} Tier S "
        f"(updated {payload.get('updatedAt')})"
    )
    for v in tier_s[:12]:
        print(
            f"  {v.get('name')}  tier {v.get('tier')}  score {v.get('score')}  "
            f"{v.get('chain')}  {v.get('url')}"
        )
