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
main.py contains the primary driver function for the program. This file focuses on the logic and execution needed to run
the full program

Comment Anchors
---------------
I am using the Comment Anchors extension for Visual Studio Code which utilizes specific keywords
to allow for quick navigation around the file by creating sections and anchor points. Any use
of "anchor", "todo", "fixme", "stub", "note", "review", "section", "class", "function", and "link" are used in conjunction with 
this extension. To trigger these keywords, they must be typed in all caps. 
"""

import pandas as pd
import os
import bookshelf
import numpy as np
import progressbar
import time
from os import error, system, name
from colored import fg, bg, attr


def loadData() -> pd.DataFrame:
    """Loads all book data for the program"""
    columnList = ['title', 'isbn13', 'num_pages']
    dataPath = 'books.csv'

    try:
        df = pd.read_csv(dataPath, usecols=columnList)
        df['num_pages'] = df['num_pages'].astype(np.int64, errors="raise")
        df['isbn13'] = df['isbn13'].astype(np.int64, errors="raise")
        print(f"Data load: {fg(82)}Success{attr(0)}")
        return df
    except:
        print(f"Data load: {fg(196)}Failed{attr(0)} - {error}")
        exit(0)

def runTests(iterations):
    """Run all of the tests and records the data for the provided number of iterations"""

    data = loadData()
    totalPages = data['num_pages'].sum()
    results = []
    columns = ['Python Insert', 'Numpy Insert', 'Linked List Insert', 'Python Search', 'Numpy Search', 'Linked List Search', 'Python Delete', 'Numpy Delete', 'Linked List Delete']

    # TODO - Add print statements
    # Run the tests for the provided number of iterations
    for i in progressbar.progressbar(range(iterations), redirect_stdout=True):

        # Shuffle data for specific test
        shuffledData = data.sample(frac=1.0, random_state=i)
        searchData = data.sample(n=100, random_state=i)
        deleteData = data.sample(n=100, random_state=i*i)

        # Run one of each test
        for j in range(1, 5):

            results.clear()

            # Calculate size of shelves and search/delete data
            if j == 1:
                size = totalPages//4
            elif j == 2:
                size = totalPages * 0.75 // 4
            elif j == 3:
                size = totalPages * 0.5 // 4
            elif j == 4:
                size = totalPages * 0.25 // 4

            # Create 3 bookcases
            pythonBookcase = bookshelf.BookCase(4, size, bookshelf.ARCHITECTURE.PYTHON_LIST)
            numpyBookcase = bookshelf.BookCase(4, size, bookshelf.ARCHITECTURE.NUMPY_ARRAY)
            linkedListBookcase = bookshelf.BookCase(4, size, bookshelf.ARCHITECTURE.DOUBLY_LINKED_LIST)

            # Test adding
            start = time.time_ns()
            for item in range(shuffledData.shape[0]):
                pythonBookcase.add(bookshelf.Book(shuffledData['title'][item], shuffledData['num_pages'][item], shuffledData['isbn13'][item]))
            end = time.time_ns()
            results.append(end-start)

            start = time.time_ns()
            for item in range(shuffledData.shape[0]):
                numpyBookcase.add(bookshelf.Book(shuffledData['title'][item], shuffledData['num_pages'][item], shuffledData['isbn13'][item]))
            end = time.time_ns()
            results.append(end-start)

            start = time.time_ns()
            for item in range(shuffledData.shape[0]):
                linkedListBookcase.add(bookshelf.Book(shuffledData['title'][item], shuffledData['num_pages'][item], shuffledData['isbn13'][item]))
            end = time.time_ns()
            results.append(end-start)

            # Test searching
            start = time.time_ns()
            for item in range(searchData.shape[0]):
                pythonBookcase.search(bookshelf.Book(searchData['title'][item], searchData['num_pages'][item], searchData['isbn13'][item]))
            end = time.time_ns()
            results.append(end-start)

            start = time.time_ns()
            for item in range(searchData.shape[0]):
                numpyBookcase.search(bookshelf.Book(searchData['title'][item], searchData['num_pages'][item], searchData['isbn13'][item]))
            end = time.time_ns()
            results.append(end-start)

            start = time.time_ns()
            for item in range(searchData.shape[0]):
                linkedListBookcase.search(bookshelf.Book(searchData['title'][item], searchData['num_pages'][item], searchData['isbn13'][item]))
            end = time.time_ns()
            results.append(end-start)




            # Test Removals
            start = time.time_ns()

            end = time.time_ns()





def clearTerminal():
    """Clears the terminal of all text on Windows/MacOs/Linux"""
    
    # For windows
    if name == 'nt':
        _ = system('cls')
    # Mac and linux 
    else:
        _ = system('clear')

# SECTION - main()

def main():

    clearTerminal()
    
    # Changes the working directory to whatever the parent directory of the script executing the code is
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    # Load the book data
    df = loadData()

    maxSize = df['num_pages'].sum()

    bookc = bookshelf.BookCase(numShelves=1)

    # NOTE - TESTING SHELF
    shelf = bookshelf.Shelf(size=maxSize)



    for i in  progressbar.progressbar(range(df.shape[0]), redirect_stdout=True):
        # Make book
        shelf.addBook(bookshelf.Book(df['title'][i], df['num_pages'][i], df['isbn13'][i]))

    books = shelf.findBooks(pages=352)

    for book in books:
        if shelf.removeBook(book):
            print(f"Removed book: {book.title}")
        else:
            print(f"remove failed for {book.title}, {book.pages}")

    print("Updating books to sort by ISBN")
    shelf.updateSortMethod(bookshelf.SORT.ISBN)
    print("Sorting by ISBN")
    shelf.sortBooks()
    print("Updating books to sort by LENGTH")
    shelf.updateSortMethod(bookshelf.SORT.LENGTH)
    print("Sorting by Length")
    shelf.sortBooks()
    

if __name__ == "__main__":
    main()

# !SECTION - main()