msg = "Hello to "
name = input("What is your name? ")
print(msg + name)

import math

X = int(input("Enter number x: "))
y = int(input("Enter number y: "))
power = X ** y
log = int(math.log(X, 2))

print("X**y = " + str(power))
print("log(x) = " + str(log))

# some methods
print("Length of your name:", len(name))
print(name.upper())

# String templating
subject_template = "Thanks for learning {} with us {}!"
print(subject_template.format("Python", "Jenn"))

# Is a string in something? Boolean return
ham = "ham"
hamster = "hamster"
is_it_true = ham in hamster
print(is_it_true)
print(ham in hamster)

# bool example
cat_lover = True
has_dog = True
print(has_dog and not cat_lover)

# conditionals
another_name = input("What is your name? ")
if another_name == "Jenn":
    print(another_name, "is learning Python")
elif another_name == "Nina":
    print(another_name, "is learning with fellow students! Me too!")
else:
    print("You should totally learn Python, {}!".format(another_name))
print("Have a great day {}!".format(another_name))
