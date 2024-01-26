#
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

list = [10,501,22,37,100,999,87,351] 

for num in list:
    if is_prime(num):
        print(num,"is a prime number.")
    else:
        print(num,"is not a prime number.")