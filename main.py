import random


# Get guess
def get_guess():
    return list(input("Input 3 digits of number: "))


# Get random number
def generate_code():
    rand_number = [str(num) for num in range(10)]

    # shuffle digits and grab first three
    random.shuffle(rand_number)
    return rand_number[:3]


# Generate the clues
def generate_clues(code, user_guess):
    if user_guess == code:
        return "CODE CRACKED!"

    clues = []

    for i, num in enumerate(user_guess):
        if num == code[i]:
            clues.append("Match")

        elif num in code:
            clues.append("Close")

    if not clues:
        return ["Nope!"]
    else:
        return clues


# Game Logic
print("Welcome Code Breaker")
secret_code = generate_code()

clue_report = []

while clue_report != "CODE CRACKED!":
    guess = get_guess()
    clue_report = generate_clues(guess, secret_code)
    print("Here is the result of your guess: ")
    for clue in clue_report:
        print(clue)