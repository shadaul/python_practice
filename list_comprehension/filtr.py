products = [
    {"name": "Laptop", "price": 4000, "in_stock": True},
    {"name": "Mouse", "price": 100, "in_stock": False},
    {"name": "Keyboard", "price": 300, "in_stock": True},
    {"name": "Monitor", "price": 1200, "in_stock": True},
    {"name": "Cable", "price": 30, "in_stock": False}
]

have = [product["price"] * 0.9 for product in products if product["in_stock"]]
print(have)


categories = ["electronics", "home", "electronics", "toys", "home", "electronics", "books"]

counts = {}
for item in categories:
    counts[item] = counts.get(item,0) + 1 
print(counts)

products = [
    {"name": "Laptop", "price": 4000},
    {"name": "Mouse", "price": 100},
    {"name": "Keyboard", "price": 300},
    {"name": "Monitor", "price": 1200}
]

sorted_products = sorted(products, key=lambda x: x["price"])
print(sorted_products)

users = [
    {"username": "anna", "rating": 4.5},
    {"username": "viktor", "rating": 3.2},
    {"username": "max", "rating": 5.0},
    {"username": "elena", "rating": 4.8}
]

sorted_users = sorted(users, key=lambda x:x["rating"])

print(sorted_users)

users = [
    {"username": "anna", "rating": 4.5},
    {"username": "viktor", "rating": 3.2},
    {"username": "max", "rating": 5.0},
    {"username": "elena", "rating": 4.8}
]

sorted_rating = sorted(users, key=lambda x:x["rating"], reverse=True)
print(sorted_rating)