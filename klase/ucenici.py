class Ucenik:
    def __init__(self, ime, prezime, OIB, godina, razred):
        '''klasa Ucenik kreira objekt s imenom, prezimenom, OIB-om, te školskom godinom i razredom koji učenik pohađa u toj godini'''
        self.i=ime
        self.p=prezime
        self.OIB=OIB
        self.g=godina
        self.r=razred
    def __repr__(self):
        return 'ime prezime:'+self.i+' '+self.p
    def __str__(self):
        return self.__repr__()

class Ponavljac(Ucenik):
    def __init__(self, ime, prezime, OIB, razred, godina, br_pon):
        '''nasljeđuje klasu Ucenik, ali dodaje svojstvo broj ponavljanja'''
        pass
        #ključna riječ pass se često koristi kao oznaka nulte operacije te čuva mjesto


class Maturant(Ucenik):
    def __init__(self, ime, prezime, OIB, razred, matura):
        '''nasljeđuje klasu Ucenik, ali dodaje rječnik matura koji ima oblik {'naziv predmeta na maturi':'razina A ili B'}'''
        pass
