# Notas para el proyecto

## Idea central

El sistema representa una parte reducida de una red de transporte mediante hechos y reglas. A partir de una estación de origen y una estación de destino, el algoritmo A\* explora diferentes estados posibles y utiliza una función heurística para orientar la búsqueda hacia el destino.

## Regla lógica general

Si `conexion(origen, destino, linea)` pertenece a la base de conocimiento, entonces el sistema puede considerar `destino` como una estación conectada desde `origen`.

Si `linea_actual != nueva_linea`, entonces se registra un transbordo y se agrega el costo correspondiente.

## Qué explicar en el video

1. Problema que se desea resolver.
2. Qué es la base de conocimiento.
3. Cómo se representan los hechos.
4. Qué reglas utiliza el sistema.
5. Qué es el algoritmo A\*.
6. Diferencia entre costo acumulado y función heurística.
7. Cómo se ejecuta una búsqueda de ruta.
8. Resultados de las pruebas realizadas.
9. Limitaciones del proyecto: red reducida y datos que no corresponden a condiciones operativas en tiempo real.
