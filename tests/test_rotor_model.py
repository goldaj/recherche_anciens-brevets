import unittest
from etudes.flettner.rotor_model import Parameters, estimate, break_even_wind_m_s


class TestRotorModel(unittest.TestCase):
    def test_wind_zero_rotor_costs_energy(self):
        self.assertLess(estimate(0, 90)["net_saving_percent"], 0)

    def test_crosswind_can_help(self):
        self.assertGreater(estimate(10, 90)["net_saving_percent"], 0)

    def test_headwind_hurts(self):
        self.assertLess(estimate(10, 180)["net_saving_percent"], 0)

    def test_threshold(self):
        threshold = break_even_wind_m_s(90)
        self.assertIsNotNone(threshold)
        self.assertAlmostEqual(estimate(threshold, 90)["net_saving_percent"], 0, places=9)

    def test_no_thrust_direction(self):
        self.assertIsNone(break_even_wind_m_s(180, Parameters(lift_coefficient=0)))

    def test_invalid_config(self):
        with self.assertRaises(ValueError):
            Parameters(propulsive_efficiency=0)
        with self.assertRaises(ValueError):
            estimate(-1, 90)


if __name__ == "__main__":
    unittest.main()
