# -*- coding: utf-8 -*-


"""
Contains a domain layer related code.


FEATURES:
---------
- Zobraz pořady pro danou stanici a daný den.  
- Zobraz pořady pro danou stanici a daný den z vybrané kategorie (zprávy a proud).


FACTS:
------

## Pořad (*Show*) entita (hodnota?)

- Pořady dělíme na dva druh buď *zprávy* nebo *proud*.
- Pořady dělímě z proudu dále dělíme do kategorií: publicistika, magazín a další, které OSR definuje. 
- Pořad má uvedené tyto atributy:
   - station_id: (StationID==string)
   - id (String)
   - name (String, required)
   - since (Timestamp, required)
   - till  (Timestamp, required)
   - duration (computed from since and till)
   - kind (Enumeration = Proud | Zprávy)
   - category (Enumeration = Publicistika | Magazín | Rozhlasová hra | ... )
   - expected_number_of_speakers
   - speakers (array of Person)
   
## Osoba (*Person*) entita
- id
- given_name
- family_name
- category = Enumeration Moderator | Respondent
- Osoba řadímě do jedné z kategorií: Respondent | Moderátor

## Station
id: StationID
"""


class Person(object):
    def __init__(self, given_name: str, family_name: str) -> None:
        self._given_name = given_name
        self._family_name = family_name

    @property  # getter /setter
    def given_name(self) -> str:
        return self._given_name

    @given_name.setter
    def given_name(self, value: str) -> None:
        assert len(given_name) > 0
        self._given_name = str(value)

    @property
    def family_name(self) -> str:
        return self._family_name

    @property
    def full_name(self) -> str:
        return self.given_name + " " + self.family_name

    # Other methods (behaviour) here.

    # def __str__(self) -> str:
    #     return f"{self.__class__.__name__}(name={self.name})"


class Station:
    """
    Toto je entita představující stanici.

    >>> from general.domain import Station
    >>> plus = Station(1, "Plus")
    >>> plus.id
    1
    >>> plus.name
    >>> 'Plus'
    """

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def __eq__(self, that: object) -> bool:
        return isinstance(that, type(self)) and self.id == that.id

    # def __hash__(self) -> int:
    #     return hash((type(self), self.id)))


class Show:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def __eq__(self, that: object) -> bool:
        return isinstance(that, type(self)) and self.id == that.id

    # def __hash__(self) -> int:
    #     return hash((type(self), self.id)))
