from collections import defaultdict

transactions = [
    {"user_id": 1, "item": "Laptop"},
    {"user_id": 2, "item": "Mouse"},
    {"user_id": 1, "item": "Keyboard"},
    {"user_id": 3, "item": "Monitor"},
    {"user_id": 2, "item": "Cable"}
]

user_purchases = defaultdict(list)

for transaction in transactions:
    user_purchases[transaction["user_id"]].append(transaction["item"])

print(dict(user_purchases))