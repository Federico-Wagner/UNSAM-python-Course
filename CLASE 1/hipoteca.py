# hipoteca.py

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 1
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    if pago_extra_mes_comienzo <= mes <= pago_extra_mes_fin:
        pago_del_mes = pago_mensual + pago_extra
    else:
        pago_del_mes = pago_mensual

    saldo = saldo * (1 + tasa / 12) - pago_del_mes
    total_pagado = total_pagado + pago_del_mes
    mes = mes + 1
    if saldo < 0:
        total_pagado = total_pagado + saldo
        saldo = 0


    print(mes, round(total_pagado, 2), round(saldo, 2))

print('Total pagado:', round(total_pagado, 2))
print('Meses:', mes-1)