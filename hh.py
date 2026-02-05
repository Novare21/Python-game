
print("Hi, let's play a game!")
users = {}

def add_name(st):
      st["name"] =  input("What is your name?")
    
def add_family(st):
    st["family name"] = input("What is your family name?")
    
def add_age(st):
    st["age"] = int(input("How old are you?"))
    
def add_national_code(st):
    national = input("Enter your Nationalcode. ")
    st["national"] = national
   
def password(st):
         while True:
             password = input("Enter a password.")
             if password.isalnum() and len(password) >= 6:
                st["password"] = password
                break
             else:
                print("Password must be letters & numbers and at least 6 characters")
    
def information_show(st):
    print("name:", st.get("name","No name"))
    print("family name:", st.get("family name", "no family name"))
    print("age:", st.get("age", "no age"))
    print("national:", st.get("national", "no national"))
    print("password:", st.get("password",  "no password"))
#------------------------------------------------
information = {}
     
add_name(information)
add_family(information)
add_age(information)
add_national_code(information)
password(information)
information_show(information)

code = information["national"]
users[code] = information
print("\nUser saved successfully!\n")

search_code = input( " Enter national code to play game :")

if search_code in users:
    information_show(users[search_code])
else:
    print("User not found")

#---------------------
while True :
    answer = input("Do you want to continue? (yes / no): ").lower()    
    if answer == "yes":
        print(" Let's continue!")
        break
    elif answer == "no":
     print(" Game stopped. Bye!")
     exit()     
    else:
        print("Please answer yes or no")
 #start the game               
import random
                                
print(" Welcome to the Ultimate Guess the Number Game!")

high_score = 0

while True:
    number_to_guess = random.randint(0, 150)
    max_attempts = 10
    attempts = 0

    print("\nChoose a hint type:")
    print("1. Easy hint")
    print("2. Medium hint")
    print("3. Hard hint")

    hint_choice = input("Enter 1, 2, or 3: ")
    if hint_choice == "1":
        hint_type = "easy"
        hint_points = 5
    elif hint_choice == "2":
        hint_type = "medium"
        hint_points = 10
    elif hint_choice == "3":
        hint_type = "hard"
        hint_points = 15
    else:
        print("Invalid choice, defaulting to easy.")
        hint_type = "easy"
        hint_points = 5

    print("\nI have picked a number between 0 and 150. You have 10 tries!")

    while attempts < max_attempts:
        guess = int(input(f"Attempt {attempts + 1}: Your guess: "))
        attempts += 1

        if guess == number_to_guess:
            points = hint_points * (max_attempts - attempts + 1)
            print(f"🎉 Congratulations! You guessed it in {attempts} tries!")
            print(f"You earned {points} points!")

            if points > high_score:
                high_score = points
                print(f" New high score: {high_score} points!")
            else:
                print(f"High score: {high_score} points")
            break  # عدد درست حدس زده شد → پایان بازی

        else:
            # راهنمایی بر اساس نوع hint
            if hint_type == "easy":
                if guess < number_to_guess:
                    print("Try bigger!")
                else:
                    print("Try smaller!")
            elif hint_type == "medium":
                group = number_to_guess // 10 + 1
                if guess < number_to_guess:
                    print(f"🔹 Higher than {guess}! It's in group {group} of ten.")
                else:
                    print(f"🔹 Lower than {guess}! It's in group {group} of ten.")
            elif hint_type == "hard":
                low = max(0, number_to_guess - 10)
                high = min(150, number_to_guess + 10)
                print(f" The number is between {low} and {high}.")

        if attempts == max_attempts:
            print(f" Game over! The number was {number_to_guess}. No points earned.")
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print(f"Thanks for playing! Final high score: {high_score}")
        
        break
        
def show_win(st):
    purple = "\033[95m"
    reset = "\033[0m"
    win_text = """
██╗    ██╗██╗███╗   ██╗
██║    ██║██║████╗  ██║
██║ █╗ ██║██║██╔██╗ ██║
██║███╗██║██║██║╚██╗██║
╚███╔███╔╝██║██║ ╚████║
 ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝
"""
    print(purple + win_text + reset)
    
show_win(users)
    
#finish