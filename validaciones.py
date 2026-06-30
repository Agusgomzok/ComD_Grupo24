def validar_usuario(Nombre,Contraseña):
    try:
        with open("Usuarios.txt","r") as archivo:   #abro el archivo el with se asegura que se cierre cuando termine el bloque
            for linea in archivo:
                nombre_archivo, clave_archivo = linea.strip().split("%") #strip borra los saltos de linea y split devuelve una lista con las 2 palabras
            
                if (Nombre == nombre_archivo) and (Contraseña == clave_archivo) :
                    return True                                                     #El return corta la ejecucion, es como un break pero devuelve un valor
            return False
    except FileNotFoundError:
        print ("Error: No se econtro el archivo usario.xtx en la carpeta")
    
def validar_extraccion(monto, saldo_actual):
    if monto <= 0:
        print("Error: el monto a extraer debe ser mayor a cero")
    if monto > saldo_actual:
        print("Saldo insuficiente")
        return False
    return False

def validar_deposito(monto):
    if monto <= 0:
        print("error: el monto debe ser mayot a cero")
        return False
    return False