"""Pruebas unitarias del generador y del entrenamiento no supervisado."""

import sys
import unittest
from pathlib import Path

CARPETA_ACTIVIDAD = Path(__file__).resolve().parents[1]
SRC_ACTIVIDAD = CARPETA_ACTIVIDAD / "src"
SRC_COMPARTIDO = CARPETA_ACTIVIDAD.parent / "src"

for ruta in (SRC_COMPARTIDO, SRC_ACTIVIDAD):
    ruta_str = str(ruta)
    if ruta_str in sys.path:
        sys.path.remove(ruta_str)
    sys.path.insert(0, ruta_str)

sys.modules.pop("entrenar_modelo", None)
sys.modules.pop("generar_dataset", None)

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

from generar_dataset import validar_resultado_ruta
from entrenar_modelo import calcular_hora_circular, preparar_variables, validar_dataset


def dataset_valido():
    return pd.DataFrame({
        "origen": ["A", "B", "C", "D", "E", "F"],
        "destino": ["B", "C", "D", "E", "F", "A"],
        "paradas": [1, 2, 8, 9, 4, 5],
        "transbordos": [0, 0, 2, 2, 1, 1],
        "costo_ruta": [1, 2, 12, 13, 6, 7],
        "hora_salida": [7, 8, 17, 18, 23, 0],
        "hora_pico": [1, 1, 1, 1, 0, 0],
        "lluvia": [0, 1, 0, 1, 0, 1],
    })


class PruebasEntrenamientoNoSupervisado(unittest.TestCase):
    def test_valida_costo_de_ruta(self):
        self.assertTrue(validar_resultado_ruta({
            "encontrada": True,
            "ruta": ["A", "B", "C"],
            "transbordos": 1,
            "costo": 4,
        }))

    def test_rechaza_costo_de_ruta_inconsistente(self):
        with self.assertRaisesRegex(ValueError, "inconsistente"):
            validar_resultado_ruta({
                "encontrada": True,
                "ruta": ["A", "B", "C"],
                "transbordos": 1,
                "costo": 3,
            })

    def test_dataset_valido(self):
        validar_dataset(dataset_valido())

    def test_rechaza_columna_faltante(self):
        datos = dataset_valido().drop(columns=["lluvia"])
        with self.assertRaisesRegex(ValueError, "Faltan columnas"):
            validar_dataset(datos)

    def test_rechaza_valores_vacios(self):
        datos = dataset_valido()
        datos.loc[0, "destino"] = None
        with self.assertRaisesRegex(ValueError, "valores vacíos"):
            validar_dataset(datos)

    def test_codificacion_horaria_es_finita(self):
        X, nombres = preparar_variables(dataset_valido())
        self.assertEqual(X.shape, (6, len(nombres)))
        self.assertTrue(np.isfinite(X).all())

    def test_kmeans_asigna_un_grupo_a_cada_registro(self):
        X, _ = preparar_variables(dataset_valido())
        grupos = KMeans(n_clusters=3, random_state=42, n_init=10).fit_predict(X)
        self.assertEqual(len(grupos), 6)
        self.assertEqual(len(set(grupos)), 3)

    def test_hora_promedio_circular_entre_23_y_00(self):
        hora = calcular_hora_circular([23, 0])
        self.assertTrue(hora < 1 or hora > 23)


if __name__ == "__main__":
    unittest.main()
