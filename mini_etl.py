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

# raw_users = [
#     {"id": 1, "name": "Daulet", "age": 25},
#     {"id": 2, "name": "Karim", "age": 16},    # Младше 18
#     {"id": 3, "name": "Roman", "age": None},  # Возраст не указан
#     {"id": 4, "name": "Anna", "age": 30}
# ]

# clean = []

# for user in raw_users:
#     if user["age"] != None and user["age"] >= 18:
#         clean.append(user)

# print(clean)

# transactions = [
#     {"id": 1, "amount_usd": 50.0, "status": "success"},
#     {"id": 2, "amount_usd": 15.0, "status": "failed"},
#     {"id": 3, "amount_usd": 100.0, "status": "success"}
# ]

# processed = []

# for i in transactions:
#     if i["status"] == "success":
#         amount_pln = i["amount_usd"] * 4
#         i["amount_pln"] = amount_pln

#         processed.append(i)

# print(processed)

# matches = [
#     {"player": "Daulet", "hero": "Sniper", "kills": 12},
#     {"player": "Roman", "hero": "Pudge", "kills": 5},
#     {"player": "Daulet", "hero": "Invoker", "kills": 8},
#     {"player": "Karim", "hero": "Crystal Maiden", "kills": 2},
#     {"player": "Roman", "hero": "Axe", "kills": 10}
# ]

# total_kills = {}

# for user in matches:
#     player_name = user["player"]
#     match_kills = user["kills"]
#     if player_name not in total_kills:
#         total_kills[player_name] = match_kills
#     else:
#         total_kills[player_name] += match_kills

api_response = {
    "status": "200 OK",
    "data": {
        "users": [
            {"info": {"name": "Daulet", "email": "daulet@example.com"}, "is_active": True},
            {"info": {"name": "Roman", "email": "roman@example.com"}, "is_active": False},
            {"info": {"name": "Karim", "email": "karim@example.com"}, "is_active": True}
        ]
    }
}

active_emails = []

for user in api_response["data"]["users"]:
    mail = user["info"]["email"]
    if user["is_active"]:
        active_emails.append(mail)

print(active_emails)