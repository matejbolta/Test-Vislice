import bottle, model

# Potrebno le, če je v urejevalniku odprta višji path.
#import os
#os.chdir('UvP/Vislice')

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

    return bottle.template('igra.tpl', igra=igra, poskus=poskus)









bottle.run(debug=True, reloader=True)
