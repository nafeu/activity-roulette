import os
import random
import datetime
from string import ascii_lowercase
from time import sleep

DEFAULT_SESSION_LENGTH = 25
DEFAULT_NUM_ACTIVITIES = 1
DEFAULT_RANDOM_ACTIVITY_AMOUNT = 5

session_length = DEFAULT_SESSION_LENGTH
num_activities = DEFAULT_NUM_ACTIVITIES
shortlist = []
queue = []

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
        prompt_arrange_shortlist()

def prompt_arrange_shortlist():
    global shortlist

    print("\nArrange your shortlist:")

    display_activity_list()

    user_input = raw_input(get_prompt())
    if (len(user_input) < 1):
        shortlist = get_random_activities(DEFAULT_RANDOM_ACTIVITY_AMOUNT)
    else:
        shortlist = get_shortlist_by_input(user_input)

    create_queue()
    prompt_prepare_to_start()

def prompt_prepare_to_start():
    global queue

    raw_input("\n[ Prepare your activity area. Once you are ready, press enter to spin ] :")

    while len(queue) > 0:
        print("\n........................\n....... SPINNING .......\n........................")
        sleep(3)
        print(".##..##...####...##..##.\n..####...##..##..##..##.\n...##....##..##..##..##.\n...##....##..##..##..##.\n...##.....####....####..\n........................")
        sleep(0.5)
        print("..####....####...######.\n.##......##..##....##...\n.##.###..##..##....##...\n.##..##..##..##....##...\n..####....####.....##...\n........................")
        sleep(0.5)
        activity_ipr = queue.pop();
        print("\n >>> [ " + activity_ipr['name'] + " for " + activity_ipr['length'] + " minutes ] <<<\n")
        # sleep(3)
        now = datetime.datetime.now()
        print("Confirm completion of [ " + activity_ipr['name'] + " for " + activity_ipr['length'] + " minutes ] performed " + now.strftime("%a, %b %-d at %I:%M %p"))
        if prompt_yes_no(get_prompt()):
            with open("log.txt", "a+") as f:
                f.write(now.strftime("%a, %b %-d, %Y %H:%I %p") + " - [ " + activity_ipr['name'] + " for " + activity_ipr['length'] + " minutes ]\n")
        else:
            pass
        if (len(queue) > 0):
            raw_input("\n[ " + str(len(queue)) + " tasks remaining. Press enter to spin again ] :")

    print("All activities completed...")

def create_queue():
    global num_activities

    random.shuffle(shortlist)
    while num_activities > 0 and len(shortlist) > 0:
        work_item = {
            "complete": False,
            "name": shortlist.pop(),
            "length": str(int(round(session_length / num_activities)))
        }
        queue.insert(0, work_item)
        num_activities -= 1

def get_shortlist_by_input(user_input):
    ids = list(set(user_input.split(" ")))
    activities = load_from_file("activities.txt")
    output = []
    for item in ids:
        if is_int(item):
            index = int(item)
            if index >= 0 and index < len(activities):
                output.append(activities[index])
    return output

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

def display_activity_list():
    activities = load_from_file("activities.txt")
    print("")
    for index, value in enumerate(activities):
        print("[" + str(index) + "] " + value)

def get_random_activities(amount):
    activities = load_from_file("activities.txt")
    if (amount > len(activities)):
        return activities
    return random.sample(activities, amount)

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
