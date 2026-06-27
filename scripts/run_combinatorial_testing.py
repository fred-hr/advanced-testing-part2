import sys
from pathlib import Path
import json
import os

# ==========================================================
# CONFIGURACIÓN DEL PROYECTO
# ==========================================================
# Agrega la carpeta principal del proyecto al PATH de Python.
# Esto permite importar archivos que están dentro de la carpeta src.

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# ==========================================================
# IMPORTACIÓN DE LOS MÓDULOS DEL PROYECTO
# ==========================================================

from src.combinatorial_engine import generate_combinatorial_cases
from src.risk_prioritizer import prioritize_cases_by_risk

# ==========================================================
# PARÁMETROS DE PRUEBA
# ==========================================================

parameters = {
    "username": ["admin", "student", "guest", "unknown", ""],
    "password": ["Admin123", "Student123", "Guest123", "wrong", ""],
    "role": ["admin", "student", "guest", "invalid"],
    "device": ["known", "unknown"],
    "network": ["private", "public"],
    "two_factor_auth": ["enabled", "disabled"],
}

# ==========================================================
# FUNCIÓN PRINCIPAL
# ==========================================================

def main():

    os.makedirs("reports", exist_ok=True)

    # Generar automáticamente todos los casos combinatorios
    cases = generate_combinatorial_cases(parameters)

    # Priorizar los casos por riesgo
    prioritized_cases = prioritize_cases_by_risk(cases)

    output_file = "reports/combinatorial_cases.json"

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(
            prioritized_cases,
            file,
            indent=4,
            ensure_ascii=False
        )

    print("=" * 60)
    print("ADVANCED COMBINATORIAL TESTING")
    print("=" * 60)
    print(f"Generated test cases : {len(prioritized_cases)}")
    print(f"Output report        : {output_file}")
    print("=" * 60)

    print("\nTOP 5 HIGH RISK CASES\n")

    for case in prioritized_cases[:5]:
        print(case)


if __name__ == "__main__":
    main()