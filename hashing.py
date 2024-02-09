import hashlib

h = hashlib.new("SHA256")
correct_password = "MyPassword1234567"
h.update(correct_password.encode())

password_hash = h.hexdigest()

user_input = input("Please put in your password:\n")

h = hashlib.new("SHA256")
h.update(user_input.encode())
input_hash = h.hexdigest()

if input_hash == password_hash:
    print("Same password")
else:
    print("Incorrect")