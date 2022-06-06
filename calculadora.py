def calculadora():
    num_1 = int (input ("Ingrese un numero: "))
    num_2 = int (input ("Ingrese otro numero: "))
    operacion = input ("Ingrese una operacion: ")
    num_3 = 0
    if operacion == "suma":
        num_3= num_1 + num_2
        print (num_3)
    elif operacion == "resta":
        num_3 = num_1 - num_2
        print (num_3)
    elif operacion == "multiplicacion":
        num_3 = num_1*num_2
        print (num_3)
    elif operacion == "division":
        num_3 = num_1 / num_2
        print (num_3)


if __name__=="__main__":
    print ("Haz abierto la calculadora de Hugo!")
    calculadora()
    repetir = "si"
    while repetir == "si":
        repetir= input ("¿Quiere hacer otra operacion? ")
        if repetir == "si":
            calculadora()
        else: 
            print ("Gracias por utilizar esta calculadora. Hasta pronto!")
