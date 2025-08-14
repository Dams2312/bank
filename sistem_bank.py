"""
Nombre : Danny Julian Velasco Olarte
Fecha: 12 de agosto del 2025
Descripcion: algoritmo que controla las cuentas banncarias de un banco
"""
usuarios = {}
verdad = True

def menu ():
    print("escoja que va acrear en su portafolio")
    print("1. Crear cuenta \n2. Depositar Dinero \n3. Solicitar Credito \n4. Retirar Dinero \n5. Pago Cuota Credito \n6. Cancelar Cuenta \n7. Salir \nIngrese opcion:  ")
    
def nombre():
    name = input("ingrese por favor su nombre: ") 
    usuario.update({"nombre": name})
    print(f"Hola {name}, bienvenido al sistema bancario.")

def edades(verdad):
    edad = int(input("ingrese por favor su edad: "))
    
    if edad > 18 :
        print("edad correcta, continuando con el proceso de creacion de cuenta...")
        usuario.update({"edad": edad})

    else :
        
        print(" no tienes edad para crear una cuenta.....")
        print("saliendo .....")
        verdad = False
        return verdad
    
def identificacion(usuarios):
    while True:
        cedula = int(input("ingrese porfavor su cedula: "))#define nombre como clave del diccionario original
        if cedula in usuarios:
            print("esta cedula ya esta registrada, por favor ingrese una cedula diferente")
            continue
        else:
            usuarios.update({cedula: usuario})
            print("cedula registrada con exito")
            break

def correo():
    email = input("ingrese su email por favor: ")
    usuario.update({"email": email})
    print("agregando email.")
    
#terminar contacto y continuar con ubicacion para guardar en diccionario
def contacto ():
    while True:
        print("ingrese contacto movil y fijo si no tiene alguno presione enter")
        movil = int(input("contacto movil: "))
        fijo = int(input(" ingrese contacto fijo: "))
    
        if movil != "" and fijo != "":
            print("agregando movil y fijo....")
            usuario.update({"movil": movil, "fijo": fijo})
            print("contacto agregado con exito")
            break
        elif movil != "" and fijo == "":
            print(" agregando movil ....")
            usuario.update({"movil": movil})
            print("contacto movil agregado con exito")
            break
        elif movil == "" and fijo != "":
            print("agregando fijo ....")
            usuario.update({"fijo": fijo})
            print("contacto fijo agregado con exito")
            break    
        else:
            print("no se agrego ningun contacto, por favor ingrese al menos uno")
            continue


def ubicacion():
    while True:
        print("ingrese su ubicacion: ")
        pais = input("pais: ")
        ciudad = input("ciudad: ")
        direccion = input("direccion: ")
        
        if ciudad == "" or pais == "" or direccion == "":
            print("deves agregar la ubicacion completa")
            continue
        else:
            print("agregando ubicacion...")
            usuario.update({"pais": pais, "ciudad": ciudad, "direccion": direccion})
            print("ubicacion agregada con exito")
            break

def portafolio():
    while True:
        print("1. Cta ahorros \n2. Cta corriente \n3. CDT \n4. Credito libre Inv \n5. Credito Vivienda \n6. Credito compra Auto movil \nIngrese opcion: ",end="")   
        cuenta = int(input())
        match cuenta:
            case 1:
                print("creando cuenta de ahorros....")
                monto = int(input("el monto minimo deve ser de $10000...ingrese monto: "))
                
                if monto >= 10000:
                    usuario.update({"cuenta ahorros": monto})
                    print("cuenta de ahorros creada con exito")
                    continue
                else:
                    print("el monto minimo es de $10000, no se creo la cuenta")
                    continue
            case 2:
                print("creando cuenta corriente....")
                monto = int(input("el monto minimo deve ser de $20000...ingrese monto: "))
                
                if monto >= 20000:
                    usuario.update({"cuenta corriente": monto})
                    print("cuenta corriente creada con exito")
                    continue
                else:
                    print("el monto minimo es de $20000, no se creo la cuenta")
                    continue
            case 3:
                print("creando CDT....")
                monto = int(input("el monto minimo deve ser de $25000...ingrese monto: "))
                
                if monto >= 25000:
                    usuario.update({"CDT": monto})
                    print("CDT creado con exito")
                    continue
                else:
                    print("el monto minimo es de $25000, no se creo el CDT")
                    continue
            case 4:
                print("creando credito libre inversion....")
                monto = int(input("el monto minimo deve ser de $30000...ingrese monto: "))
                
                if monto >= 30000:
                    usuario.update({"credito libre inversion": monto})
                    print("credito libre inversion creado con exito")
                    continue
                else:
                    print("el monto minimo es de $30000, no se creo el credito")
                    continue
            case 5:
                print("creando credito vivienda....")
                monto = int(input("el monto minimo deve ser de $40000...ingrese monto: "))
                if monto >= 40000:
                    usuario.update({"credito vivienda": monto})
                    print("credito vivienda creado con exito")
                    continue
                else:
                    print("el monto minimo es de $40000, no se creo el credito")
                    continue
            case 6:
                print("creando credito compra auto movil....")
                monto = int(input("el monto minimo deve ser de $45000...ingrese monto: "))
                if monto >= 45000:
                    usuario.update({"credito compra auto movil": monto})
                    print("credito compra auto movil creado con exito")
                    continue
                else:
                    print("el monto minimo es de $45000, no se creo el credito")
                    continue
            case _:
                print("opcion no valida, por favor ingrese una opcion del 1 al 6")
                continue
            
        if cuenta > 1 and cuenta < 6:
            otra_cuenta = input("desea agregar otra cuenta al portafolio? (si(S)/no(N)): ")
            if otra_cuenta.upper() == 'S':
                continue
            elif otra_cuenta.upper() == 'N':
                print("saliendo del menu de cuentas...")
                break
            else:
                print("opcion no valida, por favor ingrese si(S) o no(N)")
                continue
        else:
            continue

while True : 
    try:
        print(menu(), end="")
        opciones = int(input("ingrese por favor una opcion gracias"))
        
        match opciones :
            case 1:
                while verdad:
                    usuario = {}
                    identificacion(usuarios)
                    nombre() 
                    edades(verdad)
                    correo()
                    contacto()
                    ubicacion()
                    portafolio()
                    
                    agregar = input("desea agregar otra cuenta Si(S),No(N): ").upper()
                    if agregar == "S":
                        print("agregando otra cuenta....")
                        continue
                    elif agregar == "N":
                        print("saliendo....")
                        verdad = False
                    else:
                        print("opcion incorrecta ..por favor intente denuevo")
            case 2:
                pass        
    except:
        pass