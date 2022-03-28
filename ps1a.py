# Jon Formantes


print("Enter the outstanding balance on your credit card: ")
Balance = int(input())
print("Enter the annual credit card interest rates a decimal")
AnnualInterestRate = float(input())
print("Enter the minimum monthly payment rate as a decimal")
MinMonthPaymentRate = float(input())

for month in range(1, 13):
    MinMonthPayment = round(MinMonthPaymentRate * Balance, 2)
    InterestPaid = round(AnnualInterestRate / 12 * Balance, 2)
    PrincipalPaid = round(MinMonthPayment - InterestPaid, 2)
    Balance = round(Balance - PrincipalPaid, 2)
    print("Month: " + str(month))
    print("Minimum monthly payment: " + str(MinMonthPayment))
    print("Principal paid: " + str(PrincipalPaid))
    print("Remaining balance: " + str(Balance))
