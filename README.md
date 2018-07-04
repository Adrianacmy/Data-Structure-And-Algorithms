# Data structure and algorithms in Python

Abstract data types are the specifications and data structures are the concrete implementtations

| abstract data types  | data structures   |
|---|---|
|  stack | array, linked list   |
|  queue | arry, linked list   | 
|  priority queue | heap   | 
|  dictionary / hashmap | array



## Arrays: data structures

- Advantages:
  - Random access, will return  the value with the given key very fast, O(1)
  - Easy to implement and to use
  - Fast to add items to the end and take items with given indexs

- Disadvantages:
  - It is not dynamic data structure
  - It is O(n) operation to add more when it is full
  - It can not store items with different types

- Operatons:
  - add:
    - It is fast to add values at the end while it is not full
    - It is O(n) to insert values at the beginning and middle of an array with given index
  - remove:
    - Remove the last: o(1)
    - Remove an item at given index other than the last: O(n), because the rest items have to shift

## Linked list

- Linked lists are composed of nodes and references/pointers pointing from one node to thh other
- The last reference is pointing to a NULL

- Advantages:
  - Dynamic data structures
  - It allocate the needed memory in run-time
  - It is efficient if we want to manipunate the first elements
  - It is easy to iimplementation
  - It can store items with different size

- Disadvantages:
  - Waste memory because of the references
  - Nodes in a linked list must be read in order from the beginning as linked lists have sequential access(array items can be reached via indexes in O(1) time
  - It is extremely difficult to navigate backwards
  - Solution: doubly linked lists, which is easier to read, but memory is wasted in allocating space for a back pointer

```python
  class Node {
    data
    node nextNode
  }

```

- Operations:
  - insertion at the beginning is O(1)
  - insertion at the end is O(n), (loop through and check if which item is pointing to NULL)
  - remove at the beginning is O(1)
  - remove at the given positio: O(n), update the reference

## ArrayList vs LinkedList

|   | LinkedList | Arrays 
|---|---|---|
| Search | O(n) | O(1)
| Insert at the start | O(1) | o(n)
| Insert at the end | O(n) | o(1)
| Waste space | O(n) | 0
