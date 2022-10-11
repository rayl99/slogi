"""Test the methods of Queue class."""

import pytest
from queue_collection import Queue

@pytest.fixture(scope="module")
def queue():
    return Queue()


def test_enqueue(generate_data, queue):
    # Arrange
    data, n = generate_data, len(generate_data)
    # Make sure Queue is empty
    assert queue.is_empty()
    # Act
    for v in data:
        queue.enqueue(v)
    # Assert
    assert queue.get_front() == data[0]
    assert queue.get_rear() == data[n - 1]
    assert queue.size() == n
    assert str(queue) == str(data)    


def test_dequeue(generate_data, queue):
    # Arrange
    data, n = generate_data, len(generate_data)
    front = queue.get_front()
    #Act
    value = queue.dequeue()
    # Assert
    assert front == value
    assert queue.get_front() == data[1]
    assert queue.size() == n - 1
    assert str(queue) == str(data[1:])
    queue.clear()
    assert queue.is_empty()
