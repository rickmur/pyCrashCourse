person = "eric"
print("Hello " + person.title() + ", would you like to learn some Python today?")

person2 = "irene GRAve"
print(person2.title())
print(person2.lower())
print(person2.upper())

person3 = "Steve Jobs"
quote = "Stay Hungry, Stay Foolish!"
print(person3.title() + ' once said, "' + quote + "'")

message = person3.title() + ' once said, "' + quote + "'"
print(message)

name_spaces = "   rick Mur      "
message = "Names and Trim exercise:\n\t-'" + name_spaces + "'\n\t-'" + name_spaces.lstrip() + "'\n\t-'" + name_spaces.rstrip() + "'\n\t-'" + name_spaces.strip() + "'"
print(message.title())


