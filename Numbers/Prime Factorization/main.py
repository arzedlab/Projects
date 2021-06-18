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

if __name__ == '__main__':
    num = int(input('Enter num:'))
    prime_factors(num)