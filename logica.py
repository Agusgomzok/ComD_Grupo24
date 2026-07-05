import os
from validaciones import validar_deposito, validar_extraccion

def actualizar_arch(nombre,saldo_nuevo):
    try:
        with open("usuarios.txt","r") as usuarios:
            with open("usuarios_act.txt","w") as usuarios_act:
                for linea in usuarios:
                    nombre_archivo, clave_archivo, saldo_archivo = linea.strip().split("%")

                    if nombre_archivo == nombre:
                        usuarios_act.write(nombre_archivo)
                        usuarios_act.write("%")
                        usuarios_act.write(clave_archivo)
                        usuarios_act.write("%")
                        usuarios_act.write(str(saldo_nuevo))
                        usuarios_act.write("\n")
                    else:    
                        usuarios_act.write(linea)           #ya trae salto de linea por lo que no es necesario agregar

        os.remove("usuarios.txt")
        os.rename("usuarios_act.txt","usuarios.txt")
    except FileNotFoundError:
        print ("Error: No se econtro el archivo usuarios.txt en la carpeta")    


def realizar_extraccion(saldo_actual, monto):                       #Si es valida retorna saldo Act sino retorna saldo actual
    if validar_extraccion(monto, saldo_actual):
        saldo_nuevo = saldo_actual - monto
        print("Operacion Aprobada")
        return saldo_nuevo
    else:
        return saldo_actual

def realizar_deposito(saldo_actual, monto):                         #Si es valida retorna saldo Act sino retorna saldo actual
    if validar_deposito(monto): 
        return saldo_actual + monto
    else:
        return saldo_actual

def realizar_transferencias(saldo_actual, monto_a_transferir):      #Si es valida retorna saldo Act sino retorna saldo actual
    if validar_extraccion(monto_a_transferir, saldo_actual):
        print("transferencia realizada")
        return saldo_actual - monto_a_transferir
    else:
        return saldo_actual