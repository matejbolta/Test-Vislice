import os
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
with open('besede.txt', encoding='utf-8') as datoteka_besed:
    for beseda in datoteka_besed:
        bazen_besed.append(beseda.strip().lower())

# class Igra:
#     def __init__(self, geslo, crke=None):
#         self.geslo = geslo
#         if crke is None:
#             self.crke = []
#         else:
#             self.crke = crke
    
#     def napacne_crke():
#         pass

#     def pravilne_crke():
#         pass




# Metodi napacne_crke in pravilne_crke, ki vrneta seznam pravilnih
#  oz. napačnih ugibanj igralca.

# Metodo stevilo_napak, ki izračuna koliko napačnih ugibov 
# je igralec že naredil.

# Metodi zmaga in poraz, ki preverita ali trenutno stanje
#  določa zmago oz. poraz.

# Metodo pravilni_del_gesla, ki vrne niz z že uganjenim 
# delom gesla, tako da neznane črke zamenja s podčrtajem.

# Metodo nepravilni_ugibi, ki vrne niz, ki vsebuje s presledkom
#  ločene nepravilne ugibe igralca.

# Metodo ugibaj, ki sprejme črko, jo pretvori v veliko črko,
#  in vrne primernega od PRAVILNA_CRKA, PONOVLJENA_CRKA, 
#  NAPACNA_CRKA, ZMAGA, PORAZ.

# V datoteki napišite kodo, ki iz datoteke besede.txt izlušči 
# nabor besed in ga shrani v seznam bazen_besed.

# Napišite funkcijo nova_igra, ki zgradi in vrne novo igro, ki
#  ima za geslo naključno izbrano besedo iz seznama bazen_besed.
