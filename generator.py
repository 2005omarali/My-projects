


[my code to be password generator.py](https://github.com/user-attachments/files/23323393/my.code.to.be.password.generator.py)
import random
import string
password = []
print("welcome to the password generator\n")
lengh = int(input("\nenter the total number of characters in the password :"))

num_letters = int(input("\nenter the number of letters in the password :"))
num_numbers = int(input("\nenter the number of numbers in the password :"))
num_symbols = int(input("\nenter the number of symbols in the password :"))


if lengh != (num_letters  +num_numbers+ num_symbols) :
  print("\ninvaild input .the sum of letters, numbers, and symbols does not match the password")
  
else:
  letters = string.ascii_letters
  numbers = string.digits
  symbols = string.punctuation
  for le in range(num_letters):
    password.append(random.choice(letters))
  for nu in range(num_numbers):
    password.append(random.choice(numbers))
  for sy in range(num_symbols):
    password.append(random.choice(symbols))
    random.shuffle(password)

  gen = "".join(password)
print(f"the password generator is :{gen}")
