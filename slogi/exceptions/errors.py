

class BaseError(Exception):
    def __init__(self, msg: str, details: dict={} ,*args: object) -> None:
        super().__init__(*args)
        self._msg = msg
        self._details = details

    def __str__(self):
        return self._msg
    
    @property
    def details(self):
        return self._details


class AttributeError(BaseError):
    def __init__(self, msg: str, details: dict = {}, *args: object) -> None:
        super().__init__(msg, details, *args)
        self._msg = f"{self._msg} >>?<< {self.details.get('name','Undefined attribute')} = {self.details.get('data', '')}"
