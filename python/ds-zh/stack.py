class Stack(object):

    def __init__(self):
        self._list = []

    def push(self, item):
        self.__list.append(item)

    def pop(self):
        self.__list.pop()

    def peek(self):
        # return element on stack top
        if self.__list:
            return self.__list
        else:
            return None

    def is_empty(self):
        # return self.__list == []
        return not self.__list

    def size(self):
        return len(self.__list)


def main():
    new_stack = Stack()
    new_stack.push(1)
    new_stack.push(2)
    new_stack.push(3)
    new_stack.pop()


if __name__ == '__main__':
    main()
