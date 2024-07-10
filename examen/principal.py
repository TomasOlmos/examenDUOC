import funciones as fn
trabajadores = [ "Juan Pérez","María García","Carlos López",
                "Ana Martínez","Pedro Rodríguez","Laura Hernández",
                "Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández" ]

sueldos_trabajadores = {}

while True:
    try:
        print("------------ MENÚ ------------")
        print("0. Inicializar los sueldos")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        
        opcion = int(input("Ingrese una opción: "))

        if opcion == 0:
                sueldos_trabajadores = {trabajador : 0 for trabajador in trabajadores}
                print("Sueldos inicializados\n")
        elif opcion == 1:
            if not sueldos_trabajadores:
                print("Primero inicialice los sueldos.\n")
            else:
                sueldos_trabajadores = fn.asignar_sueldos_aleatorios(trabajadores)
        elif opcion == 2:
            if sueldos_trabajadores:
                fn.clasificar_sueldos(sueldos_trabajadores)
            else:
                print("Primero debe asignar los sueldos.")
        elif opcion == 3:
            if sueldos_trabajadores:
                sueldo_mas_alto,sueldo_mas_bajo,promedio_sueldos = fn.ver_estadisticas(sueldos_trabajadores)
                if sueldo_mas_alto is not None:
                    print("------------ ESTADÍSTICAS ------------\n")
                    print("Sueldo más alto $:",sueldo_mas_alto)
                    print("Sueldo más bajo $:",sueldo_mas_bajo)
                    print("Promedio de sueldos $:",promedio_sueldos)
                    print("Media geométrica de sueldos $: XXXX")
                    print()
            else:
                print("Primero debe asignar los sueldos.")
        elif opcion == 4:
            if sueldos_trabajadores:
                fn.reporte_de_sueldos(sueldos_trabajadores)
            else:
                print("Primero debe asignar los sueldos.")
        elif opcion == 5:
            print("------------------------------")
            print("Finalizando programa...")
            print("Desarrollado por Tomás Olmos")
            print("RUT 21.076.437-2")
            break
        else:
            print("Ingrese una opción válida, vuelva a intentarlo.")

    except ValueError:
        print("Ingrese un valor númerico y vuelva a intentarlo.")
