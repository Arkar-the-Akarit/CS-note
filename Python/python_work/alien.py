alien_0 = {'x-position':0, 'y-position':25,'speed':'medium'}
print(f"Original x position of alien: {alien_0['x-position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed'] == 'fast':
    x_increment = 3

alien_0['x-position'] += x_increment
print(f"Current x position of alien: {alien_0['x-position']}")