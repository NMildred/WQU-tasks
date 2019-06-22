import math
from math import sqrt
def is_prime_fast(number):
    if number <= 1:
        return False
    elif number % 2 == 0:
        if number == 2:
            return True
        else:
            return False
    for factor in range (2, (int(sqrt(number)))+1):
        if number % factor == 0:
            return False
        
    return True
        
list_of_numbers = list (range(0, 65))
get_primes_fast_list = []            
for number in list_of_numbers:
    if is_prime_fast(number):
        get_primes_fast_list.append(number)
get_primes_fast_list
