# definicion de una lista stri
Nombres=["paula", "sebas" , "mauro", "nicolas"]
#imprimir la lista nombre
print (Nombres)
#acceder a los elementos de la lista 
print (Nombres[0])
print (Nombres[1])
# accceder a los elementos de manera inversos 
print (Nombres[-1])

# imprimir un rango 
print (Nombres [3:1]) # SIN INCLUIR EL INDICE DOS 

# IR LA IINICIO DE LA LISTA SN INCLUIRLO
print(Nombres[:3])
# DESDE EL INDICE INDICADO HASTA EL FINAL DE LA LISTA 
print(Nombres[1:])
#CAMBIAR UN VALOR 
Nombres[2] = " LAURA"
print (Nombres)
#ITERAR LA LISTA
for nombre in Nombres:
    print(nombre)
else:
    print("no existen mas nombres en la lista")

# pregutar cuantos elementos tiene la lista 
print(len(Nombres))
# para agregar mas elementos
Nombres.append ("andres")

print(Nombres)
# insertr un elemento en un indice en especiico
Nombres.insert (1, "alverto")
print(Nombres)

# este es para remover un elemento de la lista
Nombres.remove ("paula")
print(Nombres)

#este es para borrar el ultmo elemento de uestra la lista que fue gregado
Nombres.pop()
print(Nombres)
# para borra un ielemento indicdo
del Nombres[0]
print(Nombres)

# para limpiar todos los elementos de la lista
Nombres.clear()
print(Nombres)

# para borrar la lista en este sale el error que die que la variable nno esta aignaaa 
del Nombres
print(Nombres)