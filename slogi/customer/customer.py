from abc import ABC, abstractmethod
from slogi.constants import Grade
from slogi.exceptions.errors import AttributeError
from slogi.utils_class import Location

class Customer(ABC):
    def __init__(self, id: str, name: str, address: Location, email: str, phone_number: str) -> None:
        self._id = id
        self._name = name
        self._address = address
        self._email = email
        self._phone_number = phone_number
    
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, data: str):
        self._name = data
    
    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, data: Location):
        self._address = data

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, data: str):
        self._email = data

    @property
    def phone_number(self):
        return self._email
    
    @phone_number.setter
    def phone_number(self, data: str):
        self._email = data

    @abstractmethod
    def shipment(self):
        pass
    
    @abstractmethod
    def track(self):
        pass


class Guest(Customer):
    def __init__(self, id: str, name: str, address: Location, email: str, phone_number: str) -> None:
        super().__init__(id, name, address, email, phone_number)
    
    def shipment(self):
        # TODO
        pass
    
    def track(self):
        # TODO
        pass


class Member(Customer):
    def __init__(self, id: str, name: str, address: Location, email: str, phone_number: str, point: int = 0, grade: str = Grade.POTENTIAL) -> None:
        super().__init__(id, name, address, email, phone_number)
        self.__point = point
        self.__grade = grade
    
    @property
    def point(self):
        return self.__point
    
    @point.setter
    def point(self, data: int):
        if data < 0:
            raise AttributeError("The data can not less than zero.", {'name':'point', 'data':data})
        self.__point = data

    @property
    def grade(self):
        return self.__grade
    
    @grade.setter
    def grade(self, data: str):
        if data.upper() not in Grade.dict:
            raise AttributeError("The data invalid.", {'name':'grade', 'data': data})
        self.__grade = Grade.dict[data.upper()]

    def shipment(self):
        # TODO
        pass
    
    def track(self):
        # TODO
        pass
    