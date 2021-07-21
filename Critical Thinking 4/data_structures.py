"""
CSC 506 CT 4 - List Based Stack & Queues
Karl Estes
Created June 29th, 2021
Due July 4th, 2021

Assignment Prompt
-----------------
Design and implement an experiment that will compare the performance of the Python list based stack and queue 
with the linked list implementation. Provide a brief discussion of both stacks and queues for this activity.

File Description
----------------
This file contains the code for both the linked-list and python list implementations of both stacks and queues.
Each class is followed by two letters denoting a python list (PL) architecture and a linked-list (LL) architecture

The linked-list is implemented as a doubly-linked-list which allows for emulation of both stack and queue behavior 

Comment Anchors
---------------
I am using the Comment Anchors extension for Visual Studio Code which utilizes specific keywords
to allow for quick navigation around the file by creating sections and anchor points. Any use
of "anchor", "todo", "fixme", "stub", "note", "review", "section", "class", "function", and "link" are used in conjunction with 
this extension. To trigger these keywords, they must be typed in all caps. 
"""

# SECTION - LISTS
# CLASS - Node()
class Node():
    """
    The Node() class stores a value and pointers to potential next and previous nodes. No methods
    are available as it is meant to be a building block for other abstract data types.
    """

    def __init__(self, value=None, next_node = None, prev_node = None) -> None:
        self.value = value
        self.next = next_node
        self.prev = prev_node
# !CLASS - Node()

# CLASS - List()
class List():
    """
    List() is comprised of Node() objects and allows for creation of a doubly linked lists.

    Only the head and tial node are tracked, and the following methods are available:
        * isEmpty()
        * append()
        * prepend()
        * getLength()
        * remove_at_front()
        * remove_at_back()
    """   
    # TODO - Print Function 
    def __init__(self) -> None:

        self.head = None
        self.tail = None

        # NOTE: Comment out when running full test run
        # self.length = 0

    def isEmpty(self) -> bool:
        return (self.head == None and self.tail == None)

    def append(self, value = None, node: Node = None):
        """
        Adds a value or node to the end of the list. 
        * If only a value is passed, a new node is created. 
        * If only a node is passed, it is appended to the list
        * If both a node and value are passed, the node is appended and the passed value overwrites
          any previous node value"""

        # Handle Node Creation if needed
        if value == None and node == None:
            # TODO - Log Error 
            print("Error")
            return
        elif value != None and node == None:
            new_node = Node(value)
        else:
            if value != None and node != None:
                node.value = value
            new_node = node


        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        # self.length += 1

    def prepend(self, value = None, node: Node = None):
        """
        Adds a value or node to the beggining of the list. 
        * If only a value is passed, a new node is created. 
        * If only a node is passed, it is appended to the list
        * If both a node and value are passed, the node is appended and the passed value overwrites
          any previous node value"""

        # Handle Node Creation if needed
        if value == None and node == None:
            # TODO - Log Error 
            print("Error")
            return
        elif value != None and node == None:
            new_node = Node(value)
        else:
            if value != None and node != None:
                node.value = value
            new_node = node

        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        # self.length += 1
    
    def getLength(self) -> int:
        """Traverses the list and return the number of nodes currently present"""

        # NOTE - Uncomment when running full test
        pCur = self.head
        count = 0

        while pCur != None:
            count += 1
            pCur = pCur.next

        return count

        # return self.length

    def remove_at_front(self):
        """Removes the node at the front of the list and returns the whole node or `None` if list is empty"""
        
        if self.isEmpty():
            return None
        else:
            removed_node = self.head

            # If only one node, reset pointers to None
            if self.head is self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None

            # self.length -= 1

            return removed_node

    def remove_at_back(self):
        """Removes the node at the back of the list and returns the whole node or `None` if list is empty"""
        
        if self.isEmpty():
            return None
        else:
            removed_node = self.tail

            # If only one node, reset pointers to None
            if self.head is self.tail:
                self.head = self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None

            # self.length -= 1

            return removed_node
# !CLASS - List()
# !SECTION

