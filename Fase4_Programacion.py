from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, Asesoria
from reserva import Reserva
import logging


logging.basicConfig(
    filename='errores.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

print("\n===== SOFTWARE FJ =====\n")

# CLIENTE VÁLIDO
try:

    cliente1 = Cliente(
        "Didier Leal",
        "didier@gmail.com",
        "3124567890"
    )

    print(cliente1.mostrar_info())

except Exception as e:

    logging.error(e)

    print(e)

# CLIENTE INVÁLIDO
try:

    cliente2 = Cliente(
        "",
        "correo",
        "123"
    )

except Exception as e:

    logging.error(e)

    print(f"Error cliente: {e}")

# SERVICIOS
try:

    sala = ReservaSala(
        "Sala Premium",
        50000
    )

    equipo = AlquilerEquipo(
        "Laptop Gamer",
        80000
    )

    asesoria = Asesoria(
        "Asesoría Python",
        100000
    )

except Exception as e:

    logging.error(e)

# RESERVA EXITOSA
try:

    reserva1 = Reserva(
        cliente1,
        sala,
        3
    )

    reserva1.confirmar()

except Exception as e:

    logging.error(e)

# RESERVA FALLIDA
try:

    reserva2 = Reserva(
        cliente1,
        equipo,
        -1
    )

    reserva2.confirmar()

except Exception as e:

    logging.error(e)

    print(f"Error reserva: {e}")

print("\nSistema ejecutado correctamente")
