import random

roll = random.randint(1, 6)
guess = int(input("Guess the roll : "))

print("your guess : "+str(guess))
print("your roll : "+str(roll))
print(roll, "is of type", type(roll))

print(guess, "is of type", type(guess))

print(guess == roll)

if guess == roll:
    print("what a guess you are right! - "+str(guess))
else:
    print("No, roll is : "+str(roll))
