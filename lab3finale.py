#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jesus Maximino Hernandez
CS 2302 Data Structures - Diego Aguirre
TA - Manoj Saha
Lab 3 - Option B 
Program that sorts english words into a Binary Search Tree and has 
differnt functions with Anagrams
"""
from AVLNode import AVLNode 
from AVLTree import AVLTree 
from RBTree import RBTree
from RBTNode import RBTNode 

fileName = "words.txt"
testFile = "testW.txt"

def main():
    #make sure input is valid
    valid = False
    while(valid == False):
        print("What type of Binary Tree? ")
        answer = input("Enter 'A' for AVL Tree or 'B' for Red-Black Tree: ")
        answer = answer.lower()
        
        if (answer != 'a' and answer != 'b'):
            valid = False
            print("Error")
        else:
            valid = True
    
        if(answer == 'a'):
            print("You have selected AVL Tree, AVL Tree now loading...")
            AVL(fileName)           
            print("Finished")
            valid = True
            
        else:
            print("You have selected Red-Black Tree, RB Tree now loading...")
            RBT(fileName)
            print("Finished")
            valid = True
        
    #Test functionality of other functions.
#    test()
    
def test():
    print()
    testWord = "spot"
    print("Here is a list of " + testWord + "'s anagrams:")
    print_anagrams(testWord)
    print("The amount of anagrams this word has: " , count_anagrams("spot")) #should print out six
    print("Word with most anagrams: " + get_largest(testFile),"-",count_anagrams(get_largest(testFile)))
      
def engish_word(word):
    
    avlTree = AVLTree()
    #opens file and puts into tree
    with open(testFile) as f: #change file to testFile when you want to test

        for line in f:
             if "\n" in line:
                 line = line.replace("\n", "")
             lowerCase = (line.lower()) #this line makes every word a lower case
             node = AVLNode(lowerCase)
             avlTree.insert(node)

    if avlTree.search(word):
        #print("FOUND")
        return True
    else:
        #print("NOT FOUND")
        return False
#function to return the word with the most amount of anagrams
def get_largest(file_name):
    counter = 0
    with open(file_name) as f:
        for line in f:
            line = line.replace("\n", "")
            cur = count_anagrams(line)
            if cur > counter:
                counter = cur 
                large = line
        return large
#counts the number of anagrams a word has
def count_anagrams(word, prefix=""):

    if len(word) <= 1:
        str = prefix + word
        #adds one to count when an anagram is a word
        if engish_word(str): 
            return 1
        return 0
    else:
        count = 0
        for i in range(len(word)):
          cur = word[i: i + 1]
          before = word[0: i] 
          after = word[i + 1:] 
          if cur not in before: 
            count += count_anagrams(before + after, prefix + cur)
        return count
      
#function to print anagrams of a word
def print_anagrams(word, prefix=""): 

    if len(word) <= 1:
        str = prefix + word
        if engish_word(str): 
            print(prefix + word)
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i] # letters before cur 
            after = word[i + 1:] # letters after cur
            
            if cur not in before: # Check if permutations of cur have not been generated. 
                print_anagrams(before + after, prefix + cur)
#function to put words into an AVL tree                
def AVL(fileName):
    avlTree = AVLTree()
    #opens file and puts into tree
    with open(fileName) as f:

        for line in f:
             if "\n" in line:
                 line = line.replace("\n", "")
             lowerCase = (line.lower()) #this line makes every word a lower case
             node = AVLNode(lowerCase)
             avlTree.insert(node)

        return avlTree
#function to put words into a Red and Black tree
def RBT(fileName):
    rbtTree = RBTree()
    with open(fileName) as f:
        for line in f:
             if "\n" in line:
                 line = line.replace("\n", "")
             node = (line.lower()) #this line makes every word a lower case
             rbtTree.insert(node)

    return rbtTree

main()
