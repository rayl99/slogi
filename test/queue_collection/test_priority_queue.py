"""Test the methods of Priority Queue class."""

import pytest
from queue_collection import PriorityQueue

@pytest.fixture(scope="module")
def priority_queue():
    return PriorityQueue(priority="MIN")


def test_enqueue(generate_data, priority_queue):
    # Arrange
    data, n = generate_data, len(generate_data)
    # Make sure Queue is empty
    assert priority_queue.is_empty()
    # Act
    for v in data:
        priority_queue.enqueue(v)
    # Assert
    assert priority_queue.get_front() == min(data)
    assert priority_queue.size() == n


def test_dequeue(generate_data, priority_queue):
    # Arrange
    data, n = generate_data, len(generate_data)
    values = []
    #Act
    for i in range(n):
        values.append(priority_queue.dequeue())
    # Assert
    assert values == sorted(data)
    assert priority_queue.size() == 0
