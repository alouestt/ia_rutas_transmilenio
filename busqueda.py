"""
Algoritmo de búsqueda A* para encontrar una ruta de menor costo.
"""

import heapq
import math

from conocimiento import (
    COORDENADAS,
    regla_estacion_valida,
    regla_transbordo,
    obtener_vecinos,
)


# Penalización agregada al costo cuando se realiza un transbordo.
PENALIZACION_TRANSBORDO = 2


def heuristica(origen, destino):
    """
    Calcula una estimación del costo restante entre dos estaciones.

    Se utiliza la distancia euclidiana sobre las coordenadas
    topológicas simplificadas de la base de conocimiento.
    """

    x1, y1 = COORDENADAS[origen]
    x2, y2 = COORDENADAS[destino]

    distancia = math.sqrt(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2
    )

    return distancia


def reconstruir_ruta(padres, estado_final):
    """
    Reconstruye la ruta encontrada por el algoritmo
    utilizando los estados padres almacenados.
    """

    ruta = []

    estado = estado_final

    while estado is not None:

        estacion, _ = estado

        ruta.append(estacion)

        estado = padres.get(estado)

    ruta.reverse()

    return ruta


def buscar_mejor_ruta(origen, destino):
    """
    Ejecuta el algoritmo de búsqueda A*.

    Criterios de costo:

    - 1 unidad por cada desplazamiento entre estaciones.
    - 2 unidades adicionales por cada transbordo.

    Retorna información sobre:

    - Ruta encontrada.
    - Costo total.
    - Número de transbordos.
    - Cantidad de nodos explorados.
    """

    # ========================================================
    # VALIDACIÓN DEL ORIGEN
    # ========================================================

    if not regla_estacion_valida(origen):

        return {
            "encontrada": False,
            "mensaje": (
                f"La estación de origen '{origen}' "
                "no existe en la base de conocimiento."
            )
        }

    # ========================================================
    # VALIDACIÓN DEL DESTINO
    # ========================================================

    if not regla_estacion_valida(destino):

        return {
            "encontrada": False,
            "mensaje": (
                f"La estación de destino '{destino}' "
                "no existe en la base de conocimiento."
            )
        }

    # ========================================================
    # CASO: ORIGEN Y DESTINO SON IGUALES
    # ========================================================

    if origen == destino:

        return {
            "encontrada": True,
            "ruta": [origen],
            "costo": 0,
            "transbordos": 0,
            "nodos_explorados": 1
        }

    # ========================================================
    # ESTADO INICIAL
    # ========================================================

    # Un estado contiene:
    #
    # (estación actual, línea utilizada para llegar)

    estado_inicial = (origen, None)

    # Cola de prioridad utilizada por A*.
    frontera = []

    contador = 0

    # ========================================================
    # AGREGAR ESTADO INICIAL
    # ========================================================

    heapq.heappush(
        frontera,
        (
            heuristica(origen, destino),
            0,
            contador,
            estado_inicial
        )
    )

    # Costos acumulados conocidos.
    costos = {
        estado_inicial: 0
    }

    # Permite reconstruir posteriormente la ruta.
    padres = {
        estado_inicial: None
    }

    # Número de transbordos realizados.
    transbordos_estado = {
        estado_inicial: 0
    }

    # Contador de nodos explorados.
    explorados = 0

    # ========================================================
    # BÚSQUEDA A*
    # ========================================================

    while frontera:

        _, costo_actual, _, estado_actual = heapq.heappop(
            frontera
        )

        estacion_actual, linea_actual = estado_actual

        # Si encontramos una versión más costosa del mismo estado,
        # se descarta.
        if costo_actual != costos.get(estado_actual):

            continue

        explorados += 1

        # ====================================================
        # DESTINO ENCONTRADO
        # ====================================================

        if estacion_actual == destino:

            ruta = reconstruir_ruta(
                padres,
                estado_actual
            )

            return {
                "encontrada": True,
                "ruta": ruta,
                "costo": costo_actual,
                "transbordos": transbordos_estado[
                    estado_actual
                ],
                "nodos_explorados": explorados
            }

        # ====================================================
        # EXPLORAR ESTACIONES VECINAS
        # ====================================================

        for vecino, nueva_linea in obtener_vecinos(
            estacion_actual
        ):

            # Determinar si el movimiento genera un transbordo.
            es_transbordo = regla_transbordo(
                linea_actual,
                nueva_linea
            )

            # Cada desplazamiento tiene un costo base de 1.
            costo_movimiento = 1

            # Si existe transbordo, se agrega la penalización.
            if es_transbordo:

                costo_movimiento += PENALIZACION_TRANSBORDO

            # Calcular el nuevo costo acumulado.
            nuevo_costo = (
                costo_actual +
                costo_movimiento
            )

            # El estado incluye la nueva estación
            # y el corredor utilizado.
            nuevo_estado = (
                vecino,
                nueva_linea
            )

            # =================================================
            # ¿ENCONTRAMOS UNA MEJOR RUTA?
            # =================================================

            if nuevo_costo < costos.get(
                nuevo_estado,
                float("inf")
            ):

                contador += 1

                costos[nuevo_estado] = nuevo_costo

                padres[nuevo_estado] = estado_actual

                transbordos_estado[nuevo_estado] = (
                    transbordos_estado[estado_actual]
                    + int(es_transbordo)
                )

                # f(n) = g(n) + h(n)
                #
                # g(n) = costo acumulado
                # h(n) = estimación del costo restante

                prioridad = (
                    nuevo_costo +
                    heuristica(
                        vecino,
                        destino
                    )
                )

                heapq.heappush(
                    frontera,
                    (
                        prioridad,
                        nuevo_costo,
                        contador,
                        nuevo_estado
                    )
                )

    # ========================================================
    # NO SE ENCONTRÓ UNA RUTA
    # ========================================================

    return {
        "encontrada": False,
        "mensaje": (
            "No se encontró una ruta entre "
            "las estaciones seleccionadas."
        ),
        "nodos_explorados": explorados
    }