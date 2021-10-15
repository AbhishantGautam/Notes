#stacks
'''
-- very similar to lists
-- ordered collection of items where addition of new item and removal of existing item always takes place at the same end
-- this end is called "top". and the other end is called "base"
-- items around the "base" have remained in stack longer than those near the top
-- most recently added item is also the first to be removed, aka LIFO (last in first out)
-- imagine this as pile of books
'''
#implementation
class stack(object):
    def __init__(self) -> None:
        self.items=[]
    def isEmpty(self): #returns true if stack empty
        return self.items==[]
    def push(self,item): #adds item to the end of stack(aka top)
        self.items.append(item)
    def pop(self): #removes item from end of stack(aka top)
        self.items.pop()
    def peek(self): #returns the item at the end of stack(ie at the top)
        return self.items[len(self.items)-1]
    def size(self): #returns the number of items in the stack
        return len(self.items)

#queue
'''
-- ordered collection of items where addition of item happens at one end("rear")
    and removal of item happens at the other end("front")
-- similar to how a queue works in sbi office.
-- oldest item is at the front
-- follow FIFO (first in first out)
-- methods:
    1. enqueue: add item
    2. dequeue: remove item
'''
# implementation
class Queue(object):
    def __init__(self) -> None:
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        self.items.pop()
    def size(self):
        return len(self.items)

# Dequeue
'''
-- we can add or remove items from any end
'''
# implementation
class Dequeue(object):
    def __init__(self) -> None:
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def add_front(self,item):
        self.items.append(item)
    def add_rear(self,item):
        self.items.insert(0,item)
    def removeFront(self):
        self.items.pop()
    def removeRear(self):
        self.items.pop(0)
    def size(self):
        return len(self.items)

#Priority Queue
'''
--Type of queue in which we remove item from front.
-- order of items is based on priority not their time of enqueue
-- higher priority items at the front of queue
-- this is implemented by a data structure called binary heap
-- binary heap : enqueue and dequeue happen in O(logn) time
-- binary heap of two types:
    1)Min heap : smallest key always at front
    2)Max heap : largest key always at front
'''
# Binary heap 
'''
-- Balanced binary tree : roughly the same number of nodes in left and right subtrees of the root.
-- We can create a balanced binary tree by creating a complete binary tree
-- complete binary tree: binary tree in which every level, except possibly the last level, is completely filled.
-- for a complete binary tree, to find children of node at position "i", children are located at position "2i" and "2i+1" for example see notes 
-- the parent of item at position "i" will be at position "i//2"
-- for simplicity we assign the 0th position of heaplist to "0" and the root item is stored at index = 1
'''
# implementation of binary heap(min heap : value of root is least)
class BinHeap:
    def __init__(self) -> None:
        self.heaplist = [0]
        self.currentsize = 0
    def percup(self,i): #if son's value is less than parent's value, this function interchanges them
        while i//2 > 0: #while parent in the heap
            if self.heaplist[i]<self.heaplist[i//2]: #if child's value less than parent value:
                self.heaplist[i],self.heaplist[i//2] = self.heaplist[i//2],self.heaplist[i] #interchange their values
            i = i//2 #now we move up a level, and repeat above
    def insert(self,k):
        self.heaplist.append(k)
        self.currentsize += 1
        self.percup(self.currentsize)
    def minchild(self,i):
        if i*2 + 1 > self.currentsize: #if right child doesnt exist
            return i*2 #left child is the only option
        else: #if both child exist
            if self.heaplist[i*2]<self.heaplist[(i*2)+1]: #check if left child is less than right child. if so:
                return i*2 #return the position of left child
            else:
                return (i*2)+1 #else, return the position of right child
    def percdown(self,i):
        while(i*2)<=self.currentsize: # while child exists:
            smaller_child = self.minchild(i) #finding the smaller of the two childs
            if self.heaplist[i]>self.heaplist[smaller_child]: #if the parent is greater than the smaller child:
                self.heaplist[i],self.heaplist[smaller_child] = self.heaplist[smaller_child],self.heaplist[i] #interchange their position
            i = smaller_child #now we move down a level and repeat the same
    def del_min(self):
        ret_val = self.heaplist[1] #storing the value of root value
        self.heaplist[1] = self.heaplist[self.currentsize] #setting the root value as the greatest number (number at the end of heap list)
        self.heaplist.pop() #removing the item from the end of the heaplist
        self.currentsize -= 1 #reducing the size of the heap
        self.percdown(1) #comparing the number with its smallest child and repeating.
        return ret_val #return the root value which was delted
    def buildheap(self,list_1):
        i = len(list_1)//2 #finding position of lowest level parent with atleast one child
        self.currentsize = len(list_1) #setting the size of heaplist as length of the list we inputed
        self.heaplist = [0] + list_1[:] #adding the "zero" in the beginning of the heaplist. (this should not be counted in the heap length)
        while i>0: #while we dont reach the item at index 0 (ie the root node)
            self.percdown(i) #compare the value of parent with smallest child
            i-=1 #going to the next parent and again checking

        