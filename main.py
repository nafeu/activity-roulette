import os
from string import ascii_lowercase

DEFAULT_SESSION_LENGTH = 25
DEFAULT_NUM_ACTIVITIES = 1

session_length = DEFAULT_SESSION_LENGTH
num_activities = DEFAULT_NUM_ACTIVITIES

def prompt_initiate():
    print("Welcome to Activity Roulette! What would you like to do?")

    display_options(["Perform Activities", "Add Tasks"])

    user_input = raw_input(get_prompt())
    if len(user_input) < 1:
        print("(Performing activities)")
        prompt_select_length()
    elif user_input.lower() == "a":
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

    print("\nHow long do you want to work for?")

    display_options(["10", "15", "25", "60"])

    valid = True
    user_input = raw_input(get_prompt())
    if (len(user_input) < 1):
        print("(Session length: " + str(session_length) + " minutes)")
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

    print("\nHow many activities do you want to try?")

    valid = True
    user_input = raw_input(get_prompt())
    if (len(user_input) < 1):
        print("(Number of activities: " + str(num_activities) + ")")
    elif user_input.lower() == "q":
        exit()
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

def display_options(options):
    output = "\n"
    for index, value in enumerate(options):
        output += "[" + ascii_lowercase[index] + "] " + value + "\n"
    output = output.rstrip()
    print(output)

def get_divider():
    return "  "

def get_prompt():
    return "> "

def main():
    prompt_initiate()

if __name__ == '__main__':
    main()
