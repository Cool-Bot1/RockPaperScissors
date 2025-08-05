import random

choice=""
enchoice=""
game=""

def mode():
    global game
    game=input("Do you want to play a person or an AI? (PE,AI) ")
    if game != "AI" and game !="PE":
        print("error type AI or PE only")
        mode()
    ask()

def ask():
    global choice
    global enchoice
    global game
    if game=="AI":
        choice=input("(Rock, Paper Scissors) ")
        gen()
    elif game=="PE":
        choice=input("Player 1: (Rock, Paper Scissors) ")
        enchoice=input("Player 2: (Rock, Paper Scissors) ")
    check()

def gen():
    global enchoice
    num=random.randint(1,3)
    if num==1:
        enchoice="Rock"
    elif num==2:
        enchoice="Paper"
    elif num==3:
        enchoice="Scissors"

def check():
    global choice
    global enchoice
    if choice==enchoice:
        print(choice,enchoice,"Tie")
        ask()
    elif choice=="Rock" and enchoice=="Scissors":
        print(choice,"beats",enchoice,"Player 1 wins")
    elif choice=="Paper" and enchoice=="Rock":
        print(choice,"beats",enchoice,"Player 1 wins")
    elif choice=="Scissors" and enchoice=="Paper":
        print(choice,"beats",enchoice,"Player 1 wins")
    elif enchoice=="Rock" and choice=="Scissors":
        print(enchoice,"beats",choice,"Player 2 wins")
    elif enchoice=="Paper" and choice=="Rock":
        print(enchoice,"beats",choice,"Player 2 wins")
    elif enchoice=="Scissors" and choice=="Paper":
        print(enchoice,"beats",choice,"Player 2 wins")
    else:
        print("error, restarting")
        ask()

mode()