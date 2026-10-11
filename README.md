# Sistema inteligente de rutas de transporte

Proyecto académico en Python que representa una red simplificada de estaciones y aplica búsqueda heurística A* para encontrar rutas de menor costo. El repositorio también incluye ejercicios de aprendizaje supervisado y no supervisado.

> **Importante:** la red es un modelo académico simplificado. No es un planificador de viajes en tiempo real ni debe utilizarse para decisiones de desplazamiento.

## Estructura del proyecto

```text
ia_rutas_transmilenio/
├── src/
│   ├── main.py
│   ├── conocimiento.py
│   └── busqueda.py
├── tests/
│   └── pruebas.py
├── actividad_3_supervisado/
│   ├── src/
│   ├── tests/
│   ├── data/
│   ├── resultados/
│   └── docs/
├── actividad_4_no_supervisado/
│   ├── src/
│   ├── tests/
│   ├── data/
│   ├── resultados/
│   └── docs/
├── requirements.txt
└── README.md
```

## Requisitos

- Python 3.10 o superior.
- Para las actividades 3 y 4, instalar las dependencias de la actividad que se vaya a ejecutar.

## Ejecutar el sistema de rutas

Desde la raíz del repositorio:

```bash
python src/main.py
```

Para ejecutar las pruebas manuales del algoritmo de búsqueda:

```bash
python tests/pruebas.py
```

## Actividad 3: aprendizaje supervisado

Consulta [README de la Actividad 3](actividad_3_supervisado/README.md) para generar los datos, entrenar el árbol de decisión y ejecutar las pruebas.

## Actividad 4: aprendizaje no supervisado

Consulta [README de la Actividad 4](actividad_4_no_supervisado/README.md) para generar los datos, ejecutar K-Means y ejecutar las pruebas.

## Alcance y limitaciones

Los datos contextuales y las etiquetas de demora utilizados en las actividades de aprendizaje automático son sintéticos. Las métricas describen el comportamiento de los modelos sobre esos datos y no representan predicciones reales de TransMilenio.

## Referencias

- TransMilenio. (2025). *Guía general de viaje de TransMilenio a corte de diciembre 2025*. https://www.transmilenio.gov.co/
- Benítez, R. (2014). *Inteligencia artificial avanzada*. Editorial UOC.
- Corporación Universitaria Iberoamericana. (s. f.). *Bibliografía - Inteligencia Artificial*. https://campusvirtual.ibero.edu.co/repositorio/Cursos-Matriz/Ingenieria/Ingenieria-software/Inteligencia-Artificial/Inteligencia_artificial/index.html
- Python Software Foundation. (s. f.). *heapq — Heap queue algorithm*. https://docs.python.org/3/library/heapq.html
