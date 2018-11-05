#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 19:38:45 2018

@author: JesusMHernandez
"""
from AVLNode import AVLNode 
from AVLTree import AVLTree 
from RBTree import RBTree
from RBTNode import RBTNode 

engish_words = None
fileName = "testW.txt"

def main():

    global engish_words
    valid = False
#    print(count_anagrams("max"))
#    print(print_anagrams("max"))
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
        print("you have selected AVL Tree")
        engish_words = AVL()
       
    else:
        print("You have selected Red-Black Tree")
        engish_words = RBT()
#    tree = AVL()
    
#    engish_word(tree)
def engish_word(word):
    avlTree = AVLTree()
    #opens file and puts into tree
    with open(fileName) as f:

        for line in f:
             node = (line.lower()) #this line makes every word a lower case
             node = AVLNode(lowerCase)
             avlTree.insert(node)
    avlTree.search("Max")
def find_largest(file):
    count = 0
    with open(fileName) as f:
        for line in f:
            temp = count_anagrams(line)
            if temp > count:
                count = temp 
                largest = line
        return largest
 
def count_anagrams(word, prefix=""):

    if len(word) <= 1:
        str = prefix + word
        if engish_words(str): 
            return 1
        return 0
        print(prefix + word)
    else:
        count = 0
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i] # letters before cur 
            after = word[i + 1:] # letters after cur
            if cur not in before: # Check if permutations of cur have not been generated. 
                count += count_anagrams(before + after, prefix + cur)
        return count
  
#function to print anagrams of a word
def print_anagrams(word, prefix=""): 
    if len(word) <= 1:
        str = prefix + word
    if engish_words("Max"): 
        print(prefix + word)
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i] # letters before cur 
            after = word[i + 1:] # letters after cur
            if cur not in before: # Check if permutations of cur have not been generated. 
                print_anagrams(before + after, prefix + cur)
def AVL():
    avlTree = AVLTree()
    #opens file and puts into tree
    with open(fileName) as f:

        for line in f:
             node = (line.lower()) #this line makes every word a lower case
             node = AVLNode(lowerCase)
             avlTree.insert(node)

        return avlTree

def RBT():
    rbtTree = RBTree()
    with open(fileName) as f:
        for line in f:
             node = (line.lower()) #this line makes every word a lower case
             rbtTree.insert(node)

    return rbtTree
'''  
class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.count = 0
'''
main()
