# Nombre del estudiante: Josué Monge Miranda
# Contexto seleccionado: Cajero automático
# Descripción: permite hacer varios retiros sobre un mismo saldo hasta que el
# usuario decida salir o hasta que ya no haya saldo disponible.

# Constantes (reglas del problema)
SALDO_INICIAL = 250000
MINIMO = 5000
MAXIMO = 100000

# Variables que cambian durante la ejecución
saldo = SALDO_INICIAL
retiros_exitosos = 0  # contador

print("=== CAJERO AUTOMÁTICO ===")
print("Saldo inicial:", saldo, "colones")

# Entrada fuera del ciclo
continuar = input("¿Desea realizar un retiro? (s/n): ").lower()

while continuar == "s" and saldo > 0:
    # Entrada dentro del ciclo
    monto = int(input("Digite el monto a retirar: "))

    if monto < MINIMO or monto > MAXIMO:
        print("Monto fuera de rango. Debe ser entre", MINIMO, "y", MAXIMO, "colones.")
        print("Retiro NO realizado.")
    elif monto > saldo:
        print("Fondos insuficientes.")
        print("Retiro NO realizado.")
    else:
        saldo = saldo - monto
        retiros_exitosos = retiros_exitosos + 1
        print("Retiro realizado.")

    print("Saldo actualizado:", saldo, "colones")

    # Entrada dentro del ciclo: cambia la variable de control
    continuar = input("¿Desea realizar otro retiro? (s/n): ").lower()

# Resultados al terminar el ciclo
print("=== RESUMEN ===")
print("Saldo restante:", saldo, "colones")
print("Retiros exitosos:", retiros_exitosos)
