TICKET_PRICE = 10
tickets_remaining = 100

# Run this code continuously until we run out of tickets
while tickets_remaining >= 1:
    # Output how many tickets are remaining using the tickets_remaining variable
    print("There are {} tickets remaining.".format(tickets_remaining))
    # Gather the user's name and assign it to a new variable
    name = input("What is your name? ")
    # Prompt the user by name and ask how many tickets they would like
    # Expect a ValueError to happen and handle it appropriately
    try:
        number_of_tickets = int(
            input("Hi {}, how many tickets would you like to purchase? ".format(name))
        )
        # Raise a ValueError if the request is for more tickets than are available
        if number_of_tickets > tickets_remaining:
            raise ValueError(
                "There are only {} tickets available.".format(tickets_remaining)
            )
    except ValueError as err:
        # Include the error text in the output
        print("Oh no, error encountered. {}".format(err))
    else:
        # Calculate the price (number of tickets * price) and assign it to a variable
        total_price = number_of_tickets * TICKET_PRICE
        # Out put the price to the screen
        print("Your total price is: {}".format(total_price))
        # Prompt user if they want to proceed. Y/N
        proceed = input("Would you like to proceed with the purchase order? (Y/N) ")
        # If they want to proceed
        if proceed.lower() == "y":
            # print out to the screen 'SOLD!' to confirm purchase
            print("Thank you for your purchase!")
            # and then decrement the tickets remaining by the number of tickets purchased
            tickets_remaining -= number_of_tickets
        # Otherwise...
        else:
            # Thank them by name
            print("{}, thank you for browsing!".format(name))
# Notify user that the tickets are sold out
print("Sorry, all the tickets are sold.")
