import bottle, model, random

# Potrebno le, če je v urejevalniku odprt višji path.
#import os
#os.chdir('UvP/Vislice')

LOGO = r'''
____   ____.__       .__  .__              
\   \ /   /|__| _____|  | |__| ____  ____  
 \   Y   / |  |/  ___/  | |  |/ ___\/ __ \ 
  \     /  |  |\___ \|  |_|  \  \__\  ___/ 
   \___/   |__/______>____/__|\_____>_____>
                                           
'''
ID_IGRE_COOKIE_NAME = 'id_igre'
COOKIE_SECRET = 'my very special - secret key and passphrase'

vislice = model.Vislice()
vislice.nalozi_igre_iz_datoteke()


@bottle.get('/')
def index():
    return bottle.template('index.tpl')


@bottle.post('/nova_igra/')
def nova_igra():
    id_nove_igre = vislice.nova_igra()
    bottle.response.set_cookie(
        ID_IGRE_COOKIE_NAME, str(id_nove_igre),
        path='/',
        secret=COOKIE_SECRET
    )

    bottle.redirect('/igra/')


@bottle.get('/igra/')
def pokazi_igro():
    id_igre = bottle.request.get_cookie(
        ID_IGRE_COOKIE_NAME,
        secret=COOKIE_SECRET
    )
    igra, poskus = vislice.igre[id_igre]

    return bottle.template('igra.tpl',
    igra=igra, poskus=poskus, id_igre=id_igre)


@bottle.post('/igra/')
def ugibaj():
    id_igre = bottle.request.get_cookie(
        ID_IGRE_COOKIE_NAME,
        secret=COOKIE_SECRET
    )

    crka = bottle.request.forms.getunicode('crka')
    
    if len(crka) != 1 or not crka.isalpha():
        bottle.redirect('/igra/')
    else:
        vislice.ugibaj(id_igre, crka)
        bottle.redirect('/igra/')


# Slika
@bottle.get('/img/<slika>')
def serve_pictures(slika):
    return bottle.static_file(slika, root='img')


bottle.run(debug=True, reloader=True)
