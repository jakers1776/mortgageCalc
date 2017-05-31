#Mortgage Calculator
"""
    Tell the program the mortgage term in months,
    the percentage of the rate, and the amount of the loan
    and it will give you the monthly payment.
"""
MortTermLength = ''

while MortTermLength != 'a' or MortTermLength != 'b':
    MortTermLength = raw_input("What is the term of your fixed-rate mortgage?\na)30 years\nb)15 years\n")
    if MortTermLength == 'a':
        MortMonths = int(360)
        break
    if MortTermLength == 'b':
        MortMonths = int(180)
        break
    else:
        "Please enter 'a' or 'b' for the question asked."

MortRate = float(raw_input("What is the interest rate percentage of your mortgage?\n"))
MortValue = float(raw_input("What is the loan value of your mortgage?\n"))

MortMonthlyRate = MortRate / 100 / 12
MortMonthlyPay = (MortMonthlyRate / (1 - (1 + MortMonthlyRate)**(-MortMonths))) * MortValue

print "Your monthly payment for your mortgage worth $%.2f over a %s year span at an interest rate of %.2f%% is: $%.2f" % (MortValue, (MortMonths / 12), MortRate, MortMonthlyPay)
