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

#i) the gallon can be defined as a constant so that it can be easier to write than the number needed in a calculation
#ii)the miles can be integers as the car's mileage only increases by integer values
#iii) the number of litres needed to fill the tank can be a decimal as the tank is not always going to take an integer amount of litres to fill.
