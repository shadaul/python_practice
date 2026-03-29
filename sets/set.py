wishlist = ["laptop", "mouse", "keyboard", "monitor"]
cart = ["mouse", "cable", "monitor", "headphones"]

in_both = set(wishlist) & set(cart)
print(in_both)

names = ["Laptop", "Mouse", "Keyboard", "Monitor"]
prices = [4000, 100, 300, 1200]

catalog = dict(zip(names, prices))
print(catalog)

cart_items = [
    {"name": "Laptop", "in_stock": True},
    {"name": "Mouse", "in_stock": True},
    {"name": "Keyboard", "in_stock": False}, 
    {"name": "Cable", "in_stock": True}
]

can_ship = all(item["in_stock"] for item in cart_items)
print(can_ship)

top_items = ["Smart TV", "Wireless Mouse", "Mechanical Keyboard"]

ranked_items = [f"{rank}: {item}" for rank, item in enumerate(top_items, start=1)]
print(ranked_items)