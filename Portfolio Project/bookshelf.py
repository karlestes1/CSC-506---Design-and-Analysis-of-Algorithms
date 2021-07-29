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

from numpy.core.numeric import argwhere

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
            
            # Insert the book
            bisect.insort(self.bookList, book)
            self.curSize += book.pages

            # Remove overflow
            while self.curSize > self.maxSize:
                extra, self.bookList = self.bookList[-1], self.bookList[:-1]
                self.curSize -= extra.pages
                overflow.append(extra)

            pass

        elif self.architecture == ARCHITECTURE.DOUBLY_LINKED_LIST:
            
            # Insert the book
            self.bookList.insertInOrder(book)

            # Remove overflow
            while self.bookList.length > self.maxSize:
                overflow.append(self.bookList.removeAtBack())

            # Update shelf size
            self.curSize = self.bookList.length

        return overflow
    
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
            results = np.where(self.bookList == book)

            if len(results) != 0:
                self.bookList = np.delete(self.bookList, results)
                return True
            
            return False
        elif self.architecture == ARCHITECTURE.DOUBLY_LINKED_LIST:
            
            return self.removeBook(book)
            
    
        return False
    
    def removeFront(self)->Book:
        """Removes the book at the front of the shelf"""
        
        if self.isEmpty():
            return None
        
        if self.architecture == ARCHITECTURE.PYTHON_LIST:
            book = self.bookList.pop(0)
        elif self.architecture == ARCHITECTURE.NUMPY_ARRAY:
            book = self.bookList[0]
            self.bookList = self.bookList[1:]
        elif self.architecture == ARCHITECTURE.DOUBLY_LINKED_LIST or self.architecture == ARCHITECTURE.DOUBLY_LINKED_LIST_AVL:
            book = self.bookList.removeAtFront().value

        self.curSize -= book.pages
        return book
    
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
            return matches
    
        # Perform search based on the underlying architecture
        if self.architecture == ARCHITECTURE.PYTHON_LIST:

            for book in progressbar.progressbar(self.bookList):
                if (name == None or name == book.name) and (pages == None or pages == book.pages) and (isbn == None or isbn == book.isbn):
                    matches.append(book)

        elif self.architecture == ARCHITECTURE.NUMPY_ARRAY:

            for book in progressbar.progressbar(self.bookList):
                if (name == None or name == book.name) and (pages == None or pages == book.pages) and (isbn == None or isbn == book.isbn):
                    matches.append(book)

        elif self.architecture == ARCHITECTURE.DOUBLY_LINKED_LIST:
            
            curNode = self.bookList.head      

            # Creates a progress bar with no percentage. It simply moves back and forth to show the program is running
            # and keeps track of the number of update iterations and the elapsed time
            bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength)
            while curNode != None:
                if (name == None or name == curNode.value.name) and (pages == None or pages == curNode.value.pages) and (isbn == None or isbn == curNode.value.isbn):
                    matches.append(curNode.value)
                bar.update()
    
        return matches

    def search(self, book: Book) -> bool:
        """ Searches the shelf for a specific book and returns true if the book is found"""

        if self.architecture == ARCHITECTURE.PYTHON_LIST:
            return True if book in self.bookList else False
        elif self.architecture == ARCHITECTURE.NUMPY_ARRAY:
            return True if len(np.where(self.bookList == book)) != 0 else False
        elif self.architecture == ARCHITECTURE.DOUBLY_LINKED_LIST:
            return self.bookList.search(book)

    def isEmpty(self) -> bool:
        # Perform sort based on the underlying architecture
        if self.architecture == ARCHITECTURE.PYTHON_LIST:
            return True if len(self.bookList) == 0 else False
        elif self.architecture == ARCHITECTURE.NUMPY_ARRAY:
            return True if len(self.bookList) == 0 else False
        elif self.architecture == ARCHITECTURE.DOUBLY_LINKED_LIST:
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
# !CLASS

# CLASS - BookCase

class BookCase():
    """ TODO - Bookcase Description """
    
    
    def __init__(self, numShelves: int = 4, shelfSize: int = 10000, architecture: ARCHITECTURE = ARCHITECTURE.PYTHON_LIST):

        if numShelves == None or numShelves == 0:
            print(f"{fg(196)}Error{attr(0)}{attr(1)} - Unable to create a bookcase with no shelves{attr(0)}")
            quit()

        self.shelves: List[Shelf] = []
        for i in range(numShelves):
            self.shelves.append(Shelf(shelfSize, architecture))

        print(f"{fg(82)}Initialized BookCase{attr(0)} - {numShelves} shelves with capacity for {shelfSize} pages each")
     
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
 
    def remove(self, book: Book) -> bool:
        """ Removes a book from the bookshelf and shifts any remaining books to ensure there is no empty space """
    
        removed = False
        for i in range(len(self.shelves)):
            removed = self.shelves[i].removeBook(book)

            if removed == True:
                # Handle shifting of all future shelves
                if i < len(self.shelves)-1:
                    for j,k in zip(range(i, len(self.shelves)-1),range(i+1, len(self.shelves))):
                        nextBook = self.shelves[k].peek()

                        while nextBook != None:
                            if (self.shelves[j].curSize + nextBook.pages) <= self.shelves[j].maxSize:
                                self.shelves[j].addBook(self.shelves[k].removeFront())
                                nextBook = self.shelves[k].peek()
                            else:
                                nextBook = None
                break

        return removed
  
    def findBooks(self, name: str = None, pages: int = None, isbn: int = None) -> list:
        """ Searches the book case for all books matching the given criteria """
        found = []

        for i in range(len(self.shelves)):
            found.append(self.shelves[i].findBooks(name, pages, isbn))

        return found

    def search(self, book: Book) -> bool:
        """Searches the bookcase for a specific book and returns true if found"""
        for i in range(len(self.shelves)):
            if self.shelves[i].search(book) == True:
                return True

        return False

# !CLASS - BookCase

# !SECTION