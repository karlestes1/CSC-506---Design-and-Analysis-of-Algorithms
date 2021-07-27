"""
CSC 506 Portfolio Project - Analysis of Algorithms and Data Structures
Created July 17th, 2021
Due August 1st, 2021

Asignment Prompt
----------------
Your portfolio project is to analyze the pragmatic differences in how two or more different algorithms and/or data structures 
solve the same problem. You will choose the subject of your project, code and profile the algorithms in the Python programming 
language, and analyze your results. You will then present your findings in a well-organized research paper that resembles the 
structure of a manuscript for publication in a computer science journal.

File Description
----------------
bookshelf.py contains the classes Book, Shelf, and Bookcase which are used for testing the various data structures. Books
are stored on shelves with some "underlying architecture", and the shelves are included in a Bookcase. The idea is to compare
the underlying architecture of the shelves (python lists, numpy arrays, linked lists, and linked lists with an AVL tree), while
dynamically adding, removing, and sorting books.

Comment Anchors
---------------
I am using the Comment Anchors extension for Visual Studio Code which utilizes specific keywords
to allow for quick navigation around the file by creating sections and anchor points. Any use
of "anchor", "todo", "fixme", "stub", "note", "review", "section", "class", "function", and "link" are used in conjunction with 
this extension. To trigger these keywords, they must be typed in all caps. 
"""

from enum import Enum
from colored import fg, bg, attr
from typing import List
from copy import deepcopy

import data_structures as ds
import numpy as np
import progressbar
import bisect

# TODO - Color Coding

# SECTION - ENUM'S
class SORT(Enum):
    TITLE = 1
    LENGTH = 2
    ISBN = 3

class ARCHITECTURE(Enum):
    PYTHON_LIST = 1
    NUMPY_ARRAY = 2
    DOUBLY_LINKED_LIST = 3
    DOUBLY_LINKED_LIST_AVL = 4

# !SECTION

# SECTION - Structures
# CLASS - Book

class Book():

    def __init__(self, title: str = None, pages: int = 0, isbn: int = None, sortScheme: SORT = SORT.TITLE) -> None:
        self.title = title
        self.pages = pages
        self.isbn = isbn
        self.sort = sortScheme

    def __eq__(self, o: object) -> bool:

        if isinstance(o, Book):
            if self.sort == SORT.TITLE:
                return True if self.title == o.title else False
            elif self.sort == SORT.LENGTH:
                return True if self.pages == o.pages else False
            elif self.sort == SORT.ISBN:
                return True if self.isbn == o.isbn else False
        return False

    def __lt__(self, o: object) -> bool:
        
        if isinstance(o, Book):
            if self.sort == SORT.TITLE:
                return True if self.title < o.title else False
            elif self.sort == SORT.LENGTH:
                return True if self.pages < o.pages else False
            elif self.sort == SORT.ISBN:
                return True if self.isbn < o.isbn else False
        return False

    def __gt__(self, o: object) -> bool:
        
        if isinstance(o, Book):
            if self.sort == SORT.TITLE:
                return True if self.title > o.title else False
            elif self.sort == SORT.LENGTH:
                return True if self.pages > o.pages else False
            elif self.sort == SORT.ISBN:
                return True if self.isbn > o.isbn else False
        return False

# !CLASS

