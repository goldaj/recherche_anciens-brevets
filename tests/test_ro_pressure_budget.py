import unittest
from etudes.dessalement_vagues.ro_pressure_budget import (
    raw_hydraulic_kwh_per_feed_m3,
    gross_pump_kwh_per_product_m3,
)


class TestROPressureBudget(unittest.TestCase):
    def test_pressure_conversion(self):
        self.assertAlmostEqual(raw_hydraulic_kwh_per_feed_m3(800), 1.5321682873706666)

    def test_product_40pct_no_erd(self):
        self.assertAlmostEqual(gross_pump_kwh_per_product_m3(800, .4), 3.8304207184266663)

    def test_efficiency_increases_work(self):
        self.assertGreater(gross_pump_kwh_per_product_m3(800, .4, .85),
                           gross_pump_kwh_per_product_m3(800, .4, 1))

    def test_zero_pressure(self):
        self.assertEqual(gross_pump_kwh_per_product_m3(0, .5), 0)

    def test_invalid_recovery(self):
        with self.assertRaises(ValueError):
            gross_pump_kwh_per_product_m3(800, 0)


if __name__ == "__main__":
    unittest.main()
