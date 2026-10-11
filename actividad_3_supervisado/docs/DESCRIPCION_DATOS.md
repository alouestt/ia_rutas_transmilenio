# Descripción de los datos — Actividad 3

## 1. Objetivo

El conjunto de datos permite entrenar un modelo de aprendizaje supervisado para clasificar el nivel simulado de demora de un viaje en tres categorías: Baja, Media y Alta.

## 2. Fuente de los datos

El archivo `dataset_viajes.csv` se genera mediante `generar_dataset.py`, reutilizando la red de estaciones de `conocimiento.py` y la búsqueda de rutas implementada en `busqueda.py`.

La ejecución de referencia genera 600 registros. Los datos de contexto y las etiquetas de demora son sintéticos y tienen fines académicos.

## 3. Descripción de las variables

- `origen`: estación de inicio del viaje.
- `destino`: estación de destino.
- `paradas`: cantidad de tramos de la ruta.
- `transbordos`: cantidad de transbordos reportados por la búsqueda.
- `costo_ruta`: costo calculado según las reglas del proyecto base.
- `hora_salida`: hora simulada de salida, entre 0 y 23.
- `hora_pico`: indicador binario de una franja horaria simulada de mayor demanda.
- `lluvia`: indicador binario de una condición meteorológica simulada.
- `nivel_demora`: variable objetivo que representa la categoría de demora simulada.

## 4. Preparación y uso

El programa valida las columnas requeridas, los valores vacíos, los rangos horarios, las variables binarias, las etiquetas y la coherencia del costo de la ruta.

El modelo utiliza las características del viaje para aprender a clasificar `nivel_demora`. Los datos se dividen en conjuntos de entrenamiento y prueba para evaluar las predicciones.

## 5. Limitaciones

La etiqueta `nivel_demora` se genera mediante una regla basada en variables del mismo conjunto de datos. Por ello, las métricas reflejan la capacidad del modelo para aprender esa regla sintética y no demuestran que pueda predecir demoras reales.

Los datos no corresponden a mediciones oficiales de TransMilenio.

## 6. Archivos relacionados

- `generar_dataset.py`: genera los datos.
- `dataset_viajes.csv`: conjunto de datos.
- `entrenar_modelo.py`: valida, entrena y evalúa el modelo.
- `predicciones_prueba.csv`: contiene las predicciones obtenidas.
- `test_entrenar_modelo.py`: contiene las pruebas unitarias.
- `requirements.txt`: especifica las dependencias.
