import unittest
from etudes.combinaisons.hybrid_budgets import (
    gravity_wh_day, gas_accumulator, cascade, experiment_rows
)

class HybridTests(unittest.TestCase):
    def test_gravity_example(self):
        self.assertAlmostEqual(gravity_wh_day(4.25,200,.6),1.38975)
    def test_gravity_linear(self):
        self.assertAlmostEqual(gravity_wh_day(4.25,1000,.6),5*gravity_wh_day(4.25,200,.6))
    def test_zero_gravity(self):
        self.assertEqual(gravity_wh_day(0,500,.7),0)
    def test_reject_invalid_gravity(self):
        with self.assertRaises(ValueError): gravity_wh_day(-1,200,.6)
    def test_accumulator_example(self):
        a=gas_accumulator(45,50,70,100)
        self.assertAlmostEqual(a["usable_feed_l"],19.8149704663,places=7)
        self.assertAlmostEqual(a["stored_ideal_wh"],32.497312006,places=7)
    def test_accumulator_volume_sensible(self):
        a=gas_accumulator(45,50,70,100)
        self.assertGreater(a["gas_volume_low_l"],a["gas_volume_high_l"])
    def test_accumulator_no_energy_creation(self):
        a=gas_accumulator(45,50,70,100)
        self.assertGreater(a["stored_ideal_wh"],0)
    def test_accumulator_invalid(self):
        with self.assertRaises(ValueError): gas_accumulator(60,50,70,100)
    def test_carnot(self):
        r=cascade(330,90,75,10,1000,.25,.7,20)
        self.assertLess(r["electric_gross_wh"],1000*r["carnot_limit"])
        self.assertAlmostEqual(r["electric_gross_wh"]+r["regeneration_heat_wh"]/.7,1000)
    def test_thermal_pinch(self):
        r=cascade(330,25,75,10,1000,.25,.7,20)
        self.assertFalse(r["compatible"])
        self.assertEqual(r["regeneration_heat_wh"],0)
    def test_cascade_aux_negative(self):
        r=cascade(100,90,75,10,1000,.25,.7,20)
        self.assertLess(r["electric_net_wh"],0)
    def test_cascade_direct_heat_baseline(self):
        r=cascade(330,90,75,10,1000,.25,.7,20)
        self.assertLess(r["regeneration_heat_wh"],r["direct_heat_reference_wh"])
    def test_row_count(self):
        self.assertEqual(len(experiment_rows()),15)

if __name__ == "__main__":
    unittest.main()
