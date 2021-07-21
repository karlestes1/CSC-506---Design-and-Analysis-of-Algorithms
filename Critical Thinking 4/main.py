"""
CSC 506 CT 4 - List Based Stacks and Queues
Created June 30th, 2021
Due July 4th, 2021

Asignment Prompt
----------------
Design and implement an experiment that will compare the performance of the Python list based stack and queue 
with the linked list implementation. Provide a brief discussion of both stacks and queues for this activity.

File Description
----------------
main.py contains the code for running the comparisons of the various data structures and saving the analysis

Comment Anchors
---------------
I am using the Comment Anchors extension for Visual Studio Code which utilizes specific keywords
to allow for quick navigation around the file by creating sections and anchor points. Any use
of "anchor", "todo", "fixme", "stub", "note", "review", "section", "class", "function", and "link" are used in conjunction with 
this extension. To trigger these keywords, they must be typed in all caps. 
"""

import pandas as pd
import numpy as np
from pandas.core.reshape.reshape import stack
import progressbar
import os
import time
from data_structures import StackLL, StackPL, QueueLL, QueuePL
from os import system, name

def clearTerminal():
    """Clears the terminal of all text on Windows/MacOs/Linux"""
    
    # For windows
    if name == 'nt':
        _ = system('cls')
    # Mac and linux 
    else:
        _ = system('clear')

# SECTION - Tests

def test_stack_single_ops(iterations=5):
    """
    Runs a series of tests and collects data on the runtime of various stack functions.
    For each test where a value must be pushed, a random number is generated

    Parameters
    ----------
    iterations
        The number of times each operation should be tested

    Returns
    -------
    A pandas data frame where each column corresponds to an operation and each row
    contains a single runtime test
    """


# !SECTION - Tests

def test_python_stack(iterations=5, stackSize=1000):
    # TODO - Function Description
    # TODO - Put in Print Statements

    # Initialize Stack
    stack = StackPL()
    
    # Create a dictionary w/ empty lists
    results = {"Push() Empty": [], f"Push() Full: {stackSize}": [], "Pop() Empty": [], f"Pop() Full: {stackSize}": [], f"GetLength() : {stackSize}" : []}

    # Loop for # of iterations w/ progress bar
    for i in progressbar.progressbar(range(iterations)):

        # Generate integers to be added based on stack size
        values = np.random.randint(0, 1000, stackSize)

        # Perform Push on Empty Stack
        start = time.time_ns()
        stack.push(values[0])
        end = time.time_ns()

        results["Push() Empty"].append(end-start)

        # Perform pop on Empty Stack
        start = time.time_ns()
        pop_value = stack.pop()
        end = time.time_ns()

        results["Pop() Empty"].append(end-start)

        # Perform Push on Full Stack
        start = time.time_ns()
        for item in values:
            stack.push(item)
        end = time.time_ns()

        results[f"Push() Full: {stackSize}"].append(end-start)

        # Test Get Length
        start = time.time_ns()
        length = stack.getLength()
        end = time.time_ns()

        results[f"GetLength() : {stackSize}"].append(end-start)

        # Perform Pop on Full Stack 
        start = time.time_ns()
        for i in range(stackSize):
            pop_value = stack.pop()
        end = time.time_ns()

        results[f"Pop() Full: {stackSize}"].append(end-start)

    df = pd.DataFrame(results)

    return df

def test_list_stack(iterations=5, stackSize=1000):
    # TODO - Function Description
    # TODO - Put in Print Statements

    # Initialize Stack
    stack = StackLL()
    
    # Create a dictionary w/ empty lists
    results = {"Push() Empty": [], f"Push() Full: {stackSize}": [], "Pop() Empty": [], f"Pop() Full: {stackSize}": [], f"GetLength() : {stackSize}" : []}

    # Loop for # of iterations w/ progress bar
    for i in progressbar.progressbar(range(iterations)):

        # Generate integers to be added based on stack size
        values = np.random.randint(0, 1000, stackSize)

        # Perform Push on Empty Stack
        start = time.time_ns()
        stack.push(values[0])
        end = time.time_ns()

        results["Push() Empty"].append(end-start)

        # Perform pop on Empty Stack
        start = time.time_ns()
        pop_value = stack.pop()
        end = time.time_ns()

        results["Pop() Empty"].append(end-start)

        # Perform Push on Full Stack
        start = time.time_ns()
        for item in values:
            stack.push(item)
        end = time.time_ns()

        results[f"Push() Full: {stackSize}"].append(end-start)

        # Test Get Length
        start = time.time_ns()
        length = stack.getLength()
        end = time.time_ns()

        results[f"GetLength() : {stackSize}"].append(end-start)

        # Perform Pop on Full Stack 
        start = time.time_ns()
        for i in range(stackSize):
            pop_value = stack.pop()
        end = time.time_ns()

        results[f"Pop() Full: {stackSize}"].append(end-start)

    df = pd.DataFrame(results)

    return df

