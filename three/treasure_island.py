print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

crossroads = input('You come across a crossroad. '
                   'You can either go "left" or "right". '
                   'Which path do you choose?\n').lower()

if crossroads == "left":
    swim = input('You come across a large lake. ' 
                 'Do you "swim", or "wait"?\n').lower()

    if swim == "wait":
        three_doors = input('You are now standing before three large doors, ' 
                            'one "red", one "yellow", and one "blue". ' 
                            'Which door do you pick to pass through?\n').lower()

        if three_doors == "red":
            print("Behold, the treasure. You win!")
        elif three_doors == "yellow":
            print("You are consumed by a raging fire. Game over.")
        elif three_doors == "blue":
            print("You are attacked by a herd of cattle. Game over.")
        else:
            print("Incorrect input. Game over.")
    else:
        print("You are attacked by trout. Game over.")

else:
    print("You fall into a huge hole. Game over.")
