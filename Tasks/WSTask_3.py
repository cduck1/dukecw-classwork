import pdb
gallon = 4.546
print("Enter the car mileage from the last time your car was filled.")
mileage1 = int(input())
print("Enter the current car mileage.")
mileage2 = int(input())
milestravelled = mileage2 - mileage1
print("Please enter the total number of litres taken to fill the tank.")
litres = float(input())
gallonsmile = (litres*gallon)/milestravelled 
print("Your car consumes",gallonsmile,"gallons per mile.")

#i) The gallon can be defined as a constant as it never changes. The advantage of doing this is that it is easier to write "gallon" than the number needed in the calculation.
#ii) The mileage can be defined as an integer as the car's mileage only increases by integer values.
#iii) The number of litres needed to fill the tank can be defined as a decimal as the tank will not always take an integer amount of litres to fill.


## ACS - Good however you need to add annotations (comments) to your code so it is clear what the calculations are doing. 
