# Mapa conceptual: Inteligencia artificial aplicada a rutas de TransMilenio

```mermaid
flowchart TD
    A["Inteligencia artificial aplicada a rutas de TransMilenio"]

    A --> B["Búsqueda informada y no informada"]
    A --> C["Actividad 3: Aprendizaje supervisado"]
    A --> D["Actividad 4: Aprendizaje no supervisado"]
    A --> E["Datos y evaluación"]

    B --> B1["Base de conocimiento"]
    B --> B2["Estaciones y conexiones"]
    B --> B3["Algoritmos de búsqueda"]
    B3 --> B4["Exploración de rutas"]
    B4 --> B5["Ruta encontrada y costo"]

    C --> C1["Datos etiquetados"]
    C1 --> C2["Generación de datos sintéticos"]
    C2 --> C3["Variables predictoras"]
    C3 --> C4["Árbol de decisión"]
    C4 --> C5["Clasificación de demora"]
    C5 --> C6["Baja, media o alta"]
    C4 --> C7["Evaluación del modelo"]
    C7 --> C8["Exactitud y matriz de confusión"]

    D --> D1["Datos sin etiquetas objetivo"]
    D1 --> D2["Preparación de variables"]
    D2 --> D3["Codificación cíclica de la hora"]
    D3 --> D4["Algoritmo K-Means"]
    D4 --> D5["Agrupación de viajes"]
    D5 --> D6["Perfiles de clústeres"]
    D4 --> D7["Coeficiente de silueta"]

    E --> E1["Paradas y transbordos"]
    E --> E2["Costo y horario"]
    E --> E3["Condición de lluvia"]
    E --> E4["Pruebas unitarias"]
    E --> E5["Archivos CSV de resultados"]

    B5 --> E4
    C8 --> E4
    D7 --> E4
    C5 --> E5
    D5 --> E5
```

## Interpretación

El proyecto integra tres enfoques. La búsqueda de rutas permite encontrar recorridos entre estaciones conectadas. El aprendizaje supervisado utiliza datos sintéticos etiquetados para clasificar el nivel simulado de demora mediante un árbol de decisión. El aprendizaje no supervisado aplica K-Means para descubrir grupos de viajes con características similares.

La evaluación se apoya en pruebas unitarias, métricas de clasificación y el coeficiente de silueta. Los resultados se almacenan en archivos CSV para su consulta.

**Alcance:** los resultados de aprendizaje automático se basan en datos sintéticos y no representan predicciones validadas sobre la operación real de TransMilenio.
