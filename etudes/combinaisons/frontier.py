#!/usr/bin/env python3
"""Frontières de faisabilité pour assemblages historiques, ordre de grandeur.

Ces scénarios n'impliquent pas une membrane validée ni un moteur certifié.
Écrire CSV : python -m etudes.combinaisons.frontier
"""
import argparse
import csv
import math
from pathlib import Path
from etudes.combinaisons.hybrid_budgets import gas_accumulator, gravity_wh_day, cascade

def necessary_water_l_day(head_m, efficiency, fan_w, hours=24):
    """Strict minimum for hypothetical electrical load, no additional losses."""
    if not all(math.isfinite(x) for x in (head_m, efficiency, fan_w, hours)):
        raise ValueError("non-finite")
    if head_m < 0 or not 0 <= efficiency <= 1 or fan_w < 0 or not 0 <= hours <= 24:
        raise ValueError("invalid parameters")
    if fan_w == 0 or hours == 0:
        return 0.
    if head_m == 0 or efficiency == 0:
        return math.inf
    return fan_w*hours/gravity_wh_day(1,head_m,efficiency)

def necessary_hot_c(reject_c, fraction_carnot, q_input_wh, aux_wh):
    """Min hot-side T for non-negative electricity, with fixed source heat input."""
    vals=(reject_c,fraction_carnot,q_input_wh,aux_wh)
    if not all(math.isfinite(x) for x in vals):
        raise ValueError("non-finite")
    if reject_c <= -273.15 or not 0 < fraction_carnot <= 1 or q_input_wh <= 0 or aux_wh < 0:
        raise ValueError("invalid parameters")
    if aux_wh >= fraction_carnot*q_input_wh:
        return math.inf
    sink_k=reject_c+273.15
    return sink_k/(1-aux_wh/(fraction_carnot*q_input_wh))-273.15

def make_rows():
    rows=[]
    for head in (200,1000):
        w=necessary_water_l_day(head,.6,1)
        rows.append(("AWH_gravity",f"head={head}m;fan=1W;eta=0.6",
                     "min_water_l_per_day_for_fan_only",w,"L/day"))
    for minimum in (50,55,60,65):
        r=gas_accumulator(45,minimum,70,100)
        rows.append(("wave_RO",f"p0=45;minimum={minimum};max=70bar_absolute;V0=100L",
                     "exchangeable_feed_volume",r["usable_feed_l"],"L"))
        rows.append(("wave_RO",f"p0=45;minimum={minimum};max=70bar_absolute;V0=100L",
                     "ideal_gas_work",r["stored_ideal_wh"],"Wh"))
    temp=necessary_hot_c(90,.25,1000,20)
    rows.append(("Stirling_AWH","reject=90C;fractionCarnot=0.25;input=1000Wh;aux=20Wh",
                 "min_hot_temperature_for_nonnegative_net_electric",temp,"C"))
    for h in (100,125,200,330):
        v=cascade(h,90,75,10,1000,.25,.7,20)
        rows.append(("Stirling_AWH",f"hot={h}C;reject=90C;1kWh_th",
                     "net_electric",v["electric_net_wh"],"Wh"))
        rows.append(("Stirling_AWH",f"hot={h}C;reject=90C;1kWh_th",
                     "delivered_regeneration_heat",v["regeneration_heat_wh"],"Wh"))
    return rows

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--out",type=Path,default=Path("resultats/frontieres_assemblages.csv"))
    a=parser.parse_args()
    a.out.parent.mkdir(parents=True,exist_ok=True)
    with a.out.open("w",encoding="utf-8",newline="") as f:
        w=csv.writer(f)
        w.writerow(("architecture","scenario","metric","value","unit"))
        w.writerows(make_rows())
    print(f"OK: {len(make_rows())} frontier values in {a.out}")

if __name__ == "__main__":
    main()
