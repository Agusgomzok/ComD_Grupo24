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
    print("\n¡Bienvenido al sistema!")
    
    while True:
        mostrar_opciones()
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == '1':
            print("\n[Llamando al módulo de Operaciones -> Consultar Saldo...]")
        elif opcion == '2':
            print("\n[Llamando al módulo de Operaciones -> Ingresar Dinero...]")
            
            
        elif opcion == '3':
            print("\n[Llamando al módulo de Operaciones -> Extraer Dinero...]")
            
            
        elif opcion == '4':
            print("\nGracias por operar con nuestro banco. ¡Hasta luego! 👋")
            break 
            
        else:
            print("\n❌ Error: Opción inválida. Por favor, ingrese un número del 1 al 4.")

# Punto de entrada del programa
if __name__ == "__main__":
    ejecutar_cajero()