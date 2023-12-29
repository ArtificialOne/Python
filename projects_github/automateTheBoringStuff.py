import random, sys, time

def ifElseTryExcept():
    print("Enter username:")
    userName=input('> ')
    print("Enter password:")
    userPass=input('> ')
    print("Enter age:")
    try:
        userAge=int(input('> '))
        print("Username:",userName,"\n","Password:",userPass,"\n","Age:",userAge)
    except ValueError:
        print("Numbers only")
#ifElseTryExcept()

def randomNumber():
    secretNumber=random.randint(1,20)
    print("Choose a number between 1 and 20")
    for i in range(1,7):
        print("Choose a number.")
        guess=int(input('> '))

        if guess < secretNumber:
            print("Too low.")
        elif guess > secretNumber:
            print("Too high.")
        else:
            break
    if guess == secretNumber:
        print("You are correct in", str(i), "entries!")
    else:
        print("Nope, the answer is", secretNumber)
#randomNumber()

def rockPaperScissors():
    wins=0
    losses=0
    ties=0

    while True:
        print("%s Wins, %s Losses, %s Ties" % (wins, losses, ties))
        while True:
            print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
            playerMove=str(input())
            if playerMove=='q':
                sys.exit()
            if playerMove=='r' or playerMove=='s' or playerMove=='p':
                break
            print("Type one of r, p, s, or q.")
        if playerMove=='r':
            print("ROCK versus...")
        elif playerMove=='p':
            print("PAPER versus...")
        elif playerMove=='s':
            print("SCISSORS versus...")

        randomNumber=random.randint(1,3)
        if randomNumber == 1:
            computerMove='r'
            print("ROCK")
        if randomNumber == 2:
            computerMove='p'
            print("PAPER")
        if randomNumber == 3:
            computerMove='s'
            print("SCISSORS")
        
        if playerMove==computerMove:
            print("Tie!")
            ties+=1
        elif playerMove=='r' and computerMove=='s':
            print("You win!")
            wins+=1
        elif playerMove=='s' and computerMove=='r':
            print("Computer wins!")
            losses+=1
        elif playerMove=='r' and computerMove=='p':
            print("Computer wins!")
            losses+=1
        elif playerMove=='s' and computerMove=='p':
            print("You win!")
            wins+=1
        elif playerMove=='r' and computerMove=='s':
            print("You win!")
            wins+=1
        elif playerMove=='p' and computerMove=='r':
            print("You lose!")
            losses+=1
#rockPaperScissors()

def magicEightBall():
    def magicEightBall(answer):
        if answer==1:
            return "It is certain"
        elif answer==2:
            return "It is not so"
        elif answer==3:
            return "It is possible."
        elif answer==4:
            return "Maybe maybe not."
        elif answer==5:
            return "Absolutely"
        elif answer==6:
            return "Absolutely not"
        elif answer==7:
            return "It is decidedtly so"
        elif answer==8:
            return "No way jose"
        elif answer==9:
            return "Yo yo no no"
    print(magicEightBall(random.randint(1,9)))
#magicEightBall()

def multiDefinitions():
    def caseA():
        print("Beginning A, running B")
        caseB()
        print("B Ran C, now B will run D")
        caseD()
    def caseB():
        print("Beginning B, running C")
        caseC()
    def caseC():
        print("Returning Test C.")
    def caseD():
        print("This is D. No other cases defined here.")
    
    while True:
        print("Choose a Case 1 - 5:")
        print("1. Case A")
        print("2. Case B")
        print("3. Case C")
        print("4. Case D")
        print("5. Quit")
        try:
            caseChoice=(int(input('> ')))
            if caseChoice==1:
                caseA()
            if caseChoice==2:
                caseB()
            if caseChoice==3:
                caseC()
            if caseChoice==4:
                caseD()
            if caseChoice==5:
                break
        except ValueError:
            print("\nPlease enter a value 1 - 5\n")
multiDefinitions()

def zigZag():
    indent=0
    indentIncreasing=True
    try:
        while True:
            print(' ' * indent, end='')
            print("*********")
            time.sleep(0.1)

            if indentIncreasing:
                indent+=1
                if indent==20:
                    indentIncreasing=False
            else:
                indent-=1
                if indent==0:
                    indentIncreasing=True
    except KeyboardInterrupt:
        sys.exit
#zigZag()