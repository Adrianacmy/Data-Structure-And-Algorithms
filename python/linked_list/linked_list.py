# Linked_list,  Python implementation 

class Node(object):
  def __init__(self, data):
    self.data = data
    self.nextNode = None


class LinkedList(object):

  def __init__(self):
    self.head = None
    self.size = 0

  #O(1)
  def insert_at_Start(self, data):
    self.size = self.size + 1
    newNode = Node(data) # create a new node

    if not self.head: # if this is the first node
      self.head = newNode
    else:
      newNode.nextNode = self.head
      self.head = newNode

  # O(1)
  def size(self):
    return self.size

  #O(n)
  def insert_at_end(self, data):
    self.size += 1
    newNode = Node(data)
    currentNode = self.head

    while currentNode.nextNode is not None:
      currentNode = currentNode.nextnode

    currentNode.nextNode = newNode
  
  # O(n)
  def remove(self, data):
    if self.head is None:
      return
    
    self.size -= 1
    currentNode = self.head
    previousNode = None

    while currentNode.data != data:
      previousNode = currentNode
      currentNode = currentNode.nextNode

    if previousNode is None:
      self.head = currentNode.nextNode
    else:
      previousNode.nextNode = currentNode.nextNode

  def traverse_list(self):
    currentNode = self.head

    while currentNode is not None:
      print(currentNode.data)
      currentNode = currentNode.nextNode

    