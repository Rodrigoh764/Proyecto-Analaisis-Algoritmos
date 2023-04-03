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
    nombreAlumnos = []
    for i in range(numAlumnos):
        for j in range(4): 
            print(lista[i][j], end = " ") 
        print()
        nombreAlumnos.append(lista[i][0])
    return nombreAlumnos
    
def promedioAlumno(lista,numAlumnos):
    listaPromedio = []
    for i in range(numAlumnos): 
        total = 0
        cont = 0
        for j in range(4):
            if j > 0:
                total = lista[i][j] + total
                promedio = total/3
        print(f"Estudiante: {lista[i][0]}")
        print(f"Promedio: {promedio}")
        listaPromedio.append(promedio)
    for p in listaPromedio:
        cont += p
    print()    
    print("--> Promedio General:")
    print(cont/numAlumnos)
    return listaPromedio

def alumnosAprobados(listaPromedio,numAlumnos,nombreAlumnos):
    cont = 0
    print("Aprobado")
    for i in range(numAlumnos):
        if listaPromedio[i] >= 7:
            print(nombreAlumnos[i], ":",listaPromedio[i])
            cont = cont + 1
    print(f"Alumnos aprobados: {cont}")
    
def alumnosReprobados(listaPromedio,numAlumnos,nombreAlumnos):
    cont = 0
    print("Reprobado")
    for i in range(numAlumnos):
        if listaPromedio[i] < 7:
            cont = cont + 1
            print(nombreAlumnos[i])
            print(listaPromedio[i])    
    print(cont)

def parcialMaximo(lista,numAlumnos):


    numMax = []
    for i in range(numAlumnos): 
        for j in range(4): 
                if j ==1:
                    numMax.append(lista[i][j])
                    
    print("Primer parcial",max(numMax))

    numMax = []
    for i in range(numAlumnos): 
        for j in range(4): 
                if j ==2:
                    numMax.append(lista[i][j])
    print("Segundo parcial",max(numMax))

    numMax = []
    for i in range(numAlumnos): 
        for j in range(4): 
                if j ==3:
                    numMax.append(lista[i][j])
    print("Tercer parcial",max(numMax))
                    
def parcialMinimo(lista,numAlumnos):
    numMin = []
    for i in range(numAlumnos): 
        for j in range(4): 
                if j ==1:
                    numMin.append(lista[i][j])
    print("Primer parcial",min(numMin))

    numMin = []
    for i in range(numAlumnos): 
        for j in range(4): 
                if j ==2:
                    numMin.append(lista[i][j])
    print("Segundo parcial",min(numMin))

    numMin = []
    for i in range(numAlumnos): 
        for j in range(4): 
                if j ==3:
                    numMin.append(lista[i][j])
    print("Tercer parcial",min(numMin))

def menu():
    while True:
        print('\n-------------------')
        print('Institucion Escolar')
        print('-------------------')
        print('[1]: Agregar alumnos')
        print("[2]: Mostrar los alumnos registrados")
        print('[3]: Promedio')
        print('[4]: Alumnos aprobados')
        print('[5]: Alumnos reprobados')
        print('[6]: Calificacion maximo por parcial')
        print('[7]: Calificacion minimo por parcial')
        print('[8]: Salir del programa')
        op = input('Opcion -> ')
        if op == '1':
            numAlumnos = int(input("\nCuantos alumnos desea registrar: "))
            lista = llenado(numAlumnos)
        elif op == '2':
            print("\n->Alumnos registrados")
            nombreAlumnos = mostrarAlumnos(lista,numAlumnos)
        elif op == '3':
            print("\n->Promedio")
            listaPromedio = promedioAlumno(lista,numAlumnos)
        elif op == '4':
            print("\n->Alumnos aprobados")
            alumnosAprobados(listaPromedio,numAlumnos,nombreAlumnos)
        elif op == '5':
            print("\n->Alumnos reprobados")
            alumnosReprobados(listaPromedio,numAlumnos,nombreAlumnos)
        elif op == '6':
            print("\n->Parcial Maximo")
            parcialMaximo(lista,numAlumnos)
        elif op == '10':
            break
menu()



