# actividad de imprimir la calificaacion de 
calificaciones= int(input("escribe tu calificacion entre 0 y 10: ")) #SIEMPRE TENGO QUE PONERLE LOS PARENTICIS DESPUES DE EL INPUT 
#si esta enetre 9 y 10  imprimir la calificacion A
if 9<= calificaciones <= 10:
    print("TU CALIFICACION ES (A) FELICIDADES😇")
elif 8<= calificaciones <9:
    print("TU CALIFICACIN ES (B) TIENES QUE MEJORAR")
elif 7<= calificaciones <8:
    print("TU CALIFICACION ES(C) TE ENVIARE A REPASAR ALGUNOS TENMAS")
elif 6<= calificaciones <7:
    print("TU CALIFICACION ES (D)MUY BAJA CALIFICACION")
elif 0<= calificaciones <6:
    print  ("TU CALIFICACION ES (F)LO SIENTO TE TOCA RECUPERAR BUENA SUERTE PARA LA PROXIOMA 😡")

else:
 print("lo sentimos tu calificacion no esta ni en cero parece que no precentaste nada")