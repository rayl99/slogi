

from typing import Optional


class Location:
    def __init__(self, street: str, ward: str, district: str, city: str, zipcode: int, detail: Optional[str]="") -> None:
        self.__street = street
        self.__ward = ward
        self.__district = district
        self.__city = city
        self.__zipcode = zipcode
        self.__detail = detail

    @property
    def street(self):
        return self.__street

    @property
    def ward(self):
        return self.__ward

    @property
    def district(self):
        return self.__district

    @property
    def city(self):
        return self.__city

    @property
    def zipcode(self):
        return self.__zipcode

    @property
    def detail(self):
        return self.__detail if self.__detail else self.__str__()

    def __str__(self) -> str:
        return ','.join(list(self.__dict__.values()))