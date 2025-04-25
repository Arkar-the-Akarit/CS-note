'''
6-1. Person: Use a dictionary to store information about a person you know. 
Store their first name, last name, age, and the city in which they live. You 
should have keys such as first_name, last_name, age, and city. Print each piece  
of information stored in your dictionary.
'''

user = {
    'first_name': 'arkar',
    'last_name' : 'phyo',
    'age' : 20,
    'city': 'yamethin',
    }

print(user['first_name'])
print(user.get('last_name','there is no last name key'))
print(user['age'])
print(user.get('city','there is no city key-value pair'))
print(user.get('home','there is no home key pairs'))