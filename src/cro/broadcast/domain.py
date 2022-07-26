# -*- coding: utf-8 -*-


"""
Contains a domain layer related code: domain models and services.
"""


class Person:
    """
    Represents a person such as moderator or respondent.
    """

    def __init__(self, unique_id: str, given_name: str, family_name: str) -> None:
        """
        FIXME: [Write a sensible documentation comment.]
        """
        self._unique_id = unique_id
        self._given_name = given_name
        self._family_name = family_name

    @property  # getter /setter
    def given_name(self) -> str:
        """
        FIXME: [Write a sensible documentation comment.]
        """
        return self._given_name

    @given_name.setter
    def given_name(self, value: str) -> None:
        """
        FIXME: [Write a sensible documentation comment.]
        """
        assert len(given_name) > 0
        self._given_name = str(value)

    @property
    def family_name(self) -> str:
        """
        FIXME: [Write a sensible documentation comment.]
        """
        return self._family_name

    @property
    def full_name(self) -> str:
        """
        FIXME: [Write a sensible documentation comment.]
        """
        return self.given_name + " " + self.family_name

    # Other methods (behaviour) here.

    # def __str__(self) -> str: ...


class Station:
    """
    Represents Czech Radio station.

    >>> from general.domain import Station
    >>> plus = Station(1, "Plus")
    >>> plus.id
    1
    >>> plus.name
    >>> 'Plus'
    """

    def __init__(self, unique_id: int, name: str):
        """
        FIXME: [Write a sensible documentation comment.]
        """
        self.unique_id = unique_id  # FIXME: [Define getter property.]
        self.name = name  # FIXME: [Define getter property.]

    # def __eq__(self, that: object) -> bool: ...

    # def __hash__(self) -> int: ...


class Show:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def __eq__(self, that: object) -> bool:
        return isinstance(that, type(self)) and self.id == that.id

    # def __hash__(self) -> int:
    #     return hash((type(self), self.id)))
