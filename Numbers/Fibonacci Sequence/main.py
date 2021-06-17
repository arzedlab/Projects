#Fibonacci Sequence

def fibonacci_seq(nterms):
    n1, n2 = 0, 1
    count = 0
    if nterms <= 0 and nterms == 1:
        print("Please enter a positive integer and bigger than 1.")
    else:
        
        print("Fibonacci sequence:")
        while count < nterms:
            print(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1

if __name__ ==  '__main__':
    nth = int(input("Number of Fibonacci Sequence: "))
    fibonacci_seq(nth)

    
