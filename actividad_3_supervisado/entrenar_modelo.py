"""Entrena y evalúa un árbol de decisión para la demora simulada."""

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
SALIDA_PREDICCIONES = CARPETA / "predicciones_prueba.csv"
OBJETIVO = "nivel_demora"
COLUMNAS_CATEGORICAS = ["origen", "destino"]
COLUMNAS_NUMERICAS = [
    "paradas", "transbordos", "costo_ruta",
    "hora_salida", "hora_pico", "lluvia",
]
COLUMNAS_REQUERIDAS = COLUMNAS_CATEGORICAS + COLUMNAS_NUMERICAS + [OBJETIVO]
ETIQUETAS = ["Baja", "Media", "Alta"]


def validar_dataset(datos):
    """Valida estructura, valores faltantes y rangos del conjunto supervisado."""
    if datos.empty:
        raise ValueError("El dataset está vacío.")

    faltantes = set(COLUMNAS_REQUERIDAS).difference(datos.columns)
    if faltantes:
        raise ValueError(f"Faltan columnas requeridas: {', '.join(sorted(faltantes))}")

    if datos[COLUMNAS_REQUERIDAS].isnull().any().any():
        raise ValueError("El dataset contiene valores vacíos en columnas requeridas.")

    if datos[COLUMNAS_CATEGORICAS].astype(str).apply(lambda columna: columna.str.strip().eq("")).any().any():
        raise ValueError("Las columnas origen y destino no pueden estar vacías.")

    for columna in COLUMNAS_NUMERICAS:
        valores = pd.to_numeric(datos[columna], errors="coerce")
        if valores.isnull().any():
            raise ValueError(f"La columna {columna} contiene valores no numéricos.")

    if not datos["hora_salida"].between(0, 23).all():
        raise ValueError("La hora_salida debe estar entre 0 y 23.")
    for columna in ["hora_pico", "lluvia"]:
        if not datos[columna].isin([0, 1]).all():
            raise ValueError(f"La columna {columna} solo admite 0 o 1.")
    for columna in ["paradas", "transbordos", "costo_ruta"]:
        if (datos[columna] < 0).any():
            raise ValueError(f"La columna {columna} no puede contener valores negativos.")

    etiquetas_desconocidas = set(datos[OBJETIVO].unique()).difference(ETIQUETAS)
    if etiquetas_desconocidas:
        raise ValueError(
            f"Etiquetas no reconocidas en {OBJETIVO}: "
            f"{', '.join(sorted(map(str, etiquetas_desconocidas)))}"
        )
    if datos[OBJETIVO].value_counts().min() < 2:
        raise ValueError("Cada clase debe tener al menos dos registros para separar entrenamiento y prueba.")


def construir_modelo():
    """Crea el pipeline de preprocesamiento y clasificación."""
    transformador = ColumnTransformer(
        transformers=[
            ("estaciones", OneHotEncoder(handle_unknown="ignore"), COLUMNAS_CATEGORICAS),
            ("numericas", "passthrough", COLUMNAS_NUMERICAS),
        ]
    )
    return Pipeline(steps=[
        ("preparacion", transformador),
        ("arbol", DecisionTreeClassifier(
            max_depth=5, random_state=42, class_weight="balanced"
        )),
    ])


def main():
    if not DATASET.exists():
        raise FileNotFoundError(
            "No existe dataset_viajes.csv. Ejecuta primero "
            "'python actividad_3_supervisado/generar_dataset.py' desde la raíz."
        )

    datos = pd.read_csv(DATASET)
    validar_dataset(datos)

    X = datos[COLUMNAS_CATEGORICAS + COLUMNAS_NUMERICAS]
    y = datos[OBJETIVO]
    X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    modelo = construir_modelo()
    modelo.fit(X_entrenamiento, y_entrenamiento)
    predicciones = modelo.predict(X_prueba)

    resultados = X_prueba.copy()
    resultados["nivel_demora_real"] = y_prueba
    resultados["nivel_demora_predicho"] = predicciones
    resultados["prediccion_correcta"] = (
        resultados["nivel_demora_real"] == resultados["nivel_demora_predicho"]
    )
    resultados.to_csv(SALIDA_PREDICCIONES, index=False, encoding="utf-8")

    print("\n=== ACTIVIDAD 3: APRENDIZAJE SUPERVISADO ===")
    print(f"Registros totales: {len(datos)}")
    print(f"Registros de entrenamiento: {len(X_entrenamiento)}")
    print(f"Registros de prueba: {len(X_prueba)}")
    print(f"Exactitud (accuracy): {accuracy_score(y_prueba, predicciones):.3f}")
    print("\nReporte de clasificación:")
    print(classification_report(y_prueba, predicciones, labels=ETIQUETAS, zero_division=0))
    print("Matriz de confusión (orden: Baja, Media, Alta):")
    print(confusion_matrix(y_prueba, predicciones, labels=ETIQUETAS))

    nombres_estaciones = modelo.named_steps["preparacion"].named_transformers_[
        "estaciones"
    ].get_feature_names_out(COLUMNAS_CATEGORICAS)
    nombres = list(nombres_estaciones) + COLUMNAS_NUMERICAS
    arbol = modelo.named_steps["arbol"]
    print("\nReglas principales aprendidas por el árbol:")
    print(export_text(arbol, feature_names=nombres, max_depth=3))
    print(f"Predicciones del conjunto de prueba guardadas en: {SALIDA_PREDICCIONES}")
    print("\nLimitación: las etiquetas objetivo se derivan de reglas simuladas;")
    print("las métricas miden el ajuste a esa simulación, no demoras reales del sistema.")


if __name__ == "__main__":
    main()