# CLASS - Shelf
class Shelf():

    def __init__(self, size: int = 10000, architecture: ARCHITECTURE = ARCHITECTURE.PYTHON_LIST, sortScheme: SORT = SORT.TITLE) -> None:
        self.maxSize = size
        self.curSize = 0
        self.architecture = architecture
        self.sortScheme = sortScheme

        # Determine underlying architecture
        if self.architecture == ARCHITECTURE.PYTHON_LIST:
            self.bookList = []
        elif self.architecture == ARCHITECTURE.NUMPY_ARRAY:
            self.bookList = np.array()
        elif self.architecture == ARCHITECTURE.DOUBLY_LINKED_LIST:
            self.bookList = ds.LinkedList()
        elif self.architecture == ARCHITECTURE.DOUBLY_LINKED_LIST_AVL:
            # TODO - Add creation for LL with AVL
            pass

    # FUNCTION - addBook
    def addBook(self, book: Book) -> list:
        """
        Adds a book to the shelf. Internally, the add is done based on the architecture of the shelf as determined
        during `__init__()`. If the shelf exceeds maximum size after a book is inserted in its proper location, any 
        books that are "pushed off" the shelf will be returned in a `Python List`.

        The list will be empty if no overflow books are returned 
        """

        overflow = []

        # Add based on the underlying architecture
        if self.architecture == ARCHITECTURE.PYTHON_LIST:

            # Insert the book
            bisect.insort(self.bookList, book)
            self.curSize += book.pages

            # Remove overflow
            while self.curSize > self.maxSize:
                extra = self.bookList.pop()
                self.curSize -= extra.pages
                overflow.append(extra)

        elif self.architecture == ARCHITECTURE.NUMPY_ARRAY:
            # TODO - Implement Add Functionality for Numpy Arrays
            pass

        elif self.architecture == ARCHITECTURE.DOUBLY_LINKED_LIST:
            # TODO - Implement Add Functionality for Doubly Linked List
            pass

        elif self.architecture == ARCHITECTURE.DOUBLY_LINKED_LIST_AVL:
            # TODO - Implement Add Functionality for Doubly Linked List with AVL Tree
            pass

        return overflow
    
    # !FUNCTION - addBook
    
    # FUNCTION - removeBook
    
    # REVIEW - Should all removals of sub-architectures return a boolean value?
    def removeBook(self, book: Book) -> bool:
        """ 
        Description
        -----------
        Searches for a book on the shelf and removes it. Removal will be done based on the underlying architecture as 
        determined during `__init__()`.

        Parameters
        ----------
        * book: The exact book value that should be removed

        Return
        ------
        * True: If the book was found in the list and removed
        * False: If the book was not found in the list
        """

        # Perform removal based on the underlying architecture
        if self.architecture == ARCHITECTURE.PYTHON_LIST:
            
            try:
                self.bookList.remove(book)
                self.curSize -= book.pages
                return True
            # Book not in list - Python inbuilt list returns ValueError if item is not in the list
            except ValueError:
                return False

        elif self.architecture == ARCHITECTURE.NUMPY_ARRAY:
            # TODO - Implement remove functionality for NumPy Array
            pass
        elif self.architecture == ARCHITECTURE.DOUBLY_LINKED_LIST:
            # TODO - Implement remove functionality for Doubly Linked List
            pass
        elif self.architecture == ARCHITECTURE.DOUBLY_LINKED_LIST_AVL:
            # TODO - Implement remove functionality for Doubly Linked List w/ AVL Tree
            pass
    
        return False
    # !FUNCTION - removeBook
    
    def removeFront(self)->Book:
        """Removes the book at the front of the shelf"""
        
        if self.isEmpty():
            return None
        
        if self.architecture == ARCHITECTURE.PYTHON_LIST:
            book = self.bookList.pop(0)
        elif self.architecture == ARCHITECTURE.NUMPY_ARRAY:
            book = self.bookList[0]
            self.bookList = np.delete(self.bookList, [0])
        elif self.architecture == ARCHITECTURE.DOUBLY_LINKED_LIST or self.architecture == ARCHITECTURE.DOUBLY_LINKED_LIST_AVL:
            book = self.bookList.removeAtFront().value

        self.curSize -= book.pages
        return book

    # FUNCTION - findBook
    
    def findBooks(self, name: str = None, pages: int = None, isbn: int = None) -> list:
        """ 
        Description
        -----------
        Searches through all the books on a shelf for any that match the provided criteria.

        Parameters
        ----------
        * name: The name/title of the book
        * pages: The number of pages in the book
        * isbn: The 13 digit isbn of the book

        Return
        ------
        Returns all books that match the provided criteria in a `Python List`. If all criteria are `None`, then `None` is returned.
        """

        matches = []

        if name == None and pages == None and isbn == None:
            return None
    
        # Perform search based on the underlying architecture
        if self.architecture == ARCHITECTURE.PYTHON_LIST:

            for book in progressbar.progressbar(self.bookList):
                if (name == None or name == book.name) and (pages == None or pages == book.pages) and (isbn == None or isbn == book.isbn):
                    matches.append(book)

        elif self.architecture == ARCHITECTURE.NUMPY_ARRAY:
            # TODO - Implement find functionality for NumPy Array
            pass
        elif self.architecture == ARCHITECTURE.DOUBLY_LINKED_LIST:
            # TODO - Implement find functionality for Doubly Linked List
            pass
        elif self.architecture == ARCHITECTURE.DOUBLY_LINKED_LIST_AVL:
            # TODO - Implement find functionality for Doubly Linked List w/ AVL Tree
            pass
    
        return matches

    # !FUNCTION - findBook

    # FUNCTION - sortBooks
    
    def sortBooks(self):
        """ 
        Sorts the books on the shelf based on the underlying sort schema. To update the sort schema, use the 
        `updateSortMethod()` function. Sorting will occur based on the underlying architecture:

        * Python List -> Built in Sort
        * NumPy Array -> ??? (REVIEW - What sort for numpy array)
        * Doubly Linked List -> Modified Insertion Sort
        * Doubly List with AVL Tree -> Modified Insertion with Tree Reconstruction
        """
    
        # Perform sort based on the underlying architecture
        if self.architecture == ARCHITECTURE.PYTHON_LIST:
            self.bookList.sort()

        elif self.architecture == ARCHITECTURE.NUMPY_ARRAY:
            # TODO - Implement sort functionality for NumPy Array
            pass
        elif self.architecture == ARCHITECTURE.DOUBLY_LINKED_LIST:
            # TODO - Implement sort functionality for Doubly Linked List
            pass
        elif self.architecture == ARCHITECTURE.DOUBLY_LINKED_LIST_AVL:
            # TODO - Implement sort functionality for Doubly Linked List w/ AVL Tree
            pass
    
    # !FUNCTION - sortBooks

    # FUNCTION - updateSortMethod
    
    def updateSortMethod(self, sortScheme: SORT):
        """ Updates the internal sort mechanism for all book objects on the shelf """

        # Perform sort update based on the underlying architecture
        if self.architecture == ARCHITECTURE.PYTHON_LIST:

            for i in progressbar.progressbar(range(len(self.bookList))):
                self.bookList[i].sort = sortScheme

        elif self.architecture == ARCHITECTURE.NUMPY_ARRAY:
            # TODO - Implement sort update functionality for NumPy Array
            pass
        elif self.architecture == ARCHITECTURE.DOUBLY_LINKED_LIST:
            # TODO - Implement sort update functionality for Doubly Linked List
            pass
        elif self.architecture == ARCHITECTURE.DOUBLY_LINKED_LIST_AVL:
            # TODO - Implement sort update functionality for Doubly Linked List w/ AVL Tree
            pass
    
    # !FUNCTION - updateSortMethod

    def isEmpty(self) -> bool:
        # Perform sort based on the underlying architecture
        if self.architecture == ARCHITECTURE.PYTHON_LIST:
            return True if len(self.bookList) == 0 else False
        elif self.architecture == ARCHITECTURE.NUMPY_ARRAY:
            return True if len(self.bookList) == 0 else False
        elif self.architecture == ARCHITECTURE.DOUBLY_LINKED_LIST:
            return self.bookList.isEmpty()
        elif self.architecture == ARCHITECTURE.DOUBLY_LINKED_LIST_AVL:
            return self.bookList.isEmpty()

    def peek(self):

        if self.isEmpty():
            return None

        # Perform sort based on the underlying architecture
        if self.architecture == ARCHITECTURE.PYTHON_LIST:
            return self.bookList[0]
        elif self.architecture == ARCHITECTURE.NUMPY_ARRAY:
            return self.bookList[0]
        elif self.architecture == ARCHITECTURE.DOUBLY_LINKED_LIST:
            return self.bookList.head.value
        elif self.architecture == ARCHITECTURE.DOUBLY_LINKED_LIST_AVL:
            return self.bookList.head.value
