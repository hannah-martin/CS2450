import random
print("Hi, I am going to try to guess your age.")
name = input("What is your name? ")

age = 1
while age == 1:
    guess = random.randrange(15, 30)
    if (input(str(guess) + "? y/n: ") == 'y'):
        age = guess
    else:
        print("Rats.")

print(name, "is", age, "years old.")


    