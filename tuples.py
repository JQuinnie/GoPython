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
