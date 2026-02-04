print("This program checks if the username is valid")

count_characters = 12
username = input("Enter your username: ")

if len(username) > count_characters:
    print(f"Your username has more then {count_characters} characters. Try again!")
elif len(username) == 0:
    print("You haven't entered your username. Try again!")
elif username.find(" ") != -1:
    print("Your username can't have any spaces. Try again!")
elif not username.isalpha():
    print("Your username has non alphabetical character. Try again!")
else:
    print("Logged in successfully!")