"""Test the methods of Queue class."""

import pytest
from queue_collection import Deque

@pytest.fixture(scope="module")
def deque():
    return Deque()


def test_add_data_to_deque(generate_data, deque):
    # Arrange
    data = generate_data
    n = len(data)
    # Make sure Deque is empty
    assert deque.is_empty()
    # Act
    # addRear
    for r in data[:5]:
        deque.addRear(r)
    # addFront
    for f in data[5:]:
        deque.addFront(f)
    # Assert
    assert deque.get_front() == data[n - 1]
    assert deque.get_rear() == data[4]
    assert deque.size() == n
    assert str(deque) == str(data[5:] + data[:5]) 



def test_pop_data_from_deque(deque):
    # Arrange
    current_rear = deque.get_rear()
    current_front = deque.get_front()
    current_size = deque.size()
    # Assert
    assert current_rear == deque.popRear()
    assert current_front == deque.popFront()
    assert deque.size() == current_size - 2
    deque.clear()
    assert deque.is_empty()
