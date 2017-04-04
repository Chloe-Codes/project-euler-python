####################################################
##                                                ##
##  Project Euler Exercise 3 Solution             ##
##  Chloe Dyke 2017                               ##
##                                                ##
##  Solution: 6857                                ##
####################################################

# Find the largest prime factors of 600851475143
import math

largest = 0
test_number = 600851475143
def isPrime(number):
    prime = True
    for num in range(2, number - 1):
        if number % num == 0:
            prime = False
            break
    return prime
	
for num in range(2, int(math.sqrt(test_number))): # only test to the sqrt, as one factor must be smaller than it
    if test_number % num == 0 and isPrime(num):
        if num > largest:
            largest = num

print (largest)