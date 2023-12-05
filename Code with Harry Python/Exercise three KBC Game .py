questions = ["Value Of Py", "Capital Of Maharashtra", "Captian Of India Cricket Team Mens "]
answers = ["3.14", "Mumbai", "Rohit Sharma"]
prizes = [100, 1000, 15000]

def check(question_number, answer):
    if answer.lower() == answers[question_number].lower():
        return True
    else:
        return False

def Khelogame():
    total_prize = 0
    for i in range(len(questions)):
        print(f"Question {i + 1}: {questions[i]}")
        answer = input("Enter Your Answer: ")
        if check(i, answer):
            total_prize += prizes[i]
            print(f"Correct! You Won ${prizes[i]}")
        else:
            print("Incorrect. Better luck next time.")
            break
    return total_prize

def phirsekhelo():
    play_more = input("Do You Want To Play Again? (y/n)")
    if play_more.lower() == "y":
        return True
    else:
        return False

while True:
    total_prize = Khelogame()
    print(f"You Won a Total Of ${total_prize}")

    if not phirsekhelo():
        break

print("Kheyla Baddal Abhaar")





