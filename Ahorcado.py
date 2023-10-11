from random import choice
def eligePalabra():
    palabras = ["murcielago", "computadora", "pantalones", "elefante", "bicicleta", "guitarra", "flamenco",
                    "carambola", "heladera", "sombrero", "avión", "sandía", "orangután", "serpiente", "hipopotamo",
                    "mariposa", "esmeralda", "albóndiga", "melodía", "camaleon", "pinguino", "dinosaurio",
                     "caballero", "guitarra", "unicornio", "paraguas", "africa", "pluma"]
    return choice(palabras)

def mostrarPalabra(palabra, letras_adivinadas):
    resultado = ""
    letrasQueSalieron = []
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra
        else:
            resultado += " _ "
            letrasQueSalieron.append(letra)
    return resultado


def juego():
    palabra_secreta = eligePalabra()
    vidas = 6
    letra_adivinadas = []
    letras_que_salieron = []
       
    print("Hola vamos a jugar al ahorcado")
    print("A ver si sos tan bueno y adivinas esta palabra ;)") 
    
    while vidas > 0:
        palabra_actual = mostrarPalabra(palabra_secreta, letra_adivinadas)
        print(f"La palabra es {palabra_actual}")
        
        letra = input("Elige una letra: ")

        if letra in palabra_secreta:
            letra_adivinadas.append(letra)
            print("****************************************************")
            print(f"Exelente, la palabra contiene {letra}")
            print(vidas)
        else:
            vidas -= 1
            print("****************************************************")
            print(f"La palabra no contiene {letra}")
            letras_que_salieron.append(letra)
            print(f"Letras que ya has dicho {letras_que_salieron}")
            print(vidas)


        if palabra_actual == palabra_secreta:
            print(f"Felicitaciones! Lo lograste! efectivamente la palabra era {palabra_secreta}")
            break

        if vidas == 0:
            print(f"Lo lamento, has quedado sin vidas :( ")
            print(f"Pero te espero para que juguemos cuando quieras :)")
            print(palabra_secreta)
            break

juego()

        
        


    