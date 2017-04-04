####################################################
##                                                ##
##  Project Euler Exercise 2 Solution             ##
##  Chloe Dyke 2017                               ##
##                                                ##
##  Solution: 4613732                             ##
####################################################

# Find the sum of the even-valued terms of fibonacci
# sequence not exceeding 4 million.

# initialise known sequence variables
fib = [1,2]
sum = 2 
max = 4000000 #max fibonacci number allowed

while 1:
    length = len(fib)
    next = fib[length - 1] + fib[length - 2] # next number in sequence sum of two previous numbers
    if next <= max:
        if next % 2 == 0: # if even, add to sum
            sum = sum + next
        fib.append(next)
    else:
        break

print(sum)
    