
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
    choice = input("What would you like to pickup first? ").lower()

    if choice in shopping_list:
        print(f"You chose {choice}")
        if choice == "milk":
            print("""

            You proceed to the milk and come across a young boy yodeling.

            """)
            response = input("""Yodel Boy wants to do sing for you""")

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
