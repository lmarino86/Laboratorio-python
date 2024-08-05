import json

class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo, titular):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        self.titular = titular

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito de {monto} realizado. Saldo actual: {self.saldo}")
        else:
            print("Error: El monto del depósito debe ser mayor que cero.")

    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro de {monto} realizado. Saldo actual: {self.saldo}")
        else:
            print("Error: Fondos insuficientes para realizar el retiro o monto inválido.")

    def mostrar_informacion(self):
        print(f"Cuenta: {self.numero_cuenta}")
        print(f"Titular: {self.titular}")
        print(f"Saldo actual: {self.saldo}")

    def guardar_json(self):
        cuenta_data = {
            "numero_cuenta": self.numero_cuenta,
            "saldo": self.saldo,
            "titular": self.titular
        }
        filename = f"cuenta_{self.numero_cuenta}.json"
        with open(filename, 'w') as file:
            json.dump(cuenta_data, file)
            print(f"Datos de la cuenta {self.numero_cuenta} guardados en {filename}")

class CuentaBancariaCorriente(CuentaBancaria):
    def __init__(self, numero_cuenta, saldo, titular, descubierto):
        super().__init__(numero_cuenta, saldo, titular)
        self.descubierto = descubierto

    def autorizar_descubierto(self, monto):
        if monto <= self.descubierto:
            print(f"Se autoriza el descubierto por {monto}.")
        else:
            print("Error: Excede el límite de descubierto autorizado.")

class CuentaBancariaAhorro(CuentaBancaria):
    def __init__(self, numero_cuenta, saldo, titular, interes):
        super().__init__(numero_cuenta, saldo, titular)
        self.interes = interes

    def aplicar_interes(self):
        self.saldo += self.saldo * (self.interes / 100)
        print(f"Interés aplicado. Saldo actual: {self.saldo}")

