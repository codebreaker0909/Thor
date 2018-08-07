###Book Cricket for a Book of 500 pages###
###Author: Codebreaker999###

from random import randint,randrange
from time import sleep
def Toss():
    print "Let's play Book Cricket...."
    sleep(1)
    while True:
        toss = ["Heads","Tails"]
        user_toss = raw_input("Let's Toss for Batting. Enter H/T: ")
        if user_toss == "H" or user_toss == "h":
            user_toss = "Heads"
        elif user_toss == "T" or user_toss == "t":
            user_toss = "Tails"
        else:
            print "Wrong Choice."
        random_toss = toss[randint(0,1)]
        print "Spinning the coin"
        sleep(1)
        print random_toss
        if user_toss == random_toss:
            print "You Won the toss. You bat first!!"
            user_bat_first()
            rematch = raw_input("Rematch?? Y/N:  ")
            if rematch == "Y" or rematch == "y":
                continue
            else:
                break
        else:
            print "I win the toss. I bat"
            AI_bat_first()
            rematch = raw_input("Rematch?? Y/N:  ")
            if rematch == "Y" or rematch == "y":
                continue
            else:
                break

#Toss()
def user_bat_first():
    Total = 0
    while True:
        turn = raw_input("Press S to start: ")
        if turn == "S" or turn == "s":
            run = randrange(0, 501, 2)
            print "Page Number: %s" %run
            run = str(run)
            run = run[-1::]
            run = int(run)
            if run == 0:
                print "You are out!!"
                Total +=run
                print "Total: %s" %Total
            else:
                Total += run
                print "Total: %s" % Total
                counter = True
                while counter:
                    bat = raw_input("Press C to continue batting: ")
                    bat = bat.lower()
                    if bat == "c":
                        run = randrange(0, 501, 2)
                        print "Page Number: %s" % run
                        run = str(run)
                        run = run[-1::]
                        run = int(run)
                        if run == 0:
                            print "You are Out!!"
                            print Total
                            counter = False
                        else:
                            Total += run
                        print "Total %s" %Total
                        continue
                break
            break
    print "You Scored %s Runs" %Total
    sleep(1)
    print "I need %s Runs to Win" %(Total+1)
    AI_Total = 0
    print "My Batting...."
    sleep(1)
    while AI_Total <= Total:
            run = randrange(0, 501, 2)
            print "Page Number: %s" % run
            run = str(run)
            run = run[-1::]
            run = int(run)
            if run == 0:
                print "I am out!!"
                AI_Total += run
                print "Total: %s" % AI_Total
                break
            else:
                AI_Total += run
                print "Total: %s" % AI_Total
                sleep(1)
    sleep(1)
    if Total > AI_Total:
        print "You Win by %s runs" %(Total-AI_Total)
    elif Total == AI_Total:
        print "Its a tie"
    else:
        print "I win "

def AI_bat_first():
    AI_Total = 0
    print "My Batting...."
    while True:
        run = randrange(0, 501, 2)
        print "Page Number: %s" % run
        run = str(run)
        run = run[-1::]
        run = int(run)
        if run == 0:
            print "I am out!!"
            AI_Total += run
            print "Total: %s" % AI_Total
            break
        else:
            AI_Total += run
            print "Total: %s" % AI_Total
            sleep(1)
    print "My score: %s" %AI_Total
    sleep(1)
    print "Beat that..."
    Total = 0
    while Total <= AI_Total:
        turn = raw_input("Press S to start")
        if turn == "S" or turn == "s":
            run = randrange(0, 501, 2)
            print "Page Number: %s" %run
            run = str(run)
            run = run[-1::]
            run = int(run)
            if run == 0:
                print "You are out!!"
                Total +=run
                print "Total: %s" %Total
                break
            else:
                Total += run
                print "Total: %s" %Total
                counter = True
                while Total <= AI_Total and counter:
                    bat = raw_input("Press C to continue batting: ")
                    bat = bat.lower()
                    if bat == "c":
                        run = randrange(0, 501, 2)
                        print "Page Number: %s" % run
                        run = str(run)
                        run = run[-1::]
                        run = int(run)
                        if run == 0:
                            print "You are Out!!"
                            print Total
                            counter = False
                        else:
                            Total += run
                        print "Total %s" % Total
                        continue
                    break
                break
            break

    print "You Scored %s Runs" %Total
    sleep(1)

    if Total > AI_Total:
        print "Congrats!! You Win"
    elif Total == AI_Total:
        print "Its a tie"
    else:
        print "Yayy...I win "

Toss()



