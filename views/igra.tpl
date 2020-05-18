% import model
% rebase('base.tpl')

<blockquote>
  Vislice, ikonična ter vsem dobro znana igra.
</blockquote>

<h3>Trenutno stanje gesla: {{ igra.pravilni_del_gesla() }}</h3>

<h4>Napačni ugibi: {{ igra.nepravilni_ugibi() }}</h4>


% if poskus == model.ZMAGA:
<h1> ZMAGAL SI </h1>
<form action="/igra/" method="post">
  <button type="submit">Grem še eno igro!</button>
</form>
% elif poskus == model.PORAZ:
<h1> IZGUBIL SI </h1>
<form action="/igra/" method="post">
  <button type="submit">Grem še eno igro!</button>
</form>
% else:
<form action="/igra/{{ id_igre }}/" method="post">
  Ugibaj črko: <input type="text", name="crka">
  <button type="submit">Ugibaj</button>
</form>
% end



<img src="img/10.jpg" alt="obesanje">