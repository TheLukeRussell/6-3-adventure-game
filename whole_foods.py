name = 'Jezebel'

print('\n Congrats ' + name + '! You have chosen the high-class, but expensive route of a health foods store. Be prepared to face the challenges of the rich, wealthy and pretentious 1 percent of modern America.')

print(
    """\n 

    Your shopping list includes:

    > Milk
    > Bread
    > Eggs
    > Fruit

    """)

print('\n Clearly you have chosen the healthier choice so every item you need from your list must be of organic nature')
print('\n You have 30 minutes inside Whole Foods to finish your shopping list or else you will be late for dinner')
print('\n So what are you thinking ' + name + '? Do you think you can get your groceries before it is time for dinner?')
print('\n Choose y/n')

minutes = 0
cart = 0

while minutes < 30:

    userInput = input('> ')
    userInput = userInput.lower()



    if userInput == '':
        print('Come on.. you need to choose')

    elif userInput == 'n':
        print('\n You were not ready to get groceries so you went home without any \n and your significant other asked for a divorce and the night was ruined')
        print('\n You lose, and now you are single')
        break

    else:
        print('\n Great! Let\'s get started!')
        print('\n So ' + name + ' Which item would you like to start with?')
        if userInput == 'milk':
            print('\nYou chose milk which is the aisle furthest away from you so you lose 5 minutes of time!')
            minutes += 5

            print('\nOn the way to grab your milk, your old friend Beatrice stops you and asks if you have a couple minutes to chat')
            print('\nWould you like to stop and chat with Beatrice?')
            print("\nType: 'Talk to Beatrice' or 'walk away'")

            milk_choice = input()

            if milk_choice.lower() == 'talk to beatrice':
                print('\nBeatrice talks about her church congregation but sees that you are in a hurry. Beatrice gives you her bread so you don\'t have to get it yourself!')
                cart += 2 
            elif milk_choice.lower() == 'walk away':
                print('\nBeatrice screams at you for not wanting to talk. You and Beatrice are escorted out and you leave with no groceries or self-esteem. :(')
                break

        elif userInput == 'bread':
            print('\nYou chose bread which is the aisle right in front of you so you do not lose any time!')
            minutes += 0
        elif userInput == 'eggs':
            print('\nYou chose eggs which is the second closest aisle so you lose 2 minutes')
            minutes += 2
        elif userInput == 'fruit':
            print('\nYou chose fruit which is the 3rd closest aisle so you lose 3 minutes')
            minutes += 3