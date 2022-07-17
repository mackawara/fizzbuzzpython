import re


class Wordgroup:
    def __init__(self, questions, hint):
        self.questions = questions
        self.hint = hint


footbalList = ["goalposts", "midfield", "striker", "scores",
               "dribble", "messi", "star", "manchester united"],

cricketList = ["fine leg", "wicket", "ball", "player",
               "club", "field", "match", "bowler", "batsman"]
rugbyList = ["tag", "sevens", "all blacks", "try",
             "tackle", "penalty", "red card", "injury"]

print(cricketList[-2:])
football = Wordgroup(footbalList, "football")
cricket = Wordgroup(cricketList, "cricket")
rugby = Wordgroup(rugbyList, "rugby")

print(rugby.questions)

hints = (football, cricket, rugby)
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
        hint = hint.hint
        print(f"Hint {hint}")
        guess = input("Guess the word that corresponds with the hint:")

        if guess in hint.questions:
            score = int(points_per_question[count])
            acc_score = score+int(score_param)
            print(f"Good guess, you win, You have scored: {score} "

                  f"and your total score is now  {acc_score}")
            return acc_score

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
        hint = question.hint
        total_score = guess_the_word(question, total_score)
    print(
        f"Game over , you scored  {str(total_score)} out of {len(questions)*5}")


questionsAdd(hints, total_score,)
