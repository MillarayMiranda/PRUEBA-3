import random
import math
import globales

productos = ["Café Americano",
"Té Chai",
"Croissant",
"Jugo Naranja",
"Panini de Pavo y Queso",
"Pastel de Zanahoria",
"Espresso Doble",
"Batido de Frutas",
"Muffin",
"Ensalada",
"Chocolate Caliente",
"Tarta de Frambuesa",
"Sándwich de Huevo",
"Galletas de Avena",
"Frappé de Caramelo"
]

def asignar_valores_aleatorios():
    elementos = []

    for producto in productos:
        elemento = {
            "nombre": producto,
            "valor": random.randint(20,100)*100,
            "iva": 0
        }
        elementos.append(elemento)

    archivo = 'productos.json'

    globales.guardar_archivo_json(dir=archivo, data= elementos)    
    input("Se ha generado el valor de los productos, presione ENTER para continuar")

def buscar_producto_mas_alto():
    if not globales.archivo_existe('productos.json'):
        print("No existen datos en el programa, asigne valores primero")
        return None

    productos = globales.leer_archivo_json('productos.json')

    max_valor = max(productos, key=lambda x: x['valor'])

    print(f"El producto de mayor valor es {max_valor['nombre']} y su valor es ${max_valor['valor']}")   

def buscar_iva_mas_bajo():
    if not globales.archivo_existe('productos.json'):
        return None
    
    productos = globales.leer_archivo_json('productos.json')

    min_iva = min(productos, key=lambda x: x['iva'])

    print(f"El producto con menor iva es {min_iva['nombre']} y su iva es ${min_iva['iva']}")        

def obtener_promedio_valores():
    if not globales.archivo_existe('productos.json'):
        return None

    productos = globales.leer_archivo_json('productos.json')

    suma_valores = 0
    cant_productos = 0

    for producto in productos:
        suma_valores += producto['valor']
        cant_productos += 1

    promedio_valores = suma_valores /cant_productos
    print(f"El promedio de los valores de los productos es ${round(promedio_valores)}")    

def obtener_media_geometrica():
    if not globales.archivo_existe('productos.json'):
        return None

    productos = globales.leer_archivo_json('productos.json')

    suma_valores = 0
    cant_productos = 0

    for producto in productos:
        suma_valores += math.log(producto['valor'])
        cant_productos += 1

    media_geometrica= math.exp(suma_valores /cant_productos)
    print(f"La media geometrica de los valores de los productos es ${round(media_geometrica)}")