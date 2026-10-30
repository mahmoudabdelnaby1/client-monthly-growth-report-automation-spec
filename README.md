# Client Monthly Growth Report Automation Spec & Deck PRD

> Plan a monthly growth-reporting workflow and use the included executive narrative template. No time-saving outcome has been measured.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Format: PROJECT_BLUEPRINT](https://img.shields.io/badge/Format-PROJECT--BLUEPRINT-green.svg)](#)
[![Tier: 3](https://img.shields.io/badge/Tier-3-orange.svg)](#)
[![Region: MENA](https://img.shields.io/badge/Region-Egypt%20%7C%20GCC%20%7C%20Saudi-purple.svg)](#)
[![Tests: Passing](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)](#)
[![Owner: mahmoudabdelnaby1](https://img.shields.io/badge/Owner-mahmoudabdelnaby1-blue.svg)](https://github.com/mahmoudabdelnaby1)

---

## 📌 Problem Statement & Target Persona

### Target Persona
**PRO** operating in high-growth e-commerce, digital publishing, and direct-response marketing across Saudi Arabia, UAE, and Egypt.

### Core Problem
Build an open-source client monthly growth reporting system: 1) System architecture PRD detailing automated ETL data aggregation from Meta, Google, and GA4, 2) 12-slide executive deck narrative framework (Executive Summary, Blended ROAS, Channel Breakdown, Top Winning Creatives, What Worked / What Didn't, Next Month Action Plan), 3) Python summary compiler (`compile_report.py`).

---

## 🛠️ Repository Architecture & Deliverables

This repository provides self-contained, documented implementations and specifications:

- `ARCHITECTURE.md`
- `DATA_MODEL.md`
- `LICENSE`
- `MONETIZATION.md`
- `prd/reporting-automation-architecture.md`
- `PRD.md`
- `PROBLEM.md`
- `README.md`
- `reports/sample_client_executive_summary.md`
- `ROADMAP.md`
- `sample_data/monthly_ad_exports.csv`
- `src/compile_report.py`
- `src/mock_report_compiler.py`
- `templates/12-slide-executive-deck-blueprint.md`
- `tests/test_compiler.py`
- `USER_FLOWS.md`
- *(Additional supporting documentation and assets)*

---

## 🚀 Quick Start & How to Run Locally

### Run Test Suite Locally
```bash
# Ensure no bytecode generation
export PYTHONDONTWRITEBYTECODE=1  # Linux / macOS
$env:PYTHONDONTWRITEBYTECODE="1"  # Windows PowerShell

# Run Python unittest discovery
python -m unittest discover -s tests
```

### Run CLI Script
```bash
python src/compile_report.py --help
```

---

## 📊 Sample Input & Output Fixtures

> **Data Disclosure:** Any included sample data is illustrative and may be synthetic; it is not a measured customer result or market benchmark unless a source and collection method are stated alongside it. These files run offline with standard libraries and require no paid third-party API credentials.

```json
{
  "domain": "reporting",
  "repository": "client-monthly-growth-report-automation-spec",
  "status": "READY_FOR_LOCAL_REVIEW",
  "license": "MIT"
}
```

---

## ⚠️ Known Technical & Domain Constraints

- **Multi-Source API Merging:** Spec outlines programmatic ingestion and reconciliation across Google Ads, Meta Ads, TikTok, and GA4.
- **Executive Deck Generation:** Mandates high-level North Star metrics (MER, Blended ROAS, Contribution Margin) before granular channel tables.
- **Currency Normalization:** Formats blended reports across GCC currencies using central bank monthly exchange rate benchmarks.

---

## 📚 Primary Documentation & Verifiable References

- [Google Analytics 4 Data API (v1beta)](https://developers.google.com/analytics/devguides/reporting/data/v1) - Programmatic interface for querying multi-channel attribution data.
- [Meta Marketing API: Insights Async Reporting](https://developers.facebook.com/docs/marketing-api/insights) - Bulk reporting endpoints for multi-account agency client data.
- [Project Management Institute (PMI) Reporting Standards](https://www.pmi.org/) - Foundational frameworks for stakeholder communication and project progress reporting.

---


## 👤 Maintainer & License

- **Author & Maintainer:** [Mahmoud Abdelnaby](https://github.com/mahmoudabdelnaby1) (`@mahmoudabdelnaby1`)
- **License:** [MIT License](LICENSE) - Open-source, auditable, and freely adaptable for internal enterprise or commercial use.
