class CircularQueue():
    def __init__(self, capacity=10):
        self.__front = 0
        self.__rear = -1
        self.__capacity = capacity
        self.__queue = [None] * capacity

    def get_front(self):
        return self.__queue[self.__front % self.__capacity]

    def get_rear(self):
        return self.__queue[self.__rear % self.__capacity]

    def enqueue(self, data: any):
        if self.size() == self.__capacity:
            raise MemoryError("The queue is full.")
        self.__rear += 1
        self.__queue[self.__rear % self.__capacity] = data

    def dequeue(self) -> any:
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
        self.__front = 0
        self.__rear = -1

    def is_empty(self) -> bool:
        return self.__rear == -1

    def size(self) -> int:
        return (self.__rear - self.__front) + 1

    # def __reduce_poniter(self):
    #     self.__front = self.__front % self.__capacity
    #     self.__rear = self.__rear % self.__capacity
    
    def __str__(self) -> str:
        return str([self.__queue[(self.__front + i) % self.__capacity] for i in range(self.size())])
