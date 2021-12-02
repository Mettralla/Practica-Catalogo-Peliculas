class Pelicula:

    def __init__(self, nombre: str) -> None:
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def set_nombre(self, nuevo_nombre: str):
        self._nombre = nuevo_nombre

    def __str__(self) -> str:
        return f'<Pelicula: {self._nombre}>'