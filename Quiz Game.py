question_answer = {
    "What year was the very first model of the iPhone released?": "2007",
    "What’s the shortcut for the “copy” function on most computers?": "ctrl c",
    "What is often seen as the smallest unit of memory?": "kilobyte",
    "Is Java a type of OS?": "no",
}

def start_newgame():
    while True:
        user_input = input("Are you ready to start the quiz? Y/N ").upper()
        if user_input == "Y":
            break
        elif user_input == "N":
            print("Ok just let me know once you're ready.")
        else:
            print("Input a valid value Y/N")
            
def show_question():
    score = 0
    question_number_count = 1
    question_answer = {
    "What year was the very first model of the iPhone released?": "2007",
    "What’s the shortcut for the “copy” function on most computers?": "ctrl c",
    "What is often seen as the smallest unit of memory?": "kilobyte",
    "Is Java a type of OS?": "no"
    }
    for question in question_answer:
        print(question)
        if question_number_count == 1:
            print("""
            a. 2007
            b. 2008
            c. 2009
            d. 2006
            """)
            answer = "a"
            question_number_count += 1
        elif question_number_count == 2:
            print("""
            a. ctrl z
            b. ctrl c
            c. shift c
            d. shift z
            """)
            answer = "b"         
            question_number_count += 1
        elif question_number_count == 3:
            print("""
            a. megabyte
            b. kilobyte
            c. kilobit
            d. bit
            """)
            answer = "b"         
            question_number_count += 1
        elif question_number_count == 4:
            print("""
            a. maybe
            b. not defined
            c. yes
            d. no
            """)
            answer = "d"         
            question_number_count += 1

        user_input = input("Answer: ").lower()
        if user_input == answer:
            print("CORRECT")
            score += 1
    return score

def display_score(score):
    print(f"You've got a total of {score}/4 score")

def play_again():
    input_user = input("Do you want to play again? Y/N").upper()
    if input_user == N:
        break
    else:
        pass

while True:
    start_newgame()
    final_score = show_question()
    display_score(final_score)
    play_again()
 