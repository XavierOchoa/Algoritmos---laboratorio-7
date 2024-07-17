#El náufrago satisfecho” ofrece hamburguesas sencillas (S), dobles
#(D) y triples (T), las cuales tienen un costo de $20, $25 y $28 respectivamente. La empresa acepta tarjetas de crédito con un cargo
#de 5 % sobre la compra. Suponiendo que los clientes adquieren N
#hamburguesas, las cuales pueden ser de diferente tipo, realice un
#algoritmo para determinar cuánto deben pagar. Represéntelo en
#diagrama de flujo, pseudocódigo y diagrama N/S.


def calcular_costo_hamburguesas(ordenes):    
    precios = [20, 25, 28]
    cargo_tarjeta = 0.05  
    costos_totales = []
    for tipo, cantidad, tipo_pago in ordenes:
        if tipo == 'S':
            precio_unitario = precios[0]
        elif tipo == 'D':
            precio_unitario = precios[1]
        elif tipo == 'T':
            precio_unitario = precios[2]

        costo_sin_cargo = precio_unitario * cantidad

        if tipo_pago == 'credito':
            costo_con_cargo = costo_sin_cargo * (1 + cargo_tarjeta)
        else:
            costo_con_cargo = costo_sin_cargo

        costos_totales.append(costo_con_cargo)

    return costos_totales

def ingresar_datos_orden():
    print("Bienvenido al Náufrago Satisfecho")
    ordenes = []    
    num_ordenes = int(input("¿Cuántas órdenes desea ingresar?: "))
        
    for i in range(num_ordenes):
        print(f"Ingresando datos para la orden {i+1}:")        
        tipo_hamburguesa = input("Ingrese el tipo de hamburguesa (S, D, T): ").upper()        
        cantidad = int(input("Ingrese la cantidad de hamburguesas: "))
        tipo_pago = input("Ingrese el tipo de pago (efectivo o credito): ").lower()
        ordenes.append([tipo_hamburguesa, cantidad, tipo_pago])
    
    return ordenes

def imprimir_costos_totales(costos_totales):
    for i in range(len(costos_totales)):
        print(f"El costo de la orden {i+1} es: ${costos_totales[i]:.2f}")

ordenes = ingresar_datos_orden()
costos_totales = calcular_costo_hamburguesas(ordenes)
imprimir_costos_totales(costos_totales)
