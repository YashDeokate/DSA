# Write a Python program to find the number of digits in the factorial of a given positive integer n.
# The factorial of a number n is the product of all positive integers from 1 to n.
# Formula:
# n! = 1 × 2 × 3 × ... × n
# Example 1:
# Input: n = 5
# Output: 3
# Explanation: 5! = 120, which contains 3 digits.


def digtFact(n):
    fact=1
    for i in range(1,n+1):
        fact *= i
    return len(str(fact))    
n= int (input("enter a number:")) 
print(digtFact(n))