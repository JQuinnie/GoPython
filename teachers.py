# The dictionary will look something like:
# {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Each key will be a Teacher and the value will be a list of courses.


def num_teachers(dict):
    num_of_teachers = len(dict)
    return num_of_teachers


def num_courses(dict):
    num_of_courses = 0
    for teacher in dict:
        num_of_courses += len(dict[teacher])
    return num_of_courses


def courses(dict):
    course = []
    for value in dict.values():
        course.extend(value)
    return course


def most_courses(dict):
    max_count = 0
    name = ""
    for teacher, courses in dict.items():
        if len(courses) > max_count:
            max_count = len(courses)
            name = teacher
    return name


def stats(dict):
    list = []
    for teacher, courses in dict.items():
        another = [teacher, len(courses)]
        list.append(another)
    return list


print(
    num_teachers(
        {
            "Andrew Chalkley": ["jQuery Basics", "Node.js Basics"],
            "Kenneth Love": ["Python Basics", "Python Collections"],
        }
    )
)

print(
    num_courses(
        {
            "Andrew Chalkley": ["jQuery Basics", "Node.js Basics"],
            "Kenneth Love": ["Python Basics", "Python Collections"],
        }
    )
)

print(
    courses(
        {
            "Andrew Chalkley": ["jQuery Basics", "Node.js Basics"],
            "Kenneth Love": ["Python Basics", "Python Collections"],
        }
    )
)

print(
    most_courses(
        {
            "Andrew Chalkley": ["jQuery Basics", "Node.js Basics", "another course"],
            "Kenneth Love": ["Python Basics", "Python Collections"],
        }
    )
)

print(
    stats(
        {
            "Andrew Chalkley": ["jQuery Basics", "Node.js Basics", "another course"],
            "Kenneth Love": ["Python Basics", "Python Collections"],
        }
    )
)
