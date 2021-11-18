from random import choice, sample

cartas = {
    chr(0x1f0a1): 11,
    chr(0x1f0a2): 2,
    chr(0x1f0a3): 3,
    chr(0x1f0a4): 4,
    chr(0x1f0a5): 5,
    chr(0x1f0a6): 6,
    chr(0x1f0a7): 7,
    chr(0x1f0a8): 8,
    chr(0x1f0a9): 9,
    chr(0x1f0aa): 10,
    chr(0x1f0ab): 10,
    chr(0x1f0ad): 10,
    chr(0x1f0ae): 10,
}

print ("Estas son las cartas: {}".format(" - ".join(cartas.keys())))

for key, value in cartas.items():
    print ("{} vale {} puntos".format(key, value))

print ("Comienza el juego 😀")

lista_cartas = list(cartas)
carta = choice (lista_cartas)

def cartas_jugador():
    mis_cartas = sample(lista_cartas, 2)
    puntos = sum(cartas[carta] for carta in mis_cartas)
    print ("Estas son tus cartas:  {}  {}  --- que suman {} puntos".format(mis_cartas[0],
                                                         mis_cartas[1],puntos))
def cartas_de_la_banca():
    cartas_banca = sample(lista_cartas, 2)
    puntos_banca = sum(cartas[carta] for carta in cartas_banca)
    print ("La banca tiene estas cartas  {}  {}  --- que suman {} puntazos".format(cartas_banca[0],
                                                    cartas_banca[1], puntos_banca))

cartas_jugador()
cartas_de_la_banca()