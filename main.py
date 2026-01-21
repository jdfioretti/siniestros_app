# Punto de entrada de la aplicación.
# Maneja el menú y la interacción con el usuario.

from storage import leer_siniestros, guardar_siniestros

# Agrega un nuevo siniestro y lo guarda en el archivo JSON.
# No devuelve nada.


def alta_siniestro():
    siniestros = leer_siniestros()

    numero = input("Número de siniestro: ")
    fecha = input("Fecha (DD/MM/AAAA): ")
    asegurado = input("Nombre del asegurado: ")

    siniestro = {
        "numero": numero,
        "fecha": fecha,
        "asegurado": asegurado,
        "estado": "abierto",
    }

    siniestros.append(siniestro)
    guardar_siniestros(siniestros)

    print("Siniestro registrado exitosamente.")


# Muestra por pantalla todos los siniestros almacenados.
# No modifica el archivo JSON.


def listar_siniestros():
    siniestros = leer_siniestros()
    if not siniestros:
        print("No hay siniestros registrados.")
        return

    for siniestro in siniestros:
        print(
            f"Número: {siniestro['numero']}, Fecha: {siniestro['fecha']}, Asegurado: {siniestro['asegurado']}, Estado: {siniestro['estado']}"
        )


# Busca un siniestro por número y lo muestra por pantalla.
# Si no lo encuentra, informa al usuario.


def buscar_siniestros():
    siniestros = leer_siniestros()
    numero_buscar = input("Ingrese número de siniesto: ")

    # Recorre todos los siniestros hasta encontrar el número buscado
    for siniestro in siniestros:
        if siniestro["numero"] == numero_buscar:
            print("\nSiniestro encontrado:")
            print(f"Número: {siniestro['numero']}")
            print(f"Fecha: {siniestro['fecha']}")
            print(f"Asegurado: {siniestro['asegurado']}")
            print(f"Estado: {siniestro['estado']}")
            return
    # Si no hay siniestros cargados, se corta la función
    print("Siniestro no encontrado")


def mostrar_menu():
    print("\n--- Gestión de Siniestros ---")
    print("1. Alta de Siniestro")
    print("2. Listar Siniestros")
    print("3. Buscar Siniestro")
    print("0. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            alta_siniestro()
        elif opcion == "2":
            listar_siniestros()
        elif opcion == "3":
            buscar_siniestros()
        elif opcion == "0":
            print("Saliendo del sistema")
            break
        else:
            print("Funcionalidad en desarrollo")


if __name__ == "__main__":
    main()
