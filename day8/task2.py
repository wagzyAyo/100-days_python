#!/usr/bin/python3
def prime_num(number):
    is_prime = True
    for x in range(2, number - 1):
        if number % x == 0:
            is_prime = False
    if is_prime == True:
        print("Its prime")
    else:
        print("Not a prime number")


prime_num(7)
prime_num(20)
prime_num(67)
