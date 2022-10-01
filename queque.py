'''Design simple Queue.'''


class Queue():
    def __init__(self) -> None:
        self._queue = []
    
    def get_front(self):
        """Get data at front of the queue."""
        return self._queue[0]

    def get_rear(self):
        """Get data at the end of the queue."""
        return self._queue[self.size()-1]

    def enqueue(self, data: any):
        """Put new data at the end of the queue."""
        self._queue.append(data)

    def dequeue(self) -> any:
        """Get and remove data at the front of the queue."""
        if self.is_empty():
            return None
        return self._queue.pop()

    def clear(self):
        """Resetting the queue become an empty queue."""
        self._queue.clear()

    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return not self.size()

    def size(self) -> int:
        """Get size of the queue"""
        return len(self._queue)
    
    def __str__(self) -> str:
        return str(self._queue)
