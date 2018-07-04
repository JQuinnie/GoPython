import math


def split_check(total, number_of_ppl):
    return math.ceil(total / number_of_ppl)


# put variables that might cause an error in 'try' and if error is 'ValueError' do thing else, do other thing
try:
    total_due = float(input("What is the check total? "))
    number_of_ppl = int(input("Between how many people? "))
except ValueError:
    print("Please provide a valid value...")
else:
    amount_due = split_check(total_due, number_of_ppl)
    print("Each person owes ${}".format(amount_due))
