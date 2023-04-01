numAlumnos = int(input("cuantos alumnos: ")) 
materia = 3 
matrix = [] 
for i in range(numAlumnos):           
    a =[] 
    for j in range(materia+1):
        if j ==0:
                print("Nombre: ")      
                a.append(input())
        else:
            print("Nota:",j)    
            a.append(int(input())) 
    matrix.append(a) 


lista = []
for i in range(numAlumnos):
    total=0 
    for j in range(materia+1):
        if j > 0: 
            total = total + matrix[i][j]
    print("-->",total) 
    #lista.append(total)
#print(lista)
        

    
    


