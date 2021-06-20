# Mortgage Calculator


                             
def paidEveryMonth(interestRate, months, borrowed):             
    return (borrowed * true_rate * ((true_rate + 1)**months)) / ((true_rate + 1)**months - 1)#Mortgage formula
def totalSumm(total_pem):                                       # Total amount of payments
    return round((total_pem * months), 2)
def totalInterest(totalSumm):                                   # total interest = Total amount of payments - Loan amount
    return round((totalSumm - borrowed), 2)

def fullReport(total_pem, borrowed):
    print("******************************************")
    print("MONTH -> P&I   " + "= PRINCIPAL + INTEREST| PRINCIPAL REMAINING")
    fmt = '{0:2d} -> {4:8.2f} = {1:8.2f} + {2:8.2f} | {3:8.2f}' 
    for index in range(1, months + 1):                          
        interest = borrowed * interestRate / 12                 
        principal = total_pem - interest                   
        borrowed -= principal                        
        print(fmt.format(index, principal, interest, borrowed, total_pem))



if __name__ == '__main__':
    years =  int(input("Loan program in years: "))
    borrowed = int(input("Loan amount: "))
    interestRate = float(input("Interest Rate: "))

    months = years * 12
    true_rate = interestRate / 12   
    
    print("******************************************")
    print("Loan amout:%7.2f"%borrowed)
    print(f"Loan duration in months: {months}")
    print(f"Annunal Interest rate in percent: {interestRate*100}")

    tmp = paidEveryMonth(interestRate, months, borrowed)
    print("Total Monthly Payment:%7.2f"%tmp)
    print(f"Total of {months} payments: {totalSumm(tmp)}")
    print(f"Over {months} months you will spend: {totalInterest(totalSumm(tmp))} in interest")
    wantFullReport = input("Do you want to make full report? (y/n) ")
    if wantFullReport == "y":
        fullReport(tmp, borrowed)