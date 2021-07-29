"""
CSC 506 Portfolio Project - Analysis of Algorithms and Data Structures
Created July 16th, 2021
Due August 1st, 2021

Asignment Prompt
----------------
Your portfolio project is to analyze the pragmatic differences in how two or more different algorithms and/or data structures 
solve the same problem. You will choose the subject of your project, code and profile the algorithms in the Python programming 
language, and analyze your results. You will then present your findings in a well-organized research paper that resembles the 
structure of a manuscript for publication in a computer science journal.

File Description
----------------
data_structures.py contains code for a doubly linked list ADT and an AVL Tree

Comment Anchors
---------------
I am using the Comment Anchors extension for Visual Studio Code which utilizes specific keywords
to allow for quick navigation around the file by creating sections and anchor points. Any use
of "anchor", "todo", "fixme", "stub", "note", "review", "section", "class", "function", and "link" are used in conjunction with 
this extension. To trigger these keywords, they must be typed in all caps. 
"""

from typing import Any, List
from colored import fg, bg, attr

# TODO - Color Coding

# CLASS - ListNode

class ListNode():
    def __init__(self, value: Any) -> None:
        self.value = value
        self.next: ListNode = None
        self.prev: ListNode = None

    # Overloaded Comparison Operators
    def __eq__(self, o: object) -> bool:

        if isinstance(self, o):
            return True if self.value == o.value else False
        else:
            return True if self.value == o else False

    def __lt__(self, o: object) -> bool:

        if isinstance(self, o):
            return True if self.value < o.value else False
        else:
            return True if self.value < o else False

    def __le__(self, o: object) -> bool:

        if isinstance(self, o):
            return True if self.value <= o.value else False
        else:
            return True if self.value <= o else False

    def __gt__(self, o: object) -> bool:

        if isinstance(self, o):
            return True if self.value > o.value else False
        else:
            return True if self.value > o else False

    def __ge__(self, o: object) -> bool:

        if isinstance(self, o):
            return True if self.value >= o.value else False
        else:
            return True if self.value >= o else False
# !CLASS - ListNode

# CLASS - LinkedList    

class LinkedList():

    def __init__(self) -> None:
        self.head: ListNode = None
        self.tail: ListNode = None
        self.length: int = 0

    def insertAtFront(self, value: Any):
        """Creates a new node and inserts a value at the start of the list"""
        if value == None:
            print(f"Will not insert value of {attr(1)}{attr(2)}None{attr(0)} into the list")
            return

        newNode = ListNode(value)
        if self.length == 0:
            self.head = self.tail = newNode
        else:
            newNode.next, self.head.prev = self.head, newNode
            self.head = newNode
        
        self.length = self.length + 1

    def insertAtBack(self, value: Any):
        """Creates a new node and inserts a value at the back of the list"""
        if value == None:
            print(f"Will not insert value of {attr(1)}{attr(2)}None{attr(0)} into the list")
            return

        newNode = ListNode(value)
        if self.length == 0:
            self.head = self.tail = newNode
        else:
            newNode.prev, self.tail.next = self.tail, newNode
            self.tail = newNode

        self.length = self.length + 1

    def insertInOrder(self, value: Any):
        """Searches through the list to place the value in ascending order"""
        if value == None:
            print(f"Will not insert value of {attr(1)}{attr(2)}None{attr(0)} into the list")
            return

        newNode = ListNode(value)
        if self.length == 0:
            self.head = self.tail = newNode
        else:
            curNode = self.head

            while curNode != None and curNode <= newNode:
                curNode = curNode.next

            # Three Cases
            if curNode == None:
                newNode.prev, self.tail.next = self.tail, newNode
                self.tail = newNode
            elif curNode is self.head:
                newNode.next, self.head.prev = self.head, newNode
                self.head = newNode
            else:
                newNode.prev, curNode.prev.next, newNode.next, curNode.prev = curNode.prev, newNode, curNode, newNode

            self.length = self.length + 1

    def removeAtFront(self) -> ListNode:
        """Removes the node at the front of the list and returns it"""

        if self.length == 0:
            return None
        
        node = self.head

        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        self.length = self.length - 1
        
        return node

    def removeAtBack(self) -> ListNode:
        """Removes the node at the back of the list and returns it"""

        if self.length == 0:
            return None

        node = self.tail

        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.length = self.length - 1
        
        return node

    def remove(self, item: Any) -> bool:
        """
        Searches the list for a specific item and removes it. Returns true if the item was removed and false otherwise
        """

        curNode = self.head

        # Iterate through list to find item
        while curNode != None:

            # Item Found
            if curNode == item:
                # Reassign pointers
                curNode.prev.next, curNode.next.prev = curNode.next, curNode.prev
                return True

            # Item not Found
            curNode = curNode.next
        
        return False
                
    def search(self, item: Any) -> bool:
        """Searches the list and returns true if the item is found"""

        curNode = self.head

        # Iterate through list to find item
        while curNode != None:

            # Item Found
            if curNode == item:
                return True

            # Item not Found
            curNode = curNode.next
        
        return False

    def isEmpty(self) -> bool:
        return True if self.head == None and self.tail == None else False

    def getLength(self) -> int:
        """Recalculates and returns list length"""
        self.length = 0

        curNode = self.head
        
        while curNode != None:
            self.length += 1
            curNode = curNode.next

        return self.length

    def sort(self) -> None:
        """Sort the list in ascending order using a modified insertion sort"""
        
        # TODO - Implement LL Sort

# !CLASS - Linked List