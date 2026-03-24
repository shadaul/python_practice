raw_codes = ["  proMo2024 ", "soap-FREE", "  WASH50  ", "cleaN-TeEth "]

clean_codes = []

for code in raw_codes:
    clean_codes.append(code.strip().upper())

print(clean_codes)

#======================================================================

skus = ["SHAMPOO-9942", "SOAP-1024", "DEODORANT-551"]

def get_categories(sku_list):
    categories = []
    
    for item in sku_list:
        pieces = item.split("-")
        categories.append(pieces[0])
    
    return categories

print(get_categories(skus))

#=========================================================

customers = [
    {"name": "Ivan", "code": "PROMO2024", "discount": 15},
    {"name": "Anna", "code": "WASH50", "discount": 50},
    {"name": "Oleg", "code": "CLEAN-TEETH", "discount": 10}
]

def send_promos(customer_list):
    for customer in customer_list:
        print(f"Hello {customer['name']} Your promo code {customer['code']} gives you a {customer['discount']} discount.")


send_promos(customers)