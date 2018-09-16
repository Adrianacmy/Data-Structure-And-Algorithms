'''



'''


class DQueue(object):

    def __init__(self):
        self._list = []

    def add_front(self, item):
        self.__list.insert(0, item)

    def add_rear(self, item):
        self.__list.append(item)

    def pop_front(self):
        return self.__list.pop(0)
        # retrun self.pop()

    def pop_rear(self):
        return self.__list.pop(0)
        # retrun self.pop()

    def is_empty(self):
        # return self.__list == []
        return not self.__list

    def size(self):
        return len(self.__list)


def main():
    new_queue = DQueue()



if __name__ == '__main__':
    main()
