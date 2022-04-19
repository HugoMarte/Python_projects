def tipo_moneda (cual_moneda, cambio): #Esta funcion tiene dos variables que se completan posteriormente.
    pesos = int(input("Ingresa la calidad de pesos " + cual_moneda +" :"))
    #pesos = float (pesos)
    euro = cambio
    euros= pesos/euro
    euros=round (euros, 2) #La funcion round delimita la cantidad de decimales.
    euros= str (euros) #str convierte de numero a string (letra).
    print ("tienes $" + euros + " euros. Gracias por utilizar mis servicios.")

menu= """
Bienvenido al conversor de monedas.

1 - pesos Dominicanos.
2 - pesos Colombianos.
3 - pesos Argentinos.

Elige una opción: """

opcion = int (input (menu))

if opcion == 1:
    tipo_moneda ("Dominicanos", 64.74) #Aqui se definen las dos variables de la funcion "tipo_moneda".
elif opcion == 2:
    tipo_moneda ("Colombianos", 4589.40)
elif opcion == 3:
    tipo_moneda ("Argentinos", 116.439)
else:
    print ("Elige una opcion valida.")
#conversor
#while True:
    #repetir=input("¿Tienes otra consulta?")
    #if repetir == "si":
        #conversor
    #elif repetir == "no":
            #break
    #continue
#print ("Adios!")