class Cliente:

    def __init__(self, nombre, correo, telefono):

        if not nombre:
            raise ValueError("El nombre no puede estar vacío")

        if "@" not in correo:
            raise ValueError("Correo inválido")

        if len(telefono) < 10:
            raise ValueError("Teléfono inválido")

        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

    def get_nombre(self):
        return self.__nombre

    def mostrar_info(self):
        return f"Cliente: {self.__nombre}"
