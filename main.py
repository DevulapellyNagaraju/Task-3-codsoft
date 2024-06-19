from password_generator import generate_password  # Import generate_password function

def main():
  # Welcome Text 
  print("""
*~*~*~*~*~*~*~*~*~*~*~*~*      
*                       *
 Welcome to the Password 
       Generator!!                 
*                       *
*~*~*~*~*~*~*~*~*~*~*~*~*
""")

  while True:
    try:
      length = int(input("Enter the desired password length: "))
      complexity = input("Enter the desired complexity (low, medium, high): ").lower()
      password = generate_password(length, complexity)
      if password:
        print(f"Generated password: {password}")
    except ValueError:
      print("Please enter a valid number for the password length.")

    continue_choice = input("Do you want to continue (y/n)?").lower()
    if continue_choice != 'y':
      print("Exiting the program. Goodbye!!!!")
      break

if __name__ == "__main__":
  main()
