import sys #sys is mdule to exitv the program once not fulfilled
import random #random module to import random number
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    

print(RPS(2))    
print(RPS.ROCK)    
print(RPS["ROCK"])  #accessing enum by name
print(RPS.ROCK.value)  #accessing enum by value

print("")
playerchoice = input("Enter..... \n1 for Rock, \n2 for Paper, \n3 for Scissors: ")

player = int(playerchoice)
print(type(playerchoice))  #check the type of playerchoice
print("You chose:", playerchoice)
if player < 1 or player > 3:
   sys.exit("Invalid choice, exiting the program...")
    
print("Program goes on...") 

computerchoice = random.choice("123")  #random number between 1 and 3   
computer = int(computerchoice)  #convert string to integer
print("")
print("You chose "+ str(RPS(player)).replace("RPS.","") + ".")
print("Python chose "+ str(RPS(computer)).replace("RPS.","") + ".")
print("")

if player == 1 and computer == 3:
    print("You win!")
elif player == 2 and computer == 1:
    print("you wins!")
elif player == 3 and computer == 2:
    print("you win1")
elif player == computer:
    print("It's a tie!")
else:
    print("Python wins!")
            