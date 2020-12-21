"""
Moduł pythona służący do interakcji z https://www.kalendarzswiat.pl/imieniny umożliwiający:

* wygenerowanie listy imion obchodzących imieniny w dniu dzisiejszym
* wygenerowanie dat imienin dla wprowadzonego imienia męskiego/żeńskiego


"""

import doctest
from datetime import datetime
import locale
import json
import re
import requests
from bs4 import BeautifulSoup as BS4

locale.setlocale(locale.LC_ALL, "pl")


class NameDay:
    """
    >>> instance = NameDay()
    >>> instance('Aleksandra')
    ['mar 20', 'kwi 21', 'maj 18', 'paź 02']
    >>> instance('Cezary')[0:6]
    ['lut 25', 'kwi 08', 'kwi 15', 'kwi 20', 'lip 27', 'sie 22']
    >>> instance('John')
    'Podane imię nie istnieje w bazie.'
    >>> isinstance(instance(), list)
    True
    >>> isinstance(instance()[0], str)
    True
    """

    URL = "https://www.kalendarzswiat.pl/imieniny"
    SOURCE = requests.get(URL, verify=False).text
    NAMES = json.loads(re.findall(r"names=(.*)?;", SOURCE)[0])

    def __call__(self, name=None):
        if not name:
            result = BS4(self.SOURCE, "html.parser").findAll("p")[3].find("b")
            return result.text.strip().split(", ")
        if name.title() not in self.NAMES:
            return "Podane imię nie istnieje w bazie."
        result = requests.post(self.URL, dict(name=name.title()), verify=False).text
        try:
            result = (
                BS4(result, "html.parser")
                .find("div", {"class": "panel-body"})
                .find("ul")
                .findAll("li")
            )
        except AttributeError:
            return "Wystąpiły problemy po stronie serwera. Proszę spróbować później."
        final_result = []
        for item in result:
            days = re.findall(r"\d+", item.text)
            month = re.findall(r"[a-zA-Z\ź]+", item.text)[0]
            for day in days:
                final_result.append(
                    datetime.strptime(
                        "1996-{}-{}".format(month[0:3], day), "%Y-%b-%d"
                    ).strftime("%b %d")
                )
        return final_result


if __name__ == "__main__":
    doctest.testmod()
