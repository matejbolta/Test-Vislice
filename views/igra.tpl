% import model
% rebase('base.tpl')

<blockquote>
  Vislice so najboljša igra za preganjanje dolgčasa (poleg tetrisa).
  <small>Študentje</small>
</blockquote>

<h2> {{ igra.pravilni_del_gesla() }} </h2>

<h2> Napačni ugibi: {{ igra.nepravilni_ugibi() }} </h2>


% if poskus == model.ZMAGA:
<h1> ZMAGAL SI </h1>
%elif poskus == model.PORAZ:
<h1> IZGUBIL SI </h1>
%else:
<form action="/igra/{{ id_igre }}/" method="post">
  Črka: <input type="text", name="crka">
  <button type="submit">Ugibaj novo črko</button>
</form>
% end



<img src="img/10.jpg" alt="obesanje">

<form action="/igra/" method="post">
  <button type="submit">Nova igra</button>
</form>