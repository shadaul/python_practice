# def get_even_numbers(nums):
#     return[num for num in nums if num % 2 ==0]


# numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# print(get_even_numbers(numbers))

def count_elements(items):
    counts = {}
    for item in items:
        if item in counts:
            counts[item] = counts[item] + 1
        else:
            counts[item] = 1
    return counts
    