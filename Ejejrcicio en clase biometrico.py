import random

datosBiometrico = [[], [], []]
numPersonas = 0

print("--------------- SISTEMA BIOMETRICO -------------")
print("-------------------Bienvenido -------------------")


print("¿Que acción desea realiar?: ")
print('*  1) Login')
print('*  2) Registro de usuarios')
print('*  3) Salir del sistema')
tipo = int(input("Ingrese la opción: "))


while tipo!=3:
  
  if tipo ==1:
    if len(datosBiometrico[0])==0:
      print("\n\t No existen usuarios registrados \n")
      print("¿Que acción desea realiar?: ")
      print('*  1) Login')
      print('*  2) Registro de usuarios')
      print('*  3) Salir del sistema')
      tipo = int(input("Ingrese la opción: "))
    
    else:
      user=input("Ingrese el rostro de la persona en la cámara: ")
      if user in datosBiometrico[1]:
        print('-------- Bienvenido ----------')
        print()
        print("\t----- Módulos disponibles -------")
        print()
        print("¿Que acción desea realiar?: ")
        print('*  3) Cerrar sesión')
        tipo = int(input("Ingrese la opción: "))
      else:
        print("No existe el usuario")
        print("¿Que acción desea realiar?: ")
        print('*  1) Login')
        print('*  2) Registro de usuarios')
        print('*  3) Salir del sistema')
        tipo = int(input("Ingrese la opción: "))
        
  elif tipo ==2:
    print("\n ¿Que acción desea realiar?: ")
    print('*  1) Ingresar usuarios')
    print('*  2) Mostrar usuarios')
    print('*  3) Salir al menú principal')
    tipoAccion = int(input("Ingrese la opción: "))
    
    while tipoAccion != 3:
      
      if tipoAccion == 1:
        numPersonas = int(input("\n¿Ingrese el número de personas a registrar?: "))
        for i in range(numPersonas):
          print("Ingrese los datos de la persona", i + 1)
          nombreUsaurio = input("Nombre del persona: ")
          huellaUsaurio = input("Huella facial: ")
    
          datosBiometrico[0].append(nombreUsaurio)
          datosBiometrico[1].append(huellaUsaurio)
          datosBiometrico[2].append(random.randrange(1000, 9999))
    
        print("¿Que acción desea realiar?: ")
        print('*  1) Ingresar usuarios')
        print('*  2) Mostrar usuarios')
        print('*  3) Salir al menú principal')
        tipoAccion = int(input("Ingrese la opción: "))

      elif tipoAccion == 2:
        for i in range(numPersonas):
          print("-------------------------------------")
          print("Mostrando los datos de la persona", i + 1)
          print("* Nombre:", datosBiometrico[0][i])
          print("* Huella dactilar:", datosBiometrico[1][i])
          print("* Código de acceso: ", datosBiometrico[2][i])
          print("-------------------------------------")
        print("¿Que acción desea realiar?: ")
        print('*  1) Ingresar usuarios')
        print('*  2) Mostrar usuarios')
        print('*  3) Salir al menú principal')
        tipoAccion = int(input("Ingrese la opción: "))

    print("¿Que acción desea realiar?: ")
    print('*  1) Login')
    print('*  2) Registro de usuarios')
    print('*  3) Salir del sistema')
    tipo = int(input("Ingrese la opción: "))
    
print("Muchas gracias")