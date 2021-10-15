#Singly linked list
'''
-- it is a collection of nodes
-- node : python object that stores (data reference + address of next node)
-- going through nodes and connections, is called traversing the linked list
-- we can only traverse through each node in forward direction only.
== linked lists dont have a predetermined fixed size. it uses space proportional to its current number of elements
-- each node is unique
-- 1st node = head, last node = tail
-- tail does not refer to address of any node, rather points at null
-- method of adding element at head:
    1. create new node and refer it to some data
    2. set its next link to the current head
    3. set list's head to point to the new node
-- insert element at tail:
    1. create new node and refer it to some data
    2. assign its next link as none
    3. update tail's next link as this new node and set list's tail to point to the new node
-- removing element from head:
    1. set list's head to point to the next node
    2. deleting the node
-- removing element from tail:
    1. not easy and requires doubly linked list
-- pros of linked list: 
    1. constant time for insertion and deletion at any position
    2. it continues to expand and doesnt require any predetermined size
-- cons of linked list:
    1. to access any item of linked list, it takes O(n) time for item at index "n" {array have constant time for accessing every item}
'''
#implementation
class Node(object):
    def __init__(self,value) -> None:
        self.value = value
        self.nextnode = None
a=Node(1)
b=Node(2)
c=Node(3)
a.nextnode=b
b.nextnode=c

#Doubly linked list:
'''
-- here each node has a reference of a node before and after it, as well as some data reference
-- traversal in front as well as backward direction possible
-- we add special nodes at both ends of list. These nodes are called sentinals. {sentinals are not part of the actual linked list, we manually added them there for our convinience}
    1. header node : placed before the first node
    2. trailer node : placed after the last node
-- inserting element:
    1. create a new node
    2. link the node's "forward" and "backward" connections to the nodes after and before it respectively.
-- deleting element:
    1. link the nodes before and after the "deleted node"
'''
#implementation
class DoublyLinkedListNode(object):
    def __init__(self,value) -> None:
        self.value = value
        self.nextnode = None
        self.prevnode = None
a = DoublyLinkedListNode(1)
b = DoublyLinkedListNode(2)
c = DoublyLinkedListNode(3)
a.nextnode = b
b.prevnode = a
b.nextnode = c
c.prevnode = b
