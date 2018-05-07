def verify():
    answer_list = ["wargames", "captain america the winter soldier", "1977", "die hard", "john mclane", "xenommorph"]
    if answer in answer_list:
        print("Correct!")
        outcome = "correct"

    if outcome == "correct":
        print("Next Question!")




print("Welcome to my Movie Quiz!")
begin = input("Shall we play a game? ")
if begin == "yes":

    #ask first question
    answer = input("First of all, what movie was that line from? ")
    verify()

    #Question 2
    print()
    answer = input("What year was the first Star Wars released? ")
    verify()

    #Question 3
    print()
    answer = input("What is Jake Peralta's favorite movie? ")
    verify()

    #question 4
    print()
    answer = input("Follow up question: What is the main protagonist's name in the film Die Hard? ")
    verify()

    #question 5
    print()
    answer = input("What is the Alien in the Alien franchise called? ")
    verify()

    #Will add more questions later now its time to refine the quiz in version 2

else:
    print("Okay, bye :(")