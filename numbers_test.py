# Rick Mur - 2015

invitations = ["steve jobs", "rob de hoog", "irene grave"]
print ("Hi, " + invitations[0].title() + " I would like to invite you to dinner")
print ("Hi, " + invitations[1].title() + " I would like to invite you to dinner")
print ("Hi, " + invitations[2].title() + " I would like to invite you to dinner")

print (invitations.pop(0).title() + " is deceased and can't make it")
print ("Hi, " + invitations[0].title() + " I would like to invite you to dinner")
print ("Hi, " + invitations[1].title() + " I would like to invite you to dinner")

print ("\nGood news! We found a bigger table")
invitations.insert(0, "Rick Mur")
invitations.insert(2, "Jitender Kumar Karg")
invitations.append("Mary Mur")
print (invitations[0].title() + " will be added")
print (invitations[2].title() + " will be added in the middle")
print (invitations[-1].title() + " will be added at the end")
print (invitations)
print ("I am inviting " + str(len(invitations)) + " persons to the party")

print ("\nUnfortunately the table is smaller again")
print ("Sorry " + invitations.pop().title() + " you can't come anymore")
print ("Sorry " + invitations.pop().title() + " you can't come anymore")
print ("Sorry " + invitations.pop().title() + " you can't come anymore")
print (invitations[0].title() + " you are still invited to come")
print (invitations[1].title() + " you are still invited to come")
del invitations[0]
del invitations[0]
print (invitations)
