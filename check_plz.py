def split_check(total, number_of_ppl):
    cost_per_pp = total / number_of_ppl
    return cost_per_pp


amount_due = split_check(84.97, 4)
print("Each person owes ${}".format(amount_due))
