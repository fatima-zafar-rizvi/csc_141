
pizzas = ['Cheese pizza', 'Buffalo chicken pizza', 'Chicken fajita pizza']
friend_pizzas = pizzas[:]

pizzas.append('Veggie pizza')
friend_pizzas.append('Pineapple pizza')

print("\tMy favorite pizzas are:\n")
for me in pizzas:
    print(me)

print("\n\tMy friend's favorite pizzas are:\n")
for you in friend_pizzas:
    print(you)