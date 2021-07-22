# CSC 506 - Design and Analysis of Algorithms

**Disclaimer:** These projects were built as a requirement for CSC 506: Design and Analysis of Algorithms at Colorado State University Global under the instruction of Dr. Pubali Banerjee. Unless otherwise noted, all programs were created to adhere to explicit guidelines as outlined in the assignment requirements I was given. Descriptions of each [programming assignment](#programming-assignments) and the [portfolio project](#portfolio-project) can be found below.

*****This repository is actively being updated and will be archived upon my completion of the class*****
___

### Languages and Tools
<!--TODO add links to each icons site-->
<img align="left" height="32" width="32" src="https://cdn.svgporn.com/logos/python.svg" />
<img align="left" height="32" width="32" src="https://cdn.svgporn.com/logos/github-octocat.svg" />
<img align="left" height="32" width="32" src="https://www.psych.mcgill.ca/labs/mogillab/anaconda2/lib/python2.7/site-packages/anaconda_navigator/static/images/anaconda-icon-512x512.png" />
<img align="left" height="32" width="32" src="https://cdn.svgporn.com/logos/visual-studio-code.svg" />
<img align="left" height="32" width="32" src="https://cdn.svgporn.com/logos/git-icon.svg" />
<img align="left" height="32" width="32" src="https://cdn.svgporn.com/logos/gitkraken.svg" />
<br />

### Textbook
The textbook for this class is Data Structures Essentials: Psueodocde with Python Examples by Roman Lysecky and Frank Vahid. The textbook was accessed and delivered through [ZyBooks](https://zybooks.com). 
<br />

### VS Code Comment Anchors Extension
I am utilizing the [Comment Anchors extension](https://marketplace.visualstudio.com/items?itemName=ExodiusStudios.comment-anchors) for Visual Studio Code which places anchors within comments to allow for easy navigation and the ability to track TODO's, code reviews, etc. 

A few custom anchors were added for project planning and issue tracking which include CLASS, CELL, and FUNCTION.
<br />

___
<!--When doing relative paths, if a file or dir name has a space, use %20 in place of the space-->
## Programming Assignments

### Discussion Post 1: [Anagrams](Discussion%20Post%201/)
- A simple script for determinging if two words are anagrams of one another
### Critical Thinking 1: [Permutations of a List of Digits](Critical%20Thinking%201/)
- Two approaches were taken to solve the problem of computing all possible increasing permutations of a list of digits:
    - The brute force approach tackled the problem by imcrementing the total value of the list of digits by one and checking if the new total value was a permutation of the original list of digits
    - The refined approach performed an inplace swap algorithm to guarantee the next largest permutation is found without the need to check values that are not possible permutations
### Discussion Post 3: [Quicksort Analysis](Discussion%20Post%203/)
- A look at quicksort and a modified quicksort which utilizes a *partition limit* for using insertion sort. With lists of small enough size, insertion sort can have a faster real-world runtime since it does not have to handle overhead from recursive function calls. 

### Critical Thinking 3: [Sorting Algorithm Comparison](Critical%20Thinking%203/)
- This assignment required the comparison of the speed various sorting algorithms when sorting a list of randomly generated integers. The sorting algorithms compared were:
    - Insertion Sort
    - Selection Sort
    - Quicksort
    - Hybrid Quicksort
    - Merge Sort
    - Shell Sort
    - Radix Sort

### Critical Thinking 4: [List Based Stacks and Queues](Critical%20Thinking%204/)
- Both stack and queue operations were compared based on two implementations. One had a Python list behind the scene while the other had a linked-list based implementation. Results were gathered for inserting and removing items and calculating the length of the data structure. 

### Critical Thinking 6: [Binary Search Tree](Critical%20Thinking%206/)
- A simple binary search tree was constructred for this assignment. The tree is able to construct itself in a balanced manner when an array of data is provided to the initialization function. Otherwise it can handle insertions and removals, but it does not guarantee maintenance of balance on these operations. 
___
## Portfolio Project: [Analysis of Algorithms and Data Structures](Portfolio%20Project/)
The porfolio project for this class presented two options: The analysis of algorithms and data structures or the creation and analysis of retroactive search trees. I chose to go with first option and compare the efficiency of various list implementations in an arbitrarily created problem. 

**Designed Problem** - There exists a pile of books and a series of bookshelves. The books must be placed on the bookshelves following a particular sorting schema, but each shelf can only hold a certain number of books. The books must be placed in sorted order without exceeding the limits of the shelves, and once placed, books will be added and removed. Each addition and removal will result in the books automatically adjusting themselves so no gap is left in the assortment and so no shelf is overcapacity. If a previous shelf has room, all the books should be shifted until only the last shelf containing books has accumulated any extra space within the system. The underlying data structure for the shelf storage is currently unknown, and the tradeoffs of various solutions should be explored.

The project will asses the efficiency of list operations with the following implementations:
- A Python List
- A Numpy Array
- A Linked List
- A Linked List with an AVL Search Tree

*Note: This project is ongoing and will be completed by August 1st, 2021. Since this project is ongoing, the exact implementations and operations examined are subject to change.*