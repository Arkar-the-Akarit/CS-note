colors = ['green', 'yellow','red']
marks = (5,10,15)

shot_alien = input("Enter the color of alien you shot: ").lower()

# used range instead of color in colors to manage index
l = len(colors)

for i in range(l):
    if colors[i] == shot_alien:
        print(f"Congratulation. You have earned {marks[i]} marks")
        break
else:
    print("You have earned zero points")