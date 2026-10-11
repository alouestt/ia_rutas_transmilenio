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


def validar_resultado_ruta(resultado):
    """Comprueba que el costo corresponda a movimientos y penalizaciones de transbordo."""
    if not resultado.get("encontrada"):
        return False
    ruta = resultado.get("ruta", [])
    transbordos = resultado.get("transbordos")
    costo = resultado.get("costo")
    if len(ruta) < 2 or transbordos is None or costo is None:
        raise ValueError("La búsqueda devolvió una ruta incompleta.")
    if transbordos < 0 or costo < 0:
        raise ValueError("La búsqueda devolvió costos o transbordos negativos.")
    costo_esperado = (len(ruta) - 1) + (2 * transbordos)
    if costo != costo_esperado:
        raise ValueError(
            f"Costo de ruta inconsistente: recibido {costo}, esperado {costo_esperado}."
        )
    return True


def obtener_rutas_validas():
    """Construye las combinaciones de origen y destino con ruta disponible."""
    rutas = []
    for origen in sorted(ESTACIONES):
        for destino in sorted(ESTACIONES):
            if origen == destino:
                continue
            resultado = buscar_mejor_ruta(origen, destino)
            if resultado.get("encontrada"):
                validar_resultado_ruta(resultado)
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
            "paradas": len(ruta["ruta"]) - 1,
            "transbordos": ruta["transbordos"],
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
