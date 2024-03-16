def calcular_descuento(monto_total):
    descuento = 0
    if monto_total > 100:
        descuento = 0.1  # 10% de descuento si el monto supera los 100
    elif monto_total > 50:
        descuento = 0.05  # 5% de descuento si el monto supera los 50 pero no los 100

    monto_final = monto_total - (monto_total * descuento)
    return monto_final


def main():
    try:
        monto_total = float(input("Ingrese el monto total de la compra: "))
        if monto_total < 0:
            print("El monto total de la compra no puede ser negativo.")
            return
        monto_final = calcular_descuento(monto_total)
        print("El monto final a pagar es: $", monto_final)
    except ValueError:
        print("Por favor, ingrese un monto válido.")


if __name__ == "__main__":
    main()