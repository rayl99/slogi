

from typing import Optional


class Location:
    def __init__(self, street: str, ward: str, district: str, city: str, zipcode: int, detail: Optional[str]="") -> None:
        self.street = street
        self.ward = ward
        self.district = district
        self.city = city
        self.zipcode = zipcode
        self.detail = detail

    def get_street(self):
        return self.street
    
    def get_ward(self):
        return self.ward

    def get_district(self):
        return self.ward

    def get_city(self):
        return self.city

    def get_zipcode(self):
        return self.zipcode

    def get_detail(self):
        return self.detail if self.detail else self.__str__()

    def __str__(self) -> str:
        return ','.join(list(self.__dict__.values()))