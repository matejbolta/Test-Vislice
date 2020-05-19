import bottle, model

# Potrebno le, če je v urejevalniku odprta višji path.
#import os
#os.chdir('UvP/Vislice')

LOGO = '''
____   ____.__       .__  .__              
\   \ /   /|__| _____|  | |__| ____  ____  
 \   Y   / |  |/  ___/  | |  |/ ___\/ __ \ 
  \     /  |  |\___ \|  |_|  \  \__\  ___/ 
   \___/   |__/______>____/__|\_____>_____>
                                           
'''

vislice = model.Vislice()

@bottle.get('/')
def index():
    return bottle.template('index.tpl')

@bottle.post('/igra/')
def nova_igra():
    id_nove_igre = vislice.nova_igra()
    bottle.redirect(f'/igra/{id_nove_igre}/')

@bottle.get('/igra/<id_igre:int>/')
def pokazi_igro(id_igre):
    igra, poskus = vislice.igre[id_igre]

    return bottle.template('igra.tpl', igra=igra, poskus=poskus, id_igre=id_igre)

@bottle.post('/igra/<id_igre:int>/')
def ugibaj(id_igre):
    crka = bottle.request.forms.getunicode('crka')

    vislice.ugibaj(id_igre, crka)

    bottle.redirect(f'/igra/{id_igre}/')

# S funkcijo static_file lahko ponujamo tudi
# statične datoteke (slike, CSS stili, …)
@bottle.get('/static/<ime_dat:path>/')
def server_static(ime_dat):
    return bottle.static_file(ime_dat, root='img')

@bottle.get('/test/')
def test():
    return bottle.template('test.tpl')

bottle.run(debug=True, reloader=True)
