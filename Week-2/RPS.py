

from random import randint
def RPS():

    cpl = 1 #initial variable reset
    cbo = 3
    choicew = (" ")
    pointspl = 0
    pointsbo = 0
    round = 0

    print ("I challenge you to a game of Rock Paper Scissors")
        
    while round <= 5:
        choice = int(input ("1 means rock, 2 means paper, 3 means scissors. Choose:  "))
        cpl = choice
        if choice == 1: 
            choicew = ("Rock")
        elif choice == (2):
            choicew = ("Paper")
        elif choice == 3:
            choicew = ("Scissors")
        else:
            choicew = ("an invalid choice, you get punished.") #invalid
            pointspl = 0
        print (choice)

        print ("You choose" ,choicew)

        cbo = randint(0,2) #choice of bot
        cbo = cbo +1

        if cbo == 1:
            cbow = ("Rock")
        elif cbo == 2:
            cbow = ("Paper")
        elif cbo == 3:
            cbow = ("Scissors")
            
        print ("I choose" ,cbow)

        if cbo == cpl + 1:  #quick maffs
            print ("I win")
            pointsbo = pointsbo + 1 #bot wins
        elif cbo == cpl - 1:
            print ("You win")
            pointspl = pointspl + 1 #player wins
        elif cbo == cpl + 2:
            print("You win")
            pointsbo = pointsbo + 1 #bot wins
        elif cbo == cpl - 2:
            pointspl = pointspl + 1 #player wins
            print ("I win")
        elif cbo == cpl:
            print("It's a draw")
            pointspl = pointspl + 1 #draw
            pointsbo = pointsbo + 1
        else:
            print("don't cheat")

        print("The score is ",pointsbo ,":", pointspl)

        round = round + 1
    if pointspl > pointsbo:
        print("PLAYER WINS. GAME OVER")
    elif pointspl < pointsbo:
        print("BOT WINS, GAME OVER") #finalisation
    else:
        print("IT'S A DRAW, PLAY AGAIN.")
        RPS()