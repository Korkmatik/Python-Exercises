class Queue:
    def __init__(self):
        self.__queue = []

    
    def empty(self):
        return self.__queue == []

    def enqueue(self, item):
        self.__queue += [item]

    def dequeue(self):
        if not self.empty():
            item = self.__queue[0]
            del self.__queue[0]
            return item

    def front(self):
        if not self.empty():
            return self.__queue[0]