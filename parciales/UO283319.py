# Se han definido nuevos módulos que no estaban requeridos por el enunciado con el objetivo de simplificar
# el main y hacer mejor uso de las funciones: nuevaCadena() es un input que dependiendo de la cadena que
# se le pasa, imprime un mensaje apropiado para cada uso en pantalla para el usuario.
# nuevoNumero() y nuevoNumeroEnfermos() hacen lo mismo pero para enteros.
# Todas estas funciones comprueban que el valor introducido no sea inváildo, es decir, que las cadenas no sean vacías,
# o que los números no sean negativos y demás comprobaciones para evitar errores.
# NO se han programado otras limitaciones más complejas como comprobar que los archivos tengan extensión o que los
# médicos sigan la misma estructura de nombre (ej: "Médico Pepito") porque se sale de los objetivos de la práctica.
# Al final de cada función principal del programa, se imprime una línea por pantalla para que el usuario tenga
# algo de feedback sobre lo que se acaba de hacer.
# Se siguen todas las estructuras de nombres impuestas por el enunciado.
# Las posiciones de los médicos y de sus enfermos comienzan en "0". Esto se tiene que tener en cuenta a la hora de
# indicar el médico que editar, eliminar, etc. Se podría solucionar fácilmente añadiendo o restando 1 a la posición
# en varios puntos del programa de modo que es más intuitivo, pero como la posición se imprime junto al médico siempre,
# no es necesario.
# Al comienzo del main se establecen unos valores de ejemplo para las listas, pero el programa funciona como debería
# si las listas se inicializan vacías.
# Las listas siempre mantienen en la misma posición al médico y a su número de enfermos, por lo que
# len(listaMedicos) == len(listaEnfermos)

def nuevaCadena(cadena):
    output = ""
    if cadena == "nombre":
        output = input("Introduzca el nombre del médico: ")
    elif cadena == "archivoLeer":
        output = input("Introduzca el nombre del archivo a leer (incluyendo su extensión): ")
    elif cadena == "archivoGuardar":
        output = input("Introduzca el nombre del archivo a guardar (incluyendo su extensión): ")
    while output == "":
        output = input("Valor inválido, inténtelo de nuevo: ")
    return output


def nuevoNumeroEnfermos():
    numEnfermos = int(input("Introduzca el nuevo número de enfermos: "))
    while numEnfermos<=0:
        numEnfermos = int(input("Valor inválido, introduzca el nuevo número de enfermos: "))
    return numEnfermos

def nuevoNumero():
    numDeseado = int(input("Introduzca el número de la posición del médico que se quiere editar: "))
    while not numDeseado>=0 and numDesea    do<=len(listaMedicos):
        numDeseado = int(input("Valor inválido, inténtelo de nuevo: "))
    return numDeseado

#Desarrollar un modulo en python con las siguientes funciones:
#(1 puntos) Alta_medico_hospital, recibe dos listas una con la lista de medicos otra con la lista de número de enfermos,
#   una cadena de texto que representa el nombre del medico y un valor numérico que indica su número de enfermos.
#   La función añade el nuevo medico y número de enfermos a la lista de medicos y número de enfermos correspondientes
def Alta_medico_hospital(listMedicos, listEnfermos, newMedico, newEnfermos):
    listMedicos.append(newMedico)
    listEnfermos.append(newEnfermos)
    print("Elemento añadido correctamente.")

#(1 puntos) Baja_medico_hospital, recibe dos listas una con la lista de medicos otra con la lista de número de enfermos
#   y un numero entero que representa el medico a eliminar, elimina de las listas el medico indicado, el valor
#   numérico representa el índice en las listas.
def Baja_medico_hospital(listMedicos, listEnfermos, num):
    listMedicos.pop(num)
    listEnfermos.pop(num)
    print("Elemento eliminado correctamente.")

#(1 puntos) Ver_medicos_hospital, recibe dos listas una con la lista de medicos otra con la lista de número de enfermos,
#   saca por pantalla la lista de medicos su número de enfermos y el número de medico (que se corresponde con la posición
#   en las listas)
def Ver_medicos_hospital(listMedicos, listEnfermos):
    for i in range(len(listMedicos)): # se presupone que len(listMedicos) == len(listEnfermos)
        print(i,listMedicos[i],";",listEnfermos[i])
    print()

#(2 puntos) Modificar_medico_hospital, recibe dos listas una con la lista de medicos otra con la lista de
#   número de enfermos, una cadena de texto que representa el nuevo nombre del medico, un valor numérico que indica
#   su nueva número de enfermos y un valor numérico que indica el medico a modificar.
def Modificar_medico_hospital(listMedicos, listEnfermos, nuevoNombre, nuevoEnfermos, num):
    listMedicos[num] = nuevoNombre
    listEnfermos[num] = nuevoEnfermos

