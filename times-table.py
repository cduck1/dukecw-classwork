#create a program that asks for the user

timestable = int(input("What times table (1-20)?"))
strtimestable = str(timestable)
while (timestable <= 1) and (timestable >= 20):
    timestable = int(input("The times table must be between 1 and 20, please re-enter your times table."))
#endwhile

cont = str(input("Did you mean ", strtimestable , " (Y/ N)?"))
lowercont = cont.lower()
while lowercont == "n":
    timestable = int(input("The times table must be between 1 and 20, please re-enter your times table."))
    cont = str(input("Did you mean ", strtimestable ," (Y/ N)?"))
    lowercont = cont.lower()
#endwhile
    
tablenumber = int(input("What table number (number of rows)(1-20)?"))
while (tablenumber <=1) and (tablenumber >= 20):
    tablenumber = int(input("The table number must be between 1 and 20, please re enter the table number."))
#endwhile

cont = str(input("Did you mean ", strtablenumber , " (Y/ N)?"))
lowercont = cont.lower()
while lowercont == "n":
    tablenumber = int(input("The times table must be between 1 and 20, please re-enter your times table."))
    cont = str(input("Did you mean ", strtablenumber ," (Y/ N)?"))
    lowercont = cont.lower()
#endwhile

for x inrange(tablenumber):
    print(timestable * tablenumber)
    tablenumber = tablenumber - 1
