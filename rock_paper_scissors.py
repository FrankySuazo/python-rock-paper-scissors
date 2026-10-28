#The import to make the 'computer' make it's own option possible
import random

#What appears in the terminal for the user can make it's selection
print("===================")
print("Rock Paper Scissors")
print("===================")

print("1) ✊")
print("2) ✋")
print("3) ✌️")

#The 'connector' for when the user pick a number it's related to the emojis/picks
choices = {
    1: "✊",
    2: "✋",
    3: "✌️"
}

#The use input and the random pick for the computer
player = int(input("Pick a number: "))
computer = random.randint(1, 3)

#The logic of the game and it's output 
if player < 1 or player > 3:
    print("Invalid choice!")
else:
    print(f"You chose: {choices[player]}")
    print(f"CPU chose: {choices[computer]}")

    if player == computer:
        print("It's a tie!")
    elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
        print("The player won!")
    else:
        print("The player lost!")
