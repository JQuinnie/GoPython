messy_list = [4, 2, 1, 3, 5]

# use slice on list to make a copy
clean_list = messy_list[:]
clean_list.sort()

print(messy_list, clean_list)

# slice [start:finish], starting with and finish before
print(clean_list[2:4])

# return last two items in clean_list as last_list
last_list = clean_list[len(clean_list) - 2:]
print(last_list)

# get a range of numbers in list form and step every other
number_list = list(range(20))
even_number_list = number_list[::2]
step_back = number_list[-2:-5:-1]
reverse_list = number_list[::-1]
last_4 = number_list[-4::1]

# print(number_list)
# print(even_number_list)
# print(step_back)
# print(reverse_list)
# print(last_4)

# slice and join together
rainbow = ["red", "orange", "yellow", "green", "blue", "pink"]
rainbow[-1:] = "purple"
rainbow[-6:] = ["".join(rainbow[-6:])]

print(rainbow)

# for loop with slice
example = "Hello World!"

for letter in example[-6:]:
    print(letter)

example = "Hello World!"

for letter in example[::-1]:
    print(letter)


# create function that will take in a string and return the first half lowercase and 2nd half upper case
def sillycase(string):
    # half = int(len(string) / 2), below is using floor division which returns an integer
    half = len(string) // 2
    first_half = string[:half].lower()
    second_half = string[half:].upper()
    return first_half + second_half


print(sillycase("treehouse"))
