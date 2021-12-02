import os

class CatalogoPeliculas:

    def __init__(self, ruta_archivo) -> None:
        self.ruta_archivo = ruta_archivo


    @staticmethod
    def agregar_pelicula(Pelicula):
        with open('catalogo/servicio/catalogo_peliculas.txt', 'a') as archivo:
            archivo.write(Pelicula.nombre + '\n')

    @staticmethod
    def lista_peliculas():
        with open('catalogo/servicio/catalogo_peliculas.txt') as archivo:
            texto = archivo.read()
            print(texto)

    @staticmethod
    def eliminar():
        os.remove('catalogo/servicio/catalogo_peliculas.txt')


