current_users = ["lenox","arkar","superman","batman","admin"]

new_users = ['aung','su','Admin','spidy','BatMan']

for new_user in new_users:
    for current_user in current_users:
        if new_user.lower() == current_user.lower():
            print(f"User name : {new_user} already exists.\nPlase enter a new username")
            break
    else:
        print(f"the username : {new_user} is available to use")

print(ord('a'))