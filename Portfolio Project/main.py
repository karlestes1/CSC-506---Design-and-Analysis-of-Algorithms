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