#    _____
#   |/   |
#   |    o
#   |   /|\
#   |   / \
#  _|_______

import random

LOGO = '''
____   ____.__       .__  .__              
\   \ /   /|__| _____|  | |__| ____  ____  
 \   Y   / |  |/  ___/  | |  |/ ___\/ __ \ 
  \     /  |  |\___ \|  |_|  \  \__\  ___/ 
   \___/   |__/______>____/__|\_____>_____>
                                           
'''

# Potrebno le, če je v urejevalniku odprt višji path.
#import random
#os.chdir('UvP/Vislice')

STEVILO_DOVOLJENIH_NAPAK = 10

# Konstanta Igre ob začetku igre
ZACETEK = 'Z'

# Konstante za rezultate ugibanj
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

# Konstante za zmago in poraz
ZMAGA = 'W'
PORAZ = 'X'

# Zgradimo bazen besed iz datoteke z besedami
bazen_besed = []
with open('besede.txt', 'r', encoding='utf-8') as datoteka_besed:
    for beseda in datoteka_besed:
        bazen_besed.append(beseda.strip().lower())

class Igra:
    def __init__(self, geslo, crke=None):
        self.geslo = geslo
        if crke is None:
            self.crke = []
        else:
            self.crke = [c.lower() for c in crke]

    def napacne_crke(self):
        '''vrne seznam napačnih ugibanj igralca'''
        return [c for c in self.crke if c not in self.geslo]

    def pravilne_crke(self):
        '''vrne seznam pravilnih ugibanj igralca'''
        return [c for c in self.crke if c in self.geslo]

    def stevilo_napak(self):
        '''izračuna koliko napačnih ugibov je igralec že naredil'''
        return len(self.napacne_crke())

    def je_zmaga(self):
        return all(c in self.crke for c in self.geslo)

    def je_poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        '''vrne niz z že uganjenim delom gesla, tako da neznane črke zamenja s podčrtajem'''
        rtr = ''
        for crka in self.geslo:
            if crka in self.crke:
                rtr += crka + ' '
            else:
                rtr += '_ '

        return rtr[:-1]

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


# Naredimo funkcijo za novo igro
def nova_igra():
    return Igra(random.choice(bazen_besed))


class Vislice:
    '''
    Skrbi za trenutno stanje VEČ iger (imel bo več objektov tipa Igra)
    '''
    def __init__(self,):
        # Slovar, ki ID-ju priredi objekt njegove igre
        self.igre = {}  #    int --> (Igra, stanje)

    def prosti_id_igre(self):
        '''Vrne nek ID, ki ga ne uporablja nobena igra'''
        return len(self.igre)
        #if not self.igre:
        #    return 0
        #else:
        #    return max(self.igre.keys()) + 1

    def nova_igra(self):
        
        # Dobimo svež ID
        nov_id = self.prosti_id_igre()

        # Naredimo novo igro
        sveza_igra = nova_igra()

        # Vse to shranimo v self.igre
        self.igre[nov_id] = sveza_igra, ZACETEK

        # Vrnemo nov ID
        return nov_id

    def ugibaj(self, id_igre, crka):
        # Dobimo staro igro ven
        trenutna_igra, _ = self.igre[id_igre]

        # Ugibamo crko
        novo_stanje = trenutna_igra.ugibaj(crka)

        # Zapišemo posodobljeno stanje in igro nazaj v 'BAZO'
        self.igre[id_igre] = (trenutna_igra, novo_stanje)
