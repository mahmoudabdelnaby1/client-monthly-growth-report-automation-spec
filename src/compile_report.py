"""
Client Monthly Growth Report Automation Compiler
Aggregates performance marketing KPIs and produces executive summaries:
- Multi-channel spend, revenue, blended ROAS, CAC
- Month-over-Month (MoM) pacing & targets variance
- Auto-generates structured performance narrative in Markdown & JSON
"""
import json
import argparse
from typing import Dict, Any

def compile_growth_kpis(current_month: Dict[str, float], previous_month: Dict[str, float], targets: Dict[str, float]) -> Dict[str, Any]:
    spend = current_month.get("spend", 0.0)
    revenue = current_month.get("revenue", 0.0)
    conversions = current_month.get("conversions", 0)
    
    roas = round(revenue / spend, 2) if spend > 0 else 0.0
    cac = round(spend / conversions, 2) if conversions > 0 else 0.0
    
    # MoM changes
    prev_rev = previous_month.get("revenue", 0.0)
    prev_roas = round(prev_rev / previous_month.get("spend", 1.0), 2)
    rev_growth_pct = round(((revenue - prev_rev) / prev_rev * 100.0), 1) if prev_rev > 0 else 0.0
    
    # Target attainment
    target_rev = targets.get("target_revenue", 0.0)
    target_attainment_pct = round((revenue / target_rev * 100.0), 1) if target_rev > 0 else 0.0
    
    narrative = (
        f"Generated {revenue:,.0f} against target {target_rev:,.0f} ({target_attainment_pct}% attainment). "
        f"Blended ROAS achieved {roas}x with {conversions} transactions at CAC of {cac}."
    )
    
    return {
        "kpis": {
            "spend": spend,
            "revenue": revenue,
            "conversions": conversions,
            "blended_roas": roas,
            "cac": cac
        },
        "mom_changes": {
            "revenue_growth_pct": rev_growth_pct,
            "previous_roas": prev_roas,
            "roas_delta": round(roas - prev_roas, 2)
        },
        "targets": {
            "revenue_attainment_pct": target_attainment_pct,
            "status": "AHEAD_OF_TARGET" if target_attainment_pct >= 100 else "BEHIND_TARGET"
        },
        "executive_summary": narrative
    }

def main():
    curr = {"spend": 15000, "revenue": 67500, "conversions": 450}
    prev = {"spend": 14000, "revenue": 56000, "conversions": 380}
    tgts = {"target_revenue": 65000}
    res = compile_growth_kpis(curr, prev, tgts)
    print(json.dumps(res, indent=2))

if __name__ == "__main__":
    main()
