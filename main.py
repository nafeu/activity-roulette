import os
from string import ascii_lowercase

session_length = 25
num_activities = 1

def prompt_initiate():
    display_options("Welcome to Activity Roulette",
                    ["Perform Activities", "Add Tasks"])

    user_input = raw_input(": ")
    if user_input.lower() == "a" or len(user_input) < 1:
        prompt_select_length()
    elif user_input.lower() == "b":
        prompt_add_tasks()
    elif user_input.lower() == "q":
        exit()
    else:
        display_invalid_input()
        prompt_initiate()

def prompt_select_length():
    global session_length

    display_options("Select session length",
                    ["10", "15", "25", "60"])

    valid = True
    user_input = raw_input(": ")
    if (len(user_input) < 1):
        pass
    elif user_input.lower() == "a":
        session_length = 10
    elif user_input.lower() == "b":
        session_length = 15
    elif user_input.lower() == "c":
        session_length = 25
    elif user_input.lower() == "d":
        session_length = 60
    elif is_int(user_input):
        session_length = int(user_input)
    else:
        valid = False

    if not valid:
        display_invalid_input()
        prompt_select_length()
    else:
        prompt_select_num_activities()

def prompt_select_num_activities():
    global num_activities

    display_options("Select the number of activites you would like to complete",
                    ["1", "2", "3", "4"])

    valid = True
    user_input = raw_input(": ")
    if (len(user_input) < 1):
        pass
    elif user_input.lower() == "a":
        num_activities = 1
    elif user_input.lower() == "b":
        num_activities = 2
    elif user_input.lower() == "c":
        num_activities = 3
    elif user_input.lower() == "d":
        num_activities = 4
    elif is_int(user_input):
        num_activities = int(user_input)
    else:
        valid = False

    if not valid:
        display_invalid_input()
        prompt_select_num_activities()
    else:
        dump_values()

def dump_values():
    print(session_length)
    print(num_activities)

def is_int(input_string):
    try:
        int(input_string)
        return True
    except ValueError:
        return False

def display_invalid_input():
    print("Invalid input.")

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

def display_options(info, options):
    if (len(info) > 0):
        print(info + "\n")
    for index, value in enumerate(options):
        print("[" + ascii_lowercase[index] + "] " + value)
    print("[q] Exit")

def main():
    prompt_initiate()

if __name__ == '__main__':
    main()
