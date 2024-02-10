import random
print('welcome to guessing game. Guess no between 1 and 100')
def num_select():
    return random.randint(0,100)
def play_game(chances):
    num=num_select()
    while chances>0:
        chances-=1
        guess= int(input("Guess the number: "))
        if guess > num:
            print(f"Guess is too high. You have {chances} chances left")
        elif guess == num:
            return print("Guess is correct. Congratulations")
        else :
            print(f"Guess is too low. You have {chances} chances left")
    if chances == 0:
        return print('You loose')
while input("press y to play and n to exit: ") == 'y':
    if input("Select difficulty level- Easy/Hard :").lower() == 'easy':
        play_game(10)
    else : play_game(5)

