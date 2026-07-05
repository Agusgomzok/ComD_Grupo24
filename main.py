import validaciones
import logica


def mostrar_opciones():
    print("\n" + "="*30)
    print("🏦 CAJERO AUTOMÁTICO UTN 🏦")
    print("="*30)
    print("1. Consultar Saldo")
    print("2. Ingresar Dinero (Depósito)")
    print("3. Extraer Dinero")
    print("4. Transferencia ")
    print("5. Salir")
    print("="*30)

def ejecutar_cajero():
    # NOTA: llamar a la función de Persona 1

    condicion = validaciones.login()
    usuario= validaciones.usuario_actual
    saldo = validaciones.saldo_actual
    
    while condicion:
        mostrar_opciones()
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == "1":
            print(f"\n su saldo actual es: ${saldo}")
        
        elif opcion == "2":
            try:
                monto = int(input("\ncuanto dinero quiere depositar?: $"))
                saldo = logica.realizar_deposito(saldo, monto)
            except ValueError:
                print("Error: Ingrese un valor numerico valido")
        
        elif opcion == "3":
            try:
                monto = int(input("\n Cuanto dinero desea extraer?: $"))
                saldo = logica.realizar_extraccion(saldo, monto)
            except ValueError:
                print(" Error: Ingrese un valor numerico valido")
        elif opcion == "4":
            try:
                usuario_transferir =input("\n Ingrese nombre de usuario a transferir: ")
                existe, saldo_transferencia =   validaciones.validar_destino(usuario_transferir)
                if usuario_transferir == usuario:
                    print("Error: no puedes transferirte a ti mismo.")
                elif existe:
                    saldo_anterior = saldo
                    saldo = logica.realizar_transferencias(saldo, monto)
                    if saldo != saldo_anterior:                                                 #hay un problema en la transferencia y esto lo parchea
                        saldo_transferencia = logica.realizar_deposito(int(saldo_transferencia), monto)

                        logica.actualizar_arch(usuario_transferir, saldo_transferencia)
                else:
                    print("Usuario no encontrado")
            except ValueError:
                print(" Error: Ingrese un valor numerico valido")
        
        elif opcion == "5":
            print("\n Gracias por operar con nuestro banco. ¡Hasta luego! 👋 ")
            logica.actualizar_arch(usuario,saldo)
            return
        
if __name__ == "__main__":
    ejecutar_cajero()






