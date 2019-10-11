import time

def is_prime(number):
    if number < 2:
        return False
    elif number is 2:
        return True
    else:
        for i in range(2, number):
            if number % i is 0:
                return False
        return True

for i in range(100):
    if is_prime(i):
        for value in range(i):
            print(str(i))
            time.sleep(1.3)
            print()
