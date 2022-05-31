import random

if random.randint(0, 1) == 1:
    a = True
else:
    a = False

if random.randint(0, 1) == 1:
    b = True
else:
    b = False

#set default
coinOne = False
coinTwo = False


#flip one
if a == True:
    print("The first coin is Heads!")
    coinOne = True
elif a == False:
    print("The first coin is Tails!")
    coinOne = False



#the second coin flip
if b == True:
    print("The second coin is Heads!")
    coinTwo = True
elif b == False:
    print("The second coin is Tails!")
    coinTwo = False
    
    
    
#select a gate

gate = input("What type of gate do you want? (A)nd, (O)r?")

#chose the And gate
if gate == "A":
    if coinOne == True and coinTwo == True:
        print("Your AND gate is True!")
    else:
        print("Your AND gate is False!")
elif gate == "O":
    if coinOne == True or coinTwo == True:
        print("Your OR gate is True!")
    else:
        print("Your OR gate is False!")
    
    
        
        
    
