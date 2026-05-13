from abc import ABC, abstractmethod


class Servicio(ABC):

    def __init__(self, nombre, precio):

        if precio <= 0:
            raise ValueError("El precio debe ser mayor a cero")

        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_costo(self, tiempo):
        pass


class ReservaSala(Servicio):

    def calcular_costo(self, horas):
        return self.precio * horas


class AlquilerEquipo(Servicio):

    def calcular_costo(self, dias):
        return self.precio * dias


class Asesoria(Servicio):

    def calcular_costo(self, horas):
        return self.precio * horas
