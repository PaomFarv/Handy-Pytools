print("Welcome! Presenting you some useful tools that you might need.")
print("(1) Armstrong Number Checker.")
print("(2) Anagram Checker.")
print("(3) Palindrome Checker.")
print("(4) Pangram Checker.")
print("(5) Punctuation Remover.")
print("(6) Word Counter.")
print("(7) To Quit.")

 
while True:
    try:
        user_resp = int(input("\nType the no. of tool you want to use: "))
    except ValueError:
        print("Invalid input.")
        continue
    
    if user_resp == 1:
#Armstrong number checker
        digits = int(input("\nHow many digits it will contain: "))
        user_input = input("Insert a number: ")

        arm_sum = 0

        if not user_input.isdigit():
            print("Invalid input.Please insert a number.")

        else: 
            for char in user_input:
                arm_nums = int(char)**digits
                arm_sum += arm_nums 
            
            if arm_sum == int(user_input):
                print("It's a Armstrong Number.")
            else:
                print("It's NOT a Armstrong number.")

    elif user_resp == 2:
#Anagram Checker
        first_input = input("\nType the 1st word : ").strip()
        sec_input = input("Type the 2nd word : ").strip()

        cmplx_1 = first_input.lower()
        cmplx_2 = sec_input.lower()

        modified_1st = sorted(cmplx_1)
        modified_2nd = sorted(cmplx_2)

        if modified_1st == modified_2nd:
            print(f"The words {first_input} & {sec_input} are Anagrams.")

        else:
            print(f"The words {first_input} & {sec_input} are NOT Anagrams.")

    elif user_resp == 3:
#Palindrome checker
        user_input = input("\nEnter the word or number you want to check: ").lower().strip()
        rev_user_input = user_input[::-1]

        if user_input == rev_user_input:
            print("That's a Palindrome.")

        else:
            print("That's NOT a Palindrome.")

    elif user_resp == 4:
#Pangram Checker
        import string
        user_input = input("\nEnter your sentence: ").lower()
        fresh_input = sorted(user_input.replace(" ",""))
        alphabets = string.ascii_lowercase

        def is_pangram():
            for char in alphabets:
                if char not in fresh_input:
                    return "That is not a Pangram"
            return "That is a pangram"

        print(is_pangram())

    elif user_resp == 5:
#Punctuation Remover
        user_input = input("\nInsert a string: ")
        no_punc = ""

        for char in user_input:
            if char.isalpha():
                no_punc += char
            if char.isdigit():
                no_punc += char
                
        print(f"String without punctuations: {no_punc}")

    elif user_resp == 6:
# Words Counter in a string
        import re
        import string

        def word_counter():
            user_input = input("\nEnter a string: ").strip()
            user_input = user_input.translate(str.maketrans('','',string.punctuation))
            
            words = re.split(r'\s+',user_input)
            words = list(filter(None,words))

            print(f"There are {len(words)} words")
            
        word_counter()

    elif user_resp == 7:
        print("You Have Exited This Program.Goodbye!")
        break