from dominio.pelicula import Pelicula
from servicio.catalogo_pelicula import CatalogoPeliculas

catalogo1 = CatalogoPeliculas('catalogo/servicio/catalogo_peliculas.txt')

def menu():
    while True:
        print('Bienvenido al Catalogo de Peliculas'.center(50, '-'))
        print('Escoja una opcion:'.center(50, '-'))
        print('''
        1. Agregar Pelicula
        2. Listar Peliculas
        3. Eliminar Catalogo de Peliculas
        4. Salir
        ''')
        
        opcion = int(input('Ingrese la opcion deseada: '))

        if opcion == 1:
            nueva_pelicula = input('Ingresar nombre de Pelicula: ')
            peli_catalogo = Pelicula(nueva_pelicula)
            catalogo1.agregar_pelicula(peli_catalogo)
        elif opcion == 2:
            catalogo1.lista_peliculas()
        elif opcion == 3:
            catalogo1.eliminar()
        elif opcion == 4:
            break 
        else: 
            print(('Opcion Invalida'.center(50, '-')))
            print('Ingrese una opcion valida (1-4)'.center(50, '-'))

menu()