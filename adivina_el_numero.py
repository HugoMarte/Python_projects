from doctest import ELLIPSIS_MARKER
import random


def run():
    contador = 0
    respuesta = random.randint(1, 100)
    jugada =  int (input("¿Qué numero crees que es? "))
    while jugada != respuesta:
        if jugada < respuesta:
            print ("Es un numero más grande.")
        else:
            print ("Es un numero más pequeño")
        contador+= 1
        jugada = int (input ("Intentalo otra vez: "))
    print ("Eso es! lo adivinaste en"+ " " + str (contador) + " "+ "Jugadas!")


if __name__=="__main__":
    print ("Voy a pensar un numero del 1 al 100. A ver si eres capaz de adivinarlo.")
    run()
    repetir = "si"
    while repetir == "si":
        repetir = input ("¿Quieres seguir jugando? ")
        if repetir == "si":
            run()
        else:
            print ("No esta mal para un humano.")