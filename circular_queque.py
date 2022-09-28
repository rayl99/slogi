'''Design simple Circular Queue.'''
class CircularQueue():
    def __init__(self, capacity=10):
        self.__front = 0
        self.__rear = -1
        self.__capacity = capacity
        self.__queue = [None] * capacity

    def get_front(self):
        """Get data at front of the queue."""
        return self.__queue[self.__front % self.__capacity]

    def get_rear(self):
        """Get data at the end of the queue."""
        return self.__queue[self.__rear % self.__capacity]

    def enqueue(self, data: any):
        """Put new data at the end of the queue."""
        if self.size() == self.__capacity:
            raise MemoryError("The queue is full.")
        self.__rear += 1
        self.__queue[self.__rear % self.__capacity] = data

    def dequeue(self) -> any:
        """Get and remove data at the front of the queue."""
        if self.is_empty():
            return None
        data = self.__queue[self.__front % self.__capacity]
        self.__front = self.__front + 1
        # if self.__front > self.__capacity:
        #     self.__reduce_pointer()
        if self.__front > self.__rear:
            self.clear()
        return data

    def clear(self):
        """Resetting the queue become an empty queue."""
        self.__front = 0
        self.__rear = -1

    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return not self.size()

    def size(self) -> int:
        """Get size of the queue"""
        return (self.__rear - self.__front) + 1

    # def __reduce_poniter(self):
    #     self.__front = self.__front % self.__capacity
    #     self.__rear = self.__rear % self.__capacity
    
    def __str__(self) -> str:
        return str([self.__queue[(self.__front + i) % self.__capacity] for i in range(self.size())])
