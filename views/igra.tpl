% import model
% rebase('base.tpl')

<blockquote>
  Vislice, ikonična ter vsem dobro znana igra.
</blockquote>

<table>
  <tr>
    <td>
      <h4>{{ igra.pravilni_del_gesla() }}</h4>
    </td>
  </tr>
  
  <tr>
    <td>
      Nepravilni ugibi: {{ igra.nepravilni_ugibi() }}
    </td>
  </tr>
</table>


% if poskus == model.ZMAGA:
<h1> !BRAVO, USPELO TI JE! </h1>
<form action="/nova_igra/" method="post">
  <button type="submit">Grem še eno igro!</button>
</form>

% elif poskus == model.PORAZ:
<h1> !!YOU LOST!! </h1>
<h3> Pravilno geslo je bilo: {{ igra.geslo }} </h3>
<form action="/nova_igra/" method="post">
  <button type="submit">Grem še eno igro!</button>
</form>

<!-- (Vnosno polje za črko)
procent else:
<form action="/igra/" method="post">
  Ugibaj črko: <input type="text", name="crka", autofocus>
  <button type="submit">Ugibaj</button>
</form>

procent end
-->

<!-- Tipkovnica -->
% else:
<table>
  % for vrsta in ['QWERTZUIOPŠĐ', 'ASDFGHJKLČĆŽ', 'YXCVBNM_____']:
  <tr>
    % for znak in vrsta:
    %   if znak == '_':
    <td></td>
    %   else:
    <td>
      <form action="/igra/" method="post">
        <button type="submit", name='crka', value='{{znak}}'>{{znak}}</button>
      </form>
    </td>
    %   end
    % end
  </tr>
  % end
</table>
% end

<!-- Slika -->
% if igra.stevilo_napak() != 0:
<img src="../img/{{igra.stevilo_napak()}}.jpg" alt="picture">
% end
