Sandwich_orders=["Tuna", "Ham & Cheese", "Beef", "Pesto"]
Finished_sandwiches = []

while Sandwich_orders:
    current_sandwich = Sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich.")
    Finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in Finished_sandwiches:
    print(f"I made a {sandwich} sandwich.")
