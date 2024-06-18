import random
import string

def generate_password(length, complexity):
  if length < 4:  # Ensure there's enough length to include all character types
    print("Password length should be at least 4")
    return None

  # Character sets
  lowercase = string.ascii_lowercase
  uppercase = string.ascii_uppercase
  digits = string.digits
  special_characters = string.punctuation

  if complexity == "low":
    all_characters = lowercase + uppercase
  elif complexity == "medium":
    all_characters = lowercase + uppercase + digits
  elif complexity == "high":
    all_characters = lowercase + uppercase + digits + special_characters
  else:
    print("Invalid complexity level. Please choose from 'low', 'medium', or 'high'.")
    return None

  # Ensure the password contains at least one character from each selected set
  password = [
    random.choice(lowercase),
    random.choice(uppercase),
    random.choice(digits if complexity in ['medium', 'high'] else lowercase),
    random.choice(special_characters if complexity == 'high' else lowercase)
  ]

  # Fill the remaining length with a mix of all selected character sets
  password += random.choices(all_characters, k=length-4)

  # Shuffle the result to avoid predictable patterns
  random.shuffle(password)

  # Convert list to string
  return ''.join(password)
