"""Pruebas unitarias del generador y del entrenamiento supervisado."""

import unittest

import pandas as pd

from generar_dataset import clasificar_demora, validar_resultado_ruta
from entrenar_modelo import construir_modelo, validar_dataset


def dataset_valido():
    filas = []
    for etiqueta in ["Baja", "Media", "Alta"]:
        for indice in range(4):
            filas.append({
                "origen": f"Estacion {indice % 2}",
                "destino": f"Destino {indice % 2}",
                "paradas": indice + 1,
                "transbordos": indice % 2,
                "costo_ruta": indice + 1 + 2 * (indice % 2),
                "hora_salida": indice + 6,
                "hora_pico": int(indice % 2 == 0),
                "lluvia": int(indice % 2 == 1),
                "nivel_demora": etiqueta,
            })
    return pd.DataFrame(filas)


class PruebasEntrenamientoSupervisado(unittest.TestCase):
    def test_regla_de_etiquetado(self):
        self.assertEqual(clasificar_demora(1, 0, 0, 0), "Baja")
        self.assertEqual(clasificar_demora(4, 1, 1, 0), "Media")
        self.assertEqual(clasificar_demora(8, 1, 1, 1), "Alta")

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
        datos.loc[0, "origen"] = None
        with self.assertRaisesRegex(ValueError, "valores vacíos"):
            validar_dataset(datos)

    def test_rechaza_hora_fuera_de_rango(self):
        datos = dataset_valido()
        datos.loc[0, "hora_salida"] = 25
        with self.assertRaisesRegex(ValueError, "entre 0 y 23"):
            validar_dataset(datos)

    def test_pipeline_entrena_y_predice(self):
        datos = dataset_valido()
        validar_dataset(datos)
        X = datos.drop(columns=["nivel_demora"])
        y = datos["nivel_demora"]
        modelo = construir_modelo()
        modelo.fit(X, y)
        self.assertEqual(len(modelo.predict(X)), len(datos))


if __name__ == "__main__":
    unittest.main()
