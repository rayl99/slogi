'''Design simple Deque.'''

from slib.queue_collection.queue import Queue


class Deque(Queue):
    def __init__(self) -> None:
        super().__init__()
    
    def addRear(self, data: any):
        super().enqueue(data)
    
    def addFront(self, data: any):
        self._queue.insert(0, data)
    
    def popRear(self):
        if self.is_empty():
            return None 
        return self._queue.pop()
    
    def popFront(self):
        return super().dequeue()
