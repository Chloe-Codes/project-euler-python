####################################################
##                                                ##
##  Project Euler Exercise 1 Solution             ##
##  Chloe Dyke 2017                               ##
##                                                ##
##  Solution: 233168                              ##
####################################################

# Find the sum of all the multiples of 3 or 5 below 1000

sum = 0 # initialise multiples

for num in range(1,1000):
    if num % 3 == 0 or num % 5 == 0: # find if number is a multiple of 3 or 5
	    sum += num
		
print (sum)