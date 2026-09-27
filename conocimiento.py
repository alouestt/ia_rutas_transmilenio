"""
Base de conocimiento del sistema inteligente de rutas.

El proyecto utiliza una red académica reducida inspirada en estaciones
y corredores documentados por TransMilenio. No representa el estado
operativo en tiempo real del sistema.
"""

# Conjunto de estaciones disponibles en la base de conocimiento.
ESTACIONES = {
    "Portal Américas",
    "Banderas",
    "Mandalay",
    "Marsella",
    "Zona Industrial",
    "Ricaurte",
    "Calle 19",
    "Calle 26",
    "Calle 45",
    "Calle 63",
    "Calle 72",
    "Paloquemao",
    "Universidad Nacional",
    "Calle 57",
    "Calle 85",
    "Calle 100",
    "Calle 127",
    "Portal Norte",
}


# ============================================================
# HECHOS DE LA BASE DE CONOCIMIENTO
# ============================================================

# Cada tupla representa una conexión entre dos estaciones:
#
# (estación_origen, estación_destino, corredor)
#
# Estas conexiones representan los hechos que conoce el sistema.

CONEXIONES = [

    # Corredor Américas
    ("Portal Américas", "Banderas", "Américas"),
    ("Banderas", "Mandalay", "Américas"),
    ("Mandalay", "Marsella", "Américas"),
    ("Marsella", "Zona Industrial", "Américas"),
    ("Zona Industrial", "Ricaurte", "Américas"),
    ("Ricaurte", "Calle 19", "Américas"),
    ("Calle 19", "Calle 26", "Américas"),
    ("Calle 26", "Calle 45", "Américas"),
    ("Calle 45", "Calle 63", "Américas"),
    ("Calle 63", "Calle 72", "Américas"),

    # Corredor NQS
    ("Ricaurte", "Paloquemao", "NQS"),
    ("Paloquemao", "Universidad Nacional", "NQS"),
    ("Universidad Nacional", "Calle 57", "NQS"),
    ("Calle 57", "Calle 63", "NQS"),

    # Corredor Caracas
    ("Calle 63", "Calle 72", "Caracas"),
    ("Calle 72", "Calle 85", "Caracas"),
    ("Calle 85", "Calle 100", "Caracas"),
    ("Calle 100", "Calle 127", "Caracas"),
    ("Calle 127", "Portal Norte", "Caracas"),
]


# ============================================================
# COORDENADAS PARA LA HEURÍSTICA
# ============================================================

# Son coordenadas simplificadas utilizadas únicamente para
# orientar el algoritmo de búsqueda.
#
# NO representan coordenadas geográficas reales.

COORDENADAS = {
    "Portal Américas": (0, 0),
    "Banderas": (1, 0),
    "Mandalay": (2, 0),
    "Marsella": (3, 0),
    "Zona Industrial": (4, 0),
    "Ricaurte": (5, 0),
    "Calle 19": (6, 0),
    "Calle 26": (7, 0),
    "Calle 45": (8, 0),
    "Calle 63": (8, 0.5),
    "Calle 72": (9, 0.5),
    "Paloquemao": (5, 0.5),
    "Universidad Nacional": (6, 0.5),
    "Calle 57": (7, 0.5),
    "Calle 85": (9.5, 1),
    "Calle 100": (10, 1.5),
    "Calle 127": (10.5, 2),
    "Portal Norte": (11, 2.5),
}


# ============================================================
# REGLAS DEL SISTEMA
# ============================================================

def regla_estacion_valida(estacion):
    """
    Regla 1:
    Una estación es válida si pertenece a la base de conocimiento.
    """

    return estacion in ESTACIONES


def regla_conexion_valida(origen, destino):
    """
    Regla 2:
    Existe un movimiento permitido si existe una conexión
    directa entre las dos estaciones.
    """

    return any(
        (a == origen and b == destino)
        or (a == destino and b == origen)
        for a, b, _ in CONEXIONES
    )


def regla_transbordo(linea_actual, nueva_linea):
    """
    Regla 3:
    Existe un transbordo cuando cambia el corredor utilizado.
    """

    return (
        linea_actual is not None
        and nueva_linea is not None
        and linea_actual != nueva_linea
    )


def obtener_vecinos(estacion):
    """
    Regla de inferencia:

    Si existe un hecho de conexión entre una estación y otra,
    entonces esa otra estación es un movimiento posible.

    Retorna:
        [(estacion_vecina, corredor), ...]
    """

    vecinos = []

    for origen, destino, linea in CONEXIONES:

        if origen == estacion:
            vecinos.append((destino, linea))

        elif destino == estacion:
            vecinos.append((origen, linea))

    return vecinos