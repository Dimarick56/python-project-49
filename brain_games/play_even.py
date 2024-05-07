import random


def even_game():
    name = welcome_game()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        question = random.randint(1, 100)
        answer = reqest(question)
        current_answer = ("no" if (question % 2) else "yes")
        correct_answer = (answer == "yes" or answer == "no")
        if result(answer, current_answer, correct_answer, name):
            count += 1
    print(f"Congratulations, {name}!'")
    exit()

def welcome_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name

def reqest(question):
    print(f'Question:{question}')
    answer = input('Your answer: ')
    return answer

def result(answer, current_answer, correct_answer, name):
    if current_answer == answer and correct_answer:
        print("Correct!")
        return True
    defeat(name, answer, current_answer)


def defeat(name, answer, current_answer):
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{current_answer}'")
    print(f"Let's try again, {name}!")
    exit()
