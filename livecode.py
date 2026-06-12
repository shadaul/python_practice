# users = [
#     {"name": "Alice", "department": "Data"},
#     {"name": "Bob", "department": "Backend"},
#     {"name": "Charlie", "department": "Data"},
#     {"name": "David", "department": "Frontend"},
#     {"name": "Eve", "department": "Backend"}
# ]

# result = {}

# for user in users:
#     dept = user["department"]
#     name = user["name"]
#     if dept not in result:
#         result[dept] = []
#     result[dept].append(name)

# print(result)

# def is_valid(s):
#     stack = []
#     pairs = {')': '(', ']': '[', '}': '{'}

#     for char in s:
#         if char not in pairs:
#             stack.append(char)
#         else:
#             if not stack:
#                 return False
#             last = stack.pop()
#             if last != pairs[char]:
#                 return False
#             pass

#     return len(stack) == 0

# print(is_valid("()[]{}"))
# print(is_valid("([)]"))

# def fir_un(s):
#     col = {}
#     for item in s:
#         if item not in col:
#             col[item] = 1
#         else:
#             col[item] += 1
#     for index, element in enumerate(s):
#         if col[element] == 1:
#             return index
        
#     return -1
        

# print(fir_un("leetcode"))     
# print(fir_un("loveleetcode")) 
# print(fir_un("aabb"))

# def twonum(nums, target):
#     seen = {}
#     for index, num in enumerate(nums):
        
#         diff = target - num
#         if diff in seen:
#             return [seen[diff], index]
#         else:
#             seen[num] = index

# print(twonum([2, 7, 11, 15], 9))

# def maxProfit(prices):
#     if not prices:
#         return 0
#     min_price = prices[0]
#     max_profit = 0

#     for price in prices:
#         if price < min_price:
#             min_price = price
#         else:
#             current_price = price - min_price
#             if current_price > max_profit:
#                 max_profit = current_price
        
#     return max_profit

# print(maxProfit([7, 1, 5, 3, 6, 4]))

# def zero_last(nums):
#     insert_pos = 0
#     for num in nums:
#         if num != 0:
#             nums[insert_pos] = num
#             insert_pos += 1
#     while insert_pos < len(nums):
#         nums[insert_pos] = 0
#         insert_pos += 1

#     return nums

# print(zero_last([0, 1, 0, 3, 12]))

# def intersection(nums1, nums2):
#     set1 = set(nums1)
#     set2 = set(nums2)
#     result = []

#     for num in set1:
#         if num in set2:
#             result.append(num)

#     return result

# print(intersection([1, 2, 2, 1], [2, 2]))
# print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))

# def find_uniq(nums):
#     uniq = set(nums)
#     result = sum(uniq) * 2 - sum(nums)
#     return result

# matches = [
#     {"match_id": 101, "player": "Daulet", "hero": "Invoker", "stats": {"kills": 12, "deaths": 3}, "won": True},
#     {"match_id": 102, "player": "Karim", "hero": "Axe", "stats": {"kills": 8, "deaths": 5}, "won": False},
#     {"match_id": 103, "player": "Daulet", "hero": "Shadow Fiend", "stats": {"kills": 15, "deaths": 2}, "won": True},
#     {"match_id": 104, "player": "Roman", "hero": "Crystal Maiden", "stats": {"kills": 2, "deaths": 10}, "won": True},
#     {"match_id": 105, "player": "Daulet", "hero": "Invoker", "stats": {"kills": 5, "deaths": 6}, "won": False}
# ]


# def total_kills():
#     total = {}
#     for i in matches:
#         name = i["player"]
#         kills = i["stats"]["kills"]
#         if not i["won"]:
#             continue
#         if name not in total:
#             total[name] = kills
#         else:
#             total[name] += kills
#     return total

# raw_transactions = [
#     {"transaction_id": "T001", "user": "Karim", "price": 100, "quantity": 2},
#     {"transaction_id": "T002", "user": "Roman", "price": 250, "quantity": 1},
#     {"transaction_id": "T001", "user": "Karim", "price": 100, "quantity": 2}, # Полный дубликат!
#     {"transaction_id": "T003", "user": "Daulet", "price": -50, "quantity": 1}, # Отрицательная цена!
#     {"transaction_id": "T004", "user": "Roman", "price": 300, "quantity": 0}, # Нулевое количество!
#     {"transaction_id": "T005", "user": "Karim", "price": None, "quantity": 2}, # Нет цены!
#     {"transaction_id": "T006", "user": "Daulet", "price": 400, "quantity": 1}
# ]

# def clean_data(transactions):
#     clean_data = []
#     seen = set()
#     for i in transactions:
#         price = i["price"]
#         quantity = i["quantity"]
#         id = i["transaction_id"]
#         if (price is None or price <= 0) or (quantity is None or quantity <= 0):
#             continue
#         if id in seen:
#             continue

#         seen.add(id)
#         clean_data.append(i)
#     return clean_data

# silver_transactions = [
#     {"transaction_id": "T001", "user": "Karim", "price": 100, "quantity": 2},
#     {"transaction_id": "T002", "user": "Roman", "price": 250, "quantity": 1},
#     {"transaction_id": "T006", "user": "Daulet", "price": 400, "quantity": 1},
#     {"transaction_id": "T007", "user": "Karim", "price": 50, "quantity": 4}
# ]

# def calculate_gmv(transactions):
#     final = {}
#     for i in transactions:
#         price = i["price"]
#         quantity = i["quantity"]
#         user = i["user"]
#         col = price * quantity
#         if user not in final:
#             final[user] = col
#         else:
#             final[user] += col

#     return final

users = [
    {"user_id": 1, "name": "Daulet", "country": "PL"},
    {"user_id": 2, "name": "Karim", "country": "KZ"},
    {"user_id": 3, "name": "Roman", "country": "PL"}
]

transactions = [
    {"txn_id": "T1", "user_id": 1, "amount": 500},
    {"txn_id": "T2", "user_id": 2, "amount": 200},
    {"txn_id": "T3", "user_id": 1, "amount": 100}
]


def enrich_transactions(users, transactions):
    new = {}
    for user in users:
        us = user["user_id"]
        name = user["name"]
        new[us] = name

    for transaction in transactions:
        cur_id = transaction["user_id"]
        transaction["name"] = new[cur_id]

    return transactions

