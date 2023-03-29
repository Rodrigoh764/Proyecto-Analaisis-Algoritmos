class Alumno:
    def __init__(self,serie, nombre,nota1,nota2,nota3):
        self.serie = serie
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
    def __str__(self):
        return f'{self.nombre} Notas:[{self.nota1}-{self.nota2}-{self.nota3}]'
    
class Escuela:
    
    def __init__(self):
        self.listaEstudiantes = []

    def agregaAlumno(self, nombre):
        self.listaEstudiantes.append(nombre)


    
    def mostrarAlumnos(self):
        for p in self.listaEstudiantes:
            print(p)



def menu(escuela):
    cont = len(escuela.listaEstudiantes)
    while True:
        print('\nInstitucion Escolar ' '\n')
        print('[1]: Agregar alumnos')
        print("[2]: Mostrar los alumnos registrados")
        print('[3]: Promedio de todos los alumnos')
        print('[4]: Alumnos aprobados')
        print('[5]: Alumnos reprobados')
        print('[6]: Calificacion maxima por parcial')
        print('[7]: Calificacion minima por parcial')
        print('[8]: Promedio maximo')
        print('[9]: Promedio minimo')
        print('[10]: Salir del programa')
        op = input('Opcion -> ')
        if op == '1':
            nombre = input("Introduce el nombre del alumno:\n")
            nota1 = input("califcacion de la nota 1:\n")
            nota2 = input("califcacion de la nota 2:\n")
            nota3 = input("califcacion de la nota 3:\n")
            escuela.agregaAlumno(Alumno(cont+1, nombre,nota1,nota2,nota3))
            
                
            cont+=1
        elif op == '2':
            print("\nLista de alumnos inscritos\n")
            escuela.mostrarAlumnos()
        elif op == '10':      
            break


escuela = Escuela()

menu(escuela)