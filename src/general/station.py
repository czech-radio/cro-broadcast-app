
"""
Obsahuje doménový model stanice.
"""


class Station:
    """
    Toto je entita představující stanici.

    >>> from general.station import Station
    >>> plus = Station(1, "Plus")
    >>> plus.id
    1
    >>> plus.name
    >>> 'Plus'
    """

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name 

