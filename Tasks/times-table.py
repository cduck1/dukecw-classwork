timestable = int(input("What times table (1-20)?"))
strtimestable = str(timestable)

#validation for the timestable number
while (timestable < 1) or (timestable > 20):
    timestable = int(input("The times table must be between 1 and 20 and an integer, please re-enter your times table."))
    strtimestable = str(timestable)
#endwhile

#continue?
cont = str(input("Did you mean " + strtimestable + " (Y/ N)?"))
lowercont = cont.lower()

while lowercont == "n":
    timestable = int(input("What times table (1-20)?"))
    strtimestable = str(timestable)
    #validation for the timestable number
    while (timestable < 1) or (timestable > 20):
        timestable = int(input("The times table must be between 1 and 20 and an integer, please re-enter your times table."))
        strtimestable = str(timestable)
    #endwhile
    cont = str(input("Did you mean " + strtimestable + " (Y/ N)?"))
    lowercont = cont.lower()
#endwhile

tablenumber = int(input("What table number (number of rows)(1-20)?"))
strtablenumber = str(tablenumber)

#validation for the tablenumber
while (tablenumber < 1) or (tablenumber > 20):
    tablenumber = int(input("The table number must be between 1 and 20, please re enter the table number."))
    strtimestable = str(timestable)
#endwhile

#continue?
cont = str(input("Did you mean " + strtablenumber + " (Y/ N)?"))
lowercont = cont.lower()

while lowercont == "n":
    tablenumber = int(input("What table number (number of rows)(1-20)?"))
    strtablenumber = str(tablenumber)
    #validation for the tablenumber
    while (tablenumber < 1) or (tablenumber > 20):
        tablenumber = int(input("The table number must be between 1 and 20, please re enter the table number."))
        strtablenumber = str(tablenumber)
    #endwhile
    cont = str(input("Did you mean " + strtablenumber + " (Y/ N)?"))
    lowercont = cont.lower()
#endwhile

#print the answer
for x in range(tablenumber):
    print(timestable * tablenumber)
    tablenumber = tablenumber - 1
#endfor
