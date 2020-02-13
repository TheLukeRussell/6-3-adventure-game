
print("Welome to Walmart! {name}")
decision = input('Would you like to start shopping? (Y/N)')


shopping_list = ['milk', 'bread', 'eggs', 'fruit']
print(shopping_list)



if decision == "Y":
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


while decision == "Y":
    choice = input("What would you like to pickup first? ")

    if choice in shopping_list:
        print(f"You chose {choice}")
        for index, char in enumerate(shopping_list):
            if char == choice:
                cart_contents[index] = choice
                print("cart contents", cart_contents)
    if choice == "exit":
        print(
        """
        You left the store without paying.
        You will now go to jail.

        """)
        break
    if shopping_list == cart_contents:
        print("go to checkout")
        break


if decision == "N":
    print("BYE")
