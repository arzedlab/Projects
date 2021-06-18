# Next prime number

def next_prime(n):
    prime = False
    while prime == False:
        prime = True
        n += 1
        for i in range(2,n):
            if (n % i == 0):
                prime = False
        if prime == True:
            return n

if __name__ == '__main__':
    num = int(input())
    print(next_prime(num))
