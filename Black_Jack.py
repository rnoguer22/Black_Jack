from random import choice, sample   # Importamos random para utilizarlo mas tarde

cartas = {   # Definimos un diccionario con las cartas y los puntos que vale cada carta
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
    
    chr(0x1f0b1): 11,
    chr(0x1f0b2): 2,
    chr(0x1f0b3): 3,
    chr(0x1f0b4): 4,
    chr(0x1f0b5): 5,
    chr(0x1f0b6): 6,
    chr(0x1f0b7): 7,
    chr(0x1f0b8): 8,
    chr(0x1f0b9): 9,
    chr(0x1f0ba): 10,
    chr(0x1f0bb): 10,
    chr(0x1f0bd): 10,
    chr(0x1f0be): 10,
    
    chr(0x1f0c1): 11,
    chr(0x1f0c2): 2,
    chr(0x1f0c3): 3,
    chr(0x1f0c4): 4,
    chr(0x1f0c5): 5,
    chr(0x1f0c6): 6,
    chr(0x1f0c7): 7,
    chr(0x1f0c8): 8,
    chr(0x1f0c9): 9,
    chr(0x1f0ca): 10,
    chr(0x1f0cb): 10,
    chr(0x1f0cd): 10,
    chr(0x1f0ce): 10,
    
    chr(0x1f0d1): 11,
    chr(0x1f0d2): 2,
    chr(0x1f0d3): 3,
    chr(0x1f0d4): 4,
    chr(0x1f0d5): 5,
    chr(0x1f0d6): 6,
    chr(0x1f0d7): 7,
    chr(0x1f0d8): 8,
    chr(0x1f0d9): 9,
    chr(0x1f0da): 10,
    chr(0x1f0db): 10,
    chr(0x1f0dd): 10,
    chr(0x1f0de): 10,
}

# Enseñamos las cartas con las que vamos a jugar
print ("Estas son las cartas: {}".format(" - ".join(cartas.keys())))   

for key, value in sorted(cartas.items()):   # Mostramos al usuario cuantos puntos vale cada carta
    print ("{} vale {} puntos".format(key, value))

print ("Comienza el juego 😀")   # Empieza el juegazo

lista_cartas = list(cartas)   # Creamos una lista para posteriormente elegir las cartas
carta = choice (lista_cartas)   # Elegimos una carta de la lista

def elegir_jugadores():
    nombres = []
    jugadores = int(input('¿Cuantos jugadores van a jugar?: '))
    for i in range(jugadores):
        nombre = str(input('Nombre del jugador ' + str(i + 1)))
        nombres.append(nombre)

def cartas_jugador():   # Creamos una funcion que va a elegir las cartas del usuario y los puntos que valen
    mis_cartas = sample(lista_cartas, 2)   # Mostramos las dos cartas elegidas aleatoriamente para el usuario
    puntos = sum(cartas[carta] for carta in mis_cartas)   # Sumamos los puntos de las dos cartas
    print ("Estas son tus cartas:  {}  {}  --- que suman {} puntos".format(mis_cartas[0],
                                                         mis_cartas[1],puntos))
    return puntos   # Nos devuelve los puntos de las cartas, para usarlo posteriormente en un bucle while

def cartas_de_la_banca():   # Creamos otra funcion que va a elegir las cartas de la banca
    cartas_banca = sample(lista_cartas, 2)   # Muestra las dos cartas de la banca
    puntos_banca = sum(cartas[carta] for carta in cartas_banca)   # Hallamos la suma de los puntos de ambas cartas
    print ("La banca tiene estas cartas:  {}  {}  --- que suman {} puntazos".format(cartas_banca[0],
                                                    cartas_banca[1], puntos_banca))
    return puntos_banca   # Devuelve los puntos de las cartas de la banca, para compararlos con los puntos de las cartas del jugador

def numero_jugadores ():
    num_jugadores = int (input ("Cuantos jugadores van a jugar al Black Jack? "))
    for i in range (num_jugadores):
        jugadores = [jugadores(i)]
        jugadores.append(jugadores)
    return num_jugadores

while True:
    x = cartas_jugador()
    y = cartas_de_la_banca()
    jugadores = numero_jugadores
    if x <= 21 and y <= 21:   # Comenzamos a comparar los puntos del jugador y de la banca
        if x < y:
            if x < 21 and y == 21:
                print ("La banca ha hecho Black Jack, no hay na que hacer, has perdido la ronda")
            else:
                print ("La banca ha estado mas cerca de los 21 puntos, ya que tiene {} puntos y tu solo tienes {}"
                    .format(y, x))
                print ("Has pedido la ronda 🥺")
            break
        elif x > y:
            if x == 21 and y < 21:
                print ("Has hecho Black Jack!!! Vaya maquina has ganado!!! ")
            else:
                print ("¡Has ganado la apuesta! ya que tienes {} puntos mas que la banca 👊👊👊"
                    .format(x-y))
            break
        else:
            print ("La banca y tu teneis los mismos puntos, por lo que hay que repetir la ronda 😞")
    else:
        if x == 22 and y < 22:
            print ("Cheee que te has pasado de los 21 puntos, has perdido la ronda")
            break
        elif y == 22 and x < 22:
            print ("Vaya, la banca ha superado los 21 puntos, por lo que automaticamente ganas la ronda")
            break
        else:
            print ("Ambos os habeis pasado de 21 puntos y ademas habeis empatado, vaya paquetes, "
                "repetimos la ronda anda")
# Con esto acabaria el codigo del juego