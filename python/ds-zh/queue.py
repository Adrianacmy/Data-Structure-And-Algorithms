class Queue(object):

    def __init__(self):
        self._list = []

    def enqueue(self, item):
        self.__list.append(item)
        # self.__list.insert(0, item)

    def dequeue(self):
        return self.__list.pop(0)
        # retrun self.pop()

    def is_empty(self):
        # return self.__list == []
        return not self.__list

    def size(self):
        return len(self.__list)


def main():
    new_queue = Queue()
    new_queue.enqueue(1)
    new_queue.enqueue(2)
    new_queue.enqueue(3)
    new_queue.dequeue()


if __name__ == '__main__':
    main()
