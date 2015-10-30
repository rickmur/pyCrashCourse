# Rick Mur - 2015

magicians = ["david", "john", "allan"]

for magician in magicians:
  print (magician.title())

print ("")
pizzas = ["tuna", "parma and pesto", "pepperoni"]
for pizza in pizzas:
  print ("I like " + pizza + " pizza")

print ("\nI like " + str(len(pizzas)) + " types of pizza very much\n")

animals = ["cat", "dog", "fish"]
num_animals = len(animals)
i = 1
for animal in animals:
  if i != num_animals:
    print ("I like a " + animal.title() + " as a pet")
    print ("But anyone of the next " + str(num_animals - i) + " also makes a great pet")
  else:
    print ("Finally I like a " + animal.title() + " as a pet")
  i=i+1

print ("\nThank you")

for value in range(1, 5):
  print(value)

squares = []
for number in range(1,11):
  squares.append(number**2)

print(squares)

squares.pop(2)

print(squares)


numbers = list(range(0,10))
print (min(numbers))
print (max(numbers))
print (sum(numbers))
print (len(numbers))

squares2 = [value+1 for value in range(1,11,2)]
print(squares2)


for number in range(1,21):
  print (number)

#for number in range(1,1000001):
#  print number

million = list(range(1,1000001))
print (min(million))
print (max(million))
print (sum(million))

for odd in range(1,20,2):
  print (odd)

print("break")

threes = list(range(3,11))
for three in threes:
  print (three*3)

print ('break')

cubes = list(range(1,11))
for cube in cubes:
  print (cube**3)

print ("break")

cubes2 = [three**3 for three in range(1,11)]

cubes3 = cubes2[: ]

cubes3.append("hoi")

print (cubes3)
print (cubes2)

animals.append('zeetong')
animals.append('paling')
animals.append('porterhouse')
animals.append('cote de boeuf')

print (animals)
print ("The first three items are: ")
print (animals[:3])
print ("The middle 3 items are:")
print (animals[2:5])
print ("The last 3 items are:")
print (animals[-3:])

print (pizzas)
frPizzas = pizzas[:]
pizzas.append("papaya")
frPizzas.append("avocado")

print ("My favorite pizzas are:")
for p in pizzas:
  print p.title()
print ("My friends favorite pizzas are:")
for p in frPizzas:
  print p.title()

