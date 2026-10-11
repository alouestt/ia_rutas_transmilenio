# Informe de pruebas — Actividad 3

## 1. Objetivo

Verificar la validación del conjunto de datos y el funcionamiento del proceso de entrenamiento y predicción del clasificador supervisado basado en un árbol de decisión.

## 2. Entorno y ejecución

Las pruebas se ejecutan con Python y `unittest`, desde la raíz del repositorio.

Comando utilizado:

`python -m unittest discover -s actividad_3_supervisado -p "test_*.py" -v`

## 3. Casos de prueba

- `test_dataset_valido`: comprueba la aceptación de un conjunto de datos válido.
- `test_pipeline_entrena_y_predice`: verifica el proceso de entrenamiento y predicción.
- `test_rechaza_columna_faltante`: comprueba el rechazo de una columna requerida ausente.
- `test_rechaza_costo_de_ruta_inconsistente`: verifica la detección de costos incoherentes.
- `test_rechaza_hora_fuera_de_rango`: comprueba la validación del rango de la hora.
- `test_rechaza_valores_vacios`: verifica el rechazo de valores vacíos.
- `test_regla_de_etiquetado`: comprueba la regla de asignación de las etiquetas simuladas.
- `test_valida_costo_de_ruta`: verifica la validación del costo de la ruta.

## 4. Resultados

En la ejecución registrada el 11 de octubre de 2026, las ocho pruebas finalizaron correctamente:

- Pruebas ejecutadas: 8.
- Pruebas aprobadas: 8.
- Pruebas fallidas: 0.
- Estado final: `OK`.

En una ejecución anterior del entrenamiento se obtuvo una exactitud (_accuracy_) de 0.900 con 600 registros. Este resultado corresponde a datos sintéticos y no representa una evaluación de demoras reales de TransMilenio.

El archivo `predicciones_prueba.csv` permite revisar las etiquetas simuladas, las predicciones y sus aciertos.

## 5. Conclusión

Las pruebas verifican los principales controles de los datos y el funcionamiento del proceso de clasificación. Los resultados respaldan el funcionamiento del ejercicio académico dentro de las condiciones implementadas, pero no demuestran capacidad predictiva sobre datos reales de TransMilenio.
