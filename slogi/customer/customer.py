from abc import ABC, abstractmethod
from email.policy import default
from slogi.utils_class import Location
from slogi.constant import Grade

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
    def name(self, value: str):
        self._name = value
    
    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, value: Location):
        self._address = value

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value: str):
        self._email = value

    @property
    def phone_number(self):
        return self._email
    
    @phone_number.setter
    def phone_number(self, value: str):
        self._email = value

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
    def point(self, value: int):
        if value < 0:
            raise Exception("Value can not less than zero.")
        self.__point = value

    @property
    def grade(self):
        return self.__grade
    
    @grade.setter
    def grade(self, value: str):
        self.__grade = Grade.dict.get(value.upper(), Grade.POTENTIAL)

    def shipment(self):
        # TODO
        pass
    
    def track(self):
        # TODO
        pass
    