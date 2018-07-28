# let the robot cheerleader cheer for you!

an_letters = "AEFHILMNORSX"
word = input("I will cheer for you! Enter a word: ").upper()
times = int(input("Enthusiastic level (0-10): "))

# i = 0

# while i < len(word):
# char = word[i]
for char in word:
    if char in an_letters:
        print("Give me an {}! {}".format(char, char))
    else:
        print("Give me a {}! {}".format(char, char))
    # i += 1

print("What does that spell??")

for i in range(times):
    print(word, "!!!")

# print((word + "!!!\n") * (times))
