my_tuple = (1, 2, 3)

# see what you can do with tuples
dir(my_tuple)

# advantage is simultaneous assignment, swapping without the need for a temp!
a = "b"
b = "a"
a, b = b, a
c = b, a
print(a, b)
print(c)

# packing arbitrary numbers into functions
def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total


print(add(5, 5))


def add2(base, *args):
    total = base
    for num in args:
        total += num
    return total


print(add2(5, 20))


def multiply(*nums):
    total = 1
    for num in nums:
        total *= num
    return total


print(multiply(2, 2, 2))
