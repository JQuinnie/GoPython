import math


def split_check(total, number_of_ppl):
    return math.ceil(total / number_of_ppl)


total_due = float(input("What is the check total? "))
number_of_ppl = int(input("Between how many people? "))

amount_due = split_check(total_due, number_of_ppl)

print("Each person owes ${}".format(amount_due))
