class Nastavnik:
    def __init__(self, ime, prezime, OIB, satnica):
        '''klasa Nastavnik kreira objekt o nastavnicima, satnica je tjedna oko 20 sati'''
        pass


class Redovni(Nastavnik):
    def __init__(self, ime, prezime, OIB, satnica, zaduzenje):
        '''nasljeđuje klasu Nastavnik, zaduzenje je lista razreda u kojima nastavnik predaje'''
        pass


class Zamjena(Nastavnik):
    def __init__(self, ime, prezime, OIB, satnica, zaduzenje, datum_od, datum_do):
        '''nasljeđuje klasu Nastavnik, zaduzenje je lista razreda u kojima nastavnik predaje ali u periodu datum_od i datum_do '''
        pass

