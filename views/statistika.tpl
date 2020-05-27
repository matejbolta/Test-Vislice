% import model
% rebase('base.tpl')

<blockquote>
  Vislice, ikonična ter vsem dobro znana igra.
</blockquote>

<h3>
  Statistika
</h3>

<table>
    <tr>
        <td>
            Število dosedanjih iger:
        </td>
        <td>
            {{slovar_statistik['stevilo_iger']}}
        </td>
    </tr>
    <tr>
        <td>
            Število nedokončanih iger:
        </td>
        <td>
            {{slovar_statistik['odstotek_nedokoncanih_iger']}}
        </td>
    </tr>
    <tr>
        <td>
            Odstotek zmag:
        </td>
        <td>
            {{slovar_statistik['odstotek_zmag']}}
        </td>
    </tr>
    <tr>
        <td>
            Odstotek porazov:
        </td>
        <td>
            {{slovar_statistik['odstotek_porazov']}}
        </td>
    </tr>
    <tr>
        <td>
            Najdaljše uganjeno geslo:
        </td>
        <td>
            {{slovar_statistik['najdaljse_uganjeno_geslo']}}
        </td>
    </tr>
    <tr>
        <td>
            Povprečen odstotek uganjenih črk:
        </td>
        <td>
            {{slovar_statistik['povprecen_odstotek_uganjenih_crk']}}
        </td>
    </tr>
</table>

<form action="/" method="get">
    <button type="submit">Domov</button>
</form>
