# Descripción de los datos — Actividad 4

## 1. Objetivo

El conjunto de datos se utiliza para explorar agrupamientos de viajes mediante K-Means, un método de aprendizaje no supervisado. El objetivo es identificar grupos de recorridos con características similares, sin proporcionar etiquetas objetivo durante el entrenamiento.

## 2. Fuente y generación de los datos

El archivo `data/dataset_viajes.csv` se genera mediante `src/generar_dataset.py`. El proceso reutiliza la red académica de estaciones y conexiones de `conocimiento.py` y la búsqueda de rutas de `busqueda.py`.

El conjunto de datos contiene 600 registros en la ejecución de referencia. Las variables contextuales, como la hora de salida y la lluvia, se simulan con fines académicos.

## 3. Descripción de las variables

- `origen`: estación de inicio del viaje.
- `destino`: estación de destino.
- `paradas`: cantidad de tramos de la ruta.
- `transbordos`: cantidad de transbordos reportados por la búsqueda.
- `costo_ruta`: costo calculado según las reglas del proyecto base.
- `hora_salida`: hora simulada de salida, expresada entre 0 y 23.
- `hora_pico`: indicador binario de una franja horaria simulada de mayor demanda.
- `lluvia`: indicador binario de una condición meteorológica simulada.

Estas variables describen el recorrido y su contexto. No existe una columna de clasificación que el modelo deba predecir.

## 4. Preparación y uso de los datos

El programa valida las columnas requeridas, los valores vacíos y la coherencia del costo de la ruta. Las variables numéricas se escalan antes del agrupamiento.

La hora se transforma mediante funciones seno y coseno para representar su carácter cíclico y mantener la cercanía entre las horas próximas a la medianoche. El modelo compara diferentes valores de k mediante el coeficiente de silueta y describe las características de los grupos obtenidos.

El archivo `resultados/viajes_agrupados.csv` contiene los registros junto con el identificador del clúster asignado.

## 5. Limitaciones

Los datos no son mediciones oficiales de TransMilenio ni representan necesariamente las condiciones reales de operación.

Los identificadores de clúster no constituyen categorías ordenadas ni niveles de calidad. Los agrupamientos son exploratorios y dependen de los datos, las variables utilizadas y los parámetros del algoritmo.

## 6. Archivos relacionados

- `src/generar_dataset.py`: generación del conjunto de datos.
- `data/dataset_viajes.csv`: datos utilizados por el modelo.
- `src/entrenar_modelo.py`: preparación, agrupamiento y evaluación.
- `resultados/viajes_agrupados.csv`: registros con su clúster asignado.
- `test_src/entrenar_modelo.py`: pruebas unitarias.
- `requirements.txt`: dependencias de Python.
