#########################################################################
#           Password Generator                                          #
#########################################################################



#save all characters
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#get nr of letters, symbols and numbers to combine
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


newPassw = ""

#add whole characters
newlist = [letters, numbers, symbols]

#execute the combination for generate the new password
for n in range(0, (nr_letters + nr_symbols + nr_numbers)):

    if nr_letters > 0 and nr_symbols > 0 and nr_numbers > 0:
        randomRows = random.randint(0, 2)


    elif nr_letters > 0 and nr_symbols > 0:
        randomRows = random.randint(0, 1) * 2

    elif nr_letters > 0 and nr_numbers > 0:
        randomRows = random.randint(0, 1)

    elif nr_symbols > 0 and nr_numbers > 0:
        randomRows = random.randint(1, 2)

    else: 
        if nr_letters > 0:
            randomRows = 0
        elif nr_numbers > 0:
            randomRows = 1
        else:
            randomRows = 2

    if randomRows == 0:
        nr_letters -= 1
    elif randomRows == 1:
        nr_numbers -= 1

    else:
        nr_symbols -= 1

    randomColumns = random.randint(0, (len(newlist[randomRows]) - 1 ) )

    newPassw += newlist[randomRows][randomColumns] 

#show the new password
print(newPassw)