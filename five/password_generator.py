import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
key_case = [letters, numbers, symbols]
new_list = []

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Code for outputting the password in a set order

#chosen_letters = random.choices(letters, k=nr_letters)
# chosen_symbols = random.choices(symbols, k=nr_symbols)
# chosen_numbers = random.choices(numbers, k=nr_numbers)
# print("".join(chosen_letters) + "".join(chosen_symbols) + "".join(chosen_numbers))

for character_list in key_case:
    new_list.extend(character_list)

chosen_letters = random.choices(letters, k=nr_letters)
chosen_symbols = random.choices(symbols, k=nr_symbols)
chosen_numbers = random.choices(numbers, k=nr_numbers)

chosen_characters = chosen_letters + chosen_numbers + chosen_symbols
random.shuffle(chosen_characters)

print("".join(chosen_characters))