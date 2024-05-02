import random


def is_even(number):
    return number % 2 == 0

def play_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")

    correct_answers = 0
    while correct_answers < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = input("Your answer: ")

        if is_even(number) == (answer.lower() == 'yes'):
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was "
                  f"'{'yes' if is_even(number) else 'no'}'. \nLet's try again, {name}!")
            return

    print(f"Congratulations, {name}!")

if __name__=="__main__":
    play_game()