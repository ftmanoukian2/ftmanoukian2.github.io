"""
Ejemplo realizado en clase el 18/4/2024
Ejercicio 5 de listas
"""

# Creo una lista desordenada que voy a pasar a la función
lista = [7,2,4,1,15,-8,2,8]

# DEFINO la función - en esta parte, el código NO SE EJECUTA
def ordenar_lista(lista_desord):
    # 1 - Definir lista vacía
    lista_ord = []

    # Repetición hasta paso 5
    while len(lista_desord) > 0:
        # 2 - Encontrar el número más chico
        mas_chico = lista_desord[0]
        for elemento in lista_desord[1:]:
            if mas_chico > elemento:
                mas_chico = elemento

        # 3 - Agregar el número encontrado al final de lista_ord
        lista_ord.append(mas_chico)

        # 4 - Sacar el número encontrado de la lista_desord
        lista_desord.remove(mas_chico)

        # 5 - Repetir --> desde el paso 2

    return lista_ord

print("Lista desordenada: " + str(lista))
print("Lista ordenada: " + str(ordenar_lista(lista)))