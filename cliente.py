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

    def get_correo(self):
        return self.__correo

    def get_telefono(self):
        return self.__telefono

    def mostrar_info(self):
        return f"""
Nombre: {self.__nombre}
Correo: {self.__correo}
Teléfono: {self.__telefono}
"""
