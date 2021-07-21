"""
CSC 506 CT 6 Option 1 - Binary Search Tree
Created July 12th, 2021
Due July 18th, 2021

Asignment Prompt
----------------
You'll build a simple binary search tree in this activity.
    - Build a Node class. It is should have attributes for the data it stores as well as its left and right children. 
      As a bonus, try including the Comparable module and make nodes compare using their data attribute.
    - Build a Tree class which accepts an array when initialized. The Tree class should have a root attribute which uses 
      the return value of #build_tree which you'll write next.
    - Write a #build_tree method which takes an array of data (e.g. [1, 7, 4, 23, 8, 9, 4, 3, 5, 7, 9, 67, 6345, 324]) 
      and turns it into a balanced binary tree full of Node objects appropriately placed (don't forget to sort and remove 
      duplicates!). The #build_tree method should return the level-1 root node.
    - Write an #insert and #delete method which accepts a value to insert/delete.

File Description
----------------
bst.py contains code for both a Node and BST class. A Node contains everything needed for a standard BST implementation 
and it also tracks the parent node (as is common in an AVL implementation) and the count of each value which helps track
duplicates in the case the number of occurences of a specific datum is needed. The assignment operators are also overloaded
to allow for easy comparisons.

The BST is a standard implementation of a binary search tree with the init method ensuring a balanced tree is built.

Comment Anchors
---------------
I am using the Comment Anchors extension for Visual Studio Code which utilizes specific keywords
to allow for quick navigation around the file by creating sections and anchor points. Any use
of "anchor", "todo", "fixme", "stub", "note", "review", "section", "class", "function", and "link" are used in conjunction with 
this extension. To trigger these keywords, they must be typed in all caps. 
"""

from collections import Counter
from os import system, name

class Node():
    '''
    A Node stores a value and tracks left, right, and parent pointers for use within a tree. The count (number of occurences)
    of a specific value can also be tracked to avoid duplicates in the BST while maintaining integrity of original dataset.
    '''

    def __init__(self, value = None, count = None) -> None:
        ''' Initializes a Node and can accept a value and count at time of instantiation'''
        self.value = value
        self.count = count if count != None else 1
        self.parent : Node = None
        self.left : Node = None
        self.right : Node = None

    # ** Overloaded Comparison Operators **

    def __eq__(self, other: object) -> bool:
        if other == None:
            return False
        return True if self.value == other.value else False

    def __gt__(self, other: object) -> bool:
        if other == None:
            return False
        return True if self.value > other.value else False

    def __lt__(self, other: object) -> bool:
        if other == None:
            return False
        return True if self.value < other.value else False

