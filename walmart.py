import random
import time, sys

def script(str):

    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)

ask_name = input("""
            Welcome to Walmart! What is your name? """)

decision = input(f"""
            Would you like to start shopping {ask_name} (Y/N)? """).lower()


shopping_list = ['milk', 'bread', 'eggs', 'bananas']
# print(shopping_list)



if decision == "y":
    script(
"""
            Ok, lets go shopping!

            This is your shopping list:

            -milk
            -bread
            -eggs
            -bananas

""")

cart_contents = ['_'] * len(shopping_list)

print("""
            cart contents:""",
            cart_contents)


while decision == "y":
    choice = input("""

            What would you like to pickup?

            """).lower()

    if choice in shopping_list:
        print(f"""
            You chose {choice}""")
        if choice == "milk":
            script("""

            You proceed to the milk and come across a young boy yodeling.

            """)
            response_to_yodel_boy = input("""

            Yodel Boy wants to sing for you.

            A: You let him sing.
            B: Tell him no.
            C: Ask him for his autograph.

            """).lower()

            if response_to_yodel_boy == "a":
                script(
            """
            Well, I'm in lOoOove, I'm in loOOove, with a beautiful gaaal
            That's what's the matter with meeeeee
            Well, I'm in love, I'm in love, with a beautiful gaal
            But she don't care about meeee

            ******************************************************************

            Yodel Boy is very pleased you let him sing.
            He hands you a coupon for milk.

            """)
                milk_response_a = input("""

            You get to the milk, would you like to pick it up (Y/N)

             """).lower()

                if milk_response_a == "y":
                    for index, char in enumerate(shopping_list):
                        if char == choice:
                            cart_contents[index] = choice
                            script("""

            You added the milk to your cart

            """)
                            print("""
            cart contents

            """, cart_contents)
                else:
                    script("""

            Why did you walk all the way over here if you if you
            aren't going to put it in your cart?

                    """)


            if response_to_yodel_boy== "b":
                if "eggs" not in cart_contents:
                    script("""

            Yodel Boy is very angry that you would not let him sing.
            You go hide in the nearest bathroom until he calms down.

                    """)
                if "eggs" in cart_contents:
                    script("""

            Yodel Boy is very angry that you would not let him sing.
            He breaks your eggs.

                """)
                    cart_contents[2] = "_"
                    print(cart_contents)

                    milk_response_b = input("""
            You get to the milk, would you like to pick it up (Y/N) """).lower()
                    if milk_response_b == "y":
                        for index, char in enumerate(shopping_list):
                            if char == choice:
                                cart_contents[index] = choice
                                script("""

            You added the milk to your cart

                                """)
                                print("""

            cart contents

            """, cart_contents)
                    else:
                        script("""

            Why did you walk all the way over here if you if you
            aren't going to put it in your cart?

                            """)

            if response_to_yodel_boy == "c":
                script("""
            Yodel Boy is not signing autographs at this time.
            """)
                milk_response_c = input("""

            You get to the milk, would you like to pick it up (Y/N) """).lower()
                if milk_response_c == "y":
                    for index, char in enumerate(shopping_list):
                        if char == choice:
                            cart_contents[index] = choice
                            print("""
            You added the milk to your cart
                                """)
                            print("""
            cart contents""", cart_contents)
                else:
                    script("""

            Why did you walk all the way over here if you if you
            aren't going to put it in your cart?

                        """)



#if player chooses eggs*******************************************************



        if choice == "eggs":
            print("""

            You proceed to the eggs.

            """)
            response_to_scooter_woman = input("""
            You are in a hurry and a woman on a scooter is blocking the eggs.

            A: Wait for her to finish.
            B: Ask woman to scoot over so you can reach the eggs.

            """).lower()
            # milk will spoil while waiting
            if response_to_scooter_woman == "a":
                if "milk" not in cart_contents:
                    script("""

            Since you are so patient, you reward yourself with a sample of cheese.
            Go you!

                    """)
                    eggs_response_a = input("""
            You get to the eggs, would you like to pick them up (Y/N) """).lower()

                    if eggs_response_a == "y":
                        for index, char in enumerate(shopping_list):
                            if char == choice:
                                cart_contents[index] = choice
                                print("""
            You added the eggs to your cart""")
                                print("""
            cart contents""", cart_contents)
                    else:
                        script("""

            Why did you walk all the way over here if you if you
            aren't going to put it in your cart?

                        """)
                if "milk" in cart_contents:
                    script("""

            Your milk spoiled waiting for her to move. So sad!

                    """)
                    cart_contents[0] = "_"
                    print(cart_contents)

                    eggs_response_a = input("""
            You get to the eggs, would you like to pick them up (Y/N) """).lower()

                    if eggs_response_a == "y":
                        for index, char in enumerate(shopping_list):
                            if char == choice:
                                cart_contents[index] = choice
                                script("""
            You added the eggs to your cart""")
                                print("""
            cart contents""", cart_contents)
                    else:
                        script("""

            Why did you walk all the way over here if you if you
            aren't going to put it in your cart?

                        """)


            # scooter lady will randomly get mad if you ask her to move
            if response_to_scooter_woman == "b":
                mad_or_not = ['mad','not mad']
                attitude = random.choice(mad_or_not)
                if attitude == 'not mad':
                    script("""
            She is not mad. She kindly moves over and lets you get your eggs.

                """)
                    for index, char in enumerate(shopping_list):
                        if char == choice:
                            cart_contents[index] = choice
                            script("""
            You added eggs to your cart!""")
                            print("""
            cart contents""", cart_contents)

                if attitude == 'mad':
                    script("""
            She is so mad! She runs you over for being rude and you lose the
            contents of your cart.
                    """)
                    cart_contents = ['_'] * len(shopping_list)
                    script("""
            Your cart is now empty!""")
                    print(cart_contents)

