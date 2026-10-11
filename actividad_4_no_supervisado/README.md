# Actividad 4: Métodos de aprendizaje no supervisado

Este módulo aplica agrupamiento (_clustering_) a viajes sintéticos construidos a partir de la red académica de rutas del proyecto.

## Objetivo

Usar el algoritmo K-Means para agrupar viajes según características de su recorrido y contexto, sin proporcionar etiquetas objetivo. Los grupos se describen con sus promedios y cantidad de registros para facilitar su interpretación.

## Archivos

- `generar_dataset.py`: genera una muestra reproducible de viajes y sus características.
- `entrenar_modelo.py`: prepara las variables, ejecuta K-Means y presenta métricas y perfiles de los grupos.
- `requirements.txt`: dependencias necesarias.
- `dataset_viajes.csv`: se genera al ejecutar el generador.

## Datos y limitaciones

La red de estaciones y las rutas se obtienen de `conocimiento.py` y `busqueda.py`. Las horas, la lluvia y las características contextuales se simulan con fines académicos. El conjunto no representa mediciones oficiales ni condiciones operativas reales de TransMilenio.

El modelo no utiliza una columna de clasificación ni etiquetas predefinidas: descubre agrupaciones a partir de las variables seleccionadas. Los números de los clústeres son identificadores, no categorías ordenadas ni niveles de calidad.

## Ejecución

Desde la raíz del repositorio:

```bash
python actividad_4_no_supervisado/generar_dataset.py
python -m pip install -r actividad_4_no_supervisado/requirements.txt
python actividad_4_no_supervisado/entrenar_modelo.py
```

## Variables del dataset

- `origen`, `destino`: estaciones de inicio y fin.
- `paradas`: cantidad de tramos de la ruta.
- `transbordos`: transbordos reportados por la búsqueda A\*.
- `costo_ruta`: costo calculado por el proyecto base.
- `hora_salida`: hora simulada de salida.
- `hora_pico`: indicador de una franja horaria simulada de mayor demanda.
- `lluvia`: condición meteorológica simulada.

Para K-Means se escalan las variables numéricas. La hora se representa con seno y coseno para reflejar que 23:00 y 00:00 son horas cercanas. La evaluación usa el coeficiente de silueta cuando es posible; este valor ayuda a estudiar la separación de los grupos, pero no demuestra que existan categorías reales de pasajeros o viajes.
