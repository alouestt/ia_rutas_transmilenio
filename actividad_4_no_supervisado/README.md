# Actividad 4: Métodos de aprendizaje no supervisado

Este módulo aplica agrupamiento (_clustering_) a viajes sintéticos construidos a partir de la red académica de rutas del proyecto.

## Objetivo

Usar K-Means para agrupar viajes según características del recorrido y contexto, sin proporcionar etiquetas objetivo. Los grupos se describen con sus tamaños y perfiles promedio.

## Archivos

- `generar_dataset.py`: genera una muestra reproducible de viajes y características.
- `entrenar_modelo.py`: valida los datos, ejecuta K-Means, compara varios valores de k y presenta métricas y perfiles.
- `test_entrenar_modelo.py`: pruebas unitarias de validación, codificación horaria y agrupamiento.
- `dataset_viajes.csv`: se genera al ejecutar el generador.
- `viajes_agrupados.csv`: se genera al entrenar y añade a cada viaje el clúster asignado.
- `requirements.txt`: dependencias necesarias.

## Datos y limitaciones

La red de estaciones y las rutas se obtienen de `conocimiento.py` y `busqueda.py`. Las horas, la lluvia y las características contextuales se simulan con fines académicos; no representan mediciones oficiales ni condiciones operativas reales de TransMilenio.

El modelo no utiliza una columna de clasificación ni etiquetas predefinidas. Los números de los clústeres son identificadores, no categorías ordenadas ni niveles de calidad.

## Ejecución

Desde la raíz del repositorio:

```bash
python actividad_4_no_supervisado/generar_dataset.py
python -m pip install -r actividad_4_no_supervisado/requirements.txt
python actividad_4_no_supervisado/entrenar_modelo.py
python -m unittest discover -s actividad_4_no_supervisado -p "test_*.py" -v
```

## Variables del dataset

- `origen`, `destino`: estaciones de inicio y fin.
- `paradas`: cantidad de tramos de la ruta.
- `transbordos`: transbordos reportados por la búsqueda A\*.
- `costo_ruta`: costo calculado por el proyecto base.
- `hora_salida`: hora simulada de salida.
- `hora_pico`: indicador de una franja horaria simulada de mayor demanda.
- `lluvia`: condición meteorológica simulada.

Para K-Means se escalan las variables numéricas. La hora se representa con seno y coseno para que 23:00 y 00:00 se consideren cercanas. El perfil horario usa un promedio circular para evitar una interpretación engañosa alrededor de medianoche.

El programa compara la silueta para k=2, 3, 4 y 5 (cuando es posible). Una silueta baja indica que los grupos no están bien separados; no es necesariamente un error del programa. Las agrupaciones siguen siendo exploratorias porque los datos son sintéticos.
