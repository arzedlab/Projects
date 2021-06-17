from math import factorial as fac

from decimal import Decimal , getcontext

getcontext().prec = 1000


# We will use Chudnovsky algorithm to find N-th of PI number. https://handwiki.org/wiki/Chudnovsky_algorithm
input_num = int(input())

def nth_pi(nth : int) -> float:
    pi = Decimal(0)
    num = Decimal(0)
    den = Decimal(0)
    for k in range(nth):
        num = (-1) ** k * fac(6*k) * (545140134*k + 13591409)
        den = fac(3*k) * fac(k) ** 3 * 640320 ** (3*k) # If we put 3*k + 3/2 will be OverflowError
        pi += Decimal(num) / Decimal(den)
    pi = pi * Decimal(12) / Decimal(640320 ** Decimal(1.5)) # Added here
    pi = 1/pi
    
    return round(pi,nth)


if __name__ == "__main__":
    print(nth_pi(input_num))
