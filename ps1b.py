# Jon Formantes
balance = float(input())
annualInterestRate = float(input())
print("Enter the outstanding balance on your credit card: " + balance)

print("Enter the annual credit card interest rates a decimal: " + annualInterestRate)

minMonthPayment = 10
month = 0
updateBalance = balance
monthlyInterestRate = annualInterestRate / 12.0
while month < 12:
    month += 1
    updateBalance = updateBalance * (1 + monthlyInterestRate) - minMonthPayment
    if month == 12 and updateBalance > 0:
        month = 0
        minMonthPayment += 10
        updateBalance = balance
    if updateBalance < 0:
        updateBalance = round(updateBalance, 2)
        break






print("RESULT")
print("Monthly payment to pay off debt in 1 year: " + str(minMonthPayment))
print("Number of months needed: " + str(month))
print("Balance: " + str(updateBalance))
