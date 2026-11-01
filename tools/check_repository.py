#!/usr/bin/env python3
"""Contrôles offline pour référentiels de recherche, sans dépendances."""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
PATTERN = re.compile(r'!?\[[^\]]+\]\(([^)]+)\)')
COLUMNS = {
    "id", "publication", "annee_publication", "technologie", "source",
    "preuve_documentaire", "statut_marche_hypothese", "rang_recherche",
    "cas_usage_a_tester", "reference_contemporaine", "verrous",
}


def check_links() -> list[str]:
    errors = []
    for doc in ROOT.rglob("*.md"):
        for match in PATTERN.finditer(doc.read_text(encoding="utf-8")):
            target = match.group(1).strip()
            if re.match(r"^(https?://|mailto:|data:|#)", target, re.I):
                continue
            relative = unquote(target.split("#")[0].split("?")[0])
            if not relative:
                continue
            linked = (doc.parent / relative).resolve()
            if not linked.is_relative_to(ROOT.resolve()) or not linked.exists():
                errors.append(f"{doc.relative_to(ROOT)} : lien manquant ou hors dépôt : {target}")
    return errors


def check_catalogue() -> list[str]:
    errors = []
    p = ROOT / "data" / "candidats.csv"
    if not p.exists():
        return ["data/candidats.csv absent"]
    with p.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        return ["catalogue vide"]
    if set(rows[0]) != COLUMNS:
        errors.append("colonnes du catalogue différentes de l'interface attendue")
    for field in ("id", "publication", "source"):
        values = [r.get(field, "").strip() for r in rows]
        if len(values) != len(set(values)):
            errors.append(f"doublon dans la colonne {field}")
        if any(not value for value in values):
            errors.append(f"champ vide pour {field}")
    for row in rows:
        if not re.fullmatch(r"P\d{2,}", row.get("id", "")):
            errors.append(f"mauvais ID : {row.get('id')}")
        if not row.get("source", "").startswith("https://patents.google.com/patent/"):
            errors.append(f"référence primaire non reconnue pour {row.get('id')}")
        try:
            y = int(row.get("annee_publication", ""))
            if y < 1800 or y > 2026:
                errors.append(f"année suspecte pour {row.get('id')}")
        except ValueError:
            errors.append(f"année non numérique pour {row.get('id')}")
    return errors


if __name__ == "__main__":
    failures = check_links() + check_catalogue()
    if failures:
        print("\n".join(f"ECHEC : {x}" for x in failures))
        sys.exit(1)
    with (ROOT / "data" / "candidats.csv").open(encoding="utf-8", newline="") as fh:
        count = sum(1 for _ in csv.DictReader(fh))
    print(f"OK : liens Markdown locaux, {count} références catalogue et colonnes validées.")
