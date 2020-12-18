def is_prime(num):
    for index in range(2,num):
        if num % index == 0:
            return False

    return True
    
for num in range(2,21):
    print(num,is_prime(num))

