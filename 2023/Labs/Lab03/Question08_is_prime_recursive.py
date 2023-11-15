
memorization_dict = {}

def is_prime_recurive(divisor,num):
    if num in memorization_dict:
        return memorization_dict[num]

    if divisor == num:
        memorization_dict[num] = True
        return True
    else:
        if num % divisor == 0:
            memorization_dict[num] = False
            return False
        else:
            divisor = divisor + 1
            return is_prime_recurive(divisor,num)

def is_prime(num):
    return is_prime_recurive(2,num)



assert is_prime(20) == False
assert is_prime(19)

assert is_prime(23)
