# set a new dict
jenn = {"first_name": "Jenn", "job": "I need one"}
# add a key/value
jenn["last_name"] = "Chu"
# update information in dict, can set or change several keys and their values at once
jenn.update({"job": "I need a developer job", "location": "Denver, CO"})
jenn["status"] = "Superstar"
# lets be modest
del jenn["status"]
jenn["status"] = "Hard worker"

print(jenn)


# most time dict packing/unpacking is in relations to functions, as that is when its most useful
# **kwargs -> function will pack key word arguments
def packer(**kwargs):
    print(kwargs)


# will not pack job key and value
def packerJob(job=None, **kwargs):
    print(kwargs)


def unpacker(first_name=None, last_name=None):
    if first_name and last_name:
        print("Hi {} {}!".format(first_name, last_name))
    else:
        print("Hi no name!")


packer(name="Jenn", exp=1, job=None)
packerJob(name="Jenn", exp=1, job=None)
unpacker(**{"last_name": "Chu", "first_name": "Jenn"})


# looping through dict
for key in jenn:
    print(key, "=", jenn[key])

# can also use
for key in jenn.keys():
    print(key)

for value in jenn.values():
    print(value)

# items give back a tuple
for item in jenn.items():
    print(item)