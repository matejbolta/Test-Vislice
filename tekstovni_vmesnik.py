#          _____  
#         |/   |  
#         |    o  
#         |   /|\ 
#         |   / \ 
#        _|_______

import model

# print('\033[1;94m' + niz + '\033[0m')
# 90 sivo, 91 rdeče, 92 zeleno, 93 rumeno, 94 modro, 95 roza, 96 svetlo modro, 97 krepko 
ime = input('\nKako ti je ime?  >')
_ = input(f'\nŽivijo {ime[0].upper() + ime[1:].lower()}, zelo appreciatam da igras mojo igrico.\nPritisni enter in začni igrati!')

def izpis_poraza(igra):
    tekst = ('\033[1;97m    ---------------\033[0m\n'
    '\033[1;91m    ---------------\033[0m\n'
    '\033[1;91m    ---------------\033[0m\n'
    f'\033[1;91m       YOU LOST\033[0m\n'
    '         _____  \n'
    '        |/   |  \n'
    '        |    o  \n'
    '        |   /|\ \n'
    '        |   / \ \n'
    '       _|_______\n\n'
    f'\033[1;97m    Pravilno geslo je bilo: {igra.geslo}\033[0m\n'
    f'\033[1;94m    Uganiti ti je uspelo:   {igra.pravilni_del_gesla()}\033[0m\n\n'
    f'\033[1;92m    Zmanjkalo ti je {len(igra.geslo) - len(igra.pravilne_crke())} črk.\033[0m\n\n'
    '\033[1;91m    ---------------\033[0m\n'
    '\033[1;91m    ---------------\033[0m\n'
    '\033[1;97m    ---------------\033[0m'
    )
    return '\n' * 50 + tekst

def izpis_zmage(igra):
    tekst = ('\033[1;97m    ---------------\033[0m\n'
    '\033[1;96m    ---------------\033[0m\n'
    '\033[1;92m    ---------------\033[0m\n\n\n'
    f'\033[1;92m     !!!YOU WON!!!\033[0m\n\n\n'
    f'\033[1;94m    Geslo: {igra.geslo}\033[0m\n'
    f'\033[1;90m    Potreboval si {len(igra.crke)} ugibov\033[0m\n\n'
    '\033[1;92m    ---------------\033[0m\n'
    '\033[1;96m    ---------------\033[0m\n'
    '\033[1;97m    ---------------\033[0m'
    )
    return '\n' * 50 + tekst

def izpis_igre(igra):
    if igra.stevilo_napak() == 0:
        pajac = '\n'
    elif igra.stevilo_napak() == 1:
        pajac = (
            '\n    _ _______\n'
        )
    elif igra.stevilo_napak() == 2:
        pajac = (
            '\n     |       \n'
            '     |       \n'
            '     |       \n'
            '     |       \n'
            '    _|_______\n'
        )
    elif igra.stevilo_napak() == 3:
        pajac = (
            '      _____  \n'
            '     |       \n'
            '     |       \n'
            '     |       \n'
            '     |       \n'
            '    _|_______\n'
        )
    elif igra.stevilo_napak() == 4:
        pajac = (
            '      _____  \n'
            '     |/      \n'
            '     |       \n'
            '     |       \n'
            '     |       \n'
            '    _|_______\n'
        )
    elif igra.stevilo_napak() == 5:
        pajac = (
            '      _____  \n'
            '     |/   |  \n'
            '     |       \n'
            '     |       \n'
            '     |       \n'
            '    _|_______\n'
        )
    elif igra.stevilo_napak() == 6:
        pajac = (
            '      _____  \n'
            '     |/   |  \n'
            '     |    o  \n'
            '     |       \n'
            '     |       \n'
            '    _|_______\n'
        )
    elif igra.stevilo_napak() == 7:
        pajac = (
            '      _____  \n'
            '     |/   |  \n'
            '     |    o  \n'
            '     |    |  \n'
            '     |       \n'
            '    _|_______\n'
        )
    elif igra.stevilo_napak() == 8:
        pajac = (
            '      _____  \n'
            '     |/   |  \n'
            '     |    o  \n'
            '     |   /|  \n'
            '     |       \n'
            '    _|_______\n'
        )
    elif igra.stevilo_napak() == 9:
        pajac = (
            '      _____  \n'
            '     |/   |  \n'
            '     |    o  \n'
            '     |   /|\ \n'
            '     |       \n'
            '    _|_______\n'
        )
    else:
        pajac = (
            '      _____  \n'
            '     |/   |  \n'
            '     |    o  \n'
            '     |   /|\ \n'
            '     |   /   \n'
            '    _|_______\n'
        )

    tekst = '\033[1;94m' + '\n' * 50 + '  -------------\n    ---------\n      -----\n\n\033[0m' + pajac + (
        f'\033[1;94m\n Geslo: {igra.pravilni_del_gesla()}\033[0m\n\n'
        f'\033[1;91m Napačno ugibane črke: {igra.nepravilni_ugibi()}\033[0m\n\n'
        f'\033[1;90m Zmotiš se lahko še {model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak()}-krat.\n\033[0m'
    )
    return tekst

def zahtevaj_vnos():
    vnos = input('Ugibaj črko: >')
    if len(vnos) != 1 or not vnos.isalpha():
        print('\nProsim, vnesi ' + '\033[1;91mčrko\033[0m')
        return zahtevaj_vnos()
    return vnos

def ponudi_naslednjo_igro():
    izbira = input('\033[1;97m\nAli želis ponovno igrati? (da / ne) >\033[0m')
    if izbira.lower() == 'da' or izbira.lower() == 'ja':
        pozeni_vmesnik()
    elif izbira.lower() =='grem raje spat' or izbira.lower() == 'ne':
        print(f'\n{ime[0].upper() + ime[1:].lower()}, želim ti vse najboljše v tvojem življenju, dragi popotnik v prostoru in času.\n\n')
        return
    else:
        print('\nProsim, vnesi ' + '\033[1;92mda\033[0m' + ' ali ' + '\033[1;91mne\033[0m')
        return ponudi_naslednjo_igro()

def pozeni_vmesnik():
    # Naredimo novo igro
    trenutna_igra = model.nova_igra()

    while True:
        # Pokažemo mu stanje
        print(izpis_igre(trenutna_igra))

        crka = zahtevaj_vnos()

        trenutna_igra.ugibaj(crka)

        if trenutna_igra.je_zmaga():
            print(izpis_zmage(trenutna_igra))
            return ponudi_naslednjo_igro()
        
        if trenutna_igra.je_poraz():
            print(izpis_poraza(trenutna_igra))
            return ponudi_naslednjo_igro()

pozeni_vmesnik()
