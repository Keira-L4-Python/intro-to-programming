Sandwich_orders = [
    'pastrami', 'Tuna', 'Ham & Cheese', 'pastrami',
    'Beef', 'Pesto', 'pastrami']
Finished_sandwiches = []

print("I'm sorry, we're all out of pastrami today.")
while 'pastrami' in Sandwich_orders:
    Sandwich_orders.remove('pastrami')

print("\n")
while Sandwich_orders:
    current_sandwich = Sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich.")
    Finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in Finished_sandwiches:
    print(f"I made a {sandwich} sandwich.")