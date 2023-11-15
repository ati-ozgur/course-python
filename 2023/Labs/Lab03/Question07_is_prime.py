def is_prime(num):
    for divisor in range(2,num):
        if num % divisor == 0:
            return False
    else:
        return True




assert is_prime(20) == False
assert is_prime(19)