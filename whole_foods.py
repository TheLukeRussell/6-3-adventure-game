import random

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

number = random.randint(1, 50)

name = 'Jezebel'
print(color.RED + color.BOLD)
print('\n Congrats ' + name + '! You have chosen the high-class, but expensive route of a health foods store. Be prepared to face the challenges of the rich, wealthy and pretentious 1 percent of modern America.')
print(color.END)
print(color.GREEN)
print(
    """
    Your shopping list includes:
    > Milk
    > Bread
    > Eggs
    > Fruit
    """)
print(color.BLUE)
print('\n You have 30 minutes inside Whole Foods to finish your shopping list or else you will be late for dinner')
print('\n So what are you thinking ' + name + '? Do you think you can get your groceries becolor it is time for dinner?')
print(color.YELLOW)
print('Choose y/n')
minutes = 0
cart = 0
unfinished = 1

while minutes < 30:
    print(color.YELLOW)
    userInput = input('> ')
    userInput = userInput.lower()

    if userInput == '':
        print('Come on.. you need to choose')

    elif userInput == 'n':
        print(color.RED)
        print('\n You were not ready to get groceries so you went home without any \n and your significant other asked for a divorce and the night was ruined')
        print('\n You lose, and now you are single')
        unfinished = 0
    else:
        print(color.BLUE)
        print('\n Great! Let\'s get started!')
        print('\n So ' + name + ' Which item would you like to start with?')
        print(color.YELLOW)
        print("\n You have a choice between 'milk', 'eggs', 'fruit', or 'bread'")
        grocery_list = input('> ')
        if grocery_list.lower() == 'milk':
            print(color.BLUE)
            print('\nYou chose milk which is the aisle furthest away from you so you lose 10 minutes of time!')
            minutes += 10
            print('\nOn the way to grab your milk, your old friend Beatrice stops you and asks if you have a couple minutes to chat')
            print('\nWould you like to stop and chat with Beatrice?')
            print(color.YELLOW)
            print("\nType: 'Talk to Beatrice' or 'walk away'")
            milk_choice = input('> ')
            print(color.BLUE)
            if milk_choice.lower() == 'talk to beatrice':
                print('\nBeatrice talks about her church congregation but sees that you are in a hurry. Beatrice gives you her bread so you don\'t have to get it yourself!')
                cart += 2
                print(color.YELLOW)
                print('\nNow that you already have milk and bread, would you like to move on to the eggs or fruit next?')
                print("\nType: 'eggs' or 'fruit'")
                eggs_fruit = input('> ')
                print(color.BLUE)
                if eggs_fruit.lower() == 'eggs':
                    print('\nGreat let\'s head to the egg aisle')
                    print('\nOH NO! All of the eggs are broken! You now have to wait 10 minutes while an employee acquires a new box of eggs')
                    minutes += 10
                    print(color.RED)
                    print('\nYou now have spent 20 minutes in Whole Foods')
                    cart += 1
                    print(color.BLUE)
                    print('\n Finally you head to the fruit aisle to pick up your last item')
                    print(color.YELLOW)
                    print('\n Would you like to ask an employee for help finding your items?')
                    print("\nType: 'help me' or 'go away'")
                    employee_help = input('> ')
                    print(color.BLUE)
                    if employee_help.lower() == 'help me':
                        print('\nYou meet a kind worker who helps you find all the fruits you were looking for in a short amount of time!')
                        minutes += 2
                        print(color.RED)
                        print('\nYou now have spent 22 minutes in Whole Foods')
                        cart += 1
                        print(color.Blue)
                    elif employee_help.lower() == 'go away':
                        print('\nYou try to grab all the fruit but end up knocking over a few of the shelves because you do not have enough hands')
                        print('\nYou are escorted out of the store becolor you got your last item and went home without groceries')
                        unfinished = 0
                    else:
                        print('Come on.. you need to choose')
                        
                elif eggs_fruit.lower() == 'fruit':
                    print('\nGreat let\'s head to the fruit aisle')
                    print('\nYou meet a kind worker who helps you find all the fruits you were looking for in a short amount of time!')
                    minutes += 2
                    print(color.RED)
                    print('\nYou now have spent 12 minutes in Whole Foods')
                    cart += 1
                    print(color.BLUE)
                    print('\n Now, we have one more item left. Let\'s head to the egg aisle!')
                    print(color.YELLOW)
                    print('\nOH NO! All of the eggs are broken! Would you like to wait for an employee to get fresh eggs or would you like to take broken eggs home?')
                    print("\n Type: 'Get help' or 'broken eggs'")
                    broken_eggs = input('> ')
                    print(color.Blue)
                    if broken_eggs.lower() == 'get help':
                        print('\nThe broken eggs only take 15 minutes to get!')
                        print(color.RED)
                        print('\nYou now have spent 27 minutes at Whole Foods')
                        print(color.BLUE)
                        cart += 1
                    elif broken_eggs.lower() == 'broken eggs':
                        print('\nYour significant other SCREAMED at you for bringing home broken eggs')
                        print('\nEven though you got all the items, you got screamed at, so did you really win?')
                        print('\n NOPE YOU DID NOT')
                        unfinished = 0
                    else:
                        print('Come on.. you need to choose')
                else:
                    print('Come on.. you need to choose')
            elif milk_choice.lower() == 'walk away':
                print(color.RED)
                print('\nBeatrice screams at you for not wanting to talk. You and Beatrice are escorted out and you leave with no groceries or self-esteem. :(')
                print(color.BLUE)
                unfinished = 0
            else:
                print('Come on.. you need to choose')
        elif grocery_list.lower() == 'bread':
            print('\nYou chose bread which is the aisle right in front of you so you do not lose any time!')
            minutes += 0
            cart += 1
            print('\nYou see someone put the last loaf of bread in their cart but falls out after')
            print(color.YELLOW)
            print('\nDo you bring them the last loaf or keep it for yourself?')
            print("\nType: 'Tell them' or 'Take it'")
            last_loaf = input('> ')
            print(color.BLUE)
            if last_loaf.lower() == 'tell them':
                print('\nThey are so grateful that you told them that they give you the remaining groceries on your list')
                print('\nYou thank them for their help and invite them over for dinner!')
                cart += 3
                print(color.ready)
            elif last_loaf.lower() == 'take it':
                print("\nYou were set up and was a secret contestant on the game-show 'What Would You Do?'. You failed the challenge and now have spent too much time at the store")
                print('\nYou spend an hour talking to TV cameras and the producers')
                minutes += 60
                print(color.BLUE)
            else:
                print('Come on.. you need to choose')
        elif grocery_list.lower() == 'eggs':
            print('\nYou chose eggs which is the second closest aisle so you lose 2 minutes')
            minutes += 2
            print(color.YELLOW)
            print('\nWhile grabbing the eggs, you see someone trying to steal some cookie dough!! What are you going to do?!')
            cart += 1
            print("\nType: 'Tell someone' or 'Let it go'")
            thief = input('> ')
            print(color.BLUE)
            if thief.lower() == 'tell someone':
                print('\nYou reported the robber to the store manager')
                print(color.RED)
                print('\nOH NO! The robber pulls a gun on the manager and holds the entire store hostage for 5 hours!!')
                print('I think it is safe to say you will not get to dinner on time...')
                minutes += 300
                print(color.BLUE)
            elif thief.lower() == 'let it go':
                print('\nYou feel bad about the robber getting away with the cookie dough but he rewards you with a loaf of bread')
                cart += 1
                minutes += 7
                print('\nFeeling guilty AF, you still need to carry on and figure out what your next item needs to be')
                print(color.YELLOW)
                print('\nWould you like to go to the milk aisle or the fruit aisle')
                print("\nType: 'milk' or 'fruit'")
                milk_fruit = input('> ')
                print(color.BLUE)
                if milk_fruit.lower() == 'milk':
                    print('\nOn the way to grab your milk, your old friend Beatrice stops you and asks if you have a couple minutes to chat')
                    print(color.YELLOW)
                    print('\nWould you like to stop and chat with Beatrice?')
                    print("\nType: 'Talk' or 'Walk'")
                    choice_milk = input('> ')
                    print(color.BLUE)
                    if choice_milk.lower() == 'talk':
                        print('\nYou and Beatrice talk about politics and the way of life')
                        print('\nThe conversation lasts for 10 minutes but you end up being able to get you milk')
                        minutes += 10
                        cart += 1
                        print('\nNow we are off to the fruit aisle for the last item!')
                        print('\nYou notice they are giving out free samples of the honeycrisp apples')
                        print(color.YELLOW)
                        print('\nWould you like to try a sample?')
                        print("\nType: 'I love honeycrisp' or 'no honeycrisp for me'")
                        honeycrisp = input('> ')
                        print(color.BLUE)
                        if honeycrisp.lower() == 'i love honeycrisp':
                            print(color.RED)
                            print('\n Oh No!! The apple gave you food poisoning and you spent 37 minutes in the bathroom!')
                            minutes += 37
                            print(color.BLUE)
                        elif honeycrisp.lower() == 'no honeycrisp for me':
                            print(color.GREEN)
                            print('\nThat was probably a good choice, the apple looked a little weird to me')
                            print(color.BLUE)
                            print('You grab the fruit you need and walk out the door in 5 minutes')
                            cart += 1
                            minutes += 5
                        else:
                            print('Come on.. you need to choose')
                    elif choice_milk.lower() == 'walk':
                        print(color.RED)
                        print('\nBeatrice screams at you for not wanting to talk. You and Beatrice are escorted out and you leave with no groceries or self-esteem. :(')
                        unfinished = 0
                        print(color.BLUE)
                    else:
                        print('Come on.. you need to choose')
                elif milk_fruit.lower() == 'fruit':
                    print('\nSo you decided to grab some fruit huh?')
                    print(color.YELLOW)
                    print('\nThere is one stipulation if you want to start with fruit though..')
                    print('\nAre you up for it?')
                    print("\nType: 'duh' or 'nah fam'")
                    workout = input('> ')
                    print(color.BLUE)
                    if workout.lower() == 'nah fam':
                        print('\nSomeone as stubborn as you deserves to shop at Whole Foods for the rest of your life')
                        print('\nYou win free groceries for life with 10 minute delivery so go home and enjoy you dinner')
                        cart += 1
                        
                        print(color.DARKCYAN)
                    elif workout.lower() == 'duh':
                        print('\nGreat! If you want your groceries, you have to pass this challenge')
                        print('I am going to randomize a number between 1-50 and if it is over 25, you have to leave without groceries.\n If you win, you get to go home and your shopping trip will be over')
                        
                        print(color.YELLOW)
                        print('\nReady?')
                        print("\nType: 'yes' or 'no'")
                        ready = input('> ')
                        if ready.lower() == 'yes':
                            
                            print(color.CYAN)
                            print('\nYour number is.... ')
                            print(number)
                            
                            print(color.BLUE)
                            if number <= 25:
                                print('Congrats, you did it!')
                                cart += 1
                                minutes += 15
                            else:
                                unfinished = 0
                                
                                print(color.RED)
                        elif ready.lower() == 'no':
                            print('Wow, you can\'t even do the challenge, get out of here!')
                            unfinished = 0
                            
                        else:
                            print(color.BLUE)
                            print('Come on.. you need to choose')
                    else:
                        print('Come on.. you need to choose')
                else:
                    print('Come on.. you need to choose')
            else:
                print('Come on.. you need to choose')
        elif grocery_list.lower() == 'fruit':
            print(color.BLUE)
            print('\nYou chose fruit which is the 3rd closest aisle so you lose 3 minutes')
            minutes += 3
            print('\nThe fruit you acquire was just stocked on the shelf so you know you are getting the best fruit')
            cart += 1
            
            print(color.YELLOW)
            print('\nWhich aisle would you like to go to next?')
            print("\nType: 'milk', 'eggs', or 'bread'")
            aisle_list = input('> ')
            
            print(color.BLUE)
            if aisle_list.lower() == 'milk':
                print('\nOn the way to the milk aisle, you catch the Corona Virus and need to drink a case of Corona Light\'s to cure yourself')
                print(color.YELLOW)
                print('\nDo you drink the Corona\'s or do you head home to stop the spread of the disease?')
                print("\nType: 'Lifes a beach' or 'Head home'")
                corona = input('> ')
                print(color.RED)
                if corona.lower() == 'lifes a beach':
                    print('\nOh no! You go drunk at Whole Foods on a Tuesday afternoon')
                    unfinished = 0
                elif corona.lower() == 'head home':
                    print('\nEven though you did the right thing, you still get chewed out by your significant other for not getting groceries')
                    unfinished = 0
                    
                    print(color.BLUE)
                else:
                    print('Come on.. you need to choose')
            elif aisle_list.lower() == 'eggs':
                print('\nYou head to the egg aisle to continue your shopping.')
                print('\nIt takes you 10 minutes to get to the bread aisle because you got distracted by the charcuterie boards that were on sale')
                
                print(color.RED)
                print('\nYou pick up the eggs and head over to the milk aisle because you saw your ex in the bread aisle')
                cart += 1
                minutes += 10
                
                print(color.YELLOW)
                print('\nEven though you tried avoiding them, your ex spots you trying to escape and wants to have a conversation, what do you do?')
                print("Type: 'Stay and talk' or 'Bye Felicia'")
                ex_lover = input('> ')
                
                print(color.BLUE)
                if ex_lover.lower() == 'stay and talk':
                    print('You stay and catch up with your ex and find out that she owns the store! She gives you the rest of your items for free!')
                    cart += 2
                    minutes += 6
                    
                    print(color.RED)
                elif ex_lover.lower() == 'bye felicia':
                    print('Your ex, having learned Mixed-Martial-Arts post-breakup, kicks you in the face for dissing her and you have to spend 45 minutes in the bathroom cleaning up your bloody nose.')
                    minutes += 45
                    
                    print(color.BLUE)
                else:
                    print('Come on.. you need to choose')
            elif aisle_list.lower() == 'bread':
                print('\nYou head to the bread aisle to continue your shopping.')
                print('\nThe bread is laid out nicely on the shelf and you put it in your cart')
                cart += 1
                minutes += 2
                
                print(color.YELLOW)
                print('\nWould you like to head to the milk or egg aisle?')
                print("Type: 'milk' or 'eggs'")
                milk_egg = input('> ')
                
                print(color.BLUE)
                if milk_egg.lower() == 'milk':
                    print('You head to the milk aisle to grab some milk for your family but the milk is out of stock due to the Milk Crisis of 2020')
                    print(color.RED)
                    print('You leave the store knowing you will get an earful from your significant other')
                    unfinished = 0
                    
                    print(color.BLUE)
                elif milk_egg.lower() == 'eggs':
                    print('Lucky You! The eggs and the milk section were recently moved right next to each other!')
                    print('You grab the last two items and make your way home')
                    minutes += 3
                    cart += 2
                else:
                    print('Come on.. you need to choose')
            else:
                print('Come on.. you need to choose')
                
        else:
            print('Come on.. you need to choose')
            
    if cart == 4:
        print(color.DARKCYAN)
        print('\nCongrats! You got all you items!')
        minutes = str(minutes)
        print('And it only took you ' + minutes + ' minutes')
        print("""
$$\     $$\  $$$$$$\  $$\   $$\       $$\      $$\ $$$$$$\ $$\   $$\ 
\$$\   $$  |$$  __$$\ $$ |  $$ |      $$ | $\  $$ |\_$$  _|$$$\  $$ |
 \$$\ $$  / $$ /  $$ |$$ |  $$ |      $$ |$$$\ $$ |  $$ |  $$$$\ $$ |
  \$$$$  /  $$ |  $$ |$$ |  $$ |      $$ $$ $$\$$ |  $$ |  $$ $$\$$ |
   \$$  /   $$ |  $$ |$$ |  $$ |      $$$$  _$$$$ |  $$ |  $$ \$$$$ |
    $$ |    $$ |  $$ |$$ |  $$ |      $$$  / \$$$ |  $$ |  $$ |\$$$ |
    $$ |     $$$$$$  |\$$$$$$  |      $$  /   \$$ |$$$$$$\ $$ | \$$ |
    \__|     \______/  \______/       \__/     \__|\______|\__|  \__|
    """)
        break

    if minutes >= 31:
        print(color.RED)
        print('\nBOO! You did not get all of your items!')
        minutes = str(minutes)
        print('You spent ' + minutes + ' minutes at the store')
        print("""
$$\     $$\  $$$$$$\  $$\   $$\       $$\       $$$$$$\   $$$$$$\  $$$$$$$$\ 
\$$\   $$  |$$  __$$\ $$ |  $$ |      $$ |     $$  __$$\ $$  __$$\ $$  _____|
 \$$\ $$  / $$ /  $$ |$$ |  $$ |      $$ |     $$ /  $$ |$$ /  \__|$$ |      
  \$$$$  /  $$ |  $$ |$$ |  $$ |      $$ |     $$ |  $$ |\$$$$$$\  $$$$$\    
   \$$  /   $$ |  $$ |$$ |  $$ |      $$ |     $$ |  $$ | \____$$\ $$  __|   
    $$ |    $$ |  $$ |$$ |  $$ |      $$ |     $$ |  $$ |$$\   $$ |$$ |      
    $$ |     $$$$$$  |\$$$$$$  |      $$$$$$$$\ $$$$$$  |\$$$$$$  |$$$$$$$$\ 
    \__|     \______/  \______/       \________|\______/  \______/ \________|
        """)
        break

    if unfinished == 0:
        print('\nBOO! You did not get all of your items!')
        minutes = str(minutes)
        print('You spent ' + minutes + ' minutes at the store')
        print("""
$$\     $$\  $$$$$$\  $$\   $$\       $$\       $$$$$$\   $$$$$$\  $$$$$$$$\ 
\$$\   $$  |$$  __$$\ $$ |  $$ |      $$ |     $$  __$$\ $$  __$$\ $$  _____|
 \$$\ $$  / $$ /  $$ |$$ |  $$ |      $$ |     $$ /  $$ |$$ /  \__|$$ |      
  \$$$$  /  $$ |  $$ |$$ |  $$ |      $$ |     $$ |  $$ |\$$$$$$\  $$$$$\    
   \$$  /   $$ |  $$ |$$ |  $$ |      $$ |     $$ |  $$ | \____$$\ $$  __|   
    $$ |    $$ |  $$ |$$ |  $$ |      $$ |     $$ |  $$ |$$\   $$ |$$ |      
    $$ |     $$$$$$  |\$$$$$$  |      $$$$$$$$\ $$$$$$  |\$$$$$$  |$$$$$$$$\ 
    \__|     \______/  \______/       \________|\______/  \______/ \________|
        """)
        break