from tokenize import Pointfloat
from circular_queque import CircularQueue
from queque import Queue
from priority_queue import PriorityQueue

def main():
    # Test CircularQueue 
    q = PriorityQueue()
    q.enqueue(12)
    q.enqueue(123)
    q.enqueue(1)
    q.enqueue(4)
    q.enqueue(44)
    print(q)
    print(q.size())

    print(q.dequeue())
    print(q)
    print(q.dequeue())
    print(q.dequeue())
    print(q.get_front())

if __name__ == "__main__":
    main()
