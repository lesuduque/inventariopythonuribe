productoTerminadoUno = {
    "referencia": 5087,
    "marca": "Americanino",
    "descripcion": "Chompa de acampargo",
    "color": "Naranja",
    "costoUnitario": 100000,
    "disponibleBodegan": True,
    "costoVenta": 850000,
    "puntosVenta": [
        "Cc Mayorca",
        "Terminal del Norte",
        "Puerta del norte",
        "Centro de la moda",
    ],
}

productoTerminadoDos = {
    "referencia": 5088,
    "marca": "Americanino",
    "descripcion": "Camiseta Polo",
    "color": "Azul oscuro",
    "costoUnitario": 30000,
    "disponibleBodegan": True,
    "costoVenta": 150000,
    "puntosVenta": [
        "Cc Mayorca",
        "Terminal del Norte",
        "Puerta del norte",
        "Centro de la modale",
    ],
}

# CREANDO UNA LISTA DE DICCIONARIOS
productos = [productoTerminadoUno, productoTerminadoDos]

# Recorriendo un lista con ciclo FOR
"""for contador in range(1,10,2):
            print(contador)"""

for producto in productos:
    for puntodeVenta in producto["puntosVenta"]:
        print(puntodeVenta)
