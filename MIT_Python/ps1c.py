# Write a program to calculate the best savings rate, as a function of your starting salary, can you afford the down payment in 3 years time?

# semi-annual raise
semi_annual_raise = .07
# monthly return on investment rate
r = 0.04 / 12
# cost of the dream house
total_cost = 1000000
# down payment for dream house
down_payment = .25 * total_cost


def calc():
    # annual salary
    annual_salary_start = 150000  # float(input("Enter the starting salary: "))
    epsilon = 100
    bisect_search_step = 0
    low = 0
    high = 10000
    portion_saved = (high + low) / 2
    amount_saved = 0

    while abs(amount_saved - down_payment) >= epsilon:
        # print(abs(amount_saved - down_payment))
        amount_saved = foo(annual_salary_start, portion_saved / 10000, 36, r)

        if amount_saved < down_payment:
            low = portion_saved
        else:
            high = portion_saved

        portion_saved = (high + low) / 2

        if low >= high:
            print("It is not posible to pay the down payment in 3 years.")
            break

        bisect_search_step += 1

        # current_savings = month_limit(annual_salary, portion_saved, current_savings)
        # print("Bisect step: ", bisect_search_step)
        # print("Portion Saved %: ", portion_saved / 10000)
        # print("Amount saved: ", amount_saved)
        # print("Annual Salary: ", annual_salary)
        # print("Current Savings 2: ", current_savings)

    print("Best savings rate: {0:.4f}".format(portion_saved / 10000))
    print("Steps in bisection search: {}".format(bisect_search_step))


# salary, savings goal, time to reach goal =>
def foo(salary, percent_to_save, time_to_reach_goal, rate_of_return):
    annual_salary = salary
    month_counter = 0
    amount_saved = 0
    while month_counter <= time_to_reach_goal:
        monthly_salary = annual_salary / 12
        amount_to_save = monthly_salary * percent_to_save
        roi = amount_saved * rate_of_return
        amount_saved += amount_to_save + roi

        if month_counter % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise

        month_counter += 1

    return amount_saved


calc()
