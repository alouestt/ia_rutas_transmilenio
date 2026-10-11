# Informe de pruebas — Actividad 4

## 1. Objetivo

Verificar la validación de los datos y el funcionamiento del proceso de agrupamiento no supervisado basado en K-Means.

## 2. Entorno y ejecución

Las pruebas se ejecutan con Python y `unittest`, desde la raíz del repositorio.

Comando utilizado:

`python -m unittest discover -s actividad_4_no_supervisado/tests -p "test_*.py" -v`

## 3. Casos de prueba

- `test_codificacion_horaria_es_finita`: comprueba que la codificación horaria produce valores finitos.
- `test_dataset_valido`: verifica la aceptación de un conjunto de datos válido.
- `test_hora_promedio_circular_entre_23_y_00`: comprueba el tratamiento circular de horas próximas a la medianoche.
- `test_kmeans_asigna_un_grupo_a_cada_registro`: verifica que K-Means asigne un grupo a cada registro procesado.
- `test_rechaza_columna_faltante`: comprueba el rechazo de una columna requerida ausente.
- `test_rechaza_costo_de_ruta_inconsistente`: verifica la detección de costos incoherentes.
- `test_rechaza_valores_vacios`: comprueba el rechazo de valores vacíos.
- `test_valida_costo_de_ruta`: verifica la validación del costo de la ruta.

## 4. Resultados

En la ejecución registrada el 11 de octubre de 2026, las ocho pruebas finalizaron correctamente:

- Pruebas ejecutadas: 8.
- Pruebas aprobadas: 8.
- Pruebas fallidas: 0.
- Estado final: `OK`.

En una ejecución anterior del análisis con 600 registros, se obtuvo un coeficiente de silueta de 0.216 para k=3 y de 0.269 para k=5. Entre los valores de k evaluados, k=5 obtuvo el valor más alto en esa ejecución.

Estos resultados describen la separación de los grupos en los datos sintéticos. Una silueta mayor no demuestra por sí sola que los grupos sean útiles en un contexto real.

## 5. Conclusión

Las pruebas verifican la validación de los datos, el tratamiento de la variable horaria y la asignación de los registros a grupos. El ejercicio permite explorar similitudes entre recorridos, con las limitaciones propias de los datos sintéticos y del método empleado.
