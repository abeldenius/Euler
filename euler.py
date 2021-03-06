# ----------- Multiples of 3 and 5 -----------------

# If we list all the natural numbers below 10 that are multiples of 3 or 5,
#  we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
""" 
import time 

start_time = time.time()

sum_multiples = 0
for _ in range(0, 1000):
    if ((_ % 3 == 0) or (_ % 5 == 0)):
        sum_multiples += _

print(sum_multiples)
print(time.time() - start_time)


 """
# ---------------- Even Fibonacci numbers --------------

# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values
# do not exceed four million, find the sum of the even-valued terms.

""" 

start_time = time.time()
def fibonacci(n):
    if (n <=0):
        return 0
    elif (n == 1):
        return 1
    elif (n == 2):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibo_list = list()
for _ in range(0, 35):
    fibo_list.append(fibonacci(_))

print(sum(fibo_list[0::3]))
print(time.time() - start_time)

 """


# ----------------------------------- Largest prime factor ----------------------------------------------

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

# import time 
# import math

# start_time = time.time()
# def maxPrimeFactor(n):
#    # number must be even
#    while n % 2 == 0:
#       max_Prime = 2
#       n /= 1
#    # number must be odd
#    for i in range(3, int(math.sqrt(n)) + 1, 2):
#       while n % i == 0:
#          max_Prime = i
#          n = n / i
#    # prime number greator than two
#    if n > 2:
#       max_Prime = n
#    return int(max_Prime)
# # Driver code to test above function
# print(maxPrimeFactor(600851475143))
# print(time.time()-start_time)