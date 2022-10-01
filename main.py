from  circular_queque import CircularQueue


def main():
    # Test CircularQueue 
    q = CircularQueue()
    q.enqueue(123)
    q.enqueue(12)
    q.enqueue(1)
    print(q)
    print(q.size())

    print(q.dequeue())
    print(q._rear)

if __name__ == "__main__":
    main()
