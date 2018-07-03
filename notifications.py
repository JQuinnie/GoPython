praise = "You are doing great"
praise = praise.upper()
number_of_characters = len(praise)
# double division is floor division, to get an integer no floats
result = praise + "!" * (number_of_characters // 2)
print(result)

advice = "Don't forget to ask for help"

# function creation
def yell(text):
    text = text.upper()
    number_of_characters = len(text)
    result = text + "!" * (number_of_characters // 4)
    print(result)


yell("You are doing great")
yell(advice)
yell("Don't Repeat Yourself. Keep things DRY")
