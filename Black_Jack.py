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
    return puntos

def cartas_de_la_banca():
    cartas_banca = sample(lista_cartas, 2)
    puntos_banca = sum(cartas[carta] for carta in cartas_banca)
    print ("La banca tiene estas cartas  {}  {}  --- que suman {} puntazos".format(cartas_banca[0],
                                                    cartas_banca[1], puntos_banca))
    return puntos_banca

while True:
    x = cartas_jugador()
    y = cartas_de_la_banca()
    if x < y:
        print ("La banca ha estado mas cerca de los 21 puntos, ya que tiene {} puntos y tu solo tienes {}"
                                                                                .format(x, y))
        break
    elif x > y:
        print ("¡Has ganado la apuesta! ya que tienes {} puntos mas que la banca"
            .format(x-y))
        break
    else:
        print ("La banca y tu teneis los mismos puntos, por lo que hay que repetir la ronda 🥺")