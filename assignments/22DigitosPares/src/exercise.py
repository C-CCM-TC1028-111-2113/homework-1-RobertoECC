def main():
    #escribe tu código abajo de esta línea
    pass

numero= input("Dame un número de  4 dígitos: ")

if int(numero[0]) % 2 ==0:
    if int(numero[1]) % 2 ==0:
        if int(numero[2]) % 2 ==0:
            if int(numero[3]) % 2 ==0:
                print("El número tiene 4 digitos pares")
            else:
                print("El número tiene 3 digitos pares")
        else:
            print("El número tiene 2 digitos pares")
    else:
        print("El número tiene 1 digito par")
else:
    print("El numero no tiene digitos pares")

if __name__ == '__main__':
    main()
