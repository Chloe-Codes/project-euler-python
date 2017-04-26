####################################################
##                                                ##
##  Project Euler Exercise 5 Solution             ##
##  Chloe Dyke 2017                               ##
##                                                ##
##  Solution: 232792560                           ##
####################################################

# Find the smallest positive number that is evenly divisible
# by all of the numbers from 1 to 20.
# To find the SMALLEST divisble, we take out the redundant values and
# use prime factors.
# Find the maximum count of each prime in each set of prime factors
# then multiply them to get a result.

# Function to return the prime factors of a number
def get_prime_factors(number):
    solved = False
    prime_factors = []
    prime = 2 # starting prime
    while(solved == False):
        if is_prime(prime):
            if number % prime == 0: # if number can be divided by smallest prime
                prime_factors.append(prime) # append the prime 
                result = int(number / prime)
                # check if the result is prime, if yes add to list
                if(is_prime(result)):
                    solved = True
                    prime_factors.append(result)
                else:
                    number = result # if not prime, the result becomes the new test number
            else:
                prime += 1
    return prime_factors

# Function that determines whether number is prime
def is_prime(number):
    nums = [x for x in range(2, number-1) if number % x == 0]
    return not nums # if nums has values, it is not prime


prime_factors = []
# Create a list of all the prime factors
for i in range(2, 20):
    if is_prime(i):
        prime_factors.append([i])
    else:
        prime_factors.append(get_prime_factors(i))

# Prime numbers between 1 and 20
primes = [2,3,5,7,11,13,17,19]

final_list = [] # a list of all the factors to be multiplied
# for each prime number, find the max count, and add those factors to the final list
for prime in primes:    
    max_list = []
    max_count = 0
    for i in range(len(prime_factors)):
        if prime_factors[i].count(prime) > max_count:
            max_count = prime_factors[i].count(prime)
            max_list = prime_factors[i]
    final_list.append(max_list)

# Flatten the nested list
flat = [y for x in final_list for y in x]
total = 1
# Calculate the total
for n in flat:
    total *= n

print(total)


