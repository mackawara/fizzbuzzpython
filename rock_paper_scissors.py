import random
import sys
print(sys.version_info)
rock = "rock"
paper = "paper"
scissors = "scissors"

game_var = [rock, paper, scissors]
while True:
    print("in loop")

    while True:

        userInput = (input("""make your choice here
        1. Rock
        2. Paper
        3. Scissors

        Write number corresponding to your choice """))
        print(userInput)
        if userInput in ("1", "2", "3"):
            break
            # userInput=int(userInput)
            # print("please enter a valid number between 1and 3")
            # break
        else:
            print("Invalid selection")

    u_sel = game_var[int(userInput)-1]
    c_sel = game_var[random.randrange(0, 3)]
    print(u_sel)
    print(c_sel)

    if (u_sel == rock and c_sel == paper) or (u_sel == paper and c_sel == scissors) or (u_sel == scissors and c_sel == rock):
        print("You lose: computer selected " +
              c_sel + " and you selected" + u_sel)
    elif u_sel == c_sel:
        print("Tie :computer selected " + c_sel +
              " and you selected " + u_sel + "please try again")

    else:
        print("congratulations you won")
        while True:
            playAgain = input("do you want to play again? Yes or no")
            if playAgain not in ("Yes", "No"):
                pass
            elif playAgain == "No":
                break
