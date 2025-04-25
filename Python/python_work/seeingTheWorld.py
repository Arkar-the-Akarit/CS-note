locations = ['Japan','Paris','Korea','Thailand','China']

print("The place i want to travel: ",locations)

print("Sorted: ",sorted(locations))

print("The original: ",locations)

print("Temporarily Reverse Sorted: ", sorted(locations,reverse=True))

print("The original: ", locations)

locations.reverse()
print("The place in permanent reverse order: ",locations)

locations.sort()
print("permanentlly sorted: ",locations)

locations.sort(reverse=True)
print("Permanetnly reverse alphabeticall order: ",locations)
