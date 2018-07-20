# attendees to the meeting

attendees = ["Ken", "Alena", "Treasure"]

print("There are", len(attendees), "attendees to begin with.")

# append an item
attendees.append("Craig")

new_attendees = ["James", "Jane"]

# add another list to existing
attendees.extend(new_attendees)

more_attendees = ["Guil", "Ryan", "Dave"]

# concat two lists together, does not modify originals
all_attendees = attendees + more_attendees

print("But now, there are", len(all_attendees), "attendees.")
