"""
Ejemplo realizado en clase el 18/4/2024
Ejercicio 5 de listas

Procedimiento:
    1 - Definir una lista vacía para almacenar los elementos ordenados ('lista_ord')
    2 - Encontrar el elemento más chico de la lista desordenada ('lista_desord')
    3 - Agregar el elemento encontrado al final de la nueva lista lista ('lista_ord')
    4 - Remover el elemento encontrado de la lista desordenada ('lista_desord')
    5 - Repetir desde el paso 2 hasta que haber removido todos los elementos de la lista desordenada
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
        mas_chico = lista_desord[0]             # suponemos que el elemento más chico es el primero (esto es sólo para iniciar el bucle - probablemente lo que asumimos no sea así).
        for elemento in lista_desord[1:]:       # comparamos el elemento más chico con todos los elementos de la lista desordenada. empezamos desde el segundo, para no comparar el primero consigo mismo.
            if mas_chico > elemento:
                mas_chico = elemento            # si el elemento con el que estamos comparando es más chico que el que pensábamos, lo cambiamos. mas_chico pasa a contener el menor encontrado hasta el momento.
                                                # al finalizar el bucle, en la variable mas_chico no puede haber otro número que no sea el más chico de la lista desordenada.
                                                
        # 3 - Agregar el número encontrado al final de lista_ord
        lista_ord.append(mas_chico)

        # 4 - Sacar el número encontrado de la lista_desord
        lista_desord.remove(mas_chico)

        # 5 - Repetir --> desde el paso 2

    return lista_ord

print("Lista desordenada: " + str(lista))
print("Lista ordenada: " + str(ordenar_lista(lista)))