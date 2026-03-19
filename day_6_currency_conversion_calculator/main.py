#   CURRENCY CONVERSION CALCULATOR
#   LIMITATIONS: not user proof, not updated conversion rate

#   header formatting
space = 60
print()
print("$" * space)
print()
print("Currency Conversion Calculator".center(space))
print()
print("$" * space)
print()
print("Euros to Dollars".center(60))
print()

#   get user input
euro = float(input("Enter Euros (€): "))

#   do the calculation
dollar_conversion_rate = 0.87
dollar = euro * dollar_conversion_rate

#   print the result
print("\nExchange results:")

#   format 1
# print("\nEuro (€): " + f"{euro:,.2f}".rjust(20))
# print("Dollar (€): " + f"{dollar:,.2f}".rjust(20))

#   format 2
print(f"{euro:,.2f}".rjust(15) + " Euro (€)")
print(f"{dollar:,.2f}".rjust(15) + " Dollar ($)")
