# -*- coding: utf-8 -*-


"""
Contains a domain layer related code.
"""


class Show:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def __eq__(self, that: object) -> bool:
        return isinstance(that, type(self)) and self.id == that.id

    def __hash__(self) -> int:
        return hash((type(self), self.id)))


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

    def __hash__(self) -> int:
        return hash((type(self), self.id)))
