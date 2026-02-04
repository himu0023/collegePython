char = input("Enter a single character: ")

if len(char)==1:
    if char.isalpha():
            print(f"'{char}' is an alphabet.")
    else:
         print(f"'{char}' is NOT an alphabet.")

else:
   print(f"Please enter a single alphabet.")