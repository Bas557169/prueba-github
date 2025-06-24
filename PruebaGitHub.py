alumnos = []


while True:
    print("=== Menú ===")
    print("1. Agregar alumno")
    print("2. Mostrar todos los alumnos")
    print("3. Cerrar")
    
    opcion = input("Selecciona una opción (1/2/3):")

    if opcion == "1":
        
        nombre = input("Introduce el nombre del alumno:")
        alumnos.append(nombre)
        print(f"Alumno {nombre} agregado exitosamente\n")
    
    elif opcion == "2":
      
        if alumnos:
            print("Lista de alumnos:")
            for alumno in alumnos:
                print(alumno)
        else:
            print("No hay alumnos en la lista\n")
    
    elif opcion == "3":
        print("Cerrando el programa")
        break
    
    else:
        print("Opción no válida, por favor elige 1, 2 o 3\n")