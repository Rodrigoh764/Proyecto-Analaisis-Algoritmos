def agregaAlumno():
    print("Agregar alumnos")

def calculaPromedio():
    print("Promedios")

def alumnosAprobados():
    print("Alumnos Aprobados")

def alumnosReprobados():
    print("Alumnos reporbados")

def calificacionMaxParcial():
    print("calificacion maxima del parcial")

def calificacionMinParcial():
    print("calificacion minima del parcial")

def promedioMax():
    print("Promedio maximo")

def promedioMin():
    print("promedio minimo")


def menu():
   
    while True:
        print('\nInstitucion Escolar ' '\n')
        print('[1]: Agregar alumnos')
        print('[2]: Promedio de todos los alumnos')
        print('[3]: Alumnos aprobados')
        print('[4]: Alumnos reprobados')
        print('[5]: Calificacion maxima por parcial')
        print('[6]: Calificacion minima por parcial')
        print('[7]: Promedio maximo')
        print('[8]: Promedio minimo')
        print('[9]: Salir del programa')
        op = input('Opcion -> ')
        if op == '1':
            agregaAlumno()
        elif op == '2':
            calculaPromedio()
        elif op == '3':
            alumnosAprobados()
        elif op == '4':
            alumnosReprobados()
        elif op == '5':
            calificacionMaxParcial()
        elif op == '6':
            calificacionMinParcial()
        elif op == '7':
            promedioMax()
        elif op == '8':
            promedioMin()
        elif op == '9':
            break


menu()