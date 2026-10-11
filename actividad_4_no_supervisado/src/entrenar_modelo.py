"""Agrupa viajes sintéticos con K-Means y evalúa diferentes cantidades de grupos."""

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

CARPETA = Path(__file__).resolve().parent.parent
DATASET = CARPETA / "data" / "dataset_viajes.csv"
SALIDA_RESULTADOS = CARPETA / "resultados" / "viajes_agrupados.csv"
NUM_CLUSTERS = 3
VALORES_K = range(2, 6)
COLUMNAS_NUMERICAS = [
    "paradas", "transbordos", "costo_ruta", "hora_pico", "lluvia",
]
COLUMNAS_REQUERIDAS = [
    "origen", "destino", "paradas", "transbordos", "costo_ruta",
    "hora_salida", "hora_pico", "lluvia",
]


def validar_dataset(datos):
    """Valida la estructura y los rangos del conjunto no supervisado."""
    if datos.empty:
        raise ValueError("El dataset está vacío.")

    faltantes = set(COLUMNAS_REQUERIDAS).difference(datos.columns)
    if faltantes:
        raise ValueError(f"Faltan columnas requeridas: {', '.join(sorted(faltantes))}")
    if datos[COLUMNAS_REQUERIDAS].isnull().any().any():
        raise ValueError("El dataset contiene valores vacíos en columnas requeridas.")
    if datos[["origen", "destino"]].astype(str).apply(
        lambda columna: columna.str.strip().eq("")
    ).any().any():
        raise ValueError("Las columnas origen y destino no pueden estar vacías.")

    columnas_numericas = COLUMNAS_NUMERICAS + ["hora_salida"]
    for columna in columnas_numericas:
        valores = pd.to_numeric(datos[columna], errors="coerce")
        if valores.isnull().any() or not np.isfinite(valores).all():
            raise ValueError(f"La columna {columna} contiene valores numéricos inválidos.")
        datos[columna] = valores

    if not datos["hora_salida"].between(0, 23).all():
        raise ValueError("La hora_salida debe estar entre 0 y 23.")
    for columna in ["hora_pico", "lluvia"]:
        if not datos[columna].isin([0, 1]).all():
            raise ValueError(f"La columna {columna} solo admite 0 o 1.")
    for columna in ["paradas", "transbordos", "costo_ruta"]:
        if (datos[columna] < 0).any():
            raise ValueError(f"La columna {columna} no puede contener valores negativos.")


def preparar_variables(datos):
    """Escala variables y codifica la hora cíclicamente."""
    variables = datos[COLUMNAS_NUMERICAS].copy()
    angulo = 2 * np.pi * datos["hora_salida"] / 24
    variables["hora_sin"] = np.sin(angulo)
    variables["hora_cos"] = np.cos(angulo)
    escalador = StandardScaler()
    transformadas = escalador.fit_transform(variables)
    return transformadas, variables.columns.tolist()


def evaluar_valores_k(X, cantidad_registros):
    """Compara la silueta para varios valores de k sin reutilizar etiquetas externas."""
    resultados = []
    for k in VALORES_K:
        if k >= cantidad_registros:
            continue
        modelo = KMeans(n_clusters=k, random_state=42, n_init=10)
        grupos = modelo.fit_predict(X)
        cantidad_grupos = len(np.unique(grupos))
        if 1 < cantidad_grupos < cantidad_registros:
            resultados.append((k, silhouette_score(X, grupos)))
    return resultados


def calcular_hora_circular(horas):
    """Calcula una hora promedio respetando la continuidad entre 23:00 y 00:00."""
    angulos = 2 * np.pi * np.asarray(horas, dtype=float) / 24
    seno = np.sin(angulos).mean()
    coseno = np.cos(angulos).mean()
    if np.isclose(seno, 0) and np.isclose(coseno, 0):
        return float("nan")
    return float((np.arctan2(seno, coseno) % (2 * np.pi)) * 24 / (2 * np.pi))


def main():
    if not DATASET.exists():
        raise FileNotFoundError(
            "No existe dataset_viajes.csv. Ejecuta primero "
            "'python actividad_4_no_supervisado/generar_dataset.py' desde la raíz."
        )

    datos = pd.read_csv(DATASET)
    validar_dataset(datos)
    if len(datos) <= NUM_CLUSTERS:
        raise ValueError("Se necesitan más registros que clústeres para entrenar el modelo.")

    X, nombres_variables = preparar_variables(datos)
    modelo = KMeans(n_clusters=NUM_CLUSTERS, random_state=42, n_init=10)
    grupos = modelo.fit_predict(X)
    datos_resultado = datos.copy()
    datos_resultado["cluster"] = grupos
    datos_resultado.to_csv(SALIDA_RESULTADOS, index=False, encoding="utf-8")

    print("\n=== ACTIVIDAD 4: APRENDIZAJE NO SUPERVISADO ===")
    print(f"Registros analizados: {len(datos_resultado)}")
    print(f"Variables utilizadas: {', '.join(nombres_variables)}")
    print(f"Número de clústeres configurado: {NUM_CLUSTERS}")
    print("\nCantidad de registros por clúster:")
    print(datos_resultado["cluster"].value_counts().sort_index().to_string())

    cantidad_grupos = datos_resultado["cluster"].nunique()
    if 1 < cantidad_grupos < len(datos_resultado):
        puntaje = silhouette_score(X, grupos)
        print(f"Coeficiente de silueta para k={NUM_CLUSTERS}: {puntaje:.3f}")
    else:
        print("Coeficiente de silueta no disponible: el modelo produjo un único grupo.")

    print("\nComparación del coeficiente de silueta:")
    evaluaciones = evaluar_valores_k(X, len(datos_resultado))
    if evaluaciones:
        for k, puntaje_k in evaluaciones:
            marca = " (configuración utilizada)" if k == NUM_CLUSTERS else ""
            print(f"k={k}: {puntaje_k:.3f}{marca}")
        mejor_k, mejor_puntaje = max(evaluaciones, key=lambda elemento: elemento[1])
        print(f"Mayor silueta observada: k={mejor_k}, valor={mejor_puntaje:.3f}")
    else:
        print("No fue posible comparar valores de k con estos datos.")

    columnas_perfil = ["paradas", "transbordos", "costo_ruta", "hora_pico", "lluvia"]
    print("\nPerfil promedio por clúster (variables no horarias):")
    print(datos_resultado.groupby("cluster")[columnas_perfil].mean().round(2).to_string())
    print("\nHora de salida promedio circular por clúster:")
    for cluster, grupo in datos_resultado.groupby("cluster"):
        hora = calcular_hora_circular(grupo["hora_salida"])
        print(f"Clúster {cluster}: {hora:.2f}" if np.isfinite(hora) else
              f"Clúster {cluster}: no definida (horas distribuidas alrededor del reloj)")

    print("\nEjemplos de viajes agrupados:")
    print(datos_resultado[
        ["origen", "destino", "paradas", "transbordos", "hora_salida", "lluvia", "cluster"]
    ].head(10).to_string(index=False))
    print(f"Asignaciones de clúster guardadas en: {SALIDA_RESULTADOS}")
    print("\nNota: los clústeres son agrupaciones exploratorias de datos sintéticos,")
    print("no categorías oficiales ni predicciones de la operación real.")
    if evaluaciones and max(evaluaciones, key=lambda elemento: elemento[1])[1] < 0.25:
        print("Interpretación: la separación entre grupos es débil; interpreta los perfiles con cautela.")


if __name__ == "__main__":
    main()
