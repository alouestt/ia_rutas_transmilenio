"""Genera un conjunto de viajes sintéticos a partir de la red del proyecto base."""

import csv
import random
import sys
from pathlib import Path

# Permite ejecutar el script desde la raíz del repositorio o desde esta carpeta.
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from conocimiento import ESTACIONES
from busqueda import buscar_mejor_ruta

OUTPUT = Path(__file__).resolve().parent / "dataset_viajes.csv"
RANDOM_SEED = 42
NUM_VIAJES = 600


def clasificar_demora(paradas, transbordos, hora_pico, lluvia):
    """Asigna una etiqueta didáctica mediante una regla de simulación."""
    puntaje = paradas + (transbordos * 2) + (2 if hora_pico else 0) + (2 if lluvia else 0)
    if puntaje <= 5:
        return "Baja"
    if puntaje <= 10:
        return "Media"
    return "Alta"


def main():
    rng = random.Random(RANDOM_SEED)
    estaciones = sorted(ESTACIONES)
    rutas_validas = []

    # Se obtienen las rutas posibles con el algoritmo A* existente.
    for origen in estaciones:
        for destino in estaciones:
            if origen == destino:
                continue
            resultado = buscar_mejor_ruta(origen, destino)
            if resultado.get("encontrada"):
                rutas_validas.append((origen, destino, resultado))

    if not rutas_validas:
        raise RuntimeError("No se encontraron rutas válidas en la base de conocimiento.")

    filas = []
    for _ in range(NUM_VIAJES):
        origen, destino, ruta = rng.choice(rutas_validas)
        hora = rng.randrange(24)
        hora_pico = int(hora in range(6, 10) or hora in range(16, 20))
        lluvia = rng.randint(0, 1)
        paradas = max(0, len(ruta["ruta"]) - 1)
        transbordos = ruta.get("transbordos", 0)
        filas.append({
            "origen": origen,
            "destino": destino,
            "paradas": paradas,
            "transbordos": transbordos,
            "costo_ruta": ruta["costo"],
            "hora_salida": hora,
            "hora_pico": hora_pico,
            "lluvia": lluvia,
            "nivel_demora": clasificar_demora(paradas, transbordos, hora_pico, lluvia),
        })

    campos = list(filas[0].keys())
    with OUTPUT.open("w", newline="", encoding="utf-8") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=campos)
        writer.writeheader()
        writer.writerows(filas)

    conteo = {}
    for fila in filas:
        etiqueta = fila["nivel_demora"]
        conteo[etiqueta] = conteo.get(etiqueta, 0) + 1

    print(f"Dataset generado: {OUTPUT}")
    print(f"Registros: {len(filas)}")
    print(f"Distribución de clases: {conteo}")
    print("Nota: los factores de demora y las etiquetas son simulados con fines académicos.")


if __name__ == "__main__":
    main()
