
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
                if "eggs" in cart_contents:
                    print("""

            Yodel Boy is very angry that you would not let him sing.
            He breaks your eggs.

                """)
                # if eggs are in your cart, they are removed
                if "eggs" not in cart_contents:
                    print("""

            Yodel Boy is very angry that you would not let him sing.

                    """)

                # if eggs are not in your cart yodel boy does not break you eggs
                # for index, char in enumerate(shopping_list):
                #     if char == choice:
                #         cart_contents[index] = choice
                #         print("You added the milk to your cart")
                #         print("cart contents", cart_contents)

                # milk_response_a = input("you get to the milk, would you like to pick it up (Y/N) ").lower()

                # if milk_response_a == "y":
                #     for index, char in enumerate(shopping_list):
                #         if char == choice:
                #             cart_contents[index] = choice
                #             print("You added the milk to your cart")
                #             print("cart contents", cart_contents)
                # else:
                #     print("""
                #
                #     Why did you walk all the way over here if you if you
                #     aren't going to put it in your cart?
                #
                #     """)

            if response_to_yodel_boy == "c":
                print("""
            Yodel Boy is not signing autographs at this time.
            """)


            # for index, char in enumerate(shopping_list):
            #     if char == choice:
            #         cart_contents[index] = choice
            #         print("cart contents", cart_contents)
        if choice == "eggs":
            for index, char in enumerate(shopping_list):
                if char == choice:
                    cart_contents[index] = choice
                    print("cart contents", cart_contents)
        if choice == "bread":
            for index, char in enumerate(shopping_list):
                if char == choice:
                    cart_contents[index] = choice
                    print("cart contents", cart_contents)
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
