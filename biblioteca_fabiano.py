def calcular_reajuste(valor_base, idade):
    if idade <= 12:
        return valor_base * 1.3
    elif 13 <= idade <= 49:
        return valor_base * 1.1
    elif 50 <= idade <= 65:
        return valor_base * 1.15
    else:
        return valor_base * 1.35