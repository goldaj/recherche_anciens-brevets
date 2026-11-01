import unittest
from etudes.eau_atmospherique.gravity_budget import recovered_wh_per_day, needed_liters_per_day


class TestGravityBudget(unittest.TestCase):
    def test_10_l_200_m(self):
        self.assertAlmostEqual(recovered_wh_per_day(10, 200, .6), 3.27)

    def test_gross_specific_energy(self):
        self.assertAlmostEqual(recovered_wh_per_day(1000, 200), 545.0)

    def test_minimum_water(self):
        self.assertAlmostEqual(needed_liters_per_day(1, 24, 200, .6), 24000 / 327)

    def test_no_head(self):
        self.assertIsNone(needed_liters_per_day(1, 24, 0, .6))

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            recovered_wh_per_day(10, 200, 1.3)


if __name__ == "__main__":
    unittest.main()
