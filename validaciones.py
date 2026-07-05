def validar_usuario(Nombre, Contraseña):
    try:
        with open("usuarios.txt", "r") as archivo:
            for linea in archivo:
                nombre_archivo, clave_archivo, saldo_archivo = linea.strip().split("%")
            
                if (Nombre == nombre_archivo) and (Contraseña == clave_archivo):
                    return float(saldo_archivo) # Si es válido, devolvemos el saldo numérico
                    
            return -1.0 # Si termina el para y no encontró coincidencias, devuelve -1.0
    except FileNotFoundError:
        print("Error: No se encontró el archivo usuarios.txt en la carpeta")
        return -1.0

def existe_usuario(Nombre):
    try:
        with open("usuarios.txt", "r") as archivo:
            for linea in archivo:
                nombre_archivo, clave_archivo, saldo_archivo = linea.strip().split("%")
                
                if Nombre == nombre_archivo:
                    return True
            return False
    except FileNotFoundError:
        return False

def validar_extraccion(monto, saldo_actual):
    if monto <= 0:
        print("Error: el monto a extraer debe ser mayor a cero")
        return False
    if monto > saldo_actual:
        print("Error: Saldo insuficiente")
        return False
    return True 

def validar_deposito(monto):
    if monto <= 0:
        print("Error: el monto debe ser mayor a cero")
        return False
    return True