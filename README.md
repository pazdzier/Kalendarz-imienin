# kalendarz_imienin

Wymagania
=========

* Python w wersji 3
* Połączenie internetowe


Instalacja
==========

```console
pip install requests
pip install beautifulsoup4
```

Uruchomienie
============

```python
>>> from nameday import NameDay
>>> instance = NameDay()
>>> instance() # zwrócenie listy osób, które obchodzą imienieny dziś (wynik z przykładu na dzień 21 grudnia)
['Anastazy', 'Balbin', 'Festus', 'Gliceriusz', 'Honorat', 'Kanizjusz', 'Piotr', 'Temistokles', 'Tolisław', 'Tomasz', 'Tomisław', 'Tomisława']
>>> instance('baltazar') # zwrócenie dat imien dla podanego string
['sty 06', 'cze 20', 'wrz 18']
```
