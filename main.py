#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
final_password = ""
for l in range(0,nr_letters):
  position_letter = letters[random.randrange(0,len(letters))]
  final_password += position_letter
  
for l in range(0,nr_numbers):
  position_number = numbers[random.randrange(0,len(numbers))]
  final_password += position_number
  
for l in range(0,nr_symbols):
  position_symbol = symbols[random.randrange(0,len(symbols))]
  final_password += position_symbol
#convert characters to list and shuffle the order
splited = list(final_password)
random.shuffle(splited)
#shuffled list to string
finale = ""
for i in splited:
  finale += i
print(finale)