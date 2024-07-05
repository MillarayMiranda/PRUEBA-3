import globales
import funciones
import os

def menu_general():
    while True:
        os.system("cls")
        print("===MENÚ GENERAL===\n")
        print("1. Asignar montos aleatorios")
        print("2. Ver estadísticas")
        print("3. Eliminar datos")
        print("4. Salir del programa\n")

        opcion = globales.seleccionar_opcion(4)

        if opcion == 1:
            funciones.asignar_valores_aleatorios()
        elif opcion == 2:
            funciones.buscar_producto_mas_alto()
            funciones.buscar_iva_mas_bajo()
            funciones.obtener_promedio_valores()
            funciones.obtener_media_geometrica()

            input()
        elif opcion == 3:
            globales.eliminar_archivo('productos.json')
        elif opcion == 4:
            break


if __name__ == "__main__":
    menu_general()        
