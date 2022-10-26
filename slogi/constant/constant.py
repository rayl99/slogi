

class Grade:
    POTENTIAL = "Potential"
    BRONZE = "Bronze"
    SILVER = "Silver"
    GOLD = "Gold"
    PLATINUM = "Platinum"

    @classmethod
    @property
    def dict(cls):
        return dict({k:v for k, v in cls.__dict__.items() if k.isupper()})