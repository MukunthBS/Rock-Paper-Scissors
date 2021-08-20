import random

choices = ["Rock", "Paper", "Scissors"]


def start():
    
    print("\nWelcome to Rock-Paper-Scissors\n")    
    print("\nChoose a game mode:\n\n\t1.Best of 3\n\t2.Best of 5\n")

    n = int(input())

    return n

def check_mode(n):
    
    if n == 1:
        best_of_three()
    elif n == 2:
        best_of_five()
    else:
        print("\nPlease Enter a valid choice.")
        start()

def best_of_three():

    points = 0
    i = 0

    while i < 3:

        user = user_pick()
        res = play(i+1, user)

        if res == 1:
            points += 1
        if res == 0:
            i = i - 1
        
        if(points == 2):
            break
        
        i = i + 1

    print("\nYour Score: ", points, "/3")

    if points >= 2:
        print("\nYou Win !\n")
    else:
        print("\nYou Lose :(\n")

    if replay():
        check_mode(start())

def best_of_five():

    points = 0
    i = 0

    while i < 5:

        user = user_pick()
        res = play(i+1, user)

        if res == 1:
            points += 1
            print("\nPoint Obtained!")
        if res == 0:
            i = i - 1

        if(points == 3):
            break
        
        i = i + 1

        if replay():
            check_mode(start())
    
    print("\nYour Score: ", points, "/5")

    if points >= 3:
        print("\nYou Win !")
    else:
        print("\nYou Lose :(")

def user_pick():

    user = input("\nEnter Your Pick: ")
    if user not in choices:
        print("\nEnter a valid choice.")
        user_pick()
    return user

def play(i, user):

    pc = random.choice(choices)

    print("\nGame ", i)
    print("\nYour Choice: ", user)
    print("Computer's Choice: ", pc)

    if user == pc :
        return 0
    elif user == "Rock" and pc == "Paper":
        return -1
    elif user == "Rock" and pc == "Scissors":
        return 1
    elif user == "Paper" and pc == "Rock":
        return 1
    elif user == "Paper" and pc == "Scissors":
        return -1
    elif user == "Scissors" and pc == "Rock":
        return -1
    elif user == "Scissors" and pc == "Paper":
        return 1

def replay():

    print("\nDo you want to replay? Y/N\n")
    rep = input()

    if rep == "Y":
        return True
    else:
        return False

check_mode(start())