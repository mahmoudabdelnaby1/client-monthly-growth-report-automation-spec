#!/usr/bin/env python3
import json

def compile_monthly_report(client_name, spend, revenue):
    roas = revenue / spend if spend else 0
    return {
        "client": client_name,
        "month": "October 2026",
        "spend_sar": spend,
        "revenue_sar": revenue,
        "blended_roas": f"{round(roas, 2)}x",
        "executive_summary_ar": f"حققنا خلال هذا الشهر عائداً استثمارياً قدره {round(roas, 2)}x بإجمالي مبيعات {revenue:,} ريال سعودي."
    }

if __name__ == "__main__":
    rep = compile_monthly_report("Noon Fashion Partner", 120000, 580000)
    print(json.dumps(rep, indent=2, ensure_ascii=False))
