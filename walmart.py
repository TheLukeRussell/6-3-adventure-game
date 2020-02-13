import random

print("Welome to Walmart! {name}")

decision = input('Would you like to start shopping? (Y/N)').lower()


shopping_list = ['milk', 'bread', 'eggs', 'fruit']
# print(shopping_list)



if decision == "y":
    print(
"""
Ok, lets go shopping!

This is your shopping list:

-milk
-bread
-eggs
-fruit

""")

cart_contents = ['_'] * len(shopping_list)
print("cart contents:",cart_contents)


while decision == "y":
    choice = input("What would you like to pickup?").lower()

    if choice in shopping_list:
        print(f"You chose {choice}")
        if choice == "milk":
            print("""

            You proceed to the milk and come across a young boy yodeling.

            """)
            response_to_yodel_boy = input("""
            Yodel Boy wants to sing for you.

            A: You let him sing.
            B: Tell him no.
            C: Ask him for his autograph.

            """).lower()

            if response_to_yodel_boy == "a":
                print(
            """
            Well, I'm in lOoOove, I'm in loOOove, with a beautiful gaaal
            That's what's the matter with meeeeee
            Well, I'm in love, I'm in love, with a beautiful gaal
            But she don't care about meeee

            ******************************************************************

            Yodel Boy is very pleased you let him sing.
            He hands you a coupon for milk.

            """)
                milk_response_a = input("you get to the milk, would you like to pick it up (Y/N) ").lower()

                if milk_response_a == "y":
                    for index, char in enumerate(shopping_list):
                        if char == choice:
                            cart_contents[index] = choice
                            print("You added the milk to your cart")
                            print("cart contents", cart_contents)
                else:
                    print("""

                    Why did you walk all the way over here if you if you
                    aren't going to put it in your cart?

                    """)


            if response_to_yodel_boy== "b":
                if "eggs" not in cart_contents:
                    print("""

            Yodel Boy is very angry that you would not let him sing.
            You go hide in the nearest bathroom until he calms down.

                    """)
                if "eggs" in cart_contents:
                    print("""

            Yodel Boy is very angry that you would not let him sing.
            He breaks your eggs.

                """)
                    cart_contents[2] = "_"
                    print(cart_contents)

                    milk_response_b = input("you get to the milk, would you like to pick it up (Y/N) ").lower()
                    if milk_response_b == "y":
                        for index, char in enumerate(shopping_list):
                            if char == choice:
                                cart_contents[index] = choice
                                print("You added the milk to your cart")
                                print("cart contents", cart_contents)
                    else:
                        print("""

                            Why did you walk all the way over here if you if you
                            aren't going to put it in your cart?

                            """)

            if response_to_yodel_boy == "c":
                print("""
            Yodel Boy is not signing autographs at this time.
            """)
                milk_response_c = input("you get to the milk, would you like to pick it up (Y/N) ").lower()
                if milk_response_c == "y":
                    for index, char in enumerate(shopping_list):
                        if char == choice:
                            cart_contents[index] = choice
                            print("You added the milk to your cart")
                            print("cart contents", cart_contents)
                else:
                    print("""

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
                    print("""

            Since you are so patient, you reward yourself with a sample of cheese.
            Go you!

                    """)
                    eggs_response_a = input("you get to the eggs, would you like to pick them up (Y/N) ").lower()

                    if eggs_response_a == "y":
                        for index, char in enumerate(shopping_list):
                            if char == choice:
                                cart_contents[index] = choice
                                print("You added the eggs to your cart")
                                print("cart contents", cart_contents)
                    else:
                        print("""

            Why did you walk all the way over here if you if you
            aren't going to put it in your cart?

                        """)
                if "milk" in cart_contents:
                    print("""

            Your milk spoiled waiting for her to move. So sad!

                    """)
                    cart_contents[0] = "_"
                    print(cart_contents)

                    eggs_response_a = input("you get to the eggs, would you like to pick them up (Y/N) ").lower()

                    if eggs_response_a == "y":
                        for index, char in enumerate(shopping_list):
                            if char == choice:
                                cart_contents[index] = choice
                                print("You added the eggs to your cart")
                                print("cart contents", cart_contents)
                    else:
                        print("""

            Why did you walk all the way over here if you if you
            aren't going to put it in your cart?

                        """)


            # scooter lady will randomly get mad if you ask her to move
            if response_to_scooter_woman == "b":
                mad_or_not = ['mad','not mad']
                attitude = random.choice(mad_or_not)
                if attitude == 'not mad':
                    print("""
            She is not mad. She kindly moves over and lets you get your eggs.

                """)
                    for index, char in enumerate(shopping_list):
                        if char == choice:
                            cart_contents[index] = choice
                            print("You added eggs to your cart!")
                            print("cart contents", cart_contents)

                if attitude == 'mad':
                    print("""
            She is so mad! She runs you over for being rude and you lose the
            contents of your cart.
                    """)
                    cart_contents = ['_'] * len(shopping_list)
                    print("Your cart is now empty!")
                    print(cart_contents)

#if the player chooses bread*************************************************


        if choice == "bread":
            print("""

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
                    print("""

            You bravely walk through the puddle, pick up the bread, and do not fall!
            Go you!

                """)
                    for index, char in enumerate(shopping_list):
                        if char == choice:
                            cart_contents[index] = choice
                            print("You added bread to your cart!")
                            print("cart contents", cart_contents)

                if accident == 'fall':
                    print("""
            You slip and fall in the floor. You sue Walmart and you get $1,000,000.
            You also get free groceries, congrats!.
                    """)
                    break
            if response_to_wet_floor == "b":
                print("""

            You told an employee about the puddle. You are now the town hero,
            but you still have to pay for your groceries.

                """)
                bread_response_a = input("you get to the eggs, would you like to pick them up (Y/N) ").lower()

                if bread_response_a == "y":
                    for index, char in enumerate(shopping_list):
                        if char == choice:
                            cart_contents[index] = choice
                            print("You added the bread to your cart")
                            print("cart contents", cart_contents)
                else:
                    print("""

                Why did you walk all the way over here if you if you
                aren't going to put it in your cart?

                    """)

# if the player chooses fruit************************************************
        if choice == "fruit":
            for index, char in enumerate(shopping_list):
                if char == choice:
                    cart_contents[index] = choice
                    print("cart contents", cart_contents)
    if choice not in shopping_list:
        if choice == "exit":
            check = any(item in cart_contents for item in shopping_list)
            if check is True:
                print(
                """

                You left the store without paying.
                You have been arrested and are going to jail.
                Your wife is going to be so mad.

                """)
                break
            else:
                print("""

                You left the store without putting anything in your cart.
                Your wife is going to be so mad.

                """)
                break

        if choice != "exit":
            print("""
            That is not on your list, stick to the list!
            """)
    if shopping_list == cart_contents:
        print("go to checkout")
        break


if decision == "N":
    print("BYE")
