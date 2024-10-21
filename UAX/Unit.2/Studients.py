nota = int(input("introduce la nota del alumno: "))
asistencia = int(input("introduce el numero de asistencias: "))

if nota >= 70:
    print("ha aprobado el examen")
    if asistencia*100/40 > 80:
        print("y la asistencia es suficiente por lo que el alumno ha pasado")
    else:
        print("a causa de faltas el alumno ha suspendido")