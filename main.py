from desafio4 import CuentaBancaria, CuentaBancariaCorriente, CuentaBancariaAhorro
import json

def menu_principal():
    print("Bienvenido al sistema de gestión de cuentas bancarias.")
    print("1. Crear cuenta")
    print("2. Consultar cuenta")
    print("3. Depositar")
    print("4. Retirar")
    print("5. Salir")

def crear_cuenta():
    numero_cuenta = input("Ingrese el número de cuenta: ")
    saldo = float(input("Ingrese el saldo inicial: "))
    titular = input("Ingrese el nombre del titular: ")

    tipo_cuenta = input("Seleccione el tipo de cuenta (Corriente/Ahorro): ").lower()

    if tipo_cuenta == 'corriente':
        descubierto = float(input("Ingrese el límite de descubierto autorizado: "))
        cuenta = CuentaBancariaCorriente(numero_cuenta, saldo, titular, descubierto)
    elif tipo_cuenta == 'ahorro':
        interes = float(input("Ingrese la tasa de interés (%): "))
        cuenta = CuentaBancariaAhorro(numero_cuenta, saldo, titular, interes)
    else:
        print("Tipo de cuenta no válido.")
        return

    cuenta.guardar_json()

def consultar_cuenta():
    numero_cuenta = input("Ingrese el número de cuenta: ")
    try:
        with open(f"cuenta_{numero_cuenta}.json", 'r') as file:
            cuenta_data = json.load(file)
            print("Información de la cuenta:")
            print(f"Número de cuenta: {cuenta_data['numero_cuenta']}")
            print(f"Titular: {cuenta_data['titular']}")
            print(f"Saldo: {cuenta_data['saldo']}")
    except FileNotFoundError:
        print("Error: La cuenta especificada no existe.")

def depositar():
    numero_cuenta = input("Ingrese el número de cuenta: ")
    try:
        with open(f"cuenta_{numero_cuenta}.json", 'r') as file:
            cuenta_data = json.load(file)
            cuenta = CuentaBancaria(cuenta_data['numero_cuenta'], cuenta_data['saldo'], cuenta_data['titular'])
            monto = float(input("Ingrese el monto a depositar: "))
            cuenta.depositar(monto)
            cuenta.guardar_json()
    except FileNotFoundError:
        print("Error: La cuenta especificada no existe.")
    except ValueError:
        print("Error: Ingrese un monto válido.")

def retirar():
    numero_cuenta = input("Ingrese el número de cuenta: ")
    try:
        with open(f"cuenta_{numero_cuenta}.json", 'r') as file:
            cuenta_data = json.load(file)
            cuenta = CuentaBancaria(cuenta_data['numero_cuenta'], cuenta_data['saldo'], cuenta_data['titular'])
            monto = float(input("Ingrese el monto a retirar: "))
            cuenta.retirar(monto)
            cuenta.guardar_json()
    except FileNotFoundError:
        print("Error: La cuenta especificada no existe.")
    except ValueError:
        print("Error: Ingrese un monto válido.")

def main():
    while True:
        menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            crear_cuenta()
        elif opcion == '2':
            consultar_cuenta()
        elif opcion == '3':
            depositar()
        elif opcion == '4':
            retirar()
        elif opcion == '5':
            print("Gracias por utilizar nuestro sistema.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
