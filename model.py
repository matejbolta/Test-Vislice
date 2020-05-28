#    _____
#   |/   |
#   |    o
#   |   /|\
#   |   / \
#  _|_______

import random, json

LOGO = r'''
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


class Igra:
    def __init__(self, geslo, crke=None):
        self.geslo = geslo
        if crke is None:
            self.crke = []
        else:
            self.crke = [c.lower() for c in crke]

    def napacne_crke(self):
        '''vrne seznam napačnih ugibanj igralca'''
        return [c.upper() for c in self.crke if c not in self.geslo]

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
                rtr += crka.upper() + ' '
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

    def stevilo_pravilnih_crk_s_ponovitvami(self):
        stevec = 0
        for crka in self.geslo:
            if crka in self.crke:
                stevec += 1
            else:
                pass
        return stevec

class Vislice:
    '''
    Skrbi za trenutno stanje VEČ iger (imel bo več objektov tipa Igra)
    '''
    def __init__(self, datoteka_s_stanjem, datoteka_z_besedami='besede.txt'):
        # Slovar, ki ID-ju priredi objekt njegove igre
        self.igre = {}  #    str(int) --> (Igra, stanje)
        self.datoteka_s_stanjem = datoteka_s_stanjem
        self.datoteka_z_besedami = datoteka_z_besedami

    def prosti_id_igre(self):
        '''Vrne nek ID, ki ga ne uporablja nobena igra'''
        if not self.igre:
            return str(0)
        else:
            return str(max([int(id) for id in self.igre.keys()]) + 1)

    def nova_igra(self):
        self.nalozi_igre_iz_datoteke()

        # Zgradimo bazen besed iz datoteke z besedami
        with open(self.datoteka_z_besedami, 'r', encoding='utf-8') as in_file:
            bazen_besed = [beseda.strip().lower() for beseda in in_file]

        # Dobimo svež ID
        nov_id = self.prosti_id_igre()

        # Naredimo novo igro
        sveza_igra = Igra(random.choice(bazen_besed))

        # Vse to shranimo v self.igre
        self.igre[nov_id] = sveza_igra, ZACETEK

        self.zapisi_igre_v_datoteko()

        # Vrnemo nov ID
        return nov_id

    def ugibaj(self, id_igre, crka):
        self.nalozi_igre_iz_datoteke()

        # Dobimo staro igro ven
        trenutna_igra, _ = self.igre[id_igre]

        # Ugibamo crko
        novo_stanje = trenutna_igra.ugibaj(crka)

        # Zapišemo posodobljeno stanje in igro nazaj v 'BAZO'
        self.igre[id_igre] = (trenutna_igra, novo_stanje)

        self.zapisi_igre_v_datoteko()

    def zapisi_igre_v_datoteko(self):
        # {  id_igre : (  (  geslo,    ugibane_crke ),   stanje   )  }
        # {    '1'   : (  ( 'balkon',   'asdfghjl'  ),     '+'    )  }

        igre1 = {
            id_igre : ((igra.geslo, igra.crke), poskus)
            for id_igre, (igra, poskus) in self.igre.items()
            #   id_igre, (Igra, poskus)
        }

        with open(self.datoteka_s_stanjem, 'w', encoding='utf-8') as out_file:
            json.dump(igre1, out_file, ensure_ascii=False)

    def nalozi_igre_iz_datoteke(self):
        with open(self.datoteka_s_stanjem, 'r', encoding='utf-8') as in_file:
            igre_iz_diska = json.load(in_file)

        self.igre = {
            id_igre: (Igra(geslo, crke), poskus)
            for id_igre, ((geslo, crke), poskus) in igre_iz_diska.items()
        }


# Za statistiko
def odstotek(stevec, imenovalec):
    return round((stevec / imenovalec) * 100)

def statistika(datoteka_s_stanjem):
    slovar_statistik = {}
    vislice = Vislice(datoteka_s_stanjem)
    vislice.nalozi_igre_iz_datoteke()

    stevilo_iger = len(vislice.igre.keys())
    slovar_statistik['stevilo_iger'] = stevilo_iger
    
    if stevilo_iger:
        stevilo_zmag = sum([1 if poskus == ZMAGA else 0 for _, poskus in vislice.igre.values()])
        slovar_statistik['odstotek_zmag'] = f'{odstotek(stevilo_zmag, stevilo_iger)}%'

        stevilo_porazov = sum([1 if poskus == PORAZ else 0 for _, poskus in vislice.igre.values()])
        slovar_statistik['odstotek_porazov'] = f'{odstotek(stevilo_porazov, stevilo_iger)}%'

        stevilo_nedokoncnih_iger = stevilo_iger - stevilo_zmag - stevilo_porazov
        slovar_statistik['odstotek_nedokoncanih_iger'] = f'{odstotek(stevilo_nedokoncnih_iger, stevilo_iger)}%'

        najdaljse_uganjeno_geslo = max([igra.geslo if poskus == ZMAGA else '' for igra, poskus in vislice.igre.values()], key=len)
        slovar_statistik['najdaljse_uganjeno_geslo'] = najdaljse_uganjeno_geslo

        odstotki_uganjenih_crk = [odstotek(igra.stevilo_pravilnih_crk_s_ponovitvami(), len(igra.geslo)) for igra, _ in vislice.igre.values()]
        slovar_statistik['povprecen_odstotek_uganjenih_crk'] = f'{round(sum(odstotki_uganjenih_crk) / len(odstotki_uganjenih_crk), 1)}%'

    return slovar_statistik
