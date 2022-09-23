class Razred:
    def __init__(self, naziv, smjer, OIB_razrednika, br_ucenika):
        '''klasa Razred kreira objekt s nazivom, smjerom, OIB-om razrednika i brojem učenika u tom razredu'''
        pass


class Grupa(Razred):
    def __init__(self, naziv, OIB_nastavnika, br_ucenika):
        '''nasljeđuje klasu Razred, ali nema smjer te umjesto razrednika ima OIB nastavnika koji vodi grupu'''
        pass
