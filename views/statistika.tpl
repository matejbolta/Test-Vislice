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
            {{slovar_statistik.get('stevilo_iger', 'N/A')}}
        </td>
    </tr>
    <tr>
        <td>
            Število nedokončanih iger:
        </td>
        <td>
            {{slovar_statistik.get('odstotek_nedokoncanih_iger', 'N/A')}}
        </td>
    </tr>
    <tr>
        <td>
            Odstotek zmag:
        </td>
        <td>
            {{slovar_statistik.get('odstotek_zmag', 'N/A')}}
        </td>
    </tr>
    <tr>
        <td>
            Odstotek porazov:
        </td>
        <td>
            {{slovar_statistik.get('odstotek_porazov', 'N/A')}}
        </td>
    </tr>
    <tr>
        <td>
            Najdaljše uganjeno geslo:
        </td>
        <td>
            {{slovar_statistik.get('najdaljse_uganjeno_geslo', 'N/A')}}
        </td>
    </tr>
    <tr>
        <td>
            Povprečen odstotek uganjenih črk:
        </td>
        <td>
            {{slovar_statistik.get('povprecen_odstotek_uganjenih_crk', 'N/A')}}
        </td>
    </tr>
</table>

<form action="/" method="get">
    <button type="submit">Domov</button>
</form>
