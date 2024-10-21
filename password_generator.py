from random import choice, randint, shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# nr_letters = randint(8, 10)
# nr_symbols = randint(2, 4)
# nr_numbers = randint(2, 4)

# word_list = [random.choice(letters) for _ in range(nr_letters)]
# number_list = [random.choice(numbers) for _ in range(nr_numbers)]
# symbol_list = [random.choice(symbols) for _ in range(nr_symbols)]
# password_list = word_list + number_list + symbol_list

password_list = ([choice(letters) for _ in range(randint(8, 10))]
                 + [choice(numbers) for _ in range(randint(2, 4))]
                 + [choice(symbols) for _ in range(randint(2,4))])
shuffle(password_list)

# password = ""
# for char in password_list:
#   password += char

password = "".join(password_list)

print(f"Your password is: {password}")