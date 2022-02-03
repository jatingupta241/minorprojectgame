import random
def gameWin(comp,you):
    
    if comp == you:
           print("you both choose same : game is Tie!")
    elif comp =='rock':
        if you=="paper":
            print("paper covers rock : you win")
        elif you =='scissor':
            print("rock smashes scissor")
    elif comp == 'paper':
        if you == 'scissor':
            print("scissor cuts papers : you win")
        elif you =='rock':
            print("paper covers rock : you loose")
    elif comp=='scissor':
        if you =='rock':
            print("rock smashes scissor : you win")
        elif you =='paper':
            print("scissor cuts paper : you loose")


randno= random.randint(1, 3)
print("computer's turn: rock(1) paper(2) scissor(3)?\n")
if randno==1:
    comp='rock'
elif randno==2:
    comp = 'paper'
elif randno==3:
    comp='scissor'
    
    
you= input("your turn: rock(r) paper(p) scissor(s)?")
if you=="r":
    you="rock"
elif you== "s":
    you= "scissor"
elif you== "p":
    you = "paper"
else:
    print("PLAY AGAIN !!! And enter valid input from ( r, p, s)")
    

a = gameWin(comp,you)
print(f"computer chose : {comp}")
print(f"you chose : {you}")       
