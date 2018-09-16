'''
單向鏈表

'''


class Node(object):
    def __init__(self, element):
        self.element = element
        self.next = None


class SingleLinkedList(object):
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        self.__head == None

    def length(self):
        cur = self.__head
        count = 0
        while cur.next != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.element)
            cur = cur.next

    def add(self, item):
        # add at head
        node = Node(item)
        node.next = self.__head  # change the new node first
        self.__head = node

    def append(self, item):
        # add at end
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        '''
        pos: start witd 0
        '''
        if pos < 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        node = Node(item)
        pre = self.__head
        count = 0
        while count < (pos-1):
            count += 1
            pre = pre.next
        node.next = pre.next
        pre.next = node

    def remove(self, item):
        pass

    def search(self, item):
        cur = self.__head
        while cur != None:
            if cur.element == item:
                return True
            else:
                cur = cur.next
        return False

    def travel(self):
        pass


def main():
    node = Node(100)
    sll = SingleLinkedList(node)
    print(sll.is_empty)
    sll.append(1)
    sll.add(10)
    sll.append(2)
    sll.insert(2, 9)
    print(sll.length())


if __name__ == '__main__':
    main()
