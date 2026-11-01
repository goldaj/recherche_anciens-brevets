#!/usr/bin/env python3
"""Bilan gravitaire maximal de l'eau atmosphérique, sans dépendance."""
from __future__ import annotations
import argparse

RHO_KG_M3 = 1000.0
G_M_S2 = 9.81


def recovered_wh_per_day(liters_per_day: float, head_m: float, efficiency: float = 1.0) -> float:
    """Électricité théorique [Wh/j] pour débit, hauteur nette et rendement.
    Ne couvre pas pertes autres que la turbine, ni le coût de production d'eau.
    """
    if liters_per_day < 0 or head_m < 0 or not 0 <= efficiency <= 1:
        raise ValueError("Débit et hauteur >= 0 ; rendement dans [0,1]")
    return (liters_per_day / 1000) * RHO_KG_M3 * G_M_S2 * head_m * efficiency / 3600


def needed_liters_per_day(fan_watts: float, hours_per_day: float, head_m: float,
                          efficiency: float) -> float | None:
    """Débit minimal pour une seule charge ; None si tête ou rendement nuls."""
    if fan_watts < 0 or not 0 <= hours_per_day <= 24 or head_m < 0 or not 0 <= efficiency <= 1:
        raise ValueError("Charge >= 0 ; durée de 0 à 24 h ; hauteur >= 0 ; rendement dans [0,1]")
    energy_per_liter = recovered_wh_per_day(1, head_m, efficiency)
    if energy_per_liter == 0:
        return 0.0 if fan_watts * hours_per_day == 0 else None
    return (fan_watts * hours_per_day) / energy_per_liter


if __name__ == "__main__":
    a = argparse.ArgumentParser(description=__doc__)
    a.add_argument("--head-m", type=float, default=200)
    a.add_argument("--liters-per-day", type=float, default=10)
    a.add_argument("--efficiency", type=float, default=0.6)
    a.add_argument("--fan-w", type=float, default=1)
    a.add_argument("--hours", type=float, default=24)
    v = a.parse_args()
    energy = recovered_wh_per_day(v.liters_per_day, v.head_m, v.efficiency)
    fan_energy = v.fan_w * v.hours
    needed = needed_liters_per_day(v.fan_w, v.hours, v.head_m, v.efficiency)
    print(f"Electricité possible : {energy:.3f} Wh/j")
    print(f"Charge de ventilation : {fan_energy:.3f} Wh/j")
    print("Débit minimal pour la ventilation SEULE : "
          + (f"{needed:.1f} L/j" if needed is not None else "impossible avec cette chute"))
