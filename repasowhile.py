NOMBRE= input("HOLA BIENVENIDO A TUS NOTAS COMO TE LLAMAS:  ")
Nota= int(input("RECUERDA QUE LAS CALIFICACIONES SON DE 0 A 10 DONDE SE CALIFICAN DE A,B,C,D,F😉🤓 ESCRIBE TU CALIFICACION : "))

# tengo que siempre para agregar otro valor (variables )tengo que poner (f) y entre corchetes poner la variable 
if 9 <= Nota <=10:
    print(f"la Nota de: {NOMBRE} es (A) 😉 ")
elif 8<= Nota <=9:
    print (f"La Nota de: {NOMBRE} es: (B)🤓")
elif 7<= Nota <= 8:
    print(f"La Nota de:{NOMBRE} es: (C) 🤩")
elif 6<= Nota <= 7:
    print(f"La Nota de: {NOMBRE} (D) es:🙄")
elif 0 <= Nota <=6:
    print(f"La Nota de: {NOMBRE} es: (F)  🙄🤐")
else: 
    print ("LO SIENTO NO SE ENCUETRA LA VALIFICACION QUE BUSCAS👽") 