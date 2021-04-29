#random password generator
import random
import string
possible_digits = ['0','1','2','3','4','5','6','7','8','9']
possible_letters = list(string.ascii_letters)
length = input("How many characters do you want in your password? ")
letters = input("How many letters do you want in your password?")
numbers = (int(length)-int(letters))
random_letters = random.sample(possible_letters, int(letters))
random_numbers = random.sample(possible_digits, numbers)
random_password = random_letters + random_numbers
random_password = ''.join(random.sample(random_password, len(random_password)))
print("Password: ", random_password)