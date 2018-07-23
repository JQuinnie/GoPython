messy_list = [4, 2, 1, 3, 5]

# use slice on list to make a copy
clean_list = messy_list[:]
clean_list.sort()

print(messy_list, clean_list)

# slice [start:finish], starting with and finish before
print(clean_list[2:4])

# return last two items in clean_list as last_list
last_list = clean_list[len(clean_list) - 2 :]
print(last_list)