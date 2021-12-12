#rebotes.py

alt_inicial = 100
ratio_rebote = 0.6
rebotes_print = 10
alt_reb = 100

for i in range(10):
        alt_reb = alt_reb * ratio_rebote
        print(i+1,round(alt_reb,4))