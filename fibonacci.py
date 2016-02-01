#!/usr/bin/python

# Task: Fibonacci numbers module
#
# Description: the Fibonacci numbers or Fibonacci sequence are the numbers in 
# the following integer sequence: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,...
# By definition, the first two numbers in the Fibonacci sequence are either 1 and 1, 
# or 0 and 1, depending on the chosen starting point of the sequence, and each 
# subsequent number is the sum of the previous two.
#
# Run: python fibonacci.py

# Implementation
def show_numbers(n):
  a, b = 0, 1
  while b < n: 
    print b, 
    a, b = b, a+b
  print
  
def show_array(n): 
  result = []
  a, b = 0, 1
  while b < n:
    result.append(b)
    a, b = b, a+b
  print result  

# Execution
show_numbers(200)
# Result: 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987

show_array(100)
# Result: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
