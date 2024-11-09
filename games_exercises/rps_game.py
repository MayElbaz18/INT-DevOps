# -----Rock Papper Sicssors Game-----

import random

def rps_game():
    rps_list = ["ROCK","PAPPER","SICSSORS"]
    computer_choice = random.choice(rps_list)


    while True:
        user_guess = str(input("Please Choose Rock, Papper Or Sicssors: ")).upper()

        if user_guess not in rps_list:
            print ("Invalid Input! Please Choose Rock, Papper Or Sicssors")
            
        
        elif user_guess == computer_choice:
            print("Its a Tie! Please Try Again!")
            continue

        elif user_guess == "ROCK" and computer_choice == "SICSSORS" or \
             user_guess == "PAPPER" and computer_choice == "ROCK" or \
             user_guess == "SICSSORS" and computer_choice == "PAPPER":
            
            print(f"Congratulations! You Win! Computer Choose: {computer_choice}.")
            break

        else:
            print(f"You Lose! Computer Choose: {computer_choice}")
            break


if __name__ == "__main__":
    rps_game()




    
