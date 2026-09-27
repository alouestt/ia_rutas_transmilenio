"""
Sistema inteligente de rutas de transporte.

Punto de entrada principal del proyecto.
"""

from busqueda import buscar_mejor_ruta
from conocimiento import ESTACIONES


def mostrar_estaciones():
    """
    Muestra las estaciones disponibles en la base de conocimiento.
    """

    print("\nESTACIONES DISPONIBLES")
    print("-" * 30)

    for estacion in sorted(ESTACIONES):
        print(f"- {estacion}")


def mostrar_resultado(origen, destino, resultado):
    """
    Muestra en pantalla el resultado de la búsqueda.
    """

    print("\n" + "=" * 50)
    print("RESULTADO DE LA BÚSQUEDA")
    print("=" * 50)

    print(f"Origen: {origen}")
    print(f"Destino: {destino}")

    # Si no se encuentra una ruta o existe algún problema
    # con las estaciones ingresadas.
    if not resultado["encontrada"]:

        print(
            f"\n{resultado['mensaje']}"
        )

        return

    # Mostrar la ruta.
    print("\nRuta encontrada:")

    print(
        " → ".join(
            resultado["ruta"]
        )
    )

    # Mostrar información adicional.
    print(
        f"\nNúmero de estaciones: "
        f"{len(resultado['ruta'])}"
    )

    print(
        f"Desplazamientos: "
        f"{len(resultado['ruta']) - 1}"
    )

    print(
        f"Transbordos: "
        f"{resultado['transbordos']}"
    )

    print(
        f"Costo total: "
        f"{resultado['costo']}"
    )

    print(
        f"Nodos explorados: "
        f"{resultado['nodos_explorados']}"
    )

    # Explicación del criterio utilizado.
    print("\nCriterio:")

    print(
        "Se selecciona la ruta con menor costo "
        "considerando 1 unidad por desplazamiento "
        "y una penalización de 2 unidades por "
        "cada transbordo."
    )


def main():

    print("=" * 50)
    print("SISTEMA INTELIGENTE DE RUTAS")
    print("Transporte masivo - prototipo académico")
    print("=" * 50)

    # Mostrar las estaciones conocidas.
    mostrar_estaciones()

    # Solicitar información al usuario.
    origen = input(
        "\nIngrese la estación de origen: "
    ).strip()

    destino = input(
        "Ingrese la estación de destino: "
    ).strip()

    # Ejecutar la búsqueda.
    resultado = buscar_mejor_ruta(
        origen,
        destino
    )

    # Mostrar los resultados.
    mostrar_resultado(
        origen,
        destino,
        resultado
    )


# Punto de entrada del programa.
if __name__ == "__main__":
    main()