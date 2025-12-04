import random
import string

# Step 1: Get password length from user
length = int(input("Enter the desired password length: "))

# Step 2: Create a pool of characters
characters = string.ascii_letters + string.digits + string.punctuation

# Step 3: Generate random password
password = ''.join(random.choice(characters) for _ in range(length))

# Step 4: Display the password
print("Generated Password:", password)
