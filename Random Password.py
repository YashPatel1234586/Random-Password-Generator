import random
import string

password_length = 12
charValue = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(password_length):
    password += random.choice(charValue)

print("Your random password is :-  ", password)