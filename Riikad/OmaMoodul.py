from random import *

sõnastik={}

def Loe_failist(fail:dict):
    '''
    loeb failist
    '''
    file=open(fail,'r',encoding='utf-8-sig')
    for line in file:
        k, v=line.strip().split('-')
    file.close()
    print(sõnastik)

def Kirjuta_failisse(fail:dict):
    '''
    sisetab failise
    '''
    file=open(fail,'r',encoding='utf-8-sig')
    for line in file:
        k, v=line.strip().split('-')
        sõnastik[k.strip()] = v.strip()    
    riik=input('Lisa riik: ')
    pealinn=input('Tema pealinn: ')
    sõnastik.update({riik:pealinn})
    file.close()
    print(sõnastik)
    return sõnastik

def vaata_sõnastiku(fail:dict):
    r={}
    p={}
    file=open(fail,'r',encoding='utf-8-sig')
    for line in file:
        k, v=line.strip().split('-')       
        r[k]=v
        p[v]=k
    file.close()
    print(r, p)   
    return r, p

def RP_find(fail:dict):
    file=open('Europa_Riigid','r',encoding='utf-8-sig')
    for line in file:
        k, v=line.strip().split('-')
        sõnastik[k.strip()] = v.strip()
    file.close()
    Riigid = list(sõnastik.keys())
    Pealinnad = list(sõnastik.values())
    RvP=input('Otsime riik või pealinn: ')
    while RvP not in ["riik","pealinn"]:
        RvP=input('riik või pealinn: ')
    if RvP=='riik':
        OtsimeR=input('Kirjuta riigi nimi: ')
        while OtsimeR not in Riigid:
            OtsimeR=input('Kirjuta riigi õigesti: ')
        num1=Riigid.index(OtsimeR)
        if OtsimeR == Riigid[num1]:
            print(OtsimeR,Pealinnad[num1])
    elif RvP=='pealinn':
        OtsimeP=input('Kirjuta pealinna nimi: ')
        while OtsimeP not in Pealinnad:
            OtsimeP=input('Kirjuta riigi õigesti: ')
        num1=Pealinnad.index(OtsimeP)
        if OtsimeP == Pealinnad[num1]:
            print(OtsimeP},'-',Riigid[num1])
          

def paranda(fail: dict):
    with open('Europa_Riigid', 'r', encoding='utf-8-sig') as file:
        for line in file:
            k, v = line.strip().split('-')
            sõnastik[k.strip()] = v.strip()

    while True:
        riik_või_pealinn = input('Kas soovite muuta riigi nime või pealinna nime? (r/p): ').lower()
        if riik_või_pealinn not in ['r', 'p']:
            print('Palun sisestage "r" või "p".')
        else:
            break
    
    if riik_või_pealinn == 'r':
        Rparanda = input('Millist riigi soovite parandada? ')
        while Rparanda not in sõnastik:
            Rparanda = input('Kirjutage õige riigi nimi: ')

        Rparandatud = input('Kirjutage parandatud riigi nimi: ')
        while not Rparandatud.isalpha():
            Rparandatud = input('Kirjutage riigi nimi: ')

        sõnastik[Rparandatud] = sõnastik.pop(Rparanda)

    else:
        Pparanda = input('Millist pealinna soovite parandada? ')
        while Pparanda not in sõnastik.values():
            Pparanda = input('Kirjutage õige pealinna nimi: ')

        Pparandatud = input('Kirjutage parandatud pealinna nimi: ')
        while not Pparandatud.isalpha():
            Pparandatud = input('Kirjutage pealinna nimi: ')

        for key, value in sõnastik.items():
            if value == Pparanda:
                sõnastik[key] = Pparandatud
                break
    
    with open(fail, 'w', encoding='utf-8-sig') as f:
        for key, value in sõnastik.items():
            f.write(f'{key}-{value}\n')
        print(sõnastik)


def test(fail:dict):
    a=[]
    vale=õige=0
    game=[]
    file=open('Europa_Riigid','r',encoding='utf-8-sig')
    for line in file:
        k, v=line.strip().split('-')
        sõnastik[k.strip()] = v.strip()
    file.close()
    Riigid = list(sõnastik.keys())
    Pealinnad = list(sõnastik.values())
    x=int(input('palju korda mängime? '))
    for i in range (x):
        num=randint(0,(len(Riigid)-1))
        while num in a:
            num=randint(0,(len(Riigid)-1))
        valik=input('Kas võtame riigi või pealinna? (riik või pealinn) ').lower()
        while valik not in ['riik','pealinn']:
            valik=input('Kirjuta riik või pealinn: ')
        if valik=='riik':
            rana=Riigid[num]
            tematähendus=input(f'Mis on riigi {rana} pealinn: ')
            if tematähendus==Pealinnad[num]:
                game.append(f'Mäng number {i+1} {valik} keeles - Õige')
                print('Õige')
                õige+=1
            else:
                game.append(f'Mäng number {i+1}, {valik} keeles - Vale') 
                print('Vale')
                vale+=1
        else:
            rana=Pealinnad[num]
            tematähendus=input(f'Mis on riigi {rana} pealinn: ') 
            if tematähendus==Pealinnad[num]:
                game.append(f'Mäng number {i+1} {valik} keeles - Õige')
                print('Õige')
                õige+=1
            else:
                game.append(f'Mäng number {i+1}, {valik} keeles - Vale') 
                print('Vale')
                vale+=1       
        a.append(num)
    print()
    print(game)
    if vale==0:
        resÕ=100
        resV=0
    elif õige==0:
        resÕ=0
        resV=100
    else:
        resÕ=round((õige/x)*100),1
        resV=round((vale/x)*100),1
    print(f'´Õige protsent - {resÕ}%')
    print(f'Vale protsent - {resV}%')
