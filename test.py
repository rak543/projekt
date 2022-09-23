from klase.ucenici import Ucenik, Ponavljac, Maturant
from klase.nastavnici import Nastavnik, Redovni, Zamjena
from klase.razredi import Razred, Grupa


def test_ucenici():
    '''funkcija kreira listu objekata klase Ucenik, upisuje ih s tipkovnice, ispisuje podatke sortirane po prezimenu pa imenu'''
    uc1 = Ucenik('Ana','Anić','4236552','4.d','2019./2020.')
    uc2=Ucenik('Ivo','Ivić','523644','3.d','2019./2020.')
    uc3=Ucenik('Iva','Ivić','111644','4.d','2019./2020.')
    #matura={'mat':'A','hrv':'B', 'eng':'A','inf':'0'}
    #mat=Maturant('Leo','Leić','4236112','4.d','2019./2020.',matura)
    L=[]
    L.append(uc1)
    L.append(uc2)
    L.append(uc3)
    for i in L:
        if i.r=='4.d':
            print(i)

def test_nastavnici():
    '''funkcija koja kreira listu objekata nastavnika,  upisuje ih s tipkovnice, ispisuje podatke sortirane po prezimenu pa imenu'''
    pass

def test_predmeti():
    '''funkcija koja kreira listu objekata razreda,  upisuje ih s tipkovnice, ispisuje podatke sortirane po nazivu'''
    pass

test_ucenici()
    
