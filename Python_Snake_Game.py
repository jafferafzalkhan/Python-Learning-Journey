import random
dict_game = {
    "stone": "1",
    "paper": "2",
    "scissors": "3" 
}


computer_choice =random.choice(list(dict_game.keys()))
user_choice = input("Enter your choice (stone, paper, scissors): ").lower()

if user_choice not in dict_game:
    print("Invalid choice. Please choose stone, paper, or scissors.")
if user_choice == computer_choice:
    print(f"Both chose {user_choice}. It's a tie!")
elif (user_choice == "stone" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "stone") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print(f"You chose {user_choice} and the computer chose {computer_choice}. You win!")
else:
    print(f"You chose {user_choice} and the computer chose {computer_choice}. You lose!")   
    
