from  circular_queque import CircularQueue


def main():
    # Test CircularQueue 
    q = CircularQueue()
    q.enqueue(123)
    print(q)
    print(q.dequeue())
    print(q.size())

if __name__ == "__main__":
    main()
