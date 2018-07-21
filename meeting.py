# attendees to the meeting

attendees = ["Ken", "Alena", "Treasure"]

print("There were", len(attendees), "attendees to begin with.")

# append an item
attendees.append("Craig")

new_attendees = ["James", "Jane"]

# add another list to existing
attendees.extend(new_attendees)

more_attendees = ["Guil", "Ryan", "Dave"]

# concat two lists together, does not modify originals
all_attendees = attendees + more_attendees

print("But now, there are", len(all_attendees), "attendees.")


# books for the meeting
books = [
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]

print("Suggested reading: {}".format(books[0]))

books.insert(0, "Learning Python: Powerful Object-Oriented Programming")
# add string to 0 index, lists are mutable but strings are not, you can access a specific character on a String using an index, but you cannot change it
books[0] += " - Mark Lutz"

# > python -i filename.py will go into interactive mode

# unicode for emoji of taco
cater_lunch = "\N{Taco}"

recommendation = books[0]
# deletes books by index
del books[0]

print(books, recommendation)

# in python you can pop a specific index to a list
print(books.pop())
print(books.pop(1))


# iterate thru list
print("Books:")
for book in books:
    print("* " + book)

# check to see if something is in a list
print("James" in attendees)

lunch_options = ["Burgers", "Salads", "Sandwiches"]

# general function because DRY
def conf_needlist(display_name, needs):
    items = needs.copy()  # create a copy of the list so cant mutate it in our function
    print(display_name + ":")
    suggested = items.pop(0)  # items.remove("item name") will also work
    print("=====>", suggested, "<=====")
    for item in items:
        print("* " + item)
    print()


conf_needlist("Lunches", lunch_options)
conf_needlist("Attendees", attendees)

# split and join
to_line = ", ".join(attendees)
cc_line = ", ".join(more_attendees)
print("To: " + to_line)
print("Cc: " + cc_line)

# back to list
print(to_line.split(", "))


# multi-dimensional lists
travel_expenses = [
    [5.00, 2.75, 22.00, 0.00, 0.00],
    [24.75, 5.50, 15.00, 22.00, 8.00],
    [2.75, 5.50, 0.00, 29.00, 5.00],
]

print("Travel Expenses:")
week_number = 1
for week in travel_expenses:
    print(
        "* Week #{}: ${}".format(week_number, sum(week))
    )  # alternatively, sum(week) for week in travel_expenses
    week_number += 1
print("Total Expense: ${}".format(sum(sum(x) for x in travel_expenses)))


# Here is a multi-dimensional list of musical groups. The first dimension is group, the second is group members.
# Can you loop through each group and output the members joined together with a ", " comma space as a separator, please?
musical_groups = [
    ["Ad Rock", "MCA", "Mike D."],
    ["John Lennon", "Paul McCartney", "Ringo Starr", "George Harrison"],
    ["Salt", "Peppa", "Spinderella"],
    ["Rivers Cuomo", "Patrick Wilson", "Brian Bell", "Scott Shriner"],
    ["Chuck D.", "Flavor Flav", "Professor Griff", "Khari Winn", "DJ Lord"],
    ["Axl Rose", "Slash", "Duff McKagan", "Steven Adler"],
    ["Run", "DMC", "Jam Master Jay"],
]
# Your code here
for group in musical_groups:
    print(", ".join(group))

# print only trios
for group in musical_groups:
    if len(group) == 3:
        print(", ".join(group))
