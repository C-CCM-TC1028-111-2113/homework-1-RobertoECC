def main():
    #escribe tu código abajo de esta línea
    #Leer los datos
    pass

msj= int(input("Dame el numero de mensajes: "))
mg= float(input("Dame le número de megas: "))
min= float(input("Dame le número de minutos: "))

CM= (msj*0.80)+(mg*0.80)+(min*0.80)

print("El costo mensual es: ",CM)

if __name__ == '__main__':
    main()