def test_python_queue(iterations=5, queueSize=100):
    # TODO - Function Description
    # TODO - Put in Print Statements

    # Initialize Stack
    queue = QueuePL()
    
    # Create a dictionary w/ empty lists
    results = {"Enqueue() Empty": [], f"Enqueue() Full: {queueSize}": [], "Dequeue() Empty": [], f"Dequeue() Full: {queueSize}": [], f"GetLength() : {queueSize}" : []}

    # Loop for # of iterations w/ progress bar
    for i in progressbar.progressbar(range(iterations)):

        # Generate integers to be added based on stack size
        values = np.random.randint(0, 1000, queueSize)

        # Perform Enqueue on Empty Queue
        start = time.time_ns()
        queue.enqueue(values[0])
        end = time.time_ns()

        results["Enqueue() Empty"].append(end-start)

        # Perform Dequeue on Empty Queue
        start = time.time_ns()
        dequeue_value = queue.dequeue()
        end = time.time_ns()

        results["Dequeue() Empty"].append(end-start)

        # Perform Enqueue on Full Queue
        start = time.time_ns()
        for item in values:
            queue.enqueue(item)
        end = time.time_ns()

        results[f"Enqueue() Full: {queueSize}"].append(end-start)

        # Test Get Length
        start = time.time_ns()
        length = queue.getLength()
        end = time.time_ns()

        results[f"GetLength() : {queueSize}"].append(end-start)

        # Perform Dequeue on Full Queue 
        start = time.time_ns()
        for i in range(queueSize):
            dequeue_value = queue.dequeue()
        end = time.time_ns()

        results[f"Dequeue() Full: {queueSize}"].append(end-start)

    df = pd.DataFrame(results)

    return df

def test_list_queue(iterations=5, queueSize=100):
    # TODO - Function Description
    # TODO - Put in Print Statements

    # Initialize Stack
    queue = QueueLL()
    
    # Create a dictionary w/ empty lists
    results = {"Enqueue() Empty": [], f"Enqueue() Full: {queueSize}": [], "Dequeue() Empty": [], f"Dequeue() Full: {queueSize}": [], f"GetLength() : {queueSize}" : []}

    # Loop for # of iterations w/ progress bar
    for i in progressbar.progressbar(range(iterations)):

        # Generate integers to be added based on stack size
        values = np.random.randint(0, 1000, queueSize)

        # Perform Enqueue on Empty Queue
        start = time.time_ns()
        queue.enqueue(values[0])
        end = time.time_ns()

        results["Enqueue() Empty"].append(end-start)

        # Perform Dequeue on Empty Queue
        start = time.time_ns()
        dequeue_value = queue.dequeue()
        end = time.time_ns()

        results["Dequeue() Empty"].append(end-start)

        # Perform Enqueue on Full Queue
        start = time.time_ns()
        for item in values:
            queue.enqueue(item)
        end = time.time_ns()

        results[f"Enqueue() Full: {queueSize}"].append(end-start)

        # Test Get Length
        start = time.time_ns()
        length = queue.getLength()
        end = time.time_ns()

        results[f"GetLength() : {queueSize}"].append(end-start)

        # Perform Dequeue on Full Queue 
        start = time.time_ns()
        for i in range(queueSize):
            dequeue_value = queue.dequeue()
        end = time.time_ns()

        results[f"Dequeue() Full: {queueSize}"].append(end-start)

    df = pd.DataFrame(results)

    return df

def run_all_tests(iterations=5, size=100):
    # TODO - Function descrtiption

    df_pystack = test_python_stack(iterations, size)
    df_liststack = test_list_stack(iterations, size)
    df_pyqueue = test_python_queue(iterations, size)
    df_listqueue = test_list_queue(iterations, size)

    df_pystack.to_csv("results/pystack.csv")
    df_liststack.to_csv("results/liststack.csv")
    df_pyqueue.to_csv("results/pyqueue.csv")
    df_listqueue.to_csv("results/listqueue.csv")

# SECTION - main()

def main():

    number_of_tests = 25
    data_size = 250000

    # Changes the working directory to whatever the parent directory of the script executing the code is
    os.chdir(os.path.dirname(os.path.realpath(__file__)))  


    clearTerminal()
    print("CSC 506 CT 4")

    # NOTE - If running all tests, check data_structures.py file for lines to comment/uncomment
    run_all_tests(number_of_tests, data_size)

    # NOTE - If running tests bellow, check data_structures.py ful for lines to comment/uncomment
    # liststack_df = test_list_stack(number_of_tests, data_size)
    # listqueue_df = test_list_queue(number_of_tests, data_size)

    # liststack_df.to_csv("results/liststack_length.csv")
    # listqueue_df.to_csv("results/listqueue_length.csv")

    print("Completed Testing")


if __name__ == "__main__":
    main()

# !SECTION - main()