# !CLASS

# CLASS - BookCase

class BookCase():
    """ TODO - Bookcase Description """
    
    # FUNCTION - __init__
    
    def __init__(self, numShelves: int = 4, shelfSize: int = 10000, architecture: ARCHITECTURE = ARCHITECTURE.PYTHON_LIST):

        if numShelves == None or numShelves == 0:
            print(f"{fg(196)}Error{attr(0)}{attr(1)} - Unable to create a bookcase with no shelves{attr(0)}")
            quit()

        self.shelves: List[Shelf] = []
        for i in range(numShelves):
            self.shelves.append(Shelf(shelfSize, architecture))

        print(f"{fg(82)}Initialized BookCase{attr(0)} - {numShelves} shelves with capacity for {shelfSize} pages each")
    
    # !FUNCTION - __init__

    # FUNCTION - add
    
    def add(self, newBook: Book) -> List[Book]:
        """ 
        Adds a to the bookcase in proper order. If there is no room for all the books, a list of the books that were
        removed will be returned.
        """

        overflow = self.shelves[0].addBook(newBook)
        temp=[]

        for i in range(1, len(self.shelves)):

            if len(overflow) == 0:
                return

            for book in overflow:
                temp.append(self.shelves[i].addBook(book))
            
            overflow.clear()
            overflow = deepcopy(temp)
            temp.clear()

    
    # !FUNCTION - add

    # FUNCTION - remove
    
    def remove(self, book: Book) -> bool:
        """ Removes a book from the bookshelf and shifts any remaining books to ensure there is no empty space """
    
        removed = False
        for i in range(len(self.shelves)):
            removed = self.shelves[i].removeBook(book)

            if removed == True:
                # Handle shifting of all future shelves
                if i < len(self.shelves)-1:
                    for j in range(i+1, len(self.shelves)):

                        # Check length of book at front

                        # Remove book if needed
                        pass
                break

        return removed
    # !FUNCTION - remove

    # TODO - search()

    # TODO - sort()

    # TODO - Update Sort Scheme Function

# !CLASS - BookCase

# !SECTION