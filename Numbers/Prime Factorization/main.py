# Prime factors
import math
 
# A function to print all prime factors of
# a given number n
def prime_factors(n):
    while n % 2 == 0:
        print(2)
        n = n/2
    
    for i in range(3,int(math.sqrt(n)),2):
        while n % i == 0:
            print(i)
            n = n/i
    
    if n > 2:
        print(n)

def prime_factors_list(n):
    out = list()
    for num in range(1, n+1):
        prime = True
        for i in range(2, num):
            if (num % i == 0):
                prime = False
        if prime:
            out.append(num)
    return out

if __name__ == '__main__':
    num = int(input('Enter num:'))
    # prime_factors(num)
    list = prime_factors_list(num)
    for element in list:
        print(element)