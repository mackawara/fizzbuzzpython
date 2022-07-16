import re
footbal = ["goalposts", "midfield", "striker", "scores",
           "dribble", "messi", "star", "manchester united"]
cricket = ["fine leg", "wicket", "ball", "player",
           "club", "field", "match", "bowler", "batsman"]
rugby = ["tag", "sevens", "all blacks", "try",
         "tackle", "penalty", "red card", "injury"]

hints = (footbal, cricket, rugby)
print("""How to play this game
        You will be given a 1 word hint of a subject matter and you will be asked to guess a word
        IF you fail you will be given 4 additional attempts.
        After 5 attempts you will have failed and the game will close  """)


total_score = 0


def guess_the_word(hint, score_param):
    points_per_question = ["5", "4", "3", "2", "1"]
    count = 0
    while True:
        print("Your count is "+str(count))
        print("Hint :")
        guess = input("Guess the word that corresponds with the hint: ")

        if guess in hint:
            score = int(points_per_question[count])
            # total_score = total_score+int(points_per_question[count])
            print("""Good guess, you win, You have scored: "+str(score) + " points
                   and your total score is now " + str(total_score)""")
            return score+int(score_param)

        else:
            count = count+1
            print("sorry please try again")
            print(count)
            # otal_score = total_score+int(points_per_question[count])
            if count >= 5:
                print("game up : try again next time")
                print("points count for this question is " +
                      str(score) + " and total score is " + str(score+score_param))
                break


def questionsAdd(questions, total_score):
    total_score = 0
    print("the score before the question is done " + str(total_score))
    for question in questions:
        total_score = guess_the_word(question, total_score)
    print("Game over , you scored " + str(total_score))


questionsAdd(hints, total_score)
