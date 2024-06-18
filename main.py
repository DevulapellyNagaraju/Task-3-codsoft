from password_generator import generate_password  # Import generate_password function

def main():
  # Welcome Text with color... (Replace with a more user-friendly method if desired)
  print("""
*~*~*~*~*~*~*~*~*~*~*~*~*      
*       """ + "\033[33m" + """                *
 Welcome to the Password 
       Generator!!                 
*       """ + "\033[0m" + """                *
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

    continue_choice = input("\033[31m" + "Do you want to continue (y/n)? " + "\033[0m").lower()
    if continue_choice != 'y':
      print("Exiting the program. Goodbye!!!!")
      break

if __name__ == "__main__":
  main()
