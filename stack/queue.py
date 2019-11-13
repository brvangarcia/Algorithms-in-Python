class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def endQueue(self,data):
        self.queue.append(data)

    def deQueue(self):
        data = self.queue[0]
        del self.queue[0]
        return data
    
    def peek(self):
        return self.queue[0]

    def sizeQueue(self):
        return len(self.queue)

queue = Queue()
queue.endQueue(10)
queue.endQueue(20)
queue.endQueue(30)
print(queue.sizeQueue())
print(queue.deQueue())
print(queue.deQueue())
print(queue.sizeQueue())