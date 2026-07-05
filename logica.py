from validaciones import validar_deposito, validar_extraccion, existe_usuario

def actualizar_saldo_archivo(usuario, nuevo_saldo):
    texto_nuevo = "" # Acumulador de texto
    try:
        with open("usuarios.txt", "r") as archivo:
            for linea in archivo:
                nombre, clave, saldo = linea.strip().split("%")
                
                if nombre == usuario:
                    # Armamos la línea concatenando con +  que no usen concatenar diria Ilse, jsjsj
                    linea_actualizada = nombre + "%" + clave + "%" + str(nuevo_saldo) + "\n"
                    texto_nuevo = texto_nuevo + linea_actualizada
                else:
                    # Dejamos la línea como estaba originalmente
                    linea_original = nombre + "%" + clave + "%" + saldo + "\n"
                    texto_nuevo = texto_nuevo + linea_original
                    
        # Escribimos todo el texto gigante de una sola vez
        with open("usuarios.txt", "w") as archivo:
            archivo.write(texto_nuevo)
            
    except FileNotFoundError:
        print("Error: archivo no encontrado")

def realizar_extraccion(usuario, saldo_actual, monto):
    if validar_extraccion(monto, saldo_actual):
        saldo_nuevo = saldo_actual - monto
        actualizar_saldo_archivo(usuario, saldo_nuevo)
        print("Operación Aprobada. Retire su dinero.")
        return saldo_nuevo
    return saldo_actual

def realizar_deposito(usuario, saldo_actual, monto):
    if validar_deposito(monto):
        saldo_nuevo = saldo_actual + monto
        actualizar_saldo_archivo(usuario, saldo_nuevo)
        print("Depósito exitoso.")
        return saldo_nuevo
    return saldo_actual

def realizar_transferencias(usuario_origen, usuario_destino, saldo_origen, monto_a_transferir):
    if usuario_origen == usuario_destino:
        print("Error: No puedes transferirte dinero a ti mismo.")
        return saldo_origen
        
    if validar_extraccion(monto_a_transferir, saldo_origen):
        if existe_usuario(usuario_destino):
            
            # 1. Restamos al origen
            saldo_nuevo_origen = saldo_origen - monto_a_transferir
            actualizar_saldo_archivo(usuario_origen, saldo_nuevo_origen)
            
            # 2. Buscamos el saldo del destinatario en el archivo
            saldo_destino = 0.0
            with open("usuarios.txt", "r") as archivo:
                for linea in archivo:
                    n, c, s = linea.strip().split("%")
                    if n == usuario_destino:
                        saldo_destino = float(s)
            
            # 3. Sumamos al destinatario
            saldo_nuevo_destino = saldo_destino + monto_a_transferir
            actualizar_saldo_archivo(usuario_destino, saldo_nuevo_destino)
            
            print(f"Transferencia realizada con éxito a {usuario_destino}.")
            return saldo_nuevo_origen
        else:
            print("Error: El usuario destinatario no existe.")
            
    return saldo_origen