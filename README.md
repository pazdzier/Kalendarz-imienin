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
>>> instance() # zwrócenie listy osób, które obchodzą imienieny dziś
>>> instance('imię') # zwrócenie dat imien dla podanego string
```
