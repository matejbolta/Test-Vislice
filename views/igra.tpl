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
    <td>
      <form action="/igra/" method="post">
        <button type="submit", name='crka', value='Q'>Q</button>
      </form>
    </td>
    <td>
      <form action="/igra/" method="post">
        <button type="submit", name='crka', value='W'>W</button>
      </form>
    </td>
    <td>
      <form action="/igra/" method="post">
        <button type="submit", name='crka', value='E'>E</button>
      </form>
    </td>
    <td>
      <form action="/igra/" method="post">
        <button type="submit", name='crka', value='R'>R</button>
      </form>
    </td>
    <td>
      <form action="/igra/" method="post">
        <button type="submit", name='crka', value='T'>T</button>
      </form>
    </td>
    <td>
      <form action="/igra/" method="post">
        <button type="submit", name='crka', value='Z'>Z</button>
      </form>
    </td>
    <td>
      <form action="/igra/" method="post">
        <button type="submit", name='crka', value='U'>U</button>
      </form>
    </td>
    <td>
      <form action="/igra/" method="post">
        <button type="submit", name='crka', value='I'>I</button>
      </form>
    </td>
    <td>
      <form action="/igra/" method="post">
        <button type="submit", name='crka', value='O'>O</button>
      </form>
    </td>
    <td>
      <form action="/igra/" method="post">
        <button type="submit", name='crka', value='P'>P</button>
      </form>
    </td>
    <td>
      <form action="/igra/" method="post">
        <button type="submit", name='crka', value='Š'>Š</button>
      </form>
    </td>
    <td>
      <form action="/igra/" method="post">
        <button type="submit", name='crka', value='Đ'>Đ</button>
      </form>
    </td>
  </tr>

  <tr>
    <td>
      <form action="/igra/" method="post">
        <button type="submit", name='crka', value='A'>A</button>
      </form>
    </td>
    <td>
      <form action="/igra/" method="post">
        <button type="submit", name='crka', value='S'>S</button>
      </form>
    </td>
    <td>
      <form action="/igra/" method="post">
        <button type="submit", name='crka', value='D'>D</button>
      </form>
    </td>
    <td>
      <form action="/igra/" method="post">
        <button type="submit", name='crka', value='F'>F</button>
      </form>
    </td>
    <td>
      <form action="/igra/" method="post">
        <button type="submit", name='crka', value='G'>G</button>
      </form>
    </td>
    <td>
      <form action="/igra/" method="post">
        <button type="submit", name='crka', value='H'>H</button>
      </form>
    </td>
    <td>
      <form action="/igra/" method="post">
        <button type="submit", name='crka', value='J'>J</button>
      </form>
    </td>
    <td>
      <form action="/igra/" method="post">
        <button type="submit", name='crka', value='K'>K</button>
      </form>
    </td>
    <td>
      <form action="/igra/" method="post">
        <button type="submit", name='crka', value='L'>L</button>
      </form>
    </td>
    <td>
      <form action="/igra/" method="post">
        <button type="submit", name='crka', value='Č'>Č</button>
      </form>
    </td>
    <td>
      <form action="/igra/" method="post">
        <button type="submit", name='crka', value='Ć'>Ć</button>
      </form>
    </td>
    <td>
      <form action="/igra/" method="post">
        <button type="submit", name='crka', value='Ž'>Ž</button>
      </form>
    </td>
  </tr>

  <tr>
    <td>
      <form action="/igra/" method="post">
        <button type="submit", name='crka', value='Y'>Y</button>
      </form>
    </td>
    <td>
      <form action="/igra/" method="post">
        <button type="submit", name='crka', value='X'>X</button>
      </form>
    </td>
    <td>
      <form action="/igra/" method="post">
        <button type="submit", name='crka', value='C'>C</button>
      </form>
    </td>
    <td>
      <form action="/igra/" method="post">
        <button type="submit", name='crka', value='V'>V</button>
      </form>
    </td>
    <td>
      <form action="/igra/" method="post">
        <button type="submit", name='crka', value='B'>B</button>
      </form>
    </td>
    <td>
      <form action="/igra/" method="post">
        <button type="submit", name='crka', value='N'>N</button>
      </form>
    </td>
    <td>
      <form action="/igra/" method="post">
        <button type="submit", name='crka', value='M'>M</button>
      </form>
    </td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  
</table>

% end
