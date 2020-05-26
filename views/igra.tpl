% import model
% rebase('base.tpl')

<blockquote>
  Vislice, ikonična ter vsem dobro znana igra.
</blockquote>

<table>
  <tr>
    <td>
      <h2>{{ igra.pravilni_del_gesla() }}</h2>
    </td>
  </tr>
  
  <tr>
    <td>
      Nepravilni ugibi: {{ igra.nepravilni_ugibi() }}
    </td>
  </tr>
  
  % if igra.stevilo_napak() != 0:
  <tr>
    <td>
      <img src="../../img/{{igra.stevilo_napak()}}.jpg" alt="picture">
    </td>
  </tr>
  % end
  
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

<!--
procent else:
<form action="/igra/" method="post">
  Ugibaj črko: <input type="text", name="crka", autofocus>
  <button type="submit">Ugibaj</button>
</form>

procent end
-->

% else:

<table>
  <tr>
    % for i in 'QWERTZUIOPŠĐ':
    <td>
      <form action="/igra/" method="post">
        <button type="submit", name='crka', value='{{i}}'>{{i}}</button>
      </form>
    </td>
    % end
  </tr>

  <tr>
    % for i in 'ASDFGHJKLČĆŽ':
    <td>
      <form action="/igra/" method="post">
        <button type="submit", name='crka', value='{{i}}'>{{i}}</button>
      </form>
    </td>
    % end
  </tr>

  <tr>
    % for i in 'YXCVBNM':
    <td>
      <form action="/igra/" method="post">
        <button type="submit", name='crka', value='{{i}}'>{{i}}</button>
      </form>
    </td>
    % end

    % for _ in range(5):
    <td></td>
    % end
  </tr>
</table>

% end
