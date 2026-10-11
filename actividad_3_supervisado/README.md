# Actividad 3: Métodos de aprendizaje supervisado

Este módulo desarrolla un ejercicio de clasificación supervisada a partir del proyecto de búsqueda de rutas de TransMilenio del repositorio.

## Objetivo

Entrenar un árbol de decisión que clasifique el nivel simulado de demora de un viaje (Baja, Media o Alta) a partir de características de la ruta y del contexto del viaje.

## Archivos

- `generar_dataset.py`: reutiliza la base de conocimiento y la búsqueda A* del proyecto principal para construir registros.
- `entrenar_modelo.py`: valida los datos, separa entrenamiento y prueba, entrena el clasificador y reporta métricas.
- `test_entrenar_modelo.py`: pruebas unitarias de validación y entrenamiento.
- `dataset_viajes.csv`: se genera al ejecutar el generador.
- `predicciones_prueba.csv`: se genera al entrenar y contiene etiquetas reales simuladas, predicciones y aciertos.
- `requirements.txt`: dependencias de esta actividad.

## Datos y limitaciones

La red de estaciones y conexiones se toma de `conocimiento.py`, y las rutas se calculan con `busqueda.py`. Los horarios, las condiciones del viaje y las etiquetas de demora son simulados con fines académicos. No son mediciones oficiales ni predicciones reales de TransMilenio.

La etiqueta `nivel_demora` se construye a partir de una regla que utiliza variables del mismo dataset. Por eso, la exactitud mide qué tan bien aprende el modelo esa regla simulada; no demuestra que prediga demoras reales. Esta limitación debe mencionarse al presentar los resultados.

## Ejecución

Desde la raíz del repositorio:

```bash
python actividad_3_supervisado/generar_dataset.py
python -m pip install -r actividad_3_supervisado/requirements.txt
python actividad_3_supervisado/entrenar_modelo.py
python -m unittest discover -s actividad_3_supervisado -p "test_*.py" -v
```

El generador añade la raíz del repositorio a la ruta de importación para reutilizar los módulos existentes. El entrenador valida las columnas, valores vacíos, rangos horarios, variables binarias y etiquetas antes de ajustar el modelo.

## Variables del dataset

- `origen`, `destino`: estaciones del viaje.
- `paradas`: cantidad de tramos entre estaciones.
- `transbordos`: transbordos reportados por la búsqueda A*.
- `costo_ruta`: costo de la ruta según el proyecto base.
- `hora_salida`: hora simulada de salida (0 a 23).
- `hora_pico`: indica una franja simulada de mayor demanda.
- `lluvia`: condición meteorológica simulada.
- `nivel_demora`: etiqueta objetivo simulada.

El entrenamiento muestra accuracy, reporte de clasificación, matriz de confusión y reglas del árbol. Las predicciones se guardan en `predicciones_prueba.csv` para facilitar su revisión.