#(2 puntos) Cargar_datos_medicos_hospital, recibe dos listas una con la lista de medicos otra con la lista
#   de número de enfermos, que pueden estar vacias o no y el nombre de un archivo, el archivo (crear uno para probar)
#   contiene en cada linea los datos de un medico: nombre;número de enfermos, entre el nombre y la número de enfermos
#   hay un ';' que separa ambos datos, la funcion carga los datos del fichero y los añade a las listas recibidas.
def Cargar_datos_medicos_hospital(listMedicos, listEnfermos, archivo):
    f = open(archivo, "r")
    data = f.readlines()
    f.close()
    for i in range(len(data)):
        listMedicos.append(data[i].split(";")[0].rstrip())
        listEnfermos.append(data[i].split(";")[1].rstrip())
    print("Archivo cargado correctamente.")


#(1 puntos) Guardar_datos_medicos_hospital, recibe dos listas una con la lista de medicos otra con la lista de
#   número de enfermos y el nombre de un fichero la función guarda en el fichero el contenido de las listas, un medico
#   por linea del fichero con el formato  "nombre;número de enfermos"
def Guardar_datos_medicos_hospital(listMedicos, listEnfermos, archivo):
    # se presupone que el archivo ya incluye la extensión
    f = open(archivo, "w")
    for i in range(len(listMedicos)):
        f.write(listMedicos[i] + ";" + str(listEnfermos[i]) + "\n")
    f.close()
    print("Archivo guardado correctamente.")

#(2 puntos) Desarrollar un programa en Python que importe en módulo anterior deberá mostrar un menú con las
#   siguientes opciones:
#   1-Alta medico hospital
#   2-Baja medico hospital
#   3-Ver medicos hospital
#   4-Modificar medico hospital
#   5-Cargar datos medicos hospital
#   6-Guardar datos medicos hospital
#   0 Salir
def menu():
    print("1-Alta medico hospital","2-Baja medico hospital","3-Ver medicos hospital","4-Modificar medico hospital",sep="\n")
    print("5-Cargar datos medicos hospital","6-Guardar datos medicos hospital","0-Salir",sep="\n")
    sol = int(input("Introduzca su selección: "))
    while not sol>=0 and sol<=6:
        sol = int(input("Selección inválida. Vuelva a introducir su selección: "))
    return sol



#   El programa principal mostrará el menú, pedirá la opción correspondiente y ejecutará la opción deseada hasta
#   que se seleccione la opción de salir. Para cada opción llamará a la función necesaria desarrollada en el
#   módulo importado, si la función necesita que le pasen datos se deberán pedir y validar antes de llamar a la
#   función salvo que ya se disponga de ellos, el resultado devuelto por la función se mostrará posteriormente.
#   Las listas con los datos de los medicos son comunes para todas las opciones. Pueden definirse al inicio del
#   programa e irse modificando según se van llamando a las distintas funciones. El resto de datos que reciben
#   las funciones tal y como se indicó será necesario pedirlos.
listaMedicos = ["Médico Álvarez", "Médico Gómez", "Médico García"]
listaEnfermos = [143, 123, 75]
# listaMedicos = []
# listaEnfermos = []

sol = menu()
while not sol==0:
    if sol==1:
        newMedico = nuevaCadena("nombre")
        newEnfermos = nuevoNumeroEnfermos()
        Alta_medico_hospital(listaMedicos, listaEnfermos, newMedico, newEnfermos)
    elif sol==2:
        num = nuevoNumero()
        Baja_medico_hospital(listaMedicos, listaEnfermos, num)
    elif sol==3:
        Ver_medicos_hospital(listaMedicos, listaEnfermos)
    elif sol==4:
        num = nuevoNumero()
        newNombre = nuevaCadena("nombre")
        newEnfermos = nuevoNumeroEnfermos()
        Modificar_medico_hospital(listaMedicos, listaEnfermos, newNombre, newEnfermos, num)
    elif sol==5:
        archivo = nuevaCadena("archivoLeer")
        Cargar_datos_medicos_hospital(listaMedicos, listaEnfermos, archivo)
    else:
        archivo = nuevaCadena("archivoGuardar")
        Guardar_datos_medicos_hospital(listaMedicos, listaEnfermos, archivo)

    if sol == 1 or sol == 2 or sol == 4 or sol == 5: Ver_medicos_hospital(listaMedicos, listaEnfermos)
    # Al modificar las listas, se vuelven a imprimir para que el usuario vea los cambios.

    sol = menu()
print("Saliendo del programa.")


#Ejemplo de listas ["medico alvarez","medico gomez","medico garcia"]  [143,123,75]
#Ejemplo de fichero
#medicos.txt:
# medico alvarez;143
# medico gomez;123
# medico garcia;75

