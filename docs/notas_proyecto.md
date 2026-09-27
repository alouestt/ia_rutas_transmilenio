# Notas para el proyecto

## Idea central

El sistema representa una parte reducida de la red de transporte mediante hechos y reglas. A partir de una estación de origen y una estación de destino, el algoritmo A\* explora estados posibles y utiliza una función heurística para orientar la búsqueda.

## Regla lógica general

Si `conexion(origen, destino, linea)` pertenece a la base de conocimiento, entonces el sistema puede considerar `destino` como un movimiento válido desde `origen`.

Si `linea_actual != nueva_linea`, entonces se registra un transbordo.

## Qué explicar en el video

1. Problema que se desea resolver.
2. Qué es la base de conocimiento.
3. Cómo se representan los hechos.
4. Qué reglas utiliza el sistema.
5. Qué es A\*.
6. Diferencia entre costo acumulado y heurística.
7. Ejecución de una ruta.
8. Resultados de las pruebas.
9. Limitaciones: red reducida y datos no operativos en tiempo real.
