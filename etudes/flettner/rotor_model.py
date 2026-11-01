#!/usr/bin/env python3
"""Modèle d'ordre de grandeur d'un rotor Flettner (sans dépendances).

Ni prédiction de voyage, ni estimation certifiée de consommation.
Angles: direction VERS laquelle souffle le vent apparent relatif au navire,
0° = vers l'avant, 90° = travers, 180° = vers l'arrière.
La rotation est choisie pour orienter la portance vers l'avant.
"""
from __future__ import annotations

import argparse
import csv
import math
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Parameters:
    air_density_kg_m3: float = 1.225
    height_m: float = 18.0
    diameter_m: float = 3.0
    ship_speed_m_s: float = 6.0
    lift_coefficient: float = 3.0
    drag_coefficient: float = 1.0
    rotor_electric_kw: float = 20.0
    propulsive_efficiency: float = 0.65
    main_engine_efficiency: float = 0.45
    auxiliary_electric_efficiency: float = 0.35
    baseline_shaft_kw: float = 2500.0

    def __post_init__(self):
        positive = ("air_density_kg_m3", "height_m", "diameter_m", "ship_speed_m_s",
                    "baseline_shaft_kw")
        for key in positive:
            if getattr(self, key) <= 0:
                raise ValueError(f"{key} doit être strictement positif")
        for key in ("propulsive_efficiency", "main_engine_efficiency", "auxiliary_electric_efficiency"):
            if not 0 < getattr(self, key) <= 1:
                raise ValueError(f"{key} doit être dans ]0,1]")
        for key in ("lift_coefficient", "drag_coefficient", "rotor_electric_kw"):
            if getattr(self, key) < 0:
                raise ValueError(f"{key} doit être positif ou nul")


def estimate(wind_m_s: float, wind_to_deg: float, p: Parameters = Parameters()) -> dict[str, float]:
    """Bilan rotor EN MARCHE, à vent apparent constant et coefficients imposés."""
    if wind_m_s < 0 or not math.isfinite(wind_m_s) or not math.isfinite(wind_to_deg):
        raise ValueError("Vent et angle doivent être finis; vitesse >= 0")
    theta = math.radians(wind_to_deg)
    q = 0.5 * p.air_density_kg_m3 * wind_m_s ** 2
    area = p.height_m * p.diameter_m
    axial_coefficient = p.lift_coefficient * abs(math.sin(theta)) + p.drag_coefficient * math.cos(theta)
    axial_force_n = q * area * axial_coefficient
    saved_shaft_kw = axial_force_n * p.ship_speed_m_s / p.propulsive_efficiency / 1000
    saved_fuel_equivalent_kw = (saved_shaft_kw / p.main_engine_efficiency
                                - p.rotor_electric_kw / p.auxiliary_electric_efficiency)
    baseline_fuel_kw = p.baseline_shaft_kw / p.main_engine_efficiency
    percent = 100 * saved_fuel_equivalent_kw / baseline_fuel_kw
    return {
        "wind_m_s": wind_m_s,
        "wind_to_deg": wind_to_deg,
        "axial_force_n": axial_force_n,
        "saved_shaft_kw": saved_shaft_kw,
        "rotor_electric_kw": p.rotor_electric_kw,
        "net_fuel_equivalent_kw": saved_fuel_equivalent_kw,
        "net_saving_percent": percent,
    }


def break_even_wind_m_s(wind_to_deg: float, p: Parameters = Parameters()) -> float | None:
    """Seuil théorique à consommation électrique constante; None si pas de poussée utile."""
    theta = math.radians(wind_to_deg)
    coefficient = p.lift_coefficient * abs(math.sin(theta)) + p.drag_coefficient * math.cos(theta)
    if coefficient <= 0:
        return None
    if p.rotor_electric_kw == 0:
        return 0.0
    numerator = (2 * p.rotor_electric_kw * 1000 * p.propulsive_efficiency
                 * p.main_engine_efficiency)
    denominator = (p.air_density_kg_m3 * p.height_m * p.diameter_m * coefficient
                   * p.ship_speed_m_s * p.auxiliary_electric_efficiency)
    return math.sqrt(numerator / denominator)


def build_rows(p: Parameters) -> list[dict[str, float]]:
    return [estimate(speed, angle, p) for speed in (0, 3, 5, 8, 10, 12, 15)
            for angle in (0, 45, 90, 135, 180)]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=Path("resultats/sensibilite_rotor.csv"))
    parser.add_argument("--lift", type=float, default=3.0)
    parser.add_argument("--drive-kw", type=float, default=20.0)
    args = parser.parse_args()
    p = Parameters(lift_coefficient=args.lift, rotor_electric_kw=args.drive_kw)
    rows = build_rows(p)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"{len(rows)} scenarios écrits dans {args.out}")
    for w, a in ((5, 90), (10, 90), (15, 90), (10, 180)):
        r = estimate(w, a, p)
        print(f"vent={w:>2} m/s, direction={a:>3}°, gain carburant théorique={r['net_saving_percent']:>6.2f}%")
    print(f"Seuil théorique à 90°: {break_even_wind_m_s(90, p):.2f} m/s")


if __name__ == "__main__":
    main()