#if the player chooses bread*************************************************


        if choice == "bread":
            script("""

            You proceed to the bread aisle.

            """)
            response_to_wet_floor = input("""
            You notice the floor is wet, what should you do?

            A: Go through the puddle.
            B: Tell an employee.

            """).lower()
            if response_to_wet_floor == "a":
                fall_or_not = ['fall','not fall','fall']
                accident = random.choice(fall_or_not)
                if accident == 'not fall':
                    script("""

            You bravely walk through the puddle, pick up the bread, and do not fall!
            Go you!

                """)
                    for index, char in enumerate(shopping_list):
                        if char == choice:
                            cart_contents[index] = choice
                            print("""
            You added bread to your cart!""")
                            print("""
            cart contents""", cart_contents)

                if accident == 'fall':
                    script("""
            You slip and fall in the floor. You sue Walmart and you get $1,000,000.
            You also get free groceries, congrats!.
                    """)
                    break
            if response_to_wet_floor == "b":
                script("""

            You told an employee about the puddle. You are now the town hero,
            but you still have to pay for your groceries.

                """)
                bread_response_a = input("""
            You get to the bread, would you like to pick them up (Y/N) """).lower()

                if bread_response_a == "y":
                    for index, char in enumerate(shopping_list):
                        if char == choice:
                            cart_contents[index] = choice
                            script("""
            You added the bread to your cart
            """)
                            print("""
            cart contents
            """, cart_contents)
                else:
                    script("""

            Why did you walk all the way over here if you if you
            aren't going to put it in your cart?

                    """)

# if the player chooses fruit************************************************
        if choice == "bananas":
            script("""

            You get to the fruit section and come across a monkey guarding the bananas.

             """)
            approach_monkey = input("""

            Do you want to approach the monkey? (Y/N)

             """).lower()
            if approach_monkey == "y":
                 script("""

            You chose to approach the monkey. The monkey would like to ask you a riddle.
            If you get the answer right, he will give you a banana.

            """)
                 answer_riddle = input("""
            Do you want to answer a riddle? (Y/N)

            """).lower()
                 if answer_riddle == "y":
                    riddle1 = input(
            """
            David's father has three sons: Snap, Crackle
            and_____?

                    """)
                    if riddle1 == "David" or "david":
                        script("""

            The monkey is pleased that you got the answer to his riddle right.
            The monkey gives you a banana.

                         """)
                        for index, char in enumerate(shopping_list):
                            if char == choice:
                                cart_contents[index] = choice
                                print("""
            cart contents""", cart_contents)
                    else:
                        script("""

            The monkey thinks you are very dumb. He is not going to give you a banana.

                         """)

                 if answer_riddle == "n":
                        script("""

            The monkey thinks you are boring and eats your bread.

                         """)
                        cart_contents[1] = "_"
                        print(cart_contents)


            if approach_monkey == "n":
                 script("""
            You can't complete your shopping trip if you don't get bananas""")
            #
            # for index, char in enumerate(shopping_list):
            #     if char == choice:
            #         cart_contents[index] = choice
            #         print("cart contents", cart_contents)
    if choice not in shopping_list:
        if choice == "exit":
            check = any(item in cart_contents for item in shopping_list)
            if check is True:
                script(
                """

            You left the store without paying.
            You have been arrested and are going to jail.
            Your wife is going to be so mad.

                """)
                break
            else:
                script("""

            You left the store without putting anything in your cart.
            Your wife is going to be so mad.

                """)
                break

        if choice != "exit":
            script("""

            That is not on your list, stick to the list!

            """)
    if shopping_list == cart_contents:
        print("""

            You got everything on your list!

         """)
        checkout_response = input("""

            Would you like to checkout? (Y/N)

         """).lower()

        if checkout_response == "y":
            script("""

            You get to the checkout line and there is only one register open.

            """)

            run_for_it = input("""

            Do you want to run for it? They probably won't catch you. (Y/N)

            """).lower()
            if run_for_it == 'y':
                script("""

            RUN FOR IT!

            """)
                caught_or_not = ['caught','not caught','not caught']
                outcome = random.choice(caught_or_not)
                if outcome == 'caught':
                    script("""
            You are caught running from the store. You are arrested and go to jail.
            Your wife is going to be so mad.

                """)
                    break
                if outcome == 'not caught':
                    script("""
            WOOOOO!!!! You got away with it you sneaky devil.
            Congrats on your free groceries.
                        """)
                    break

            if run_for_it == 'n':
                script("""

            It's probably for the best.

            Wow, you are such a good person!
            You checkout and leave the store.

            """)
                break

        if checkout_response == "n":
            leave_without_paying = input("""

            Are you sure you want to leave without paying? (Y/N)

                """).lower()
            if leave_without_paying == "y":
                script("""

            RUN FOR IT!

            """)
                caught_or_not2 = ['caught','not caught','not caught']
                outcome = random.choice(caught_or_not2)
                if outcome2 == 'caught':
                    script("""
            You are caught running from the store. You are arrested and go to jail.
            Your wife is going to be so mad.

                """)
                    break
                if outcome2 == 'not caught':
                    script("""
            WOOOOO!!!! You got away with it you sneaky devil.
            Congrats on your free groceries.
                        """)
                    break
            if leave_without_paying == "n":
                script("""
            Wow, you are such a good person!
            You checkout and leave the store.
                    """)
                break


        break


if decision == "N":
    print(f"""
            Bye {player_name} hope to see you again soon!""")
