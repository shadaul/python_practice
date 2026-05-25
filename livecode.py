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

def find_uniq(nums):
    uniq = set(nums)
    result = sum(uniq) * 2 - sum(nums)
    return result

