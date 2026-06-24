from validaciones import Validacion

def realizar_extraccion(saldo_actual, monto):
    if validar_extraccion(monto, saldo_actual):
        saldo_nuevo: saldo_actual - monto
        print("Operacion Aprobada")
        return saldo_nuevo
    return saldo_actual

def realizar_deposito(saldo_actual, monto):
    if validar_deposito(monto):
        return saldo_actual + monto
    return saldo_actual

def realizar_transferencias(saldo_actual, monto_a_transferir):
    if validar_extraccion(monto_a_transferir, saldo_actual):
        return saldo_actual - monto_a_transferir
    return saldo_actual

def realizar_