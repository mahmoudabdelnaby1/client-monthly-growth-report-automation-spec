"""
Unit tests for Client Growth Report Compiler
"""
import unittest
from src.compile_report import compile_growth_kpis

class TestGrowthReport(unittest.TestCase):
    def test_kpi_calculations(self):
        curr = {"spend": 10000, "revenue": 40000, "conversions": 200}
        prev = {"spend": 10000, "revenue": 30000, "conversions": 150}
        tgts = {"target_revenue": 35000}
        
        res = compile_growth_kpis(curr, prev, tgts)
        self.assertEqual(res["kpis"]["blended_roas"], 4.0)
        self.assertEqual(res["kpis"]["cac"], 50.0)
        self.assertEqual(res["mom_changes"]["revenue_growth_pct"], 33.3)
        self.assertEqual(res["targets"]["status"], "AHEAD_OF_TARGET")

if __name__ == "__main__":
    unittest.main()
