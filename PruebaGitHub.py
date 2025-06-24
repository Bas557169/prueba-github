alumnos = []

while True:
    print("\n=== Menú ===")
    print("1. Agregar alumno")
    print("2. Mostrar todos los alumnos")
    print("3. Eliminar alumno")
    print("4. Cerrar")

    opcion = input("Selecciona una opción (1/2/3/4):")

    if opcion == "1":
        nombre = input("Introduce el nombre del alumno:")
        if nombre.isalpha():
            alumnos.append(nombre)
            print(f"Alumno '{nombre}' agregado exitosamente")
        else:
            print("El nombre debe contener solo letras")

    elif opcion == "2":
        if alumnos:
            print("\nLista de alumnos:")
            for idx, alumno in enumerate(alumnos, start=1):
                print(f"{idx}. {alumno}")
        else:
            print("No hay alumnos en la lista")

    elif opcion == "3":
        nombre = input("Introduce el nombre del alumno a eliminar:")
        if nombre in alumnos:
            alumnos.remove(nombre)
            print(f"Alumno '{nombre}' eliminado exitosamente")
        else:
            print(f"El alumno '{nombre}' no se encuentra en la lista")

    elif opcion == "4":
        print("Cerrando el programa")
        break

    else:
        print("Opción no válida, por favor elige 1, 2, 3 o 4")
