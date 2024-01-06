import os

path = os.getcwd()

print(path)
# /Users/mbp/Documents/my-project/python-snippets/notebook

print(type(path))
# <class 'str'>


# Using readlines()
file1 = open('example_input.txt', 'r')
Lines = file1.readlines()