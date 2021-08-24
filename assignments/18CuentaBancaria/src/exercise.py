def main():
    #escribe tu código abajo de esta línea
    pass

sma= float(input("Dame el saldo del mes anterior: "))
ing= float(input("Dame los ingresos de este mes: "))
eg= float(input("Dame los egresos de este mes: "))
ch= int(input("Dame el número de cheques: "))

csf= (((sma+ing)-eg)-ch*13)*0.075
sf= (((sma+ing)-eg)-ch*13)-csf

print("El saldo final de la cuenta es: ",sf)

if __name__ == '__main__':
    main()
