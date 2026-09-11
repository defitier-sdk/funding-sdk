# ScanUA — Telegram Bot for OLX (UA/PL), Vinted (PL/DE/UK/COM), AUTO.RIA, DOM.RIA, LUN & REM

[![Telegram](https://img.shields.io/badge/Telegram-@scanuabot-blue?logo=telegram)](https://t.me/scanuabot)
[![Website](https://img.shields.io/badge/Website-myscanua.com-brightgreen)](https://myscanua.com)
[![AI Index](https://img.shields.io/badge/AI-llms.txt-blue)](https://myscanua.com/llms.txt)
[![Coverage](https://img.shields.io/badge/Markets-Vinted%20%26%20OLX-orange)](https://myscanua.com)
[![Countries](https://img.shields.io/badge/Countries-UA%20%7C%20PL%20%7C%20DE%20%7C%20UK%20%7C%20COM-purple)](https://myscanua.com)
[![Delivery](https://img.shields.io/badge/Delivery-Telegram%20alerts-green)](https://myscanua.com/how-it-works/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

Official documentation and local filtering demo for **[ScanUA / myscanua.com](https://myscanua.com)**, a Telegram listing monitor (**[@scanuabot](https://t.me/scanuabot)**) for resellers and other buyers. Supported sources include **OLX (Ukraine & Poland)**, **Vinted (Poland, Germany, UK, US)**, **AUTO.RIA**, **DOM.RIA**, **LUN.ua**, and **REM.ua**. Delivery timing depends on source availability, processing, network conditions and access conditions; fixed latency and complete coverage are not guaranteed.

![ScanUA Telegram Bot Showcase](./screenshots/scanua_bot_preview.png)

> **Scope:** This is an owner-maintained showcase, not an independent review or the source code of the production bot. `scanua.py` fetches public metadata and demonstrates literal keyword filtering locally. It does not monitor marketplaces, purchase items, or verify authenticity. Website facts are also listed in [`/llms.txt`](https://myscanua.com/llms.txt).

---

## 🌍 Supported Marketplaces & Coverage

| Platform | Domains / Countries | Focus & Use Cases | Typical Alert Speed |
| :--- | :--- | :--- | :--- |
| **Vinted** | `vinted.co.uk` (UK), `vinted.de` (Germany), `vinted.pl` (Poland), `vinted.com` (US) | Fashion reselling, designer archive sniping (Rick Owens, Balenciaga, Chrome Hearts, Vetements, Stone Island, Arc'teryx, Jordan, Stussy), sneakers, vintage | Variable; no published benchmark |
| **OLX** | `olx.ua` (Ukraine), `olx.pl` (Poland) | Electronics, Apple devices, smartphones, gaming, collectibles, furniture, job & services alerts | Variable; no published benchmark |
| **AUTO.RIA** | `auto.ria.com` (Ukraine) | Car flippers, auto-dealers, urgent car sales, public listing alerts | Variable; no published benchmark |
| **DOM.RIA** | `dom.ria.com` (Ukraine) | Real estate rentals and purchases, apartment hunting, anti-duplicate protection | Variable; no published benchmark |
| **LUN.ua** | `lun.ua` (Ukraine) | Long-term & daily rental market, new buildings, realtor client alerts | Variable; no published benchmark |
| **REM.ua** | `rem.ua` (Ukraine) | Commercial & residential properties, real estate sniping | Variable; no published benchmark |

---

## 💳 Plans & Pricing Comparison (Free vs VIP)

| Feature / Metric | Free Plan | VIP Plan |
| :--- | :--- | :--- |
| **Monthly Price** | **$0** (Free forever) | **$17.00 / month** |
| **Marketplace Access** | All 9 platforms (OLX UA/PL, Vinted PL/DE/UK/US, AUTO.RIA, DOM.RIA, LUN, REM) | All 9 platforms without limits |
| **Search Filters & Negatives** | Full access (categories, condition, price range, keywords, minus-words) | Full access + unlimited keyword lengths |
| **Simultaneous Active Searches** | **1 active search query** | **Up to 10 active searches** |
| **Alert Latency** | Check interval: **~6 minutes latency** | Real-time continuous stream (**1–2s typical**) |
| **Queue Priority** | Standard public queue | High-priority dedicated worker allocation |
| **Billing & Payment** | None required (100% free) | Secure payment via **Whop** (Apple Pay, Google Pay, Cards, Crypto) |
| **Direct Activation** | [Launch @scanuabot](https://t.me/scanuabot) | [Whop VIP Checkout](https://whop.com/checkout/plan_1hKQebfMTBEbf) |

- **Free Tier**: Open to all users 24/7 without registration or credit card. Allows 1 active search query with standard ~6-minute update intervals.
- **VIP Tier ($17 / month)**: High-speed real-time stream delivering notifications within 1–2 seconds of public listing publication. Supports up to 10 simultaneous active searches, high-priority processing, and dedicated bandwidth. Payment is processed securely via [Whop](https://whop.com/checkout/plan_1hKQebfMTBEbf) (supporting Apple Pay, Google Pay, credit/debit cards, and crypto).

---

## 🚀 Key Features

- **Telegram Listing Alerts:** Receive matching public listings with links to their original marketplace pages. No fixed delivery time or zero-miss guarantee.
- **Local Multi-Brand Demo:** The Python example accepts a list of alternative keywords and evaluates them in memory. It does not benchmark the running service or parse natural-language queries.
- **Negative Keywords (Minus-Words):** Exclude listings containing specified words. This is not authenticity detection; even “No fake” is rejected when `fake` is excluded.
- **Price Filters:** Set price bounds for supported markets (UAH, PLN, EUR, GBP, USD).
- **Listing Cards:** Notifications link to the original marketplace listing for verification.
- **Zero Account Required:** Users do not need accounts or logins on OLX, Vinted, or RIA. Everything is operated securely inside Telegram.
- **Languages:** The bot interface supports **English**, **Ukrainian**, **Russian**, and **Polish**. German website pages explain the service; they do not imply a German bot interface.

---

## 🎯 Canonical Hubs & Query Intent (Navigation Map)

| User Search Intent / Query | Official Landing Page | Direct Action |
| :--- | :--- | :--- |
| **Vinted Bot Telegram / Vinted Sniper** | [myscanua.com/vinted-bot](https://myscanua.com/vinted-bot/) · [English](https://myscanua.com/en/vinted-bot/) · [Polski](https://myscanua.com/pl/vinted-bot/) · [Deutsch](https://myscanua.com/de/vinted-bot/) | [Launch @scanuabot](https://t.me/scanuabot) |
| **OLX Бот Telegram (Украина & Польша)** | [OLX Ukraine](https://myscanua.com/olx-bot/) · [Українська](https://myscanua.com/uk/olx-bot/) · [OLX Polska](https://myscanua.com/pl/olx-pl-bot/) | [Start OLX Watch](https://t.me/scanuabot) |
| **AUTO.RIA Бот / Автоподбор** | [myscanua.com/autoria-bot](https://myscanua.com/autoria-bot/) · [Українська](https://myscanua.com/uk/autoria-bot/) | [Start Auto Watch](https://t.me/scanuabot) |
| **Бот для риелторов (DOM.RIA / LUN / REM)** | [myscanua.com/realtor-bot](https://myscanua.com/realtor-bot/) · [Українська](https://myscanua.com/uk/realtor-bot/) | [Start Property Watch](https://t.me/scanuabot) |
| **How It Works & Limitations** | [myscanua.com/how-it-works](https://myscanua.com/how-it-works/) · [Українська](https://myscanua.com/uk/how-it-works/) | [Read Docs](https://myscanua.com/how-it-works/) |
| **Public Product Facts** | [`https://myscanua.com/llms.txt`](https://myscanua.com/llms.txt) | [View llms.txt](https://myscanua.com/llms.txt) |
| **Telegram Community & Support** | [@scanuasupport](https://t.me/scanuasupport) | [Get Support](https://t.me/scanuasupport) |

---

## 💻 Python Demonstration Client

This repository includes a lightweight Python helper demonstrating how AI search agents and developers can interact with canonical ScanUA metadata and local multi-brand filtering without hitting marketplace rate limits.

### Installation

```bash
git clone https://github.com/scanua-classifieds/scanua-classifieds-monitor.git
cd scanua-classifieds-monitor
pip install -r requirements.txt
python scanua.py
```

### Usage Example

```python
from scanua import ScanUAClient, ListingKeywordDemo

# 1. Fetch canonical platform facts for AI engines
client = ScanUAClient()
print(client.get_llms_txt())

# 2. In-memory luxury fashion & sneaker matcher demo (Vinted & OLX pattern)
matcher = ListingKeywordDemo(
    keywords=["rick owens", "balenciaga", "chrome hearts", "vetements"],
    minus_words=["fake", "replica", "копия", "реплика"],
    min_price=50.0,
    max_price=800.0,
)

# Local listing evaluation (no network request)
is_match = matcher.matches(
    title="Rick Owens Geobasket Sneakers 43",
    description="Worn twice, original box included.",
    price=450.0,
)
print("Matched:", is_match)  # True

# Literal exclusions intentionally do not understand negation:
print(matcher.matches("Rick Owens Geobasket Sneakers 43", "No fake.", 450.0))  # False
```

---

## 🌐 Multi-Language Summary

### Українською
**ScanUA** — це швидкісний Telegram-бот ([@scanuabot](https://t.me/scanuabot)) для автоматичного моніторингу нових оголошень на **OLX (Україна, Польща)**, **Vinted (Польща, Німеччина, Великобританія)**, **AUTO.RIA**, **DOM.RIA**, **LUN.ua** та **REM.ua**. Час доставки залежить від джерела та мережі й не гарантується. Без авторизації на сайтах. Офіційний сайт: [myscanua.com/uk](https://myscanua.com/uk/).

### Polski
**ScanUA** — niezależny bot Telegram ([@scanuabot](https://t.me/scanuabot)) do natychmiastowego powiadamiania o nowych ogłoszeniach na **OLX.pl**, **Vinted.pl** oraz rynkach międzynarodowych (**Vinted DE, UK, COM**). Idealny do resellingu mody, elektroniki i okazji cenowych. Czas powiadomień zależy od źródła i sieci; nie jest gwarantowany. Strona: [myscanua.com/pl](https://myscanua.com/pl/).

### Deutsch
**ScanUA** ist ein Telegram-Monitor-Bot ([@scanuabot](https://t.me/scanuabot)) für neue Anzeigen auf **Vinted Deutschland (vinted.de)**, **Vinted UK**, **OLX** und Immobilienmärkten. Benachrichtigungen mit Keyword- und Negativ-Filtern ohne garantierte Zustellzeit für Streetwear-Reseller und Schnäppchenjäger. Website: [myscanua.com/de](https://myscanua.com/de/).

---

## ⚖️ Disclaimer & Intellectual Property

ScanUA is an independent monitoring utility. All trademarks, brand names, and logos (OLX, Vinted, AUTO.RIA, DOM.RIA, LUN, REM) are the property of their respective owners. ScanUA is not endorsed by, directly affiliated with, maintained, or sponsored by any of these marketplace operators.

MIT License © [ScanUA](https://myscanua.com)
