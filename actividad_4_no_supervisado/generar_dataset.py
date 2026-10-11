"""Genera viajes sintéticos para el ejercicio de aprendizaje no supervisado."""

import csv
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from busqueda import buscar_mejor_ruta
from conocimiento import ESTACIONES

OUTPUT = Path(__file__).resolve().parent / "dataset_viajes.csv"
RANDOM_SEED = 43
NUM_VIAJES = 600


def obtener_rutas_validas():
    """Construye las combinaciones de origen y destino con ruta disponible."""
    rutas = []
    for origen in sorted(ESTACIONES):
        for destino in sorted(ESTACIONES):
            if origen == destino:
                continue
            resultado = buscar_mejor_ruta(origen, destino)
            if resultado.get("encontrada"):
                rutas.append((origen, destino, resultado))
    return rutas


def main():
    rng = random.Random(RANDOM_SEED)
    rutas_validas = obtener_rutas_validas()
    if not rutas_validas:
        raise RuntimeError("No se encontraron rutas válidas en la base de conocimiento.")

    filas = []
    for _ in range(NUM_VIAJES):
        origen, destino, ruta = rng.choice(rutas_validas)
        hora = rng.randrange(24)
        filas.append({
            "origen": origen,
            "destino": destino,
            "paradas": max(0, len(ruta["ruta"]) - 1),
            "transbordos": ruta.get("transbordos", 0),
            "costo_ruta": ruta["costo"],
            "hora_salida": hora,
            "hora_pico": int(hora in range(6, 10) or hora in range(16, 20)),
            "lluvia": rng.randint(0, 1),
        })

    with OUTPUT.open("w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=list(filas[0].keys()))
        escritor.writeheader()
        escritor.writerows(filas)

    print(f"Dataset generado: {OUTPUT}")
    print(f"Registros: {len(filas)}")
    print(f"Columnas: {', '.join(filas[0].keys())}")
    print("Nota: las variables de contexto son simuladas con fines académicos.")


if __name__ == "__main__":
    main()
