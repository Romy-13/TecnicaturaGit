from abc import ABC, abstractmethod
# ABC significa: Abstrac base class, convierte una clase en abstracta

class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        if self._validar_valores(ancho):
            if 0 < ancho < 10:
                self._ancho = ancho
        else:
            self._ancho = 0
            print(f"valor erroneo para el ancho: {ancho}")
        if self._validar_valores(ancho):
            if self._validar_valores(ancho):
                self._alto= alto
        else:
            self._alto = 0
            print(f"valor erroneo para el ancho: {alto}")

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valores(ancho):
            self._ancho = ancho
        else:
            print(f'valor erroneo ancho: {ancho}')

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validar_valores(alto):
            self._alto = alto
        else:
            print(f'valor erroneo alto: {alto}')

    @abstractmethod
    def calcular_area(self):
        pass

    def __str__(self):
        return f"figura Geometrica (Ancho: {self._ancho}, Alto: {self._alto}"

    # Método encapsulado
    def _validar_valores(self,valor):
        return True if 0 < valor < 10 else False

