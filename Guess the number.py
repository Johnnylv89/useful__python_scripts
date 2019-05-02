import random
num = random.randint(1, 100)
while True:
    print "Try to guess the number from 1 to 100"
    guess = input()
    i = int(guess)
    if i == num:
        print "Corect!"
        break
    elif i < num:
        print "Number is bigger"
    elif i > num:
        print "Number is smaller"
