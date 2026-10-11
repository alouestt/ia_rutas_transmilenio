# Actividad 3: Métodos de aprendizaje supervisado

Este módulo entrena un árbol de decisión para clasificar el nivel **simulado** de demora de un viaje (Baja, Media o Alta) a partir de características de la ruta y su contexto.

## Estructura

- `src/generar_dataset.py`: genera los viajes sintéticos reutilizando el sistema base.
- `src/entrenar_modelo.py`: valida los datos, entrena el clasificador y presenta métricas.
- `tests/test_supervisado.py`: pruebas unitarias.
- `data/dataset_viajes.csv`: conjunto de datos utilizado por el modelo.
- `resultados/predicciones_prueba.csv`: predicciones generadas durante el entrenamiento.
- `docs/DESCRIPCION_DATOS.md`: descripción de las variables y limitaciones.
- `docs/PRUEBAS.md`: informe de pruebas.
- `requirements.txt`: dependencias de la actividad.

## Ejecución

Ejecutar los comandos desde la raíz del repositorio:

```bash
python -m pip install -r actividad_3_supervisado/requirements.txt
python actividad_3_supervisado/src/generar_dataset.py
python actividad_3_supervisado/src/entrenar_modelo.py
python -m unittest discover -s actividad_3_supervisado/tests -p "test_*.py" -v
```

El generador y el entrenador utilizan rutas relativas a la ubicación de los scripts, por lo que los archivos de datos y resultados permanecen en sus carpetas aunque el comando se ejecute desde la raíz.

## Variables y limitaciones

El dataset incluye origen, destino, paradas, transbordos, costo de ruta, hora de salida, hora pico, lluvia y nivel de demora. Los datos y las etiquetas son simulados con fines académicos. La exactitud mide el ajuste a la regla usada para crear las etiquetas; no demuestra capacidad para predecir demoras reales.

## Documentación complementaria

- [Descripción de los datos](docs/DESCRIPCION_DATOS.md)
- [Informe de pruebas](docs/PRUEBAS.md)
