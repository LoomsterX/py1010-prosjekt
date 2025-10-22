import math

antall_elever = int(input('Skriv inn antall elever:' ))
pizzaer_per_elev = 0.25
total_pizzaer = math.ceil(antall_elever * pizzaer_per_elev)

print(f'Det må handles inn {total_pizzaer} pizzaer.')