# users = [
#     {"id": 1, "name": "Daulet"},
#     {"id": 2, "name": "Karim"},
#     {"id": 3, "name": "Roman"}
# ]

# roles = [
#     {"id": 2, "role": "Data Engineer"},
#     {"id": 1, "role": "AI Trainer"},
#     {"id": 3, "role": "Manager"}
# ]
# new = {}
# for role in roles: 
    
#     new[role["id"]] = role["role"]
# for user in users:
#     user_id = user["id"]
#     user["role"] = new[user_id]

# print(users)

# layers = ["bronze", "silver", "bronze", "gold", "silver", "bronze"]

# counts = {}

# for layer in layers:
#     if layer not in counts:
#         counts[layer] = 1
#     else:
#         counts[layer] += 1
# print(counts)

raw_users = [
    {"id": 1, "name": "Daulet", "age": 25},
    {"id": 2, "name": "Karim", "age": 16},    # Младше 18
    {"id": 3, "name": "Roman", "age": None},  # Возраст не указан
    {"id": 4, "name": "Anna", "age": 30}
]

clean = []

for user in raw_users:
    if user["age"] != None and user["age"] >= 18:
        clean.append(user)

print(clean)