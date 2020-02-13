# import walmart
# import whole_foods
import time, sys

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def script(str):

    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
script(color.GREEN + color.BOLD + color.UNDERLINE + '\nWelcome to THE Choose Your Own Adventure Game!' + color.END)
script(color.BLUE + color.BOLD + '\n\nUsually, going to the grocery store is easy right?!' + color.END)
script(color.RED + color.BOLD + '\n\nThink again          muahahaha    ' + color.END)
script(color.YELLOW + color.BOLD + '\n\nPlayer 1....... are you ready? Y/N' + color.END)
player_ready = input(color.YELLOW + color.BOLD + '\n> ' + color.END)
if player_ready.lower() == 'y':
    script(color.YELLOW + color.BOLD + """
Let's get started!
What's your name?
> """ + color.END)
    player_name = input()
    script(color.GREEN + color.BOLD + '\nNice to meet you ' + player_name + color.END)
    script(color.RED + color.BOLD + '\nLET\'S DO THIS' + color.END)
    script(color.GREEN + '\n\n\nYour goal is simple, go to a grocery store and get items off the list' + color.END)
    script(color.GREEN + '\nHere\'s the kicker..   you have options' + color.END)
    script(color.YELLOW + '\nWould you like to shop at Walmart or Whole Foods?\n> ')
    store = input()
    if store.lowercase() == 'walmart':
        import walmart
    elif store.lowercase() == 'whole foods':
        import whole_foods
    else:
        print('You have to choose!')
elif player_ready.lower() == 'n':
    script(color.RED + color.BOLD + """
TOO BAD

LET'S
     GET
        STARTED!!
    """ + color.END)
    script(color.YELLOW + color.BOLD + 'What is your name?\n> ' + color.END)
    player_name = input()
    script(color.GREEN + color.BOLD + '\nNice to meet you ' + player_name + color.END)
    script(color.RED + color.BOLD + '\nLET\'S DO THIS' + color.END)
    script(color.GREEN + '\n\n\nYour goal is simple, go to a grocery store and get items off the list' + color.END)
    script(color.GREEN + '\nHere\'s the kicker..   you have options' + color.END)
    script(color.YELLOW + '\nWould you like to shop at Walmart or Whole Foods\n> ')
    store = input()
    if store == 'walmart':
        import walmart
    elif store == 'whole foods':
        import whole_foods
    else:
        print('You have to choose!')
