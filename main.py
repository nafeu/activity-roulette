import os
from string import ascii_lowercase

session_length = 30
num_activities = 1

def display_intro():
    print("Welcome to Activity Roulette\n")

def prompt_initiate():
    display_options(["Perform Activities", "Add Tasks"])

    user_input = raw_input("Select option: ")
    if user_input.lower() == "a" or len(user_input) < 1:
        prompt_select_length()
    elif user_input.lower() == "b":
        prompt_add_tasks()
    elif user_input.lower() == "q":
        exit()
    else:
        print("Invalid input.")
        prompt_initiate()

def prompt_select_length():
    print("LENGTH")

def prompt_add_tasks():
    print("ADD TASKS")

def prompt_yes_no(prompt_text):
  user_input = raw_input(prompt_text).lower()
  if (user_input == "y" or user_input == "yes" or len(user_input) == 0):
      return True
  else:
      return False

def load_from_file(file_name):
    with open("activities.txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

def clear():
    os.system('clear')

def display_options(options):
    for index, value in enumerate(options):
        print("[" + ascii_lowercase[index] + "] " + value)
    print("[q] Exit")

def main():
    display_intro()
    prompt_initiate()

if __name__ == '__main__':
    main()
