"""Agrupa viajes sintéticos con K-Means sin utilizar etiquetas objetivo."""

from pathlib import Path

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

CARPETA = Path(__file__).resolve().parent
DATASET = CARPETA / "dataset_viajes.csv"
NUM_CLUSTERS = 3

COLUMNAS_NUMERICAS = [
    "paradas",
    "transbordos",
    "costo_ruta",
    "hora_pico",
    "lluvia",
]


def preparar_variables(datos):
    """Escala variables numéricas y codifica la hora de forma cíclica."""
    variables = datos[COLUMNAS_NUMERICAS].copy()
    angulo = 2 * 3.141592653589793 * datos["hora_salida"] / 24
    variables["hora_sin"] = __import__("numpy").sin(angulo)
    variables["hora_cos"] = __import__("numpy").cos(angulo)
    escalador = StandardScaler()
    transformadas = escalador.fit_transform(variables)
    return transformadas, variables.columns.tolist()


def main():
    if not DATASET.exists():
        raise FileNotFoundError(
            "No existe dataset_viajes.csv. Ejecuta primero "
            "'python actividad_4_no_supervisado/generar_dataset.py' desde la raíz."
        )

    datos = pd.read_csv(DATASET)
    if datos.empty:
        raise ValueError("El dataset está vacío.")

    columnas_requeridas = {
        "origen", "destino", "paradas", "transbordos", "costo_ruta",
        "hora_salida", "hora_pico", "lluvia",
    }
    faltantes = columnas_requeridas.difference(datos.columns)
    if faltantes:
        raise ValueError(f"Faltan columnas requeridas: {', '.join(sorted(faltantes))}")
    if len(datos) <= NUM_CLUSTERS:
        raise ValueError("Se necesitan más registros que clústeres para entrenar el modelo.")

    X, nombres_variables = preparar_variables(datos)
    modelo = KMeans(n_clusters=NUM_CLUSTERS, random_state=42, n_init=10)
    grupos = modelo.fit_predict(X)
    datos_resultado = datos.copy()
    datos_resultado["cluster"] = grupos

    cantidad_grupos = datos_resultado["cluster"].nunique()
    print("\n=== ACTIVIDAD 4: APRENDIZAJE NO SUPERVISADO ===")
    print(f"Registros analizados: {len(datos_resultado)}")
    print(f"Variables utilizadas: {', '.join(nombres_variables)}")
    print(f"Número de clústeres configurado: {NUM_CLUSTERS}")
    print("\nCantidad de registros por clúster:")
    print(datos_resultado["cluster"].value_counts().sort_index().to_string())

    if 1 < cantidad_grupos < len(datos_resultado):
        puntaje = silhouette_score(X, grupos)
        print(f"Coeficiente de silueta: {puntaje:.3f}")
    else:
        print("Coeficiente de silueta no disponible: el modelo produjo un único grupo.")

    columnas_perfil = [
        "paradas", "transbordos", "costo_ruta",
        "hora_salida", "hora_pico", "lluvia",
    ]
    print("\nPerfil promedio por clúster:")
    print(datos_resultado.groupby("cluster")[columnas_perfil].mean().round(2).to_string())

    print("\nEjemplos de viajes agrupados:")
    print(
        datos_resultado[
            ["origen", "destino", "paradas", "transbordos", "hora_salida", "lluvia", "cluster"]
        ].head(10).to_string(index=False)
    )
    print("\nNota: los clústeres son agrupaciones exploratorias de datos sintéticos,")
    print("no categorías oficiales ni predicciones de la operación real.")


if __name__ == "__main__":
    main()
