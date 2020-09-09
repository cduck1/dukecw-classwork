import pdb
print("Enter the height of the walls.")
height = int(input())
print("Enter the length of one wall.")
width = int(input())
print("Enter the length of the other wall.")
length = int(input())
totaldimensions = (2*(height*width))+(width*length)+(2*(height*length))
print("Now enter the total dimensions of the unpaintable areas.")
unpaintdimensions = int(input())
print("Now enter how many layers of paint you would like.")
layers = int(input())
paintneeded = ((totaldimensions - unpaintdimensions)*layers)/11
print("You need", paintneeded,"litres of paint.")

