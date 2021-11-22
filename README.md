# Black_Jack

Este es el link de mi repositorio del Black Jack: [GitHub](https://github.com/rnoguer22/Black_Jack.git)

Hemos resuelto la tarea del juego del Black Jack, y hemos añadido un bucle while con una serie de condicionales para hacer que el juego sea un poquito mas parecido a lo que es el Black Jack en la vida real

Este es el diagrama de flujo que representa el codigo del juego:

![Diagrama de flujo - Black Jack drawio (1)](https://user-images.githubusercontent.com/91721762/142731864-f8a8321f-f5ae-45f5-89b7-fac135ccba1c.png)



El codigo del Black Jack es el siguiente:

```
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
}

# Enseñamos las cartas con las que vamos a jugar
print ("Estas son las cartas: {}".format(" - ".join(cartas.keys())))   

for key, value in sorted(cartas.items()):   # Mostramos al usuario cuantos puntos vale cada carta
    print ("{} vale {} puntos".format(key, value))

print ("Comienza el juego 😀")   # Empieza el juegazo

lista_cartas = list(cartas)   # Creamos una lista para posteriormente elegir las cartas
carta = choice (lista_cartas)   # Elegimos una carta de la lista

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

while True:
    x = cartas_jugador()
    y = cartas_de_la_banca()
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
```
