#!/usr/bin/env python3
"""Bilans de premier ordre pour trois architectures hybrides historiques.

Aucune donnée d'entrée fictive n'est une mesure de machine. L'objectif est
de falsifier des hypothèses simplistes. Sans dépendance externe.
"""
import argparse
import csv
import math
from pathlib import Path

GRAVITY = 9.81
ABS_ZERO_OFFSET = 273.15

def gravity_wh_day(liters_day, height_m, efficiency):
    vals = (liters_day, height_m, efficiency)
    if not all(math.isfinite(v) for v in vals):
        raise ValueError("Non-finite value")
    if liters_day < 0 or height_m < 0 or not 0 <= efficiency <= 1:
        raise ValueError("Invalid volume, height or efficiency")
    # One liter of water weighs approximately 1 kg.
    return liters_day * GRAVITY * height_m * efficiency / 3600.0

def gas_accumulator(p0_bar_abs, p_low_bar_abs, p_high_bar_abs, volume0_l, n=1.4):
    vals = (p0_bar_abs, p_low_bar_abs, p_high_bar_abs, volume0_l, n)
    if not all(math.isfinite(v) for v in vals):
        raise ValueError("Non-finite value")
    if not (0 < p0_bar_abs <= p_low_bar_abs < p_high_bar_abs and volume0_l > 0 and n > 1):
        raise ValueError("Require 0<p0<=p_low<p_high, V0>0, n>1")
    # Isentropic/polytropic ideal-gas relation, ABSOLUTE pressure.
    v_low = volume0_l * (p0_bar_abs / p_low_bar_abs) ** (1/n)
    v_high = volume0_l * (p0_bar_abs / p_high_bar_abs) ** (1/n)
    # E = integral(p dV); 1 bar.litre = 100 Joule.
    ideal_wh = (p_high_bar_abs * v_high - p_low_bar_abs * v_low) * 100 / ((n-1) * 3600)
    return {"usable_feed_l": v_low - v_high, "stored_ideal_wh": ideal_wh,
            "gas_volume_low_l": v_low, "gas_volume_high_l": v_high}

def cascade(hot_c, reject_c, regeneration_min_c, min_approach_c,
            input_thermal_wh, fraction_carnot, exchanger_efficiency, auxiliaries_wh):
    vals = (hot_c, reject_c, regeneration_min_c, min_approach_c, input_thermal_wh,
            fraction_carnot, exchanger_efficiency, auxiliaries_wh)
    if not all(math.isfinite(v) for v in vals):
        raise ValueError("Non-finite value")
    if not (-273.15 < reject_c < hot_c and -273.15 < regeneration_min_c and
            min_approach_c >= 0 and input_thermal_wh >= 0 and
            0 <= fraction_carnot <= 1 and 0 <= exchanger_efficiency <= 1 and
            auxiliaries_wh >= 0):
        raise ValueError("Invalid thermal parameters")
    carnot = 1 - (reject_c + ABS_ZERO_OFFSET) / (hot_c + ABS_ZERO_OFFSET)
    electric_gross = input_thermal_wh * carnot * fraction_carnot
    rejected_heat = input_thermal_wh - electric_gross
    compatible = reject_c >= regeneration_min_c + min_approach_c
    return {"compatible": compatible, "carnot_limit": carnot,
            "electric_gross_wh": electric_gross,
            "electric_net_wh": electric_gross - auxiliaries_wh,
            "regeneration_heat_wh": rejected_heat * exchanger_efficiency if compatible else 0.,
            "direct_heat_reference_wh": input_thermal_wh * exchanger_efficiency}

def experiment_rows():
    rows = []
    for h in (200, 1000):
        energy = gravity_wh_day(4.25, h, .6)
        rows += [
            {"study": "AWH-gravity", "scenario": f"water=4.25L_day;h={h}m;eta=0.6",
             "metric": "potential_wh_day", "value": energy},
            {"study": "AWH-gravity", "scenario": f"water=4.25L_day;h={h}m;eta=0.6",
             "metric": "fraction_of_24Wh_fan", "value": energy/24},
        ]
    a = gas_accumulator(45, 50, 70, 100)
    for k in ("usable_feed_l", "stored_ideal_wh"):
        rows.append({"study": "wave-RO-accumulator",
                     "scenario": "p0=45barabs;low=50;high=70;gas=100L;n=1.4",
                     "metric": k, "value": a[k]})
    for h, t in ((330,90), (100,90), (330,25)):
        c = cascade(h,t,75,10,1000,.25,.7,20)
        for key in ("electric_net_wh","regeneration_heat_wh","direct_heat_reference_wh"):
            rows.append({"study": "Stirling-AWH", "scenario": f"source={h}C;reject={t}C;Q=1kWh",
                         "metric": key, "value": c[key]})
    return rows

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=Path("resultats/assemblages_scenarios.csv"))
    args = parser.parse_args()
    rows = experiment_rows()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=("study","scenario","metric","value"))
        writer.writeheader()
        writer.writerows(rows)
    print(f"OK: {len(rows)} model outputs exported to {args.out}")

if __name__ == "__main__":
    main()
