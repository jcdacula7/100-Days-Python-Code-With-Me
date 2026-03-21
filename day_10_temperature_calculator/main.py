#   TEMPERATURE CALCULATOR
#   LIMITATIONS: not user proof

#   header formatting
space = 60
print()
print("#" * space)
print()
print("Temperature Calculator".center(space))
print()
print("#" * space)
print()
print("Enter 1 for Fahrenheit to Celcius".center(60))
print("Enter 2 for Celcius to Fahrenheit".center(60))
print()

#   get user input (choice)
choice = input("What do you choose?: ")
print()

#   calculate temperature depending on the choice
if choice == "1":
    temperature_fahrenheit = float(input("Enter temperature in Fahrenheit (°F): "))
    temperature_celcius = (temperature_fahrenheit - 32) / 1.8
    print(f"The temperature in Celcius: {temperature_celcius:,.2f} °C")
elif choice == "2":
    temperature_celcius = float(input("Enter temeprature in Celcius (°C): "))
    temperature_fahrenheit = (temperature_celcius * 1.8) + 32
    print(f"The temperature in Fahrenheit: {temperature_fahrenheit:,.2f} °F")
else:
    print("Invalid choice. Try again!")
