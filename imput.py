#Sirve para pedir datos
'''varibale = input("Escriba aca lo que desea: ")
print(varibale)
print("Fin del programa")
'''
#Input con suma
'''numero1 = int(input("Ponga el primer numero "))
numero2 = int(input("Ponga el segundo numero "))
resultado = numero1 + numero2
print("El resultado de la suma es ", resultado)'''

'''dia = input("Como estuvo tu dia del 1 al 10 ")
print("Mi dia estuvo de ", dia)'''

'''autor = input("Proporciona el nombre del autor ")
libro = input("Proporciona el nombre del libro ")
print("fue escrito por ", autor, "y se llama ",libro )'''

'''print("Bienvenuda paula a la calculadora colvatel")
numero1 = int(input("Por favor digite el primer numero de la operacion"))
numero2 = int(input("Por favor digite el segundo numero de la operacion"))

numero = numero1 * numero2

print(f"El resultado de la multiplicacion es {numero}")'''

print("Proporcione los siguientes datos del libro ")
nombre = input("Proporcione el nombre del libro ")
id = int(input("Proporcione el ID del libro"))
precio = float(input("Proporcione el precio del libro "))
envio = input("Indique si el envio es gratis (True/False): ")

if envio == "True":
    envio = True
elif envio == "False":
    envio = False
else:
    envio = "Valor incorrecto debe escribir True/False"

print(f'''
      Nombre {nombre} 
      Id {id} 
      Precio {precio} 
      Envio {envio}''')





