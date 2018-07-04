TICKET_PRICE = 10
SERVICE_CHARGE = 2
tickets_remaining = 100


def calculate_price(number_of_tickets):
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE


while tickets_remaining >= 1:
    print("There are {} tickets remaining.".format(tickets_remaining))
    name = input("What is your name? ")
    try:
        number_of_tickets = int(
            input("Hi {}, how many tickets would you like to purchase? ".format(name))
        )
        if number_of_tickets > tickets_remaining:
            raise ValueError(
                "There are only {} tickets available.".format(tickets_remaining)
            )
    except ValueError as err:
        print("Oh no, error encountered. {}".format(err))
    else:
        total_price = calculate_price(number_of_tickets)
        print("Your total price is: {}".format(total_price))
        proceed = input("Would you like to proceed with the purchase order? (Y/N) ")
        if proceed.lower() == "y":
            print("Thank you for your purchase!")
            tickets_remaining -= number_of_tickets
        else:
            print("{}, thank you for browsing!".format(name))
print("Sorry, all the tickets are sold.")
