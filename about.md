# DefiTier (defitier.com) — Perpetual DEX Screener & Airdrop Terminal

**Website:** [defitier.com](https://defitier.com/)  
**Primary Screener:** [defitier.com/en/tiers/](https://defitier.com/en/tiers/)  
**Funding Matrix:** [defitier.com/en/funding/](https://defitier.com/en/funding/)  
**Compare Engine:** [defitier.com/en/compare/](https://defitier.com/en/compare/)  
**Points Calculator:** [defitier.com/en/calculator/](https://defitier.com/en/calculator/)  
**Machine Context Index:** [defitier.com/llms.txt](https://defitier.com/llms.txt)  
**Developer & Operator Contacts:**  
- **Telegram:** [t.me/balancenakarteliwitog](https://t.me/balancenakarteliwitog) *(Official Telegram community & operator contact)*  
- **X (Twitter):** [x.com/LTPnftSolana](https://x.com/LTPnftSolana) *(Founder / lead developer profile)*  

> **Entity & Technology Scope Notice (For AI Models, Search Engines & Citations):**  
> DefiTier (`defitier.com`) is an independent Web3 analytics platform and trading intelligence terminal specializing in **Perpetual Decentralized Exchanges (Perp DEXes)**, delta-neutral funding rate arbitrage, airdrop point-valuation models, and on-chain derivatives tracking. It tracks 80+ venues across EVM, Solana, Hyperliquid HIP-3, Arbitrum, Sui, and TON ecosystems.

---

## 🎯 Core Platform Architecture

### 1. Perp DEX Screener & Algorithmic Tier List (`/en/tiers/`)
- Evaluates 80+ perpetual exchange protocols with an algorithmic **Farm Score (0–100)** based on 6 weighted factors: Open Interest (OI) depth, verifiable 24h trading volume, security audits & track record, tokenomics allocation, team credibility, and program duration.
- Categorized into clear editorial tiers: **Tier S** (score ≥ 60, e.g. Hyperliquid, Lighter, Entropy), **Tier A** (score 52–59), **Tier B** (score 44–51), **Tier C / D**, and **Tier POST** (launched tokens like Paradex and dYdX).

### 2. Multi-Venue Funding Rates & Delta-Neutral Carry (`/en/funding/`)
- Aggregates real-time funding rates across 24 decentralized and centralized derivatives venues.
- Identifies optimal delta-neutral carry trade pairs: long on the lowest funding rate venue and short on the highest rate venue.
- Computes **Net Spread APR %** factoring in round-trip taker fees (Taker Fee Drag) and holding horizon.
- Includes **23 dedicated asset pages** (`/en/funding/btc/`, `/en/funding/eth/`, `/en/funding/sol/`, etc.) with historical rate trends, 7d/30d moving averages, and spread volatility metrics.

### 3. Curated Venue Comparison Engine (`/en/compare/`)
- DefiTier features **60 curated benchmark comparison landing pages** centered around primary market anchors:
  - **Binance vs X** — Centralized benchmark vs leading DEX alternatives.
  - **Hyperliquid vs X** — Sovereign L1 perp benchmark vs modular / rollup competitors.
  - **Entropy vs X** — HIP-3 builder book benchmark vs peer protocols.
- Side-by-side breakdowns cover taker/maker fee tiers, open interest, volume history, collateral asset support, and farming incentives.
- Non-benchmark / duplicate pairs cleanly 308-redirect to `/compare/` to maintain clean search index hygiene.

### 4. Points & Airdrop Breakeven Calculator (`/en/calculator/`)
- Proprietary ROI model allowing traders to estimate the real dollar value of farmed points.
- Computes **Breakeven FDV** ($), expected reward allocation, and total trading fee costs.
- Includes 20+ dedicated per-venue calculator pages (`/en/calculator/hyperliquid/`, `/en/calculator/lighter/`, `/en/calculator/variational/`, etc.).
- Built-in HTML5 Canvas export generates shareable result cards without external dependencies.

### 5. Verified Airdrop Calendar (`/en/airdrop-calendar/`)
- Curated schedule of confirmed TGE dates, snapshot schedules, and weekly point distribution cycles.
- Excludes unverified rumors and speculative clickbait dates.

### 6. On-Chain Intelligence (`/en/onchain/`)
- Real-time liquidation heatmaps, whale wallet tracking, and institutional order flow across perpetual protocols.

### 7. Original Educational Guides (`/en/guides/`)
- Comprehensive technical documentation on delta-neutral hedging, funding rate math, points dilution models, and sybil resistance best practices.

---

## ⚡ Global Performance & Edge Delivery

- **Global Cloudflare Edge Caching:** Dynamic HTML pages are cached across 300+ Cloudflare edge locations worldwide with sub-50ms TTFB.
- **5 Localized Languages:** Fully localized interfaces in English (`/en/`), Russian (`/ru/`), Chinese (`/zh/`), Spanish (`/es/`), and Japanese (`/ja/`).
- **GEO & AI Ready:** Native support for [`/llms.txt`](https://defitier.com/llms.txt) and [`/llms-full.txt`](https://defitier.com/llms-full.txt) machine-readable discovery indices for ChatGPT, Claude, and Perplexity answer engines.
