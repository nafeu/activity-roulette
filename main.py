def display_intro():
  print("Welcome to Creator's Roulette")
  if (prompt_yes_no("Begin?")):
    print("okie dokes")
  else:
    print("nvm")

def prompt_yes_no(prompt_text):
  user_input = raw_input(prompt_text).lower()
  if (user_input == "y" or user_input == "yes" or len(user_input) == 0):
    return True
  else:
    return False

def main():
  display_intro()

if __name__ == '__main__':
  main()
