guests = ['Da Vinci','Leonardo','Cindy']

gretting = 'Hello!'
invite = "can you please come to my dinner?"

print(f"{gretting} {guests[0]}, {invite}")
print(f"{gretting} {guests[1]}, {invite}")
print(f"{gretting} {guests[2]}, {invite}")

print(f"\nA sad new. {guests[2]} replied that she wont be able to make it to the dinner.\n")

# removing Cindy from list
del guests[2]
# guests.pop(2)
# guests.remove('Cindy')

# adding a new member
# guests.append('Sparrow')
guests.insert(2,'Sparrow')

print(f"{gretting} {guests[0]}, {invite}")
print(f"{gretting} {guests[1]}, {invite}")
print(f"{gretting} {guests[2]}, {invite}")

print(f"Total invited guests till now: ",len(guests))
print(f"\nGood news everybody, I found a bigger dining place.\n")

# adding to the place of first guest with insert()
guests.insert(0,'Sabrina')

# adding new guest into the middle of guest list
guests.insert(2,'Mr.Bean')

guests.append('Naruto')

print(f"{gretting} {guests[0]}, {invite}")
print(f"{gretting} {guests[1]}, {invite}")
print(f"{gretting} {guests[2]}, {invite}")
print(f"{gretting} {guests[3]}, {invite}")
print(f"{gretting} {guests[4]}, {invite}")


print(f"Total invited guests till now: ",len(guests))

print(f"\n I am so sorry that I can only invite two people now.")

print("Current Guest List: ",guests)

print(f"Total invited guests till now: ",len(guests))

for i in range (4):
    uninvited_guest = guests.pop(0)
    print(f"Dear {uninvited_guest}, I am so heartbroken to remove you from guest list. But I will invite you next time.")

print("\n")

print(guests,'-----\n\n')

print(f"Total invited guests till now: ",len(guests))

for j in range(2):
    print(f"Dear {guests[0]}, you are still invited to the dinner tho. Pls come for sure.")
    guests.pop(0)


print("\nCurrent Guest List: ",guests)

print(f"Total invited guests till now: ",len(guests))