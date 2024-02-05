print("WELCOME TO TRESSURE ISLAND. YOUR MISSION IS TO FIND THE TREASURE")
a= input('Do you wanna go left or right? ')
if a.lower() == 'left':
    b= input('Correct! There is a croc in the river near you. Do you wanna swim or wait ?')
    if b.lower() == 'wait':
        c=input('there are 3 door: red, blue, yellow. Choose one: ')
        if c.lower()== 'yellow':
            print('Winner winner chicken dinner')
        else: print('Spider will kill you. Game Over loser!')
    else:
        print('Game Over loser!')
else: print('Game Over loser!')
