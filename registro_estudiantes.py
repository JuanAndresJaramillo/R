import pickle
from functools import reduce

def ingresar_opcion(mensaje, opciones, numero_letras_respuesta):
    bandera = 0
    while bandera == 0:
        opcion_escogida = input(mensaje)
        try: 
            if opcion_escogida not in opciones or len(opcion_escogida) != numero_letras_respuesta:
                raise ValueError("Esta opcion no puede ser seleccionada")
        except ValueError as mes:  #En el if se evalua si la opcion ingresada si está en las posibles
            print('--'*30)      #opciones que se pueden escoger, estas posibles opciones son el
            print(mes)          #parametro de entrada 'opciones'
            print('--'*30)
        else:
            bandera = 1
    return opcion_escogida

def ingresar_nombre(mensaje):
    palabras_incorrectas = 1
    while palabras_incorrectas != 0:
        string = input(mensaje)
        string = string.split()  #para que acepte texto con espacios
        palabras_incorrectas = 0
        try:
            for i in string:     #Recorre todos los strings que separamos en listas para ver que sean
                if i.isalpha() == False:                                 #solo alfabeticos
                    palabras_incorrectas += 1
            if palabras_incorrectas != 0 :
                raise TypeError("Ingrese un nombre valido, sin numeros ni caracteres especiales")
        except TypeError as mes:
            print('--'*30)
            print(mes)
            print('--'*30)
    return ' '.join(string)   #Juntamos nuevamente los strings de las listas y lo retornamos

def ingresar_numero_real_rango(limite_inferior, limite_superior, mensaje):
    bandera = 0
    while (bandera == 0) :
        try :
            numero = float(input(mensaje))
            if numero < limite_inferior or numero > limite_superior :
                raise TypeError( f"Numero invalido, debe estar ente {limite_inferior} y {limite_superior}" )
        except TypeError as mes : #El TypeError se levanta cuando el numero no esta entre el rango pedido
            print('--'*30)
            print(mes)
            print('--'*30)
        except ValueError : #El valueError se da cuando se ingresa en 'numero' algo diferente a un numero
            print('--'*30)
            print("Error")
            print('--'*30)
        else :
            bandera = 1     
    return numero

def ingresar_edad(mensaje):
    bandera = 0
    while (bandera == 0):
        try:
            numero = int( input( mensaje ) )
            if numero < 15 or numero > 80 :
                raise TypeError("Edad del estudiante invalida")
        except TypeError as mes :
            print('--'*30)
            print( mes )
            print('--'*30)
        except ValueError : #Se levanta el ValueError cuando se ingresa una edad alfanumerica o flotante
            print('--'*30)
            print("ERROR")
            print('--'*30)
        else:
            bandera = 1
    return numero

def mostrar_menu():
    print(f'\n', '*'*6, 'MENU', '*'*6)
    print(' 1. Registrar estudiantes\n',
          '2. Consultar estudiantes de una carrera\n',
          '3. Calcular promedio general\n',
          '4. Ver estudiantes destacados\n',
          '5. Guardar y salir\n')

def mostrar_carreras():
    carreras = {'1' : 'Ingenieria de productividad y calidad',
                '2' : 'Ingenieria agropecuaria',
                '3' : 'Ingenieria civil',
                '4' : 'Ingenieria en seguridad y salud en el trabajo',
                '5' : 'Ingenieria en automatización y control',
                '6' : 'Ingenieria informatica'}
    print("\nSeleccione una carrera de la siguiente lista \n")
    for i, j in carreras.items(): #Para recorrer el diccionario e imprimirlo
        print( f'{i}. {j}' )

def escoger_carrera(opc):
    carreras = {'1' : 'Ingenieria de productividad y calidad',
                '2' : 'Ingenieria agropecuaria',
                '3' : 'Ingenieria civil',
                '4' : 'Ingenieria en seguridad y salud en el trabajo',
                '5' : 'Ingenieria en automatización y control',
                '6' : 'Ingenieria informatica'}
    carrera = carreras[opc] #Según el key que mete el usuario se le asigna la carrera correspondiente
    return carrera

