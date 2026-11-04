def pago_horas_extra(valor_hora, diurnas, nocturnas):
    recargo_diurno = valor_hora * 1.25
    recargo_nocturno = valor_hora * 1.75

    total_pagar = round((recargo_nocturno * nocturnas) + (recargo_diurno * diurnas))

    return total_pagar

# Prueba con tus propios datos:
print(pago_horas_extra(10000, 2, 1))