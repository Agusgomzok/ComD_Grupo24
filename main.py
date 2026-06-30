from logica import realizar_deposito, realizar_extraccion, realizar_transferencias
from validaciones import validar_usuario

def mostrar_opciones():
    print("\n" + "="*30)
    print("🏦 CAJERO AUTOMÁTICO UTN 🏦")
    print("="*30)
    print("1. Consultar Saldo")
    print("2. Ingresar Dinero (Depósito)")
    print("3. Extraer Dinero")
    print("4. Salir")
    print("="*30)

def ejecutar_cajero():
    # NOTA: llamar a la función de Persona 1
    print("\n--- Inicie sesion---")

    usuario = input("Ingrese un usuario: ")
    contraseña = input("Ingrese contraseña: ")

    if not validar_usuario(usuario, contraseña):
        print("error de datos; fin del programa")
        return
    print(f"\n Bienvenidos al sistema, {usuario}")
    
    saldo = 1000.0
    
    while True:
        mostrar_opciones()
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == "1":
            print(f"\n su saldo actual es: ${saldo:.2f}")
        
        elif opcion == "2":
            try:
                monto = float(input("\cuanto dinero quiere depositar?: $"))
                saldo = realizar_deposito(saldo, monto)
            except ValueError:
                print("Error:ingrese un valor numerico valido")
        
        elif opcion == "3":
            try:
                monto = float(input("\n Cuanto dinero desea extraer?: $"))
                saldo = realizar_extraccion(saldo, monto)
            except ValueError:
                print(" Error: Error:ingrese un valor numerico valido")
        elif opcion == "4":
            try:
                monto = float(input("\n Cuanto dinero desea transferir?: $"))
                saldo = realizar_transferencias(saldo, monto)
            except ValueError:
                print(" Error: Error:ingrese un valor numerico valido")
        
        elif opcion == "5":
            print("\n Gracias por operar con nuestro banco. ¡Hasta luego! 👋 ")
        
if __name__ == "__main__":
    ejecutar_cajero()







