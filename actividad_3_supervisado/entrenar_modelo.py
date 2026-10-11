"""Entrena y evalúa un clasificador de árbol de decisión para la demora simulada."""

from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier, export_text

CARPETA = Path(__file__).resolve().parent
DATASET = CARPETA / "dataset_viajes.csv"
OBJETIVO = "nivel_demora"


def main():
    if not DATASET.exists():
        raise FileNotFoundError(
            "No existe dataset_viajes.csv. Ejecuta primero "
            "'python actividad_3_supervisado/generar_dataset.py' desde la raíz."
        )

    datos = pd.read_csv(DATASET)
    if datos.empty:
        raise ValueError("El dataset está vacío.")
    if OBJETIVO not in datos.columns:
        raise ValueError(f"Falta la columna objetivo: {OBJETIVO}")

    X = datos.drop(columns=[OBJETIVO])
    y = datos[OBJETIVO]

    columnas_categoricas = ["origen", "destino"]
    columnas_numericas = [
        "paradas", "transbordos", "costo_ruta",
        "hora_salida", "hora_pico", "lluvia",
    ]

    transformador = ColumnTransformer(
        transformers=[
            ("estaciones", OneHotEncoder(handle_unknown="ignore"), columnas_categoricas),
            ("numericas", "passthrough", columnas_numericas),
        ]
    )

    modelo = Pipeline(steps=[
        ("preparacion", transformador),
        ("arbol", DecisionTreeClassifier(max_depth=5, random_state=42, class_weight="balanced")),
    ])

    X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    modelo.fit(X_entrenamiento, y_entrenamiento)
    predicciones = modelo.predict(X_prueba)

    print("\n=== ACTIVIDAD 3: APRENDIZAJE SUPERVISADO ===")
    print(f"Registros totales: {len(datos)}")
    print(f"Registros de entrenamiento: {len(X_entrenamiento)}")
    print(f"Registros de prueba: {len(X_prueba)}")
    print(f"Exactitud (accuracy): {accuracy_score(y_prueba, predicciones):.3f}")
    print("\nReporte de clasificación:")
    print(classification_report(y_prueba, predicciones, zero_division=0))
    etiquetas = ["Baja", "Media", "Alta"]
    print("Matriz de confusión (orden: Baja, Media, Alta):")
    print(confusion_matrix(y_prueba, predicciones, labels=etiquetas))

    nombres_estaciones = modelo.named_steps["preparacion"].named_transformers_["estaciones"].get_feature_names_out(columnas_categoricas)
    nombres = list(nombres_estaciones) + columnas_numericas
    arbol = modelo.named_steps["arbol"]
    print("\nReglas principales aprendidas por el árbol:")
    print(export_text(arbol, feature_names=nombres, max_depth=3))

    print("\nLimitación: las etiquetas objetivo se derivan de reglas simuladas;")
    print("las métricas miden el ajuste a esa simulación, no demoras reales del sistema.")


if __name__ == "__main__":
    main()
