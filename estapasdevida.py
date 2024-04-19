# ejersicio etapas de vida 
#recordaar que el else es opsional para dar el mensje 
edad= int(input("escribe tu edad "))
mensaje = None
if 0 <= edad < 10:
    mensaje="TU INFANCIA ES INCREIBLE"
    
elif 10 <= edad < 20:

    mensaje="tu edad tiene muchos cambios "
elif 20>= edad <30:
    mensaje="tu edad es una monda te toca trabajar como negrito jajaja"
else:
    mensaje="lo siento no estas en el rango de edades"
print(f"TU EDAD ES: {edad}, {mensaje}")
