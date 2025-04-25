age = int(input("Please enter your age: "))

if age < 2 :
    print("you are a baby")
elif 2 <= age < 4:
    print("you are a toddler")
elif 4<= age < 13:
    print("you are a kid")
elif 13 <= age < 20:
    print("you are a teenager")
elif 20 <= age < 65:
    print("you are an adult")
elif age >= 65:
    print("you are an elder")