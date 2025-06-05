#clase 1 // 5/06/25
#pablo nicolas marin 2459440
#Ing industrial

###La tarea es preparar un código simple para evaluar o encontrar el tiempo final de un periodo de tiempo
#dado, expresándolo en horas y minutos. Las horas van de 0 a 23 y los minutes de 0 a 59. El resultado#
#debe ser mostrado en la consola.
#Por ejemplo, si el evento comienza a las 12:17 y dura 59 minutos, terminará a las 13:16.###

hora = 12
minutos = 17

duracion_evento = int(input("Pls write the durations of the event in minuts: "))

def calcularEvento(hora, minutos):
    ##sumamos cuantos minutos tenemos en total
    total_minutes = minutos + duracion_evento
    #1 hora = 60 minutos
    #ahora vemos cuantas hora tenemos con el operador % (modulo)

    hora += total_minutes // 60
    minutos = total_minutes % 60

    return("the finish of the event will be: " + str(hora) + ":" + str(minutos))

print(calcularEvento(hora, minutos))





