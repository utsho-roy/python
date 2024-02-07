import random
card=[11,2,3,4,5,6,7,8,9,10,10,10,10]
a = []
b = []
for _ in range(2):
    a.append(random.choice(card))
    b.append(random.choice(card))
print('Welcome to black jack game. Let the game begin')
print(f'computer\'s First card is: {a[0]}')
print(f'Your cards are: {b}')
c=input('Do you wanna roll or pass? ').lower()

if c == 'roll':
    b.append(random.choice(card))

    total_c = sum(a)
    total_p = sum(b)
    x = 0
    for i in b:
        if i == 11 and total_p > 21:
            x += 1
            total_p = sum(b) - (10 * x)

    for i in a:
        if i == 11 and total_c > 21:
            x += 1
            total_c = sum(a) - (10 * x)
    if total_p >= total_c and total_p < 22:
        print(f"Comp= {a}, Player= {b}. Player wins. ")
        print(f"Comp sum= {total_c}, Player sum= {total_p} ")
    else:
        print(f"Comp= {a}, Player= {b}. Computer wins. ")
        print(f"Comp sum= {total_c}, Player sum= {total_p} ")



elif c == 'pass':

    total_c = sum(a)
    total_p = sum(b)
    x = 0
    for i in b:
        if i == 11 and total_p > 21:
            x += 1
            total_p = sum(b) - (10 * x)

    for i in a:
        if i == 11 and total_c > 21:
            x += 1
            total_c = sum(a) - (10 * x)
    if total_p >= total_c and total_p < 22:
        print(f"Comp= {a}, Player= {b}. Player wins. ")
        print(f"Comp sum= {total_c}, Player sum= {total_p} ")
    else:
        print(f"Comp= {a}, Player= {b}. Computer wins. ")
        print(f"Comp sum= {total_c}, Player sum= {total_p} ")

