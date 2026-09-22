import random

random_int=random.randint(1,100)
print("Guess the number\n")
num=int(input("Enter a number:"))

while random_int!=num:
  if random_int<num:
    print("try with lesser number")
  elif random_int>num:
    print("try with greater number")
  num=int(input("Enter a number:"))

print("you guessed correct number",random_int)
