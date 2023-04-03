def llenado(numAlumnos):#SI SE LLENA
    matrix = []
    for i in range(numAlumnos):   
        print(f"Alumno {i+1}:")        
        a =[] 
        for j in range(4):
            if j == 0:
                print("Nombre: ")      
                a.append(input())
            else:
                print("Nota:",j)    
                a.append(int(input())) 
        matrix.append(a) 
    return  matrix


def mostrarAlumnos(lista,numAlumnos):
    nombreAlumnos = []
    for i in range(numAlumnos):
        for j in range(4): 
            print(lista[i][j], end = " ") #MOSTRAMOS LOS NOMBRES DE LOS ALUMNOS
        print()
    j=0
    for i in range(numAlumnos):
        nombreAlumnos.append(lista[i][j]) #GUARDAMOS LOS NOMBRES DE LOS ALUMNOS
    return nombreAlumnos
        

def promedio(lista,numAlumnos):#ARROJA EL PROMEDIO PERO NO EL NOMBRE DE LOS ALUMNOS
    listaPromedio = []
    for i in range(numAlumnos):
        total=0 
        for j in range(4):
            if j > 0: 
                total = total + lista[i][j]
                promedio = total/3
        listaPromedio.append(promedio)


    for i in listaPromedio:
        print(i)
  
    
    return listaPromedio


def alumnosAprobados(promedio,nombres):
    #for a in promedio:
    #    if a >= 7:
     #       print("Aprobado",a)
      #  contador += 1
    print(nombres[0],promedio[0])


def menu():
    while True:
        print('-------------------')
        print('Institucion Escolar')
        print('-------------------')
        print('[1]: Agregar alumnos')
        print("[2]: Mostrar los alumnos registrados")
        #print('[3]: Promedio de todos los alumnos')
        #print('[4]: Alumnos aprobados')
        #print('[5]: Alumnos reprobados')
        #print('[6]: Calificacion maxima por parcial')
        #print('[7]: Calificacion minima por parcial')
        #print('[8]: Promedio maximo')
        #print('[9]: Promedio minimo')
        print('[10]: Salir del programa')
        op = input('Opcion -> ')
        if op == '1':
            numAlumnos = int(input("Cuantos alumnos desea registrar: "))
            lista = llenado(numAlumnos)
        elif op == '2':
            nombres = mostrarAlumnos(lista,numAlumnos)
        elif op == '3':
            promedioGeneral = promedio(lista,numAlumnos)
        elif op == '4':
            alumnosAprobados(promedioGeneral,nombres)
        elif op == '10':
            break
menu()