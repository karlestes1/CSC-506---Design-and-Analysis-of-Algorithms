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
    dfFull, dfThreeQuater, dfHalf, dfQuarter = pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

    # TODO - Add print statements
    # Run the tests for the provided number of iterations
    
    for i in range(iterations):

        print(f"\n\n***** Running Iteration - {i+1} out of {iterations} *****\n\n")

        # Shuffle data for specific test
        shuffledData = data.sample(frac=1, random_state=i)
        searchData = data.sample(frac=.1, random_state=i)
        deleteData = data.sample(frac=.1, random_state=i*i)

        # Run one of each test
        for j in range(1, 5):

            print(f"\n*** Running Subtest - {j} of iteration - {i + 1} ***\n")

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
            for item in progressbar.progressbar(range(shuffledData.shape[0])):
                pythonBookcase.add(bookshelf.Book(shuffledData.iloc[item]['title'], shuffledData.iloc[item]['num_pages'], shuffledData.iloc[item]['isbn13']))
            end = time.time_ns()
            results.append(end-start)

            start = time.time_ns()
            for item in progressbar.progressbar(range(shuffledData.shape[0])):
                numpyBookcase.add(bookshelf.Book(shuffledData.iloc[item]['title'], shuffledData.iloc[item]['num_pages'], shuffledData.iloc[item]['isbn13']))
            end = time.time_ns()
            results.append(end-start)

            start = time.time_ns()
            for item in progressbar.progressbar(range(shuffledData.shape[0])):
                linkedListBookcase.add(bookshelf.Book(shuffledData.iloc[item]['title'], shuffledData.iloc[item]['num_pages'], shuffledData.iloc[item]['isbn13']))
            end = time.time_ns()
            results.append(end-start)

            # Test searching
            start = time.time_ns()
            for item in progressbar.progressbar(range(searchData.shape[0])):
                pythonBookcase.search(bookshelf.Book(searchData.iloc[item]['title'], searchData.iloc[item]['num_pages'], searchData.iloc[item]['isbn13']))
            end = time.time_ns()
            results.append(end-start)

            start = time.time_ns()
            for item in progressbar.progressbar(range(searchData.shape[0])):
                numpyBookcase.search(bookshelf.Book(searchData.iloc[item]['title'], searchData.iloc[item]['num_pages'], searchData.iloc[item]['isbn13']))
            end = time.time_ns()
            results.append(end-start)

            start = time.time_ns()
            for item in progressbar.progressbar(range(searchData.shape[0])):
                linkedListBookcase.search(bookshelf.Book(searchData.iloc[item]['title'], searchData.iloc[item]['num_pages'], searchData.iloc[item]['isbn13']))
            end = time.time_ns()
            results.append(end-start)

            # Test Removals
            start = time.time_ns()
            for item in progressbar.progressbar(range(deleteData.shape[0])):
                pythonBookcase.remove(bookshelf.Book(deleteData.iloc[item]['title'], deleteData.iloc[item]['num_pages'], deleteData.iloc[item]['isbn13']))
            end = time.time_ns()
            results.append(end-start)

            start = time.time_ns()
            for item in progressbar.progressbar(range(deleteData.shape[0])):
                numpyBookcase.remove(bookshelf.Book(deleteData.iloc[item]['title'], deleteData.iloc[item]['num_pages'], deleteData.iloc[item]['isbn13']))
            end = time.time_ns()
            results.append(end-start)

            start = time.time_ns()
            for item in progressbar.progressbar(range(deleteData.shape[0])):
                linkedListBookcase.remove(bookshelf.Book(deleteData.iloc[item]['title'], deleteData.iloc[item]['num_pages'], deleteData.iloc[item]['isbn13']))
            end = time.time_ns()
            results.append(end-start)

            if j == 1:
                dfFull = dfFull.append(pd.DataFrame([results], columns=columns), ignore_index=True)
                dfFull.to_csv('results/FullSize.csv')
            if j == 2:
                dfThreeQuater = dfThreeQuater.append(pd.DataFrame([results], columns=columns), ignore_index=True)
                dfThreeQuater.to_csv('results/ThreeQuarterSize.csv')
            if j == 3:
                dfHalf = dfHalf.append(pd.DataFrame([results], columns=columns), ignore_index=True)
                dfHalf.to_csv('results/HalfSize.csv')
            if j == 4:
                dfQuarter = dfQuarter.append(pd.DataFrame([results], columns=columns), ignore_index=True)
                dfQuarter.to_csv('results/QuarterSize.csv')
                
    dfFull.to_csv('results/FullSize.csv')
    dfThreeQuater.to_csv('results/ThreeQuarterSize.csv')
    dfHalf.to_csv('results/HalfSize.csv')
    dfQuarter.to_csv('results/QuarterSize.csv')




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

    runTests(25)

    print("\n ***** TESTING COMPLETE ***** \n")
    

if __name__ == "__main__":
    main()

# !SECTION - main()