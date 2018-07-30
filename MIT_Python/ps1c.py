# Write a program to calculate the best savings rate, as a function of your starting salary, can you afford the down payment in 3 years time?


def calc():
    # annual salary
    annual_salary_start = float(input("Enter the starting salary: "))
    # semi-annual raise
    semi_annual_raise = .07
    # monthly return on investment rate
    r = 0.04 / 12
    # cost of the dream house
    total_cost = 1000000
    # down payment for dream house
    down_payment = .25 * total_cost

    current_savings = 0
    epsilon = 100
    bisect_search_step = 0
    low = 0
    high = 10000
    portion_saved = (high + low) / 2

    while abs(current_savings - down_payment) >= epsilon:
        bisect_search_step += 1
        print("Bisect step: ", bisect_search_step)
        print("Portion Saved %: ", portion_saved / 10000)
        month_count = 0
        current_savings = 0
        annual_salary = annual_salary_start
        print("Current savings 1: ", current_savings)
        print("Annual Salary: ", annual_salary)
        # calc current savings after 36 months
        while month_count <= 36:
            month_count += 1
            monthly_savings = annual_salary / 12 * portion_saved / 10000
            if month_count % 6 == 0:
                annual_salary = annual_salary + annual_salary * semi_annual_raise
            return_on_invest = current_savings * r
            current_savings = current_savings + monthly_savings + return_on_invest

        print("Current Savings 2: ", current_savings)

        if current_savings < down_payment:
            low = portion_saved
        else:
            high = portion_saved

        portion_saved = (high + low) / 2

        if low >= high:
            print("It is not posible to pay the down payment in 3 years.")
            break

        print("Best savings rate: {0:.4f}".format(portion_saved / 10000))
        print("Steps in bisection search: {}".format(bisect_search_step))


calc()
