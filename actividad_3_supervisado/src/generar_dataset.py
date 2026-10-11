"""Genera un conjunto de viajes sintéticos a partir de la red del proyecto base."""

import csv
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC_COMPARTIDO = ROOT / "src"
if str(SRC_COMPARTIDO) not in sys.path:
    sys.path.insert(0, str(SRC_COMPARTIDO))

from conocimiento import ESTACIONES
from busqueda import buscar_mejor_ruta

OUTPUT = Path(__file__).resolve().parents[1] / "data" / "dataset_viajes.csv"
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


def main():
    rng = random.Random(RANDOM_SEED)
    estaciones = sorted(ESTACIONES)
    rutas_validas = []

    for origen in estaciones:
        for destino in estaciones:
            if origen == destino:
                continue
            resultado = buscar_mejor_ruta(origen, destino)
            if resultado.get("encontrada"):
                validar_resultado_ruta(resultado)
                rutas_validas.append((origen, destino, resultado))

    if not rutas_validas:
        raise RuntimeError("No se encontraron rutas válidas en la base de conocimiento.")

    filas = []
    for _ in range(NUM_VIAJES):
        origen, destino, ruta = rng.choice(rutas_validas)
        hora = rng.randrange(24)
        hora_pico = int(hora in range(6, 10) or hora in range(16, 20))
        lluvia = rng.randint(0, 1)
        paradas = len(ruta["ruta"]) - 1
        transbordos = ruta["transbordos"]
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
