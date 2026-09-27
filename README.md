# Sistema inteligente de rutas de transporte

## Actividad 3 - Inteligencia Artificial

Proyecto académico desarrollado en Python para representar conocimiento mediante hechos y reglas, y utilizar una búsqueda heurística A\* para encontrar una ruta de menor costo entre dos estaciones de una red reducida de transporte masivo.

> **Importante:** la red incluida en este proyecto es un modelo académico simplificado. No constituye un planificador de viajes en tiempo real ni debe utilizarse para tomar decisiones de desplazamiento. La selección de estaciones y corredores se tomó como referencia de documentación oficial de TransMilenio.

## 1. Objetivo

Desarrollar un sistema inteligente que:

1. represente una base de conocimiento sobre estaciones y conexiones;
2. utilice reglas para determinar estaciones válidas, conexiones y transbordos;
3. explore diferentes alternativas mediante búsqueda heurística A\*;
4. seleccione una ruta de menor costo entre un punto de origen y un destino.

## 2. Conceptos utilizados

### Base de conocimiento

La base de conocimiento está formada por:

- estaciones;
- conexiones entre estaciones;
- corredor asociado a cada conexión;
- coordenadas topológicas utilizadas por la función heurística.

### Reglas

El sistema incorpora reglas que pueden expresarse de forma lógica:

- Si una estación pertenece a la base de conocimiento, entonces es una estación válida.
- Si existe una conexión entre dos estaciones, entonces es posible desplazarse entre ellas.
- Si la línea utilizada cambia durante el recorrido, entonces existe un transbordo.
- Si una conexión permite llegar a un vecino, entonces ese vecino puede ser considerado por el algoritmo de búsqueda.

### Búsqueda heurística

Se implementa A\*. La prioridad de cada estado se calcula como:

`f(n) = g(n) + h(n)`

donde:

- `g(n)` representa el costo acumulado;
- `h(n)` representa la estimación del costo restante;
- `f(n)` representa la prioridad utilizada para explorar el estado.

La heurística se calcula mediante distancia euclidiana sobre coordenadas topológicas simplificadas.

El costo utilizado por el prototipo es:

- 1 unidad por desplazamiento entre estaciones;
- 2 unidades adicionales por cada transbordo.

Por tanto, el sistema busca una ruta que reduzca el costo total y no simplemente una ruta cualquiera.

## 3. Estructura del proyecto

```text
Actividad_3_IA_Rutas_TransMilenio/
│
├── main.py
├── conocimiento.py
├── busqueda.py
├── pruebas.py
├── README.md
│
├── pruebas/
│   └── resultados_pruebas.pdf
│
└── docs/
    └── notas_proyecto.md
```

## 4. Requisitos

- Python 3.10 o superior.
- No se requieren librerías externas.

El proyecto utiliza únicamente módulos de la biblioteca estándar de Python, entre ellos `heapq`.

## 5. Ejecución

Abrir una terminal en la carpeta del proyecto y ejecutar:

```bash
python main.py
```

Después:

1. revisar las estaciones disponibles;
2. ingresar el origen;
3. ingresar el destino;
4. revisar la ruta encontrada y sus métricas.

## 6. Ejecución de pruebas

Ejecutar:

```bash
python pruebas.py
```

El programa ejecuta casos de prueba relacionados con:

- rutas entre diferentes estaciones;
- rutas con posibles transbordos;
- origen y destino iguales;
- estación inexistente.

## 7. Archivos principales

### `conocimiento.py`

Contiene los hechos y reglas que representan el conocimiento del sistema.

### `busqueda.py`

Contiene la implementación de A\* y la función heurística.

### `main.py`

Permite interactuar con el sistema mediante la consola.

### `pruebas.py`

Ejecuta casos de prueba para verificar el comportamiento del sistema.

## 8. Fuente de referencia de la red

TransMilenio. (2025). _Guía general de viaje de TransMilenio a corte de diciembre 2025_. https://www.transmilenio.gov.co/

La red académica no pretende reproducir todos los servicios ni condiciones operativas del sistema real.

## 9. Bibliografía académica

Benítez, R. (2014). _Inteligencia artificial avanzada_. Editorial UOC.

Corporación Universitaria Iberoamericana. (s. f.). _Bibliografía - Inteligencia Artificial_. https://campusvirtual.ibero.edu.co/repositorio/Cursos-Matriz/Ingenieria/Ingenieria-software/Inteligencia-Artificial/Inteligencia_artificial/index.html

Python Software Foundation. (s. f.). _heapq — Heap queue algorithm_. https://docs.python.org/3/library/heapq.html
