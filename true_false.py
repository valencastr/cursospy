'''paula = True
if paula:
    print ("condicion verdadera")
elif paula==False:
    print ("condicion falsa")'''

# como se esta usando int en le momento de ejecutar no se podra poner letras solo numero 

'''numero= int (input("proporsiona un valor del 1 y 3: "))
numerotexto = '''

'''if numero == 1:
    numerotexto = "numero uo"
elif numero == 2:
    numerotexto= "numero dos "
elif numero == 3:
    numerotexto= "numero tres"
else:
    numerotexto ="valor fuera de rango"
print(f"numero proporsionado: {numero}: {numerotexto}")
'''

# esta es para hacer el codigo mas corto simplificado en los ´rin siempre tengo que tener parentecis
'''
paula=True
print("condicin vrdadera")if paula else print("condicion falsa")'''

'''mes = int(input("ingresa mess del año 1 a 12 "))# para que pueda digitar tengo que ponerle es input no print 
estacion=None # none significa que est variable no tiene ningu valor
if mes == 1 or mes==2 or mes==12:
    estacion= "invierno"

elif mes == 3 or mes==4 or mes==5 : # recuerda que siempre tienes que nrmabrar la varibles para que te ejecute bien el programa 
    estacion= "primavera"

elif mes == 6 or mes ==7 or mes==8:
    estacion=" verano" 

elif mes== 9 or mes ==10 or mes ==11:
    estacion=" otoño   "
else:
    estacion="lo siento pero no es valido lo que digitaste"

print(f"para el mes {mes} la estacon es {estacion} ")'''


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++------------------------------+++++++++++++++++++++++++++++++++++++++++++

numero = int(input("proporciona el valor:  "))
numerotexto= None
if numero== 1:
    numerotexto = "Numero uno"
elif numero== 2:
    numerotexto = "Numero dos "

elif numero== 3:
    numerotexto= "Numero tres"
else:
   numerotexto= "Valor incorrecto"
print(f"Numero proporcionado: {numero} {numerotexto}:")