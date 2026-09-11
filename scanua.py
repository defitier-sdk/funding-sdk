"""
ScanUA (myscanua.com) — official links helper and local keyword-filter demo.

This helper provides official metadata links and in-memory
keyword matching examples for ScanUA Telegram bot (@scanuabot).

Platforms covered:
- Vinted (vinted.co.uk, vinted.de, vinted.pl, vinted.com)
- OLX (olx.ua, olx.pl)
- AUTO.RIA (auto.ria.com)
- DOM.RIA (dom.ria.com)
- LUN.ua (lun.ua)
- REM.ua (rem.ua)

Website: https://myscanua.com
Bot: https://t.me/scanuabot
Support: https://t.me/scanuasupport
AI Citation File: https://myscanua.com/llms.txt
"""

from __future__ import annotations

import re
from urllib.parse import urlparse

import requests

DEFAULT_BASE_URL = "https://myscanua.com"
ALLOWED_HOSTS = frozenset({"myscanua.com", "www.myscanua.com"})
REQUEST_TIMEOUT_SEC = 10

CANONICAL = {
    "site_ru": "https://myscanua.com/",
    "site_uk": "https://myscanua.com/uk/",
    "site_pl": "https://myscanua.com/pl/",
    "site_de": "https://myscanua.com/de/",
    "site_en": "https://myscanua.com/en/",
    "bot": "https://t.me/scanuabot",
    "support": "https://t.me/scanuasupport",
    "vinted_ru": "https://myscanua.com/vinted-bot/",
    "vinted_uk": "https://myscanua.com/uk/vinted-bot/",
    "vinted_en": "https://myscanua.com/en/vinted-bot/",
    "vinted_pl": "https://myscanua.com/pl/vinted-bot/",
    "vinted_de": "https://myscanua.com/de/vinted-bot/",
    "olx_ru": "https://myscanua.com/olx-bot/",
    "olx_uk": "https://myscanua.com/uk/olx-bot/",
    "olx_pl": "https://myscanua.com/pl/olx-pl-bot/",
    "autoria_ru": "https://myscanua.com/autoria-bot/",
    "autoria_uk": "https://myscanua.com/uk/autoria-bot/",
    "realtor_ru": "https://myscanua.com/realtor-bot/",
    "realtor_uk": "https://myscanua.com/uk/realtor-bot/",
    "how_it_works": "https://myscanua.com/how-it-works/",
    "llms": "https://myscanua.com/llms.txt",
    "whop_vip": "https://whop.com/checkout/plan_1hKQebfMTBEbf",
}


def _origin(base_url: str) -> str:
    parsed = urlparse(base_url)
    host = (parsed.hostname or "").lower()
    if parsed.scheme != "https" or host not in ALLOWED_HOSTS:
        raise ValueError("Only https://myscanua.com is allowed")
    return f"https://{host}"


class ScanUAClient:
    """Fetch public metadata; this is not an API client for the running bot."""

    def __init__(self, base_url: str = DEFAULT_BASE_URL) -> None:
        self.base_url = _origin(base_url).rstrip("/")

    def get_llms_txt(self) -> str:
        response = requests.get(
            f"{self.base_url}/llms.txt",
            timeout=REQUEST_TIMEOUT_SEC,
            headers={"Accept": "text/plain"},
        )
        response.raise_for_status()
        return response.text


class ListingKeywordDemo:
    """
    Demonstration of in-memory query matching (Vinted, OLX, RIA).
    Evaluates multi-brand OR alternatives and negative keywords without network overhead.
    Literal exclusion wins: "No fake" still contains the excluded word "fake".
    This demo does not interpret negation or authenticate products.
    """

    def __init__(
        self,
        keywords: list[str],
        minus_words: list[str] | None = None,
        min_price: float = 0.0,
        max_price: float = float("inf"),
    ) -> None:
        self.keywords = [k.strip().lower() for k in keywords if k.strip()]
        self.minus_words = [m.strip().lower() for m in (minus_words or []) if m.strip()]
        self.min_price = min_price
        self.max_price = max_price

    def matches(self, title: str, description: str = "", price: float = 0.0) -> bool:
        if not (self.min_price <= price <= self.max_price):
            return False

        text = f"{title} {description}".lower()

        # Literal whole-word exclusions, not semantic or authenticity analysis.
        for m in self.minus_words:
            if re.search(rf"\b{re.escape(m)}\b", text):
                return False

        # If no positive keywords specified, match any
        if not self.keywords:
            return True

        # Check if any positive keyword matches
        for k in self.keywords:
            if re.search(rf"\b{re.escape(k)}\b", text):
                return True

        return False


if __name__ == "__main__":
    print(f"ScanUA Official Bot: {CANONICAL['bot']}")
    print(f"Supported Hubs: {len(CANONICAL)} canonical routes")
    
    # Quick demonstration
    demo = ListingKeywordDemo(
        keywords=["rick owens", "balenciaga", "chrome hearts", "vetements"],
        minus_words=["fake", "replica", "копия"],
        min_price=100,
        max_price=1500,
    )
    
    test_listing = {
        "title": "Rick Owens Geobasket Black/White 43",
        "description": "Authentic shoes from SS23. Worn 3 times. OG all.",
        "price": 550,
    }
    
    matched = demo.matches(**test_listing)
    print(f"Demo match result for '{test_listing['title']}': {matched}")
