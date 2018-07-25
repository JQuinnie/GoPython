# determine how long it will take you to save enough money to make housing down payment


def calc():

    # annual salary
    annual_salary = int(input("Enter your annual salary: "))
    # dedicate a certain amount of your salary each month to saving for the down payment
    portion_saved = float(
        input("Enter the percent of your salary to save, as a decimal: ")
    )
    # cost of dream house
    total_cost = int(input("Enter the cost of your dream house: "))
    # semi-annual raise
    semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

    # portion of cost needed for down payment
    portion_down_payment = .25
    # monthly return on investment rate
    r = 0.04 / 12
    # down payment for dream house
    down_payment = portion_down_payment * total_cost
    current_savings = 0
    return_on_invest = 0
    month_count = 0

    while current_savings != down_payment:
        month_count += 1
        monthly_savings = annual_salary / 12 * portion_saved

        # semi-annual promotion
        if month_count % 6 == 0:
            annual_salary = annual_salary + annual_salary * semi_annual_raise

        return_on_invest = current_savings * r
        current_savings = current_savings + monthly_savings + return_on_invest
        # print(month_count, current_savings, monthly_savings, return_on_invest)

        if current_savings > down_payment:
            print("Number of months: {}".format(month_count))
            break


# run calculator
calc()
