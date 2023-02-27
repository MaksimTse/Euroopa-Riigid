
sonastik={}
def Loe(file1:str):
    file=open(file1,'r', encoding='utf-8-sig')
    for line in file:
        k, v=line.strip().split('-')
        sonastik[k.strip()] = v.strip()
    return (sonastik)

def find(d:dict, v:int):
    word=input()
    x=sonastik.get(word)
    if x==None:
        p=o.get(word)
        if p==None:
            err=input('Lisada uue riigi või pealinn?').lower()
            while err not in ['jah','ei']:
                err=input('Ainult jah või ei')
            if err=='jah':
                loc=input(f'Kas {word} on riigi või pealinna').lower()