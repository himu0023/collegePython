char = input("Enter single Character: ")

if len(char)==1:
    if char.isalpha():
        if (char=='a' or char=='e' or char=='i' or char=='o' or char=='u'):
            print(f"'{char}' is Vowel.")
        else:
            print(f"'{char}' is Consonent.")
    else:
     print(f"'{char}' is not Character")