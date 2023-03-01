from OmaMoodul import *
sõnastik={}
while True:
    v=int(input('''
    0-välju
    1-loeme failist
    2-Salvestame failisse 
    3-Vaata sõnastiku
    4-Näita riigi ja tema pealinna
    5-Paranda viga sõnastikus
    6-Test
    '''))
    if v==0:
        break
    if v==1:
        sõnastik=Loe_failist('Europa_Riigid')
    elif v==2:
        Kirjuta_failisse('Europa_Riigid')
    elif v==3:
        vaata_sõnastiku('Europa_Riigid')
    elif v==4:
       RP_find('Europa_Riigid')
    elif v==5:
        paranda('Europa_Riigid')
    elif v==6:
        test('Europa_Riigid')
