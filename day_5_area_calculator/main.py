#   AREA CALCULATOR
#   LIMITATIONS: not user proof

space = 60
print()
print("*" * space)
print("Area Calculator".center(space))
print("*" * space)
print("Enter the height and width, and I will tell you the area.".center(60))
print("")
height = float(input("Enter height (cm): "))
width = float(input("Enter width (cm): "))
area = width * height
print(f"Area: {area} cm²")
