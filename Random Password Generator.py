import random
import string

length = int(input("Enter passwordm length:"))
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits
password = [
    random.choice(lowercase),
    random.choice(uppercase),
    random.choice(numbers)
]

characters = lowercase + uppercase + numbers

for i in range(length - 3):
    password.append(random.choice(characters))

random.shuffle(password)

password = '' .join(password)

print("Generated Password:", password)