class BST():
    '''
    A BST is a binary search tree which allows for insertion, deletions, searches, and in/pre/post order traversal. 
    A balanced tree is created during the initial instantiation if an array of values is provided. No guarantee of 
    balance is provided beyond that point.
    '''

    def __init__(self, values = None) -> None:
        
        if values == None:
            self.root = None
        else:
            self.root = self._buildTree(values)

    def _buildTree(self, values) -> Node:
        '''Constructs a balanced BST and returns the root node'''

        # Exit if no provided values
        if values == None:
            return None

        # Get Count of Items where each item is the key
        counts = dict(Counter(values))

        # Ensure array is sorted and remove duplicates
        sortedValues = sorted(set(values))

        # Build the balanced tree
        return self._buildBalancedTree(sortedValues, counts)
    
    def _buildBalancedTree(self, values, counts) -> Node:
        '''Helper function to recursively construct balanced tree in _buildTree method'''

        # Check to make sure there are values to add
        if values == None or len(values) == 0:
            return None
        
        # Calculate Midpoint
        mid = len(values) // 2

        # Create Node
        newNode = Node(values[mid], counts[values[mid]])

        # Base Case
        if mid == 0:
            return newNode

        # Recursive Left
        newNode.left = self._buildBalancedTree(values[:mid], counts)
        if newNode.left != None:
            newNode.left.parent = newNode

        # Recursive Right
        newNode.right = self._buildBalancedTree(values[mid+1:], counts)
        if newNode.right != None:
            newNode.right.parent = newNode

        return newNode
         
    def inOrderPrint(self):
        '''Prints the contents of the BST using an in-order traversal'''
        self._inOrderTraversal(self.root)
        print()

    def preOrderPrint(self):
        '''Prints the contents of the BST using a pre-order traversal'''
        self._preOrderTraversal(self.root)
        print()

    def postOrderPrint(self):
        '''Print the contents of the BST using a post-order traversal'''
        self._postOrderTraversal(self.root)
        print()

    def _inOrderTraversal(self, node: Node):

        if node == None:
            return

        # Traverse Left Subtree
        self._inOrderTraversal(node.left)

        # Print
        print(f"{node.value}:{node.count}  ", end='')

        # Traverse Right Subtree
        self._inOrderTraversal(node.right)

    def _preOrderTraversal(self, node: Node):
        
        if node == None:
            return

        # Print
        print(f"{node.value}:{node.count}  ", end='')

        # Traverse Left Subtree
        self._preOrderTraversal(node.left)

        # Traverse Right Subtree
        self._preOrderTraversal(node.right)

    def _postOrderTraversal(self, node: Node):
        
        if node == None:
            return

        # Traverse Left Subtree
        self._postOrderTraversal(node.left)

        # Traverse Right Subtree
        self._postOrderTraversal(node.right)

        # Print
        print(f"{node.value}:{node.count}  ", end='')

    def insert(self, value):
        '''Takes a value and inserts it into the BST'''

        # Ensure a value was provided
        if value == None:
            print("Cannot insert a lack of a value!")
            return

        newNode = Node(value)

        # Find insert spot
        curNode = self.root

        while True:
            
            # Check if smaller than current node
            if newNode < curNode:
                if curNode.left == None:
                    curNode.left = newNode
                    newNode.parent = curNode
                    break
                curNode = curNode.left
            
            # Check if larger than current node
            elif newNode > curNode:
                if curNode.right == None:
                    curNode.right = newNode
                    newNode.parent = curNode
                    break
                curNode = curNode.right
            
            # Update count if value already exists
            elif newNode == curNode:
                curNode.count += 1
                break

        return   

    def delete(self, value, all = False):
        '''
        Searches for a specified value and removes it from the tree.
        
        If the flag all is set to true, it will remove all instances of a data value, otherwise count will
        be decremented by 1 until no more exist in the structure at whihc point the node will be removed. 
        '''

        # Ensure a value was passed
        if value == None:
            print("Unable to delete a null value")
            return

        curNode = self.root

        # Search for the node with the specified value
        while curNode != None and curNode.value != value:
            curNode = curNode.left if value < curNode.value else curNode.right

        if curNode != None:
            # Determine if decrement or replacement
            if all == False and curNode.count != 1:
                curNode.count = curNode.count - 1
                print(f"Removed 1 cound of {value} from the BST: {curNode.count} remain")
                return

            # Handle three cases of deletion

            # Case: Leaf Node
            if curNode.left == None and curNode.right == None:
                if curNode is self.root:
                    self.root = None
                else:
                    if curNode.parent.left is curNode:
                        curNode.parent.left = None
                    else:
                        curNode.parent.right = None

            # Case: Two Children
            elif curNode.left != None and curNode.right != None:

                # Search for Successor Node
                successor = curNode.right

                while successor.left != None:
                    successor = successor.left

                # Case: No Child -> Copy
                if successor.left == None and successor.right == None:
                    if curNode.right is successor:
                        curNode.right = None
                    else:
                        successor.parent.left = None

                # Case: 1 Child (Right) -> Replace and Copy
                else:
                    successor.right.parent = successor.parent

                    if curNode.right is successor:
                        curNode.right = successor.right
                    else:
                        successor.parent.left = successor.right

                # Copy the successor node into the correct spot
                

                if curNode is self.root:
                    successor.left = self.root.left
                    successor.right = self.root.right
                    successor.parent = None
                    self.root = successor
                else:
                    successor.parent, successor.left, successor.right, curNode.parent.right = curNode.parent, curNode.left, curNode.right, successor
                    

            # Case: Single Child
            else:
                replacement = curNode.left if curNode.left != None else curNode.right

                if curNode is self.root:
                    self.root = replacement
                    replacement.parent = None
                else:
                    if curNode.parent.left is curNode:
                        curNode.parent.left = replacement
                    else:
                        curNode.parent.right = replacement

                    replacement.parent = curNode.parent

            return

        # Exit since no value was found
        print(f"Unable to find {value} in the BST")
        return

def clearTerminal():
    """Clears the terminal of all text on Windows/MacOs/Linux"""
    
    # For windows
    if name == 'nt':
        _ = system('cls')
    # Mac and linux 
    else:
        _ = system('clear')

if __name__ == "__main__":

    clearTerminal()
    print("Constructing initial BST with value [10, 5, -6, 8, 123, 9, 5, 7, -123, 6, -3]")
    tree = BST([10, 5, -6, 8, 123, 9, 5, 7, -123, 6, -3])
    print("Press enter to continue")
    input()


    loop = True
    while loop:
        clearTerminal()
        print("CSC 506 Critical Thinking 6 - Binary Search Trees")
        print("i: Insert\nd: Delete\npr: Pre-Order Print\npi: In-Order Print\npo: Post-Order Print\ne: Exit\n", end=">> ")
        userInput = input()

        if userInput == "i":
            print("What value would you like to add? >> ", end='')
            try:
                ui = input()
                value = int(ui)
                tree.insert(value)
            except:
                print(f"Illegal value {ui}")
                print("Press enter to continue")
                input()
            
        elif userInput == "d":
            print("What value would you like to delete? >> ", end='')
            ui = input()
            print("Would you like to delete all counts? (y or n) >> ", end='')
            yn = input()

            try: 
                value = int(ui)
                all = True if yn == 'y' else False
                tree.delete(value, all)
            except:
                print(f"Illegal value {ui}")
                print("Press enter to continue")
                input()

        elif userInput == "pr":
            tree.preOrderPrint()
            print("Press enter to continue")
            input()
        elif userInput == "pi":
            tree.inOrderPrint()
            print("Press enter to continue")
            input()
        elif userInput == "po":
            tree.postOrderPrint()
            print("Press enter to continue")
            input()
        elif userInput == "e":
            print("Have a nice day")
            loop = False
        else:
            clearTerminal()
  