import random

def number_guessing_game():

    secret_number = random.randint(1, 100)
    attempts = 0

    while True: #------Loop For Handle User Input Until Correct-----#
        try:
            user_guess = int(input("Please Guess The Secret Number Between 1 To 100: "))

            if user_guess < 1 or user_guess > 100:
                print('Please Enter Number Between 1 To 100!')
                continue

            attempts += 1

            if user_guess == secret_number:
                print(f'Congratulations! You Guessed The Secret Number ({secret_number})! In {attempts} Attempts!')
                break

            elif user_guess < secret_number:
                print(f'{user_guess} Is Too Low!, Plesae Try Higher Number!')
                
            else:
                print(f'{user_guess} Is Too High!, Please Try Lower Number!')

        except ValueError: #-------Handle Keys Error (If Not INT)-------#
            print('Invalid Input!, Please Enter A Valid Number!') 


if __name__ == "__main__":
    number_guessing_game()                            

    