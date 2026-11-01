#!/usr/bin/env python3
"""Bilan BRUT de pompage RO à pression fixe, sans récupération de saumure."""
import argparse

PA_PER_PSI = 6894.757293168
J_PER_KWH = 3600000.0


def raw_hydraulic_kwh_per_feed_m3(pressure_psi: float) -> float:
    if pressure_psi < 0:
        raise ValueError("pression non négative")
    return pressure_psi * PA_PER_PSI / J_PER_KWH


def gross_pump_kwh_per_product_m3(pressure_psi: float,
                                   recovery: float,
                                   pump_efficiency: float = 1.0) -> float:
    """SEC de pression, sans ERD, ni pertes hors pompe ni énergie osmotique."""
    if not 0 < recovery <= 1 or not 0 < pump_efficiency <= 1:
        raise ValueError("récupération et rendement dans ]0,1]")
    return raw_hydraulic_kwh_per_feed_m3(pressure_psi) / recovery / pump_efficiency


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pressure-psi", type=float, default=800)
    parser.add_argument("--recovery", type=float, default=.4)
    parser.add_argument("--pump-efficiency", type=float, default=.85)
    opts = parser.parse_args()
    print(f"Travail pression BRUT par m³ d'eau entrante : {raw_hydraulic_kwh_per_feed_m3(opts.pressure_psi):.3f} kWh/m³")
    print(f"Travail pompe BRUT par m³ de perméat SANS récupération d'énergie : {gross_pump_kwh_per_product_m3(opts.pressure_psi,opts.recovery,opts.pump_efficiency):.3f} kWh/m³")
    print("Ce chiffre n'est pas la consommation d'une usine RO avec récupérateur de saumure.")
