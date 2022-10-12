"""Test the methods of Circular Queue class."""

import pytest
from queue_collection import CircularQueue

@pytest.fixture(scope="module")
def circular_queue():
    return CircularQueue(capacity=100)


def test_enqueue(generate_data, circular_queue):
    # Arrange
    data, n = generate_data, len(generate_data)
    # Make sure Queue is empty
    assert circular_queue.is_empty()
    # Act
    for v in data:
        circular_queue.enqueue(v)
    # Assert
    assert circular_queue.get_front() == data[0]
    assert circular_queue.get_rear() == data[n - 1]
    assert circular_queue.size() == n
    assert str(circular_queue) == str(data)
    with pytest.raises(MemoryError) as e_info:
        circular_queue.enqueue(123)
        assert str(e_info) == "The queue is full."



def test_dequeue(generate_data, circular_queue):
    # Arrange
    data, n = generate_data, len(generate_data)
    front = circular_queue.get_front()
    new_data = [123,1234,12345]
    #Act
    dequeue_values = [circular_queue.dequeue() for i in range(10)]
    # Assert
    assert front == dequeue_values[0]
    assert circular_queue.get_front() == data[10]
    assert circular_queue.size() == n - 10
    [circular_queue.enqueue(v) for v in new_data]
    assert str(circular_queue) == str(new_data + [None]*(10-len(new_data)) + data[10:])
    circular_queue.clear()
    assert circular_queue.is_empty()