comfy_pizzas = ['cheese pizza', 'double spicy pizza', 'spicy seafood pizza']

for pizza in comfy_pizzas:
    print(f"I fw {pizza}")

friend_pizzas = comfy_pizzas[:]

comfy_pizzas.insert(3,'double chicken pizza')
friend_pizzas.append('mexican pizza')

print(comfy_pizzas)
print(friend_pizzas)