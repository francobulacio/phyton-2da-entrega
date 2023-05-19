class Persona:
    def __init__(self, nombre, edad, telefono):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono

    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Teléfono:", self.telefono)


class Cliente(Persona):
    def __init__(self, nombre, correo, direccion, edad, telefono):
        super().__init__(nombre, edad, telefono)
        self.correo = correo
        self.direccion = direccion

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Correo electrónico:", self.correo)
        print("Dirección:", self.direccion)

    def actualizar_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion
        print("La dirección se ha actualizado correctamente.")

    def enviar_correo_promocional(self):
        print("Se ha enviado un correo promocional a", self.correo)

Franco = Cliente("Franco", 38, 1234567890)
Ernesto = Cliente("Ernesto", 35, 504556405)
Camila = Cliente("Camila", 32, 304045549)