import pytest
from random import random


@pytest.fixture(scope="module")
def generate_data():
    return [random for i in range(10)]