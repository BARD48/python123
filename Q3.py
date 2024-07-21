import random
picked_number=random.randint(1,15)
guess_Number=int(input("Please enter your guess: "))
while picked_number!=guess_Number:
    if guess_Number< picked_number:
        print("increase your number")
    elif guess_Number>picked_number:
        print("Decrease your number")
    elif guess_Number==picked_number:
        print("Your guess is right")
    guess_Number=int(input("Please enter your guess: "))
if picked_number==guess_Number:
    print("Your guess is true")