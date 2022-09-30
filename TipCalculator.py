# Ask the user for the charge
charge=float(input("What is the charge? "))

# Calculate the tip for 18%
tip=0.18*charge

# Calculate the tax for 7%
tax=round(0.07*charge, 2)

#Calculate Total
total=charge+tip+tax

#Display each amount and total
print(f'Tip is ${tip}\n')

print(f'Sales Tax is ${tax}\n')

print(f'Grand Total is ${total}\n')