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