def registrar_estudiante() :
    nombre = ingresar_nombre("Nombre:(Ingrese primero los apellidos y luego los nombres) ")
    nombre = nombre.title()
    edad = ingresar_edad("Edad: ")
    mostrar_carreras()
    opcion = ingresar_opcion("\nRecuerde seleccionar el numero correspondiente a la carrera: ", "123456", 1)
    carrera = escoger_carrera(opcion)
    promedio = ingresar_numero_real_rango(0, 5, "Promedio = ")
    estudiante = {'nombre' : nombre,
                  'edad' : edad,
                  'carrera' : carrera,
                  'promedio' : promedio} #Cada estudiante queda registrado en un diccionario
    return estudiante

def guardar_estudiante(estudiante, base_de_datos) :
    base_de_datos.append(estudiante)

def mostrar_estudiantes(base_de_datos):
    mostrar_carreras()
    opcion = ingresar_opcion("\n Recuerde seleccionar solo el numero correspondiente a la carrera: ", "123456", 1)
    carrera = escoger_carrera(opcion)
    lista_estudiantes = []
    for i in base_de_datos :  #Se recorre toda la base de datos buscando los estudiantes de la carrera
        if i['carrera'] == carrera :                   #seleccionada
            lista_estudiantes.append(i['nombre'])
    lista_estudiantes.sort() #Organiza los nombres en orden alfabetico
    try :
        print('\n')
        for estudiante in lista_estudiantes  : #Para imprimir la lista de estudiantes
            print(estudiante)
        if len(lista_estudiantes) == 0 :
            raise ValueError('No hay estudiantes registrados en esta carrera')
    except ValueError as mes :
        print('--'*30)
        print(mes)
        print('--'*30)

def calcular_promedio(base_de_datos) :
    promedios = []
    try :
        for element in base_de_datos :
            promedios.append(element['promedio']) #Se crea una nueva lista con todos los promedios
        promedio_general = (reduce(lambda a,b : a+b, promedios))/len(promedios) #Se suman todos los promedios
        print(f'\nEl promedio general es de {round(promedio_general, 2)}') #y se divide por el tamaño de la lista
    except TypeError :
        print('--'*30)
        print("No hay estudiantes registrados todavia")
        print('--'*30)

def mostrar_sobresalientes(base_de_datos) :
    try:
        tupla = tuple(filter(lambda dicc : dicc['promedio'] >= 4.5, base_de_datos)) #Para filtrar los estudiantes
        for diccionario in tupla :                                       #sobresalientes y se guardan en una tupla
            print('*'*80)
            for i, j in diccionario.items() : #Se imprime cada elemento del diccionario
                print( f'{i} = {j}' )
        if len(base_de_datos) == 0 :
            raise ValueError("No hay estudiantes registrados todavia")
    except ValueError as mes :
        print('--'*30)
        print(mes)
        print('--'*30)

def main() :
    registro_estudiantes = []
    try :
        archivo = open('estudiantes.pkl', 'rb')  #Se abre la base de datos
        registro_estudiantes = pickle.load(archivo) #Se carga con info previa
    except FileNotFoundError :
        pass

    print(f'\nLa base de datos esta cargada con {len(registro_estudiantes)} estudiantes')
    
    while True :  #Ciclo infinito
        mostrar_menu()
        opcion_menu = ingresar_opcion("Que acción quiere realizar: ", '12345', 1)
        if opcion_menu == '1' :
            estudiante = registrar_estudiante()
            guardar_estudiante(estudiante, registro_estudiantes)
            print('\nEl estudiante se ha registrado correctamente')
        elif opcion_menu == '2' :
            mostrar_estudiantes(registro_estudiantes)
        elif opcion_menu == '3' :
            calcular_promedio(registro_estudiantes)
        elif opcion_menu == '4' :
            print('\n')
            mostrar_sobresalientes(registro_estudiantes)
        elif opcion_menu == '5' :
            arch = open('estudiantes.pkl', 'wb')
            pickle.dump(registro_estudiantes, arch) #Siempre que sale guarda la info en estudiantes.pkl
            print('\n¡Hasta pronto!')
            break

if __name__ == '__main__' :
    main()
