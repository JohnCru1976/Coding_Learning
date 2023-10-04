class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
        
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Datos cliente\n\tNombre: {self.nombre}\n\tApellido: {self.apellido}\n\tNúmero de cuenta: {self.numero_cuenta}\n\tBalance: {self.balance}"

    def depositar(self, cantidad):
        self.balance += cantidad
        self.balance = round(self.balance, 2)

    def retirar(self, cantidad):
        if self.balance - cantidad < 0:
            return -1
        else:
            self.balance -= cantidad
            self.balance = round(self.balance, 2)
            return self.balance
        