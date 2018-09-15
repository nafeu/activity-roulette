import os

session_length = 30
num_activities = 1

def display_intro():
    print("Welcome to Activity Roulette\n")

def prompt_initiate():
    print("[a] Perform Activities")
    print("[b] Add Tasks")
    print("[q] Exit")

    user_input = raw_input("Select option: ")
    if user_input.lower() == "a" or len(user_input) < 1:
        prompt_length()
    elif user_input.lower() == "b":
        prompt_add_tasks()
    elif user_input.lower() == "q":
        exit()
    else:
        print("Invalid input.")
        prompt_initiate()

def prompt_length():
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

def main():
    display_intro()
    prompt_initiate()

if __name__ == '__main__':
    main()
