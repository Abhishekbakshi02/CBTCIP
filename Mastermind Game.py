import random
import sys
print("Welcome")
player1=input(" Enter your name player1: ") 
player2=input(" Enter your name player2: ")
print("Time for toss")
toss_win=random.choice([player1, player2])# Randomly choosing who gets to decide first
toss_loss = player2 if toss_win == player1 else player1
def enter_game(toss_win,toss_loss):
    
    num1 = int(input(f"Enter the number you want to set  '{toss_win}': "))
    def integer_to_list(number):
        return [int(digit) for digit in str(number)]
    list1=integer_to_list(num1)
    num1_len=len(list1)
    print(f"Now '{toss_loss}' will gess the nummber ")
    print(f"length of number is '{num1_len}'")
    guess_num1=int(input(f"Enter the number you guessed '{toss_loss}': "))

    count1=0
    if guess_num1==num1:
        return 1

    while(not(guess_num1==num1)):
        list_guess=integer_to_list(guess_num1)
        same_numbers=list()
        for i in range(len(list_guess)):
            if list1[i]==list_guess[i]:
                same_numbers.append(i+1)
        print(" Wrong guess , but the elements at these position(start from left)")
        for element in same_numbers:
            print(element, end=' ')
        print(" are correct")
        print(" Try again  , by keeping these ppositions in mind !!")
        guess_num1=int(input(f"Enter the number you guessed '{toss_loss}': "))
        count1=count1+1

    return count1

    
print(f"'{toss_win}' will set the number first")
count1=enter_game(toss_win,toss_loss)
print("Horray!! you have guessed it correct")
print("score : ", end=' ')
print(count1)
if count1==1:
    print(f"'{toss_loss}' has won the game")
    sys.exit()
print(f" Now , '{toss_loss}' will set the number ")
count2=enter_game(toss_loss,toss_win)
print("Horray!! you have guessed it correct")
print("score : ", end=' ')
print(count2)
print(" Now its the time for decision")
winner = toss_win if count1 > count2 else (toss_loss if count2 > count1 else 0)
if winner!=0:
    print(f"Congratulations  ! '{winner}' is the winner")


