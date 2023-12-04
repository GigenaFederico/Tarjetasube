from random import randint
import time

# Constantes
ID_INICIAL = '6061 268'
SALDO_DESCUBIERTO_MAXIMO = -100
TARIFA_VIAJE = 50
TIEMPO_PARA_DESCUENTO = 0.2

def generar_id():
    id_parcial = '6061 268' + str(randint(0, 9))
    for _ in range(2):
        id_parcial += ' ' + str(randint(0, 9999)).zfill(4)
    print('ID generado:', id_parcial)
    return id_parcial

def recargar(saldo, monto):
    try:
        if monto > 0:
            saldo += monto
            return saldo, True
        else:
            imprimir_error()
            return saldo, False
    except:
        imprimir_error()
        return saldo, False

def imprimir_error():
    print('Un error ha ocurrido! :(\nIntente nuevamente')

def tarifa_red_sube(tarifa_inicial, ultimo_viaje, viaje_actual):
    tarifa_final = tarifa_inicial
    if viaje_actual - ultimo_viaje <= TIEMPO_PARA_DESCUENTO:
        tarifa_final = tarifa_final * 0.5
    return tarifa_final

def registrar_viaje(ultimo_viaje, viaje_actual):
    return viaje_actual

class Sube():

    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0.0
        self.id = generar_id()
        self.ultimo_viaje = 0

def cobrar_viaje(sube, tipo_tarjeta):
    viaje_actual = time.time()

    if tipo_tarjeta == "Normal":
        tarifa = tarifa_red_sube(TARIFA_VIAJE, sube.ultimo_viaje, viaje_actual)
    elif tipo_tarjeta == "Diferencial":
        tarifa = tarifa_red_sube((TARIFA_VIAJE * 45) / 100, sube.ultimo_viaje, viaje_actual)
    else:
        print("Tipo de tarjeta no válido")
        return False

    if sube.saldo - tarifa >= SALDO_DESCUBIERTO_MAXIMO:
        sube.saldo -= tarifa
        sube.ultimo_viaje = registrar_viaje(sube.ultimo_viaje, viaje_actual)
        return True
    else:
        print('Saldo insuficiente')
        return False

# Ejemplo de uso
def main():
    titular = "John Doe"

    # Crear tarjeta Normal
    sube_normal = Sube(titular)
    sube_normal.saldo, _ = recargar(sube_normal.saldo, 100)
    cobrar_viaje(sube_normal, "Normal")

    # Crear tarjeta Diferencial
    sube_diferencial = Sube(titular)
    sube_diferencial.saldo, _ = recargar(sube_diferencial.saldo, 150)
    cobrar_viaje(sube_diferencial, "Diferencial")

if __name__ == "__main__":
    main()
    