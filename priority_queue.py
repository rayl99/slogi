'''Design simple Priority Queue.'''
from queque import Queue
from operator import lt, gt

class PriorityQueue(Queue):
    def __init__(self, priority="MAX") -> None:
        super().__init__()
        self.__priority = priority
    
    def heapify(self, i:int, compare):
        highest_priority = i
        l = 2*i + 1
        r = 2*i + 2
        if l < self.size() and compare(self._queue[l], self._queue[highest_priority]):
            highest_priority = l
        if r < self.size() and compare(self._queue[r],  self._queue[highest_priority]):
            highest_priority = r
        
        if highest_priority != i:
            self._queue[i], self._queue[highest_priority] = self._queue[highest_priority], self._queue[i]
            self.heapify(highest_priority, compare)


    def enqueue(self, data: any):
        super().enqueue(data)
        if self.size() > 1:
            self.reconstruct_heap()
    
    def dequeue(self) -> any:
        data = super().dequeue()
        self.reconstruct_heap()
        return data
       
    
    def reconstruct_heap(self):
        compare = gt if self.__priority == "MAX" else lt
        for i in range(self.size()//2 - 1, -1, -1):
            self.heapify(i, compare)
