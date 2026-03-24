boxes = [15.5, 20.0, 10.2, 30.5, 5.0, 40.2, 12.0]

heaviest = 0
total = 0

for weight in boxes:
    total += weight
    if weight > heaviest:
        heaviest = weight

print(f" тяжелая: {heaviest},total: {total}")

def quality_control(all_boxes):
    approved_boxes = []
    for weight in all_boxes:
        if weight >= 10 and weight <= 30:
            approved_boxes.append(weight)
    return approved_boxes

good_boxes = quality_control(boxes)
print(f" korobki proshedshie kontrol' {good_boxes}")


inventory = {
    "Soap": 50,
    "Shampoo": 12,
    "Toothpaste": 150,
    "Deodorant": 8
}

def check_low_stock(stock_dict, limit):
    for item,quantity in stock_dict.items():
        if quantity < limit:
            print(f"tovar {item} ostalos' {quantity}")

check_low_stock(inventory,15)