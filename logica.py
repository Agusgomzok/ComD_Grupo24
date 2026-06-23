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


"""pruebita"""
#   prueba1=login() # admin%1234 usuario y contraseña cargados en el txt
#   if prueba1:
#       print("deberia mostrarte true")
#       print("\n",prueba1)
#   else:
#       print("deberia mostrarte false")
#       print("\n",prueba1)


