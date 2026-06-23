def Validacion(Nombre,Contraseña):
    with open("Usuarios.txt","r") as archivo:   #abro el archivo el with se asegura que se cierre cuando termine el bloque
        for linea in archivo:
            nombre_archivo, clave_archivo = linea.strip().split("%") #strip borra los saltos de linea y split devuelve una lista con las 2 palabras
            
            if (Nombre == nombre_archivo) and (Contraseña == clave_archivo) :
                return True                                                     #El return corta la ejecucion, es como un break pero devuelve un valor
            
        return False


