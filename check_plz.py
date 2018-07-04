import math


def split_check(total, number_of_ppl):
    if number_of_ppl <= 1:
        raise ValueError("More than 1 person is required to split the check")
    return math.ceil(total / number_of_ppl)


# put variables that might cause an error in 'try' and if error is 'ValueError' do thing else, do other thing
try:
    total_due = float(input("What is the check total? "))
    number_of_ppl = int(input("Between how many people? "))
    amount_due = split_check(total_due, number_of_ppl)
except ValueError as err:
    print("Please provide a valid value...")
    print("({})".format(err))
else:
    print("Each person owes ${}".format(amount_due))
