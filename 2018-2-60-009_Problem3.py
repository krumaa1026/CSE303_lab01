def compound_interest_2018_2_60_073(P, R , T):
    A = P * (1 + (R/100)) ** T
    return A

P = int(input("Enter principle amount: "))
R = int(input("Enter interest rate: "))
T = int(input("Enter time: "))
print(compound_interest_2018_2_60_073(P, R , T))