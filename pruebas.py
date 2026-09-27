"""
Pruebas del sistema inteligente de rutas.
"""

from busqueda import buscar_mejor_ruta


def ejecutar_prueba(nombre, origen, destino):
    """
    Ejecuta una prueba y muestra sus resultados.
    """

    resultado = buscar_mejor_ruta(
        origen,
        destino
    )

    print("=" * 70)
    print(nombre)
    print("=" * 70)

    print(f"Origen: {origen}")
    print(f"Destino: {destino}")

    if resultado["encontrada"]:

        print("Estado: EXITOSA")

        print(
            "Ruta:",
            " -> ".join(
                resultado["ruta"]
            )
        )

        print(
            "Costo:",
            resultado["costo"]
        )

        print(
            "Transbordos:",
            resultado["transbordos"]
        )

        print(
            "Nodos explorados:",
            resultado["nodos_explorados"]
        )

    else:

        print("Estado: CONTROLADA")

        print(
            "Mensaje:",
            resultado["mensaje"]
        )

    print()


def main():

    # ========================================================
    # PRUEBA 1
    # ========================================================

    ejecutar_prueba(
        "PRUEBA 1 - Ruta de Portal Américas a Portal Norte",
        "Portal Américas",
        "Portal Norte"
    )

    # ========================================================
    # PRUEBA 2
    # ========================================================

    ejecutar_prueba(
        "PRUEBA 2 - Ruta de Banderas a Calle 26",
        "Banderas",
        "Calle 26"
    )

    # ========================================================
    # PRUEBA 3
    # ========================================================

    ejecutar_prueba(
        "PRUEBA 3 - Ruta de Ricaurte a Calle 57",
        "Ricaurte",
        "Calle 57"
    )

    # ========================================================
    # PRUEBA 4
    # ========================================================

    ejecutar_prueba(
        "PRUEBA 4 - Origen y destino iguales",
        "Ricaurte",
        "Ricaurte"
    )

    # ========================================================
    # PRUEBA 5
    # ========================================================

    ejecutar_prueba(
        "PRUEBA 5 - Estación inexistente",
        "Estación Inexistente",
        "Portal Norte"
    )


if __name__ == "__main__":
    main()