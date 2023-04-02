def llenado(numAlumnos):
    matrix = []
    for i in range(numAlumnos):
        print(f"Alumno {i+1}:")
        a = []           
        for j in range(4):
            if j == 0:
                nombre = input("Nombre: ") 
                a.append(nombre)
                if nombre == "":
                    print("Nombre no puede estar vacio")
                    nombre = input("Nombre: ")
                    a.append(nombre)
            else:
                nota = float(input(f"Nota {j}: "))
                if 0 < nota > 10:
                    print("La calificación debe ser entre 0-10")
                    nota = float(input(f"Nota {j}: "))
                    a.append(nota)
                else:
                    a.append(nota)
        matrix.append(a)
    return matrix
    

def mostrarAlumnos(lista,numAlumnos):
    for i in range(numAlumnos):
        for j in range(4): 
            print(lista[i][j], end = " ") 
        print()


def promedioAlumno(lista,numAlumnos):
    listaPromedio = []
    for i in range(numAlumnos): 
        total = 0
        for j in range(4):
            if j > 0:
                total = lista[i][j] + total
                promedio = total/3
        print(f"Estudiante: {lista[i][0]}")
        listaPromedio.append(lista[i][0])
        print(f"Promedio: {promedio}")
        listaPromedio.append(promedio)
    print(listaPromedio)
    return listaPromedio


def promedioGeneral(listaPromedio,numAlumnos):
    promedioGeneral = 0
    for i in range(numAlumnos):
        promedioGeneral += listaPromedio[i]
    print(f"Alumnos en total: {numAlumnos}")
    promedioGeneral = promedioGeneral/numAlumnos
    print (f"--> {promedioGeneral}")


#def alumnosAprobados():



def menu():
    while True:
        print('\n-------------------')
        print('Institucion Escolar')
        print('-------------------')
        print('[1]: Agregar alumnos')
        print("[2]: Mostrar los alumnos registrados")
        print('[3]: Promedio')
        print('[4]: Alumnos aprobados')
        #print('[5]: Alumnos reprobados')
        #print('[6]: Calificacion maxima por parcial')
        #print('[7]: Calificacion minima por parcial')
        #print('[8]: Promedio maximo')
        #print('[9]: Promedio minimo')
        #print('[10]: Salir del programa')
        op = input('Opcion -> ')
        if op == '1':
            numAlumnos = int(input("\nCuantos alumnos desea registrar: "))
            lista = llenado(numAlumnos)
        elif op == '2':
            print("\n>Alumnos registrados")
            mostrarAlumnos(lista,numAlumnos)
        elif op == '3':
            print("\n>Promedio por alumno")
            listaPromedio = promedioAlumno(lista,numAlumnos)
            print("\>Promedio general")
            #promedioGeneral(listaPromedio,numAlumnos)
        elif op == '4':
            print("\n>Alumnos aprobados")
            #alumnosAprobados(promedioGeneral,nombres)
        elif op == '10':
            break
menu()



