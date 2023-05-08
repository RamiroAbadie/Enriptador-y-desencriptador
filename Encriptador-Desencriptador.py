# Ramiro Abadie - Proyecto Encriptador
import random
import string

def GenerarKey(LstChars):
    '''Genera una key'''
    Key = LstChars.copy()
    random.shuffle(Key)
    KeyStr = "".join(Key)
    
    return KeyStr

def Encriptar(LstChars, LstKeys, Texto):
    '''Encriptar texto'''
    TextoEncriptado = ""
    
    for Letra in Texto:
        Index = LstChars.index(Letra)
        TextoEncriptado += LstKeys[Index]
    
    return TextoEncriptado

def Desencriptar(LstChars, LstKeys, Texto):
    '''Decriptar texto'''
    TextoDecriptado = ""
    
    for Caracter in Texto:
        Index = LstKeys.index(Caracter)
        TextoDecriptado += LstChars[Index]
        
    return TextoDecriptado

def main():
    print("------MENU------")
    Menu = '''1) Generar Key
2) Encriptar
3) Desencriptar
4) Generar Clave (en progreso)'''
    print(Menu)
    Eleccion = int(input("Seleccione opcion: "))
    # Crear lista de caracteres
    Chars = string.punctuation + string.digits + string.ascii_letters + "¿" + " " 
    Chars = list(Chars)
    
    if Eleccion==1:
        print("\n------GENERAR KEY------")
        Key = GenerarKey(Chars)
        print(f"{Key}")
    elif Eleccion==2:
        print("\n------ENCRIPTAR------")
        # Pedir key usada para encriptar
        Key = input("Introducir llave: ")
        while len(Key)<96:
            print("\a\n<ERROR>--> Key invalida")
            Key = input("Introducir llave: ")
        Key = list(Key)
        
        print("1) Palabra unica\n2) Archivo")
        Opcion = int(input("Ingrese eleccion: "))
        if Opcion==1:
            Palabra = input("Ingrese el texto: ")
            Encriptado = Encriptar(Chars, Key, Palabra)
            print("-"*10)
            print(f"{Encriptado}")
        elif Opcion==2:
            # Encriptar palabras del archivo
            ArchivoLectura = input("Nombre del archivo a encriptar: ")
            LstEncriptadas = []
            with open(ArchivoLectura, 'r') as File:
                LstPalabras = File.readlines()
                for PalabraRaw in LstPalabras:
                    Palabra = PalabraRaw.rstrip("\n") # Limpieza
                    Palabra = Palabra.replace("Â", "") # Limpieza
                    Palabra = Palabra.replace("â", "") # Limpieza
                    Encriptada = Encriptar(Chars, Key, Palabra)
                    LstEncriptadas.append(Encriptada)
            # Agregar LstEncriptadas a un nuevo archivo
            ArchivoEscritura = input("Nombre del archivo a escribir: ")
            with open(ArchivoEscritura, 'w') as File:
                for PalabraRaw in LstEncriptadas:
                    Palabra = PalabraRaw + "\n"
                    File.write(Palabra)
            print("----Completado con exito (Cheque archivos)----")
                
    elif Eleccion==3:
        print("\n------DESENCRIPTAR------")
        # Pedir key usada para desencriptar
        Key = input("Introducir llave: ")
        while len(Key)<96:
            print("\a\n<ERROR>--> Key invalida")
            Key = input("Introducir llave: ")
        Key = list(Key)
        
        print("1) Palabra unica\n2) Archivo")
        Opcion = int(input("Ingrese eleccion: "))
        if Opcion==1:
            Palabra = input("Ingrese el texto: ")
            Desencriptado = Desencriptar(Chars, Key, Palabra)
            print("-"*10)
            print(f"{Desencriptado}")
        elif Opcion==2:
            # Desencriptar palabras del archivo
            ArchivoLectura = input("Nombre del archivo a desencriptar: ")
            LstDesencriptadas = []
            with open(ArchivoLectura, 'r') as File:
                LstPalabras = File.readlines()
                for PalabraRaw in LstPalabras:
                    Palabra = PalabraRaw.rstrip("\n") # Limpieza
                    Palabra = Palabra.replace("Â", "") # Limpieza
                    Palabra = Palabra.replace("â", "") # Limpieza
                    Desencriptada = Desencriptar(Chars, Key, Palabra)
                    LstDesencriptadas.append(Desencriptada)
            # Agregar LstDesencriptadas a un nuevo archivo
            ArchivoEscritura = input("Nombre del archivo a escribir: ")
            with open(ArchivoEscritura, 'w') as File:
                for PalabraRaw in LstDesencriptadas:
                    Palabra = PalabraRaw + "\n"
                    File.write(Palabra)
            print("----Completado con exito (Cheque archivos)----")
       
main()