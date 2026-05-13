class Reserva:

    def __init__(self, cliente, servicio, tiempo):

        if tiempo <= 0:
            raise ValueError("Tiempo inválido")

        self.cliente = cliente
        self.servicio = servicio
        self.tiempo = tiempo
        self.estado = "Pendiente"

    def confirmar(self):

        self.estado = "Confirmada"

        total = self.servicio.calcular_costo(self.tiempo)

        print(f"Reserva confirmada para {self.cliente.get_nombre()}")
        print(f"Total a pagar: {total}")

    def cancelar(self):

        self.estado = "Cancelada"

        print("Reserva cancelada")
