from validaciones import Validacion

def login():
    cont=1
    while cont<=3:
        print("\nIngrese Nombre: ")
        Nombre= input()
        print("Ingrese contraseña: ")
        Contraseña= input()
        if Validacion(Nombre,Contraseña):
            print("Inicio de sesion correcto")
            return True                             #Por ahora retorna true nose que vamos a hacer si llamamos a otra funcion
        else:
            print("Intento nro: ",cont,"Fallido le quedan: ",(3-cont))
            cont= cont+1
    print("Tarjeta bloqueada")
    return False                                    # y tambien retornara false




