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

def create_files():
    for data_file in ["activities.txt", "log.txt"]:
        if not os.path.exists(data_file):
            with open(data_file, "w+") as f:
                if data_file == "activities.txt":
                    f.write("Edit activity list using 'aredit' command\n")
                else:
                    f.write("")

def prompt_initiate():
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
        prompt_initiate()()
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

    if user_input.lower() == "q":
        exit()
    elif (len(user_input) < 1):
        shortlist = get_random_activities(DEFAULT_RANDOM_ACTIVITY_AMOUNT)
    else:
        shortlist = get_shortlist_by_input(user_input)

    if len(shortlist) < 1:
        print("\nNo items matched, please try again.")
        prompt_arrange_shortlist()
    else:
        print("\nAre you okay with these activities? (y/n)\n")
        for item in shortlist:
            print("    " + strip_item_tags(item))

        if prompt_yes_no(get_prompt()):
            create_queue()
            prompt_prepare_to_start()
        else:
            prompt_arrange_shortlist()


def prompt_prepare_to_start():
    global queue

    user_input = raw_input("\n[ Prepare your activity area. Once you are ready, press enter to spin ] : ")

    if user_input.lower() == "q":
        exit()

    while len(queue) > 0:
        print("\n    ........................\n    ....... SPINNING .......\n    ........................")
        sleep(3)
        print("    .##..##...####...##..##.\n    ..####...##..##..##..##.\n    ...##....##..##..##..##.\n    ...##....##..##..##..##.\n    ...##.....####....####..\n    ........................")
        sleep(0.5)
        print("    ..####....####...######.\n    .##......##..##....##...\n    .##.###..##..##....##...\n    .##..##..##..##....##...\n    ..####....####.....##...\n    ........................")
        sleep(0.5)
        activity_ipr = queue.pop();
        print("\n    " + activity_ipr['name'] + " for " + activity_ipr['length'] + " minutes")
        print("\n    ........................\n    ........................")
        now = datetime.datetime.now()
        sleep(5)
        if prompt_yes_no("\n[ Upon completion, confirm: " + activity_ipr['name'] + " for " + activity_ipr['length'] + " minutes performed " + now.strftime("%a, %b %-d at %I:%M %p") + " ] : "):
            print("(Activity logged)")
            with open("log.txt", "a+") as f:
                f.write(now.strftime("%a, %b %-d, %Y %H:%I %p") + " - [ " + activity_ipr['name'] + " for " + activity_ipr['length'] + " minutes ]\n")
        else:
            print("(Activity discarded)")
        if (len(queue) > 0):
            user_input = raw_input("\n[ " + str(len(queue)) + " remaining. Press enter to spin again ] : ")
            if user_input.lower() == "q":
                exit()

    prompt_queue_empty()

def prompt_queue_empty():
    global session_length
    global num_activities
    session_length = DEFAULT_SESSION_LENGTH
    num_activities = DEFAULT_NUM_ACTIVITIES

    if prompt_yes_no("\nNo activities left, would you like to start again? (y/n)\n\n> "):
        prompt_initiate()
    else:
        print("\nThank you for using Activity Roulette.")


def create_queue():
    global num_activities

    random.shuffle(shortlist)
    length = str(int(round(session_length / num_activities)))
    while num_activities > 0 and len(shortlist) > 0:
        work_item = {
            "complete": False,
            "name": shortlist.pop(),
            "length": length
        }
        queue.insert(0, work_item)
        num_activities -= 1

def get_shortlist_by_input(user_input):
    output = []
    activities = load_from_file("activities.txt")

    ids_by_tag = get_activity_ids_by_tags(activities, [tag.strip() for tag in user_input.split(",")])
    if len(ids_by_tag) > 0:
        ids = ids_by_tag
    elif "," in user_input:
        ids = list(set(user_input.split(",")))
    else:
        ids = list(set(user_input.split(" ")))

    for item in ids:
        if is_int(item):
            index = int(item)
            if index >= 0 and index < len(activities):
                output.append(activities[index])

    return output

def get_activity_ids_by_tags(activities, input_tags):
    output = []
    for index, tags in enumerate([get_item_tags(item) for item in activities]):
        for tag in tags:
            if tag in input_tags:
                output.append(index)
                break
    return output

def is_int(input_string):
    try:
        int(input_string)
        return True
    except ValueError:
        return False

def display_invalid_input():
    print("Invalid input.")

def prompt_yes_no(prompt_text):
    user_input = raw_input(prompt_text).lower()
    if user_input == "q":
        exit()
    if (includes_yes_utterance(user_input) or len(user_input) == 0):
        return True
    else:
        return False

def load_from_file(file_name):
    with open(file_name) as f:
        content = f.readlines()
    content = [x.strip() for x in content if is_valid_activity(x)]
    return content

def is_valid_activity(activity):
    if len(activity) < 2 or activity[0] == "#":
        return False
    return True

def display_activity_list():
    activities = load_from_file("activities.txt")
    available_tags = ", ".join(get_all_tags(activities)).rstrip()
    print("\nAvailable tags: " + available_tags + "\n")

    for index, value in enumerate(activities):
        print("    [" + str(index) + "] " + strip_item_tags(value))

def get_random_activities(amount):
    print("(Randomly picking " + str(amount) + " activities for shortlist)")
    activities = load_from_file("activities.txt")
    if (amount > len(activities)):
        return activities
    return random.sample(activities, amount)

def clear():
    os.system('clear')

def display_options(options):
    output = "\n"
    for index, value in enumerate(options):
        output += "    [" + ascii_lowercase[index] + "] " + value + "\n"
    output = output.rstrip()
    print(output)

def get_divider():
    return "  "

def get_prompt():
    return "\n> "

def get_item_tags(raw_item):
    tags = raw_item.split(" (")
    if len(tags) > 1:
        return [item.strip() for item in tags[1].rstrip(")").split(",")]
    return []

def get_all_tags(activities):
    output = []
    for activity in activities:
        tag_split = activity.split(" (")
        if len(tag_split) > 1:
            for tag in tag_split[1].rstrip(")").split(","):
                output.append(tag.strip())
    return list(set(output))

def strip_item_tags(raw_item):
    return raw_item.split(" (")[0]

def includes_yes_utterance(user_input):
    if "y" in user_input:
        return True
    return False

def main():
    create_files()
    print("Welcome to Activity Roulette!")
    prompt_initiate()

if __name__ == '__main__':
    main()
