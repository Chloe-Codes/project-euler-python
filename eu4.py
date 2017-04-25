####################################################
##                                                ##
##  Project Euler Exercise 4 Solution             ##
##  Chloe Dyke 2017                               ##
##                                                ##
##  Solution: 906609                              ##
####################################################

# Find the largest palindrome made from the product of two 3-digit numbers.
from itertools import product
largest_palindrome = 0

# Check if palindrome
def check_palindrome(num):
    str_num = str(num)
    if str_num == str_num[::-1]: # Check if the reversed string is the same as the string
        return True
    else:
        return False

#Tried to find max palindrome in most pythonic way I could
palindromes = [i * j for i in range(999) for j in range(999) if check_palindrome(i*j)]
print(max(palindromes))

