from turtle import clear
from morse_dict import morse_code_dict
from art import logo
import os

end_of_game = False
end_text = []


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def encrypt(text):
    """Translates letter text to morse text"""
    for item in text:
        end_text.append(morse_code_dict[item])
    print(end_text)
    print("".join(end_text))


def get_key(val):
    """Retrieves the key based on the value"""
    for key, value in morse_code_dict.items():
        if val == value:
            return key


def decrypt(text):
    """Translates morse text to letter text"""
    for item in text:
        end_text.append(get_key(item))
    print("".join(end_text))


# my_text = ["....", ".", ".-..", ".-..", "---"]
# decrypt(my_text)

# User experience


print("Welcome to the morse code translator!")

while not end_of_game:
    print(logo)
    user_choice = input("Do you want to encrypt pr decrypt?").lower()
    if user_choice == "encrypt":
        user_text = input("Please enter you text.\nSeparate letters with space\nSeparate the words with space*space")
        user_text = user_text.upper()
        user_text = [*user_text]
        encrypt(text=user_text)
    elif user_choice == "decrypt":
        user_text = input("Please enter you text.\nSeparate letters with space\nSeparate the words with space*space")
        user_text = user_text.split(' ')
        decrypt(text=user_text)
    else:
        print("You did not make a valid function.")
    refresh = (input("Do you want to refresh? Yes or No")).lower()
    if refresh == "no":
        end_of_game = True
    elif refresh == "yes":
        clear_screen()
