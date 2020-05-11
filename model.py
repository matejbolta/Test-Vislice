import os, random
os.chdir('UvP/Vislice')

STEVILO_DOVOLJENIH_NAPAK = 10

# Konstante za rezultate ugibanj
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

# Konstante za zmago in poraz
ZMAGA = 'W'
PORAZ = 'X'

bazen_besed = []
with open('besede.txt', 'r', encoding='utf-8') as datoteka_besed:
    for beseda in datoteka_besed:
        bazen_besed.append(beseda.strip().lower())

 class Igra:
    def __init__(self, geslo, crke=None):
        self.geslo = geslo.lower()
        if crke is None:
            self.crke = []
        else:
            self.crke = [c.lower() for c in crke]

    def napacne_crke(self):
        '''vrnet seznam napačnih ugibanj igralca'''
        return [c for c in self.crke if c not in self.geslo]

    def pravilne_crke(self):
        '''vrnet seznam pravilnih ugibanj igralca'''
        return [c for c in self.crke if c in self.geslo]

    def stevilo_napak(self):
        '''izračuna koliko napačnih ugibov je igralec že naredil'''
        return len(self.napacne_crke)

    def je_zmaga(self):
        return all(c in self.crke for c in self.geslo)

    def je_poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        '''vrne niz z že uganjenim delom gesla, tako da neznane črke zamenja s podčrtajem'''
        rtr = ''
        for crka in self.geslo:
            if crka in self.crke:
                rtr += crka
            else:
                trenutno += '_'

        return rtr

    def nepravilni_ugibi(self):
        '''vrne niz, ki vsebuje s presledkom ločene nepravilne ugibe igralca'''
        return ' '.join(self.napacne_crke())

    def ugibaj(self, ugibana_crka):
        '''vrne primernega od PRAVILNA_CRKA, PONOVLJENA_CRKA, NAPACNA_CRKA, ZMAGA, PORAZ'''
        ugibana_crka = ugibana_crka.lower()
        if ugibana_crka in self.crke:
            return PONOVLJENA_CRKA
        
        self.crke.append(ugibana_crka)

        if ugibana_crka in self.geslo:
            if self.je_zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        else:
            if self.je_poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA


def nova_igra():
    return Igra(random.choice(bazen_besed))
