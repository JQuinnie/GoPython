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
