def is_prime(number):
    for factor in range (2, number):
        if number%factor==0:
            return False
        
    return True

list_of_numbers = list (range (3,65))
prime_list =[]
for number in list_of_numbers:
    if is_prime (number):
        prime_list.append (number)
prime_list
