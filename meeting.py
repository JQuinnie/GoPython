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
