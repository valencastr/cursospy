frutas=( "manzana", "pera","melon","quiwi" ,"mora", "fresa" )
print (len(frutas))
#acccder a un elemento
print (frutas [0]) 
#navegacion inversa osea sacando el ultimo elemento
print(frutas [-1])
#acceder a un rango de valores si en la tupla llego a tener un solo elemento me oca ponerle una coma al final

print(frutas[0:2])

# para recorrer los elementos osea saber que tenemos almacenado en la tupla tengo que usar el ciclo for 
for frutas in frutas:          # TAMBIEN ES PARA QUE NO SALGA DE LARGO SI NO SEGUIDO LOS ELEMENTOS
    print(frutas, end=  " ,")# LO QUE ESTA DENTRO DEL PARENTICIS ES LO QUE SE REFLETA AL EJECUTAR POR LO TANTO ES MEJOR DEJARLA VACIA 

# CAMBIAR VALOR TUPLA
#frutas[0]="manzana"
 frutalista= list(frutas)
frutalista[0]= 0 "pera"
frutalista








#NAVEGACIO INVERSA
print(frutas [-1] ) 


