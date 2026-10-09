# def get_even_numbers(nums):
#     return[num for num in nums if num % 2 ==0]


# numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# print(get_even_numbers(numbers))

# def count_elements(items):
#     counts = {}                         alternamtive: counts[item] = counts.get(item, 0) + 1
#     for item in items:
#         if item in counts:
#             counts[item] = counts[item] + 1
#         else:
#             counts[item] = 1
#     return counts
    
# def get_names(users):
#     names = []
#     for user in users:
#         names.append(user['name'])             alternative: return [user['name'] for user in users]
#     return names

# def filter_approved(comments):
#     approv = []
#     for comment in comments:
#         if comment['status'] == 'approved':               alternamtive: return[comment for comment in comments if comment['status'] == 'approved']
#             approv.append(comment)

#     return approv

# def clean_names(names):
#     return [name.strip().capitalize() for name in names ]

# raw_api_response = [
#     {"transaction_id": "TX1001", "user_id": 42, "amount": "150.50", "status": "completed"},
#     {"transaction_id": "TX1002", "user_id": 15, "amount": None, "status": "failed"},
#     {"transaction_id": "TX1003", "user_id": 42, "amount": "89.90", "status": "completed"},
#     {"transaction_id": "TX1004", "user_id": 88, "amount": "200.00", "status": "pending"},
# ]

# def clean_transactions(data):
#     result = {}
#     for tr in data:
#         user_id = tr["user_id"]
#         amount = tr['amount']
#         if tr["status"] == 'completed' and tr["amount"] is not None:
#             result[user_id] = result.get(user_id, 0.0) + float(amount)
#     return result

# from pyspark.sql import functions as F

# result_df = (
#     sales_df
#     .filter(F.col("status") == "completed")
#     .withColumn("amount_vat", F.col("amount") * 1.2)
#     .groupBy("client_id")
#     .agg(F.sum("amount_vat").alias("total_spent"))
# )

transactions = [
    {"user_id": 101, "type": "deposit", "amount": 500},
    {"user_id": 102, "type": "deposit", "amount": 200},
    {"user_id": 101, "type": "withdrawal", "amount": 150},
    {"user_id": 103, "type": "deposit", "amount": 1000},
    {"user_id": 101, "type": "deposit", "amount": 300},
    {"user_id": 102, "type": "withdrawal", "amount": 50},
]

def calculate_balances(transactions):
    result = {}
    for transaction in transactions:
        type = transaction["type"]
        user_id = transaction["user_id"]
        amount = transaction["amount"]
        if type == 'deposit':
            result[user_id] = result.get(user_id, 0) + amount
        elif:
            result[user_id] = result.get(user_id, 0) - amount
    return result 