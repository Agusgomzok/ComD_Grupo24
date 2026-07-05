
saldo_actual = 0
usuario_actual = ""

#Me va a retornar booleano y Guarda el saldo y el nombre para posterior trabajo
def validar_usuario(Nombre,Contraseña):
    #Variables globales
    global saldo_actual 
    global usuario_actual 
    try:
        with open("usuarios.txt","r") as archivo:   #abro el archivo el with se asegura que se cierre cuando termine el bloque
            for linea in archivo:
                nombre_archivo, clave_archivo, saldo_archivo = linea.strip().split("%") #strip borra los saltos de linea y split devuelve una lista con las 2 palabras
            
                if (Nombre == nombre_archivo) and (Contraseña == clave_archivo) :
                    usuario_actual = nombre_archivo
                    saldo_actual = int(saldo_archivo)
                    return True                                                     #El return corta la ejecucion, es como un break pero devuelve un valor
            return False
    except FileNotFoundError:
        print ("Error: No se econtro el archivo usuarios.txt en la carpeta")

def validar_destino(nombre_destino):
    try:
        with open("usuarios.txt", "r") as archivo:
            for linea in archivo:
                nombre_archivo, clave_archivo, saldo_archivo = linea.strip().split("%")

                if nombre_destino == nombre_archivo:
                    return True, saldo_archivo

            return False, 0

    except FileNotFoundError:
        print("Error: No se encontró el archivo usuarios.txt en la carpeta")
        return False
    
def login():
    cont=1
    print("\n--- Inicie sesion---")
    while cont<=3:
        print("\nIngrese Nombre: ")
        Nombre= input()
        print("Ingrese contraseña: ")
        Contraseña= input()
        if validar_usuario(Nombre,Contraseña):
            print("Inicio de sesion correcto")
            return True                             #Por ahora retorna true nose que vamos a hacer si llamamos a otra funcion
        else:
            print("Intento nro: ",cont,"Fallido le quedan: ",(3-cont))
            cont= cont+1
    print("No se pudo loguear")
    return False                                    # y tambien retornara false 


def validar_extraccion(monto, saldo_actual):                                    #Evita que se extraiga montos mayores al saldo
    if monto <= 0:
        print("Error: el monto a extraer debe ser mayor a cero")
        return False
    elif monto > saldo_actual:
        print("Saldo insuficiente")
        return False
    else:
        return True

def validar_deposito(monto):                                                
    if monto <= 0:
        print("Error: el monto debe ser mayor a cero")
        return False
    else:
        return True

