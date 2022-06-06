import random
print random.randint(1,9)
chances=0
while chances<5:
    guess=int(input("Enter the guess"))
    if not chances < 5:
        print("You lose!!! The number is", number)
if guess==number:
   print("Congratulations You Have Won!!")
   break
