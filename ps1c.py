# Jon Formantes

balance = float(input())
print("Enter the outstanding balance on your credit card: " + str(balance))
annualInterestRate = float(input())
print("Enter the annual credit card interest rate as a decimal: " + str(annualInterestRate))

updateBalance = balance
monthlyInterestRate = annualInterestRate/12
low = balance/12.0
high = (balance * (1 + annualInterestRate/12) **12)/12
epsilon = 0.03

while abs(updateBalance) > epsilon:
    minMonthPayment = (low + high)/2.0
    for i in range(0, 12):
        updateBalance = updateBalance * (1 + monthlyInterestRate) - minMonthPayment
    if updateBalance < -epsilon:
        high = minMonthPayment
        updateBalance = balance
    elif updateBalance > epsilon:
        low = minMonthPayment     
        updateBalance = balance
    else:
        break


print("RESULT")
print("Monthly payment to pay off debt in 1 year: " + str(round(minMonthPayment, 2)))
print("Number of months needed: 12")
print("Balance: " + str(round(updateBalance, 2)))
