import sys
print("Welcome ")
player1=input("Please enter you name player1 : ")
player2=input("Please enter you name player2 : ")
print(" Rules of game : ")    
print("1. You can choose among the rock (r) , paper (p) or scissor(s):")
print("2. If it is rock and paper then paper wins")
print("3. If it is paper and scissor then scissor wins")
print("3. If it is rock and scissor then rock wins")
opt={'r','p','s'}
opt1=input(f"Enter your choice '{player1}' :")
while(opt1 not in opt ):
    print("Invalid input ! kindly enter valid input from the rules")
    opt1=input(f"Enter your choice '{player1}' :")
opt2=input(f"Enter your choice '{player2}' :")
while(opt2 not in opt ):
    print("Invalid input ! kindly enter valid input from the rules")
    opt2=input(f"Enter your choice '{player2}' :")

if opt1==opt2:
    print("It's a tie ")
    sys.exit()
def result(opt1,opt2):
    win=0
    if (opt1=='r' and opt2=='p') or (opt1=='p' and opt2=='r'):
        win=opt2 if opt2=='p' else opt1
    elif (opt1=='r' and opt2=='s') or (opt1=='s' and opt2=='r'):
         win=opt2 if opt2=='r' else opt1
    elif (opt1=='p' and opt2=='s') or (opt1=='s' and opt2=='p'):
         win=opt2 if opt2=='s' else opt1
    return win
win=result(opt1,opt2)    
winner=player1 if win==opt1 else player2
print(f"Congratulations !! '{winner}' You have won the game")

