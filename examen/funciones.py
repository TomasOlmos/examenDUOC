import statistics
import random
import csv

def asignar_sueldos_aleatorios(trabajadores):
    sueldos_trabajadores = {}
    for trabajador in trabajadores:
        sueldo = random.randint(300000,2500000)
        sueldos_trabajadores[trabajador] = sueldo
    print("Sueldos asignados aleatoriamente.")
    print(sueldos_trabajadores)
    return(sueldos_trabajadores)

def clasificar_sueldos(sueldos_trabajadores):
    menor_800000 = {}
    entre_800000_2000000 = {}
    mayor_2000000 = {}

    for trabajador,sueldo in sueldos_trabajadores.items():
        if sueldo < 800000:
            menor_800000[trabajador] = sueldo
        elif sueldo <= 2000000:
            entre_800000_2000000[trabajador] = sueldo
        else:
            sueldo > 2000000
            mayor_2000000[trabajador] = sueldo
    print()
    print("Sueldos mayores a $800.000 / TOTAL: ",len(menor_800000))
    print()
    print("Nombre empleado        ","Sueldo ")
    for trabajador,sueldo in menor_800000.items():
        print(trabajador,"        $",sueldo)

    print()
    print("Sueldos entre $800.000 y $2.000.000 / TOTAL: ",len(entre_800000_2000000))
    print()
    print("Nombre empleado        ","Sueldo ")
    for trabajador,sueldo in entre_800000_2000000.items():
        print(trabajador,"        $",sueldo)

    print()
    print("Sueldos mayores a $2.000.000 / TOTAL: ",len(mayor_2000000))
    print()
    print("Nombre empleado        ","Sueldo ")
    for trabajador,sueldo in mayor_2000000.items():
        print(trabajador,"        $",sueldo)

    print("TOTAL SUELDOS: $ XXXX")

def ver_estadisticas(sueldos_trabajadores):
    sueldo = list(sueldos_trabajadores.values())
    if not sueldo:
        print("No se han asignado sueldos.")
        return None,None,None,None
    
    sueldo_mas_alto = max(sueldo)
    sueldo_mas_bajo = min(sueldo)
    promedio_sueldos = sum(sueldo) / len(sueldo)

    return sueldo_mas_alto,sueldo_mas_bajo,promedio_sueldos

def reporte_de_sueldos(sueldos_trabajadores):

    # for sueldo in sueldos_trabajadores:
    #     descSalud = sueldo * 0.7
    #     descAFP = sueldo * 0.12
    #     sueldoLiquido = sueldo - descAFP - descSalud
    #         Traceback (most recent call last):
    # File "c:\Users\vina\Desktop\examen\principal.py", line 47, in <module>
    #     fn.reporte_de_sueldos(sueldos_trabajadores)
    # File "c:\Users\vina\Desktop\examen\funciones.py", line 66, in reporte_de_sueldos
    #     descSalud = sueldo * 0.7
    #                 ~~~~~~~^~~~~
    # TypeError: unsupported operand type(s) for *: 'type' and 'float'

    # with open("reporte_de_sueldos.csv","w",newline="") as archivo:
    #     escritor = csv.writer(archivo,delimiter=",")
    #     escritor.writerow(["Nombre trabajador","Sueldo Base","Descuento Salud","Descuento AFP","Sueldo Líquido"])
    #     for trabajador,sueldo in sueldos_trabajadores.items():
    #         escritor.writerow([trabajador,sueldo,descSalud,descAFP,sueldoLiquido])

    with open("reporte_de_sueldos.csv","w",newline="") as archivo:
        escritor = csv.writer(archivo,delimiter=",")
        escritor.writerow(["Nombre trabajador","Sueldo"])
        for trabajador,sueldo in sueldos_trabajadores.items():
            escritor.writerow([trabajador,sueldo])

    print("-------- GENERANDO REPORTE, POR FAVOR ESPERE --------")
    print("Reporte de sueldos generado en reporte_de_sueldos.csv")

            

    
