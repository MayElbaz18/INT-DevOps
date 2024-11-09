# 1. os module

import os

cwd = os.getcwd()    #---------Showing your current directory-----------#
print(f"Current Working Directory: {cwd}")

directory = "exercise_folder"
path = os.path.join(cwd, directory)
os.chdir('exercise_folder')    #------Changing Directory-------#
cwd = os.getcwd()
print(f"Directory: {cwd}")
os.mkdir(path)   #-------Crating Directory--------#
print(f"{directory} Created in {cwd}!")

with open('example.txt', 'w') as fp: #-------Creating a file--------#
    pass

dir_list = os.listdir()
print(dir_list)

# 2. datetime module

from datetime import datetime
#-----Get the current date and time-----#
current_datetime = datetime.now()
#-----Format the date and time as "YYYY-MM-DD HH-MM"-----#
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H-%M")
#-----Print the formatted date and time-----#
print(f"The Current Date+Time Is: {formatted_datetime}")

# 3. random module

import string
import random
 
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = [random.choice(characters) for _ in range(length)]
    password_string = ''.join(password)
    return password_string

length = int(input("Enter Password Length To Generate: "))
password = generate_password(length)
print(f"Password: {password}") 

# 4. json module

import json

my_book = {
    "title" : "The Secret",
    "author" : "M.Elbaz",
    "year" : 2024
}

with open("book.json", "w") as outfile:
    json.dump(my_book, outfile, indent=3)