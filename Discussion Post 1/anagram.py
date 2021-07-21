# CSC506 Discussion Post 1
# Created by Karl Estes
# Created: Wednesday, June 9th, 2021

# Requirement for Discussion Post 1 was to design an algorithm to check whether two words were anagrams
# of one another. That is, can one word be created by a permutation of all the letters of the second word

# I am using the Comment Anchors extension for Visual Studio Code which utilizes specific keywords
# to allow for quick navigation around the file by creating sections and anchor points. Any use
# of "ANCHOR", "TODO", "FIXME", "STUB", "NOTE", "REVIEW", "SECTION", and "LINK" are used in conjunction with 
# this extension

import numpy as np

def isAnagram(w1, w2):
    '''
    Description: Takes two words and determines if they are anagrams

    Stipulations: Only alpha characters will be considered, and capitalization will be disregarded 

    Return: true if the words are anagrams and false if they are not
    '''

    w1_count = [0] * 26
    w2_count = [0] * 26

    if not w1.isalpha() or not w2.isalpha():
        print("isAnagram() only supports alpha characters")
        return False

    for c1,c2 in zip(w1.lower(),w2.lower()):
        w1_count[ord('a') - ord(c1)] += 1
        w2_count[ord('a') - ord(c2)] += 1

    return np.array_equal(w1_count, w2_count)


if __name__ == "__main__":

    w1 = "Test"
    w2 = "yest"

    result = isAnagram(w1, w2)

    print(result)
