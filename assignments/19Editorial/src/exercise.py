def main():
    #escribe tu código abajo de esta línea
    pass
palabras= int(input("Dame el número de palabras: "))
completas= (palabras//475)
medias= (palabras%475)

if (completas>0) and (medias>0):
    print("El número de páginas es: ", completas+1)
elif (completas>0) and (medias==0):
    print("El número de páginas es: ", completas)

if __name__ == '__main__':
    main()
