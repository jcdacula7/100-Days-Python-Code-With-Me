#   MORTGAGE PAYMENT CALCULATOR
#   LIMITATIONS: not user proof

#   welcome the user with header formatting
space = 60
print()
print("=" * space)
print()
print("Mortgage Payment Calculator".center(space))
print()
print("=" * space)
print()


#   get user loan amount
loan_amount = float(input("Enter loan amount ($): "))

#   annual interest rate
annual_interest_rate = int(input("Enter annual interest rate (%): "))

#   number of years for the loan
loan_years = int(input("Enter number of years for the loan: "))

#   number of annual payments
annual_payments = int(input("Number of payments per year: "))

#   calculate monthly interest rate
monthly_interest_rate = (annual_interest_rate / 100) / annual_payments

#   calculate total number of payments
total_number_payments = loan_years * annual_payments

#   calculate repeated section (1+r)² payments
repeated_section = (1 + monthly_interest_rate) ** total_number_payments

#   do the final calculation
monthly_pay = (loan_amount * monthly_interest_rate * repeated_section) / (
    repeated_section - 1
)

#   total amount payed
total_amount_payed = total_number_payments * monthly_pay


#   print results - format 1
# print("\nMonthly Payment".ljust(30, ".") + f"$ {monthly_pay:,.2f}".rjust(30, "."))
# print("Loan Amount".ljust(30, ".") + f"$ {loan_amount:,.2f}".rjust(30, "."))
# print("Total Payed".ljust(30, ".") + f"$ {total_amount_payed:,.2f}".rjust(30, "."))


#   print results - format 2
print()
print(f"{'Monthly Payment':.<30}{f'$ {monthly_pay:,.2f}':.>30}")
print(f"{'Loan Amount':.<30}{f'$ {loan_amount:,.2f}':.>30}")
print(f"{'Total Payed':.<30}{f'$ {total_amount_payed:,.2f}':.>30}")