# SECTION - STACKS
# CLASS - StackPL()
class StackPL():
    """
    StackPL() is a stack with an underlying implementation comprising of Python's built in lists. The back of the list
    is treated as the top of the stack since a pythonic list's built in pop() function defaults to the last index.

    This stack conforms to LIFO handling of data and can perform the following operations:
        * push()
        * pop()
        * peek()
        * isEmpty()
        * getLength() 
    """

    # TODO - Print Function

    def __init__(self) -> None:
        # Initialize the internal python list
        self._list = []  
    
    def push(self, value):
        """Pushes a value onto the stack"""
        self._list.append(value)


    def pop(self):
        """Remove a value from the top of the stack and returns it"""
        if len(self._list) == 0:
            #TODO - Format print with color indication
            print("Empty List")
            return

        return self._list.pop()
    
    def peek(self):
        """Returns the value at the top of the stack without removing it"""
        if len(self._list) == 0:
            # TODO - Format print with color indication
            print("Empty List")
            return

        return self._list[len(self._list)-1]
    
    def isEmpty(self) -> bool:
        return True if len(self._list) == 0 else False

    def getLength(self) -> int:
        return len(self._list)        

# !CLASS - StackPL()            
# CLASS - StackLL()
class StackLL():
    """
    StackLL() is a stack with an underlying implementation comprising of a doubly-linked-list.
    This implementation treats the end of the list as the head of the stack so at to maintain 
    consistency with internal list manipulations of the StackPL() class.

    This stack conforms to LIFO handling of data and can perform the following operations:
        * push()
        * pop()
        * peek()
        * isEmpty()
        * getLength() 
    """

    def __init__(self) -> None:

        # Initialize internal list object
        self._list = List()

    def push(self, value):
        """Pushes a value onto the stack"""
        self._list.append(value)

    def pop(self):
        """Remove a value from the top of the stack and returns it"""
        if self._list.isEmpty():
            # TODO - Format printing with color
            print("Empty stack")
            return
        
        return self._list.remove_at_back()

    def peek(self):
        """Returns the value at the top of the stack without removing it"""
        if self._list.isEmpty():
            # TODO - Format printing with color
            print("Empty stack")
            return
        
        return self._list.tail.value
    
    def isEmpty(self) -> bool:
        return self._list.isEmpty()
    
    def getLength(self) -> int:
        return self._list.getLength()

    # TODO - Write a print function

# !CLASS - StackLL()
# !SECTION

# SECTION - QUEUES
# CLASS - QueuePL()
class QueuePL():
    """
    QueuePL() is a queue with an underlying implementation comprising of Python's built in lists. The front of the list will be considered
    the front of the queue, and the back of the list will be considered the end of the queue. Dequeues will happen at the front and enqueues
    will happen at the back.

    This stack conforms to FIFO handling of data and can perform the following operations:
        * enqueue()
        * dequeue()
        * peek()
        * isEmpty()
        * getLength() 
    """

    def __init__(self) -> None:

        # Initialize internal list object
        self._list = []
    
    def enqueue(self, value):
        """Adds an item to the back of the queue"""
        self._list.append(value)

    def dequeue(self):
        """Removes an item from the front of the queue and returns the value"""
        if self.isEmpty():
            # TODO - Format printing with color
            print("Empty queue")
            return

        return self._list.pop(0)

    def peek(self):
        """Returns the value of the item at the front of the queue without removing it"""
        if self.isEmpty():
            # TODO - Format printing with color
            print("Empty queue")

        return self._list[0]

    def isEmpty(self) -> bool:
        return True if len(self._list) == 0 else False

    def getLength(self) -> int:
        return len(self._list)

    # TODO - Write a print function
# !CLASS - QueuePL()

# CLASS - QueueLL()
class QueueLL():
    """
    QueueLL() is a queue with an underlying implementation comprising of Python's built in lists. The front of the list will be considered
    the front of the queue, and the back of the list will be considered the end of the queue. Dequeues will happen at the front and enqueues
    will happen at the back.

    This stack conforms to FIFO handling of data and can perform the following operations:
        * enqueue()
        * dequeue()
        * peek()
        * isEmpty()
        * getLength() 
    """
    def __init__(self) -> None:

        # Initialize internal list object
        self._list = List()
    
    def enqueue(self, value):
        """Adds an item to the back of the queue"""
        self._list.append(value)

    def dequeue(self):
        """Removes an item from the front of the queue and returns the value"""
        if self.isEmpty():
            # TODO - Format printing with color
            print("Empty queue")
            return

        return self._list.remove_at_front().value

    def peek(self):
        """Returns the value of the item at the front of the queue without removing it"""
        if self.isEmpty():
            # TODO - Format printing with color
            print("Empty queue")
            return

        return self._list.head.value

    def isEmpty(self) -> bool:
        return self._list.isEmpty()

    def getLength(self) -> int:
        return self._list.getLength()

# !CLASS - QueuePL()
# !SECTION