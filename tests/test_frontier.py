import math
import unittest
from etudes.combinaisons.frontier import necessary_water_l_day, necessary_hot_c, make_rows

class FrontierTests(unittest.TestCase):
    def test_water_threshold_200m(self):
        self.assertAlmostEqual(necessary_water_l_day(200,.6,1),73.39449541284404,places=5)
    def test_water_threshold_1000m(self):
        self.assertAlmostEqual(necessary_water_l_day(1000,.6,1)*5,
                               necessary_water_l_day(200,.6,1),places=8)
    def test_zero_water_when_no_aux(self):
        self.assertEqual(necessary_water_l_day(0,.6,0),0)
    def test_impossible_without_head(self):
        self.assertTrue(math.isinf(necessary_water_l_day(0,.6,1)))
    def test_invalid_thermal(self):
        with self.assertRaises(ValueError): necessary_hot_c(90,0,1000,20)
    def test_thermal_break_even(self):
        self.assertAlmostEqual(necessary_hot_c(90,.25,1000,20),121.57826086956521,places=5)
    def test_thermal_impossibility(self):
        self.assertTrue(math.isinf(necessary_hot_c(90,.25,1000,250)))
    def test_scenario_count(self):
        self.assertEqual(len(make_rows()),19)

if __name__ == "__main__":
    unittest.main()
