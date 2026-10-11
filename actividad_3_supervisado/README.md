# Actividad 3: Métodos de aprendizaje supervisado

Este módulo desarrolla un ejercicio de clasificación supervisada a partir del proyecto de búsqueda de rutas de TransMilenio del repositorio.

## Objetivo

Entrenar un árbol de decisión que clasifique el nivel estimado de demora de un viaje (Baja, Media o Alta) a partir de características de la ruta y del contexto del viaje.

## Estructura

- generar_dataset.py: reutiliza la base de conocimiento y la búsqueda A\* del proyecto principal para construir registros de viajes.
- entrenar_modelo.py: prepara los datos, separa entrenamiento y prueba, entrena el clasificador y reporta métricas.
- dataset_viajes.csv: se genera localmente al ejecutar el generador; no hace falta modificar los archivos originales.
- requirements.txt: dependencias exclusivas de esta actividad.

## Importante sobre los datos

La red de estaciones y conexiones se toma de conocimiento.py, y las rutas se calculan con busqueda.py. **Los horarios, las condiciones del viaje y las etiquetas de demora son simulados con fines académicos**. No son mediciones oficiales ni predicciones reales de TransMilenio. El modelo aprenderá patrones de la regla de simulación, por lo que sus resultados no deben interpretarse como desempeño operativo real.

## Cómo ejecutar

Desde la raíz del repositorio:

```bash
python actividad_3_supervisado/generar_dataset.py
python -m pip install -r actividad_3_supervisado/requirements.txt
python actividad_3_supervisado/entrenar_modelo.py
```

También puedes entrar a la carpeta y ejecutar ambos scripts desde allí. El generador añade la raíz del repositorio a la ruta de importación para reutilizar los módulos existentes.

## Variables del conjunto de datos

- origen, destino: estaciones del viaje.
- paradas: cantidad de tramos entre estaciones.
- transbordos: transbordos reportados por la búsqueda A\*.
- costo_ruta: costo de la ruta según el proyecto base.
- hora_salida: hora simulada de salida.
- hora_pico: indica si el viaje cae en una franja simulada de alta demanda.
- lluvia: condición meteorológica simulada.
- nivel_demora: etiqueta objetivo de clasificación.

## Qué revisar en el informe

El script muestra la distribución de clases, la exactitud (accuracy), el reporte de clasificación y la matriz de confusión. Como las etiquetas se generan mediante reglas, conviene explicar las limitaciones del conjunto sintético y que una evaluación alta no demuestra que el modelo funcione con datos reales.
