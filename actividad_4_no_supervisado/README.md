# Actividad 4: Métodos de aprendizaje no supervisado

Este módulo aplica K-Means a viajes sintéticos para explorar agrupamientos según características del recorrido y contexto, sin etiquetas objetivo.

## Estructura

- `src/generar_dataset.py`: genera una muestra reproducible de viajes.
- `src/entrenar_modelo.py`: valida los datos, ejecuta K-Means, compara valores de k y presenta métricas.
- `tests/test_no_supervisado.py`: pruebas unitarias.
- `data/dataset_viajes.csv`: conjunto de datos utilizado por el modelo.
- `resultados/viajes_agrupados.csv`: registros con el clúster asignado.
- `docs/DESCRIPCION_DATOS.md`: descripción de las variables y limitaciones.
- `docs/PRUEBAS.md`: informe de pruebas.
- `requirements.txt`: dependencias de la actividad.

## Ejecución

Ejecutar los comandos desde la raíz del repositorio:

```bash
python -m pip install -r actividad_4_no_supervisado/requirements.txt
python actividad_4_no_supervisado/src/generar_dataset.py
python actividad_4_no_supervisado/src/entrenar_modelo.py
python -m unittest discover -s actividad_4_no_supervisado/tests -p "test_*.py" -v
```

## Variables y limitaciones

Las variables incluyen origen, destino, paradas, transbordos, costo de ruta, hora de salida, hora pico y lluvia. La hora se representa con seno y coseno para respetar su naturaleza cíclica. Los datos son sintéticos y no representan las condiciones operativas reales de TransMilenio.

Los números de los clústeres son identificadores, no categorías ordenadas ni niveles de calidad. La silueta ayuda a comparar la separación de los grupos, pero no demuestra por sí sola que sean útiles en un contexto real.

## Documentación complementaria

- [Descripción de los datos](docs/DESCRIPCION_DATOS.md)
- [Informe de pruebas](docs/PRUEBAS.md)
