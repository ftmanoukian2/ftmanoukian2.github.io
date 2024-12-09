lista_colores = ["rojo","naranja","verde","negro","azul"]
lista_cantidades = [100, 2, 3, 7, 10]

def funcion(lista_colores,lista_cantidades):

    cant_elementos = len(lista_cantidades)
    for pos in range(cant_elementos):
        
        color_actual = lista_colores[pos]
        cantidad_actual = lista_cantidades[pos]

        if cantidad_actual < 7:
            cantidad_necesaria = 7 - cantidad_actual
            print(f"El color actual es: {color_actual} - La cantidad necesaria para completar 7 es {cantidad_necesaria}")
        else:
            print(f"El color actual es: {color_actual} - La cantidad actual es: {cantidad_actual}")

        # Recuerden ✨consultar✨!!!!

funcion(lista_colores,lista_cantidades)
print("🐰")