# Симулации за колективен имунитет Covid-19
*Дипломска работа*
- **Ментор**: д-р Ласко Баснарков
- **Студенти** Кирил Зеленковски 
- **Тема:** Во овој предлог проект не интересира како при природно стекнат имунитет на стадо е распределен имунитетот по единки во однос на нивната повзраност. Се гледа следното на СИР модел, како едноставен и делумно соодветен на болеста:
  1. Мрежа со дадена распределба на број на соседи (degree distribution). Се решаваат равенките на еволуција на веројатност на заразен кога јазлите се групирани по број на соседи (degree based mean field DBMF). Овие равенки може да се земат од ревијалниот труд, од страна 22 . За разни параметри на заразност (ламбда) кога има епидемија, се гледа распределбата на веројатноста на заразен, или оздравен, на крајот од епидемијата, во функција од бројот на соседи. После тоа се гледа колкав процент има имунитет. Треба да се спореди за истото ламбда, кај компартментен модел, колкав процент ќе има имунитет на крајот од епидемијата. Ова може да се види за разни распределби на број на соседи како што се степенска (Барабаши-Алберт БА), или експоненцијална (Ердош-Рењи ЕР). Најарно е ако има некаде на интернет каква е распределбата во реалноста
   2. Истото од горе може да се проба на мрежи со 10 000 јазли и да се решава СИР со еден зараен јазол на почетокот. Ќе се повторат симулациите. Мрежите би биле БА, ЕР и за нив се наоѓа распределбата по број на соседи и распределбата на веројатност на зараза. Ова може да се спореди со претходното (средно поле DBMF ако е изводливо) и со компарментен модел.
- **Клучни Зборови**: Python, Plotly, Covid-19, degree based mean field DBMF, Scale-free networks, Herd immunity

<hr>
<p align="center">
<img src="https://raw.githubusercontent.com/zelenelez/images/master/finki.jpg" width=50%;></img> <br>
Есен, 2021
</p>
