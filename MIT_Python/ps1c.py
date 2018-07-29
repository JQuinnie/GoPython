# Write a program to calculate the best savings rate, as a function of your starting salary, can you afford the down payment in 3 years time?


def calc():
    # annual salary
    annual_salary = int("Enter the starting salary: ")
    # semi-annual raise
    semi_annual_raise = .07
    # monthly return on investment rate
    r = 0.04 / 12
    # cost of the dream house
    total_cost = 1000000
    # down payment for dream house
    down_payment = .25 * total_cost
