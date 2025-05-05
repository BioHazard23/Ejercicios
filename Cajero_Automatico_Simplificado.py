#Cajero automatico

import time
saldo = 15000000
movimientos = []

while True:
    time.sleep (0.6)
    print ("\n  1. Ver saldo.")
    print ("\n  2. Retirar dinero.")
    print ("\n  3. Agregar dinero.")
    print ("\n  4. Ver movimientos.")
    print ("\n  5. Salir")
    opcion = int(input ("\nEscoge una de las opciones: "))

    if opcion == 1:
        time.sleep (0.6)
        print ("\nSaldo actual:",saldo)
        movimientos.append("Vio el saldo")

    elif opcion == 2:
        time.sleep (0.6)
        retirar = int(input("Ingresa cantidad a retirar: "))
        if retirar <= saldo:
            saldo -= retirar
            print ("Retiraste de tu cuenta:", retirar)
            movimientos.append(f"Se retiro {retirar}")
        else:
            print("Saldo insuficiente")
            movimientos.append("Se intento retirar sin saldo")

    elif opcion == 3:
        time.sleep (0.6)
        agregar = int(input("Ingresar cantidad a depositar: "))
        saldo += agregar
        print ("Depositaste:",agregar)
        movimientos.append(f"Se deposito {agregar}")

    elif opcion == 4:
        time.sleep (0.6)
        for movimientos in movimientos:
            print(movimientos)

    elif opcion == 5:
        time.sleep (0.6)
        print ("¡Bye!")
        break

    else:
        print("Opcion invalida")


