# Rick Mur - 2015

bikes = [ 'bla', 'bla2', 'bla3', 'bla4']
print (bikes[1])
print (bikes[-1])



print ("\nMy friends")
friends = ['rob', 'irene', 'michael', 'edwin', 'lucio']
print (friends[0])
print (friends[1])
print (friends[2])
print (friends[3])
print (friends[4])
print (friends[-1])
print (friends[-2])

print ("Hoi " + friends[0].title() + ", hoe laat?")
print ("Hoi " + friends[1].title() + ", hoe laat?")
print ("Hoi " + friends[2].title() + ", hoe laat?")
print ("Hoi " + friends[3].title() + ", hoe laat?")
print ("Hoi " + friends[4].title() + ", hoe laat?")


print (friends)
friends.append("pieter")
print (friends)
friends.insert(-1, "object")
print (friends)
laatste = friends.pop(-2)
print (laatste)
print (friends)
friends.pop()
print (friends)
friends.remove("lucio")
print (friends)

friends.sort()
print (friends)
friends.sort(reverse=True)
print (friends)

print (len(friends))



