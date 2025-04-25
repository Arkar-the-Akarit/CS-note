users = ['arkar','lenox','admin','nyein','pyae']

del users[0]
del users[0]

users.pop(0)
users.pop(0)

users.remove('pyae')

print(users)

if users:
    for user in users:
        if user == 'admin':
            print(f"Hello {user.title()}, how are you today? would you like to see status report")
        else:
            print(f"Hello User: {user.title()}, how are your day?")
else: 
    print("we need to find some users.")

