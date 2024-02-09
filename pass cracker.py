import random
import string
import time

def crack_password(password):
    attempts = 0
    while True:
        guess = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=len(password)))
        attempts +=1
        if guess == password:
            return attempts
        
password = input("Enter a password to crack: ")
print("Cracking password")

attempts = crack_password(password)

print(f"Took {attempts} to crack password")