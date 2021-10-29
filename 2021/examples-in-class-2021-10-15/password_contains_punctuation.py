import string
password = "xxxx567."

for ch in string.punctuation:
    if ch in password:
        print("password contains punctuation")
        break
else:
    print("password DOES NOT contain punctuation")
