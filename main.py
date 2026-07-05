from logica import realizar_deposito, realizar_extraccion, realizar_transferencias
from validaciones import validar_usuario

def mostrar_opciones():
    print("\n" + "="*30)
    print("🏦 CAJERO AUTOMÁTICO UTN 🏦")
    print("="*30)
    print("1. Consultar Saldo")
    print("2. Ingresar Dinero (Depósito)")
    print("3. Extraer Dinero")
    print("4. Transferencia")
    print("5. Salir")
    print("="*30)

def ejecutar_cajero():
    print("\n--- Inicie sesión ---")

    usuario = input("Ingrese un usuario: ")
    contraseña = input("Ingrese contraseña: ")

    # Recibimos un solo valor: el saldo real o un -1.0 si hubo error
    saldo_inicial = validar_usuario(usuario, contraseña)

    if saldo_inicial == -1.0:
        print("Error de datos; fin del programa.")
        return
        
    print(f"\n¡Bienvenidos al sistema, {usuario}!")
    
    saldo = saldo_inicial
    
    while True:
        mostrar_opciones()
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == "1":
            print(f"\nSu saldo actual es: ${saldo:.2f}")
        
        elif opcion == "2":
            try:
                monto = float(input("¿Cuánto dinero quiere depositar?: $"))
                saldo = realizar_deposito(usuario, saldo, monto)
            except ValueError:
                print("Error: ingrese un valor numérico válido.")
        
        elif opcion == "3":
            try:
                monto = float(input("\n¿Cuánto dinero desea extraer?: $"))
                saldo = realizar_extraccion(usuario, saldo, monto)
            except ValueError:
                print("Error: ingrese un valor numérico válido.")
                
        elif opcion == "4":
            try:
                usuario_destino = input("Ingrese el nombre del usuario a transferir: ")
                monto = float(input("¿Cuánto dinero desea transferir?: $"))
                saldo = realizar_transferencias(usuario, usuario_destino, saldo, monto)
            except ValueError:
                print("Error: ingrese un valor numérico válido.")
        
        elif opcion == "5":
            print("\nGracias por operar con nuestro banco. ¡Hasta luego! 👋")
            break
        else:
            print("\nOpción inválida. Seleccione un número del 1 al 5.")
        
if __name__ == "__main__":
    ejecutar_cajero()


