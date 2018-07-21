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
