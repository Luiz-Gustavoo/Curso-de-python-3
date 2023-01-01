velocidade_carro = 120
local_carro = 110 # km100

LIMITE_RADAR = 120 #km/h
LOCAL_RADAR = 110
RADAR_RANGE = 1 # o radar aplica multa sendo o LOCAL_RADAR -1 ou +1

if velocidade_carro <= LIMITE_RADAR  and local_carro >= (LOCAL_RADAR - RADAR_RANGE) and local_carro <=(LOCAL_RADAR + RADAR_RANGE) : # local_carro tem que estar entre 109, 110 ou 111
    print('não foi multado')

elif velocidade_carro > LIMITE_RADAR and local_carro >= (LOCAL_RADAR - RADAR_RANGE) and local_carro <=(LOCAL_RADAR + RADAR_RANGE):
    print('multado')

