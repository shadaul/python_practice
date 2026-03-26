def print_receipt(customer_name, *items, **details):
    for item in items:
        print(f"tovar - {item}")
    for key, value in details.items():
        print(f"{key}, {value}")


print_receipt("Даулет", "Яблоки", "Молоко", "Хлеб", discount="10%", payment_method="Card")

def calculate_total(player, *args):
    print(f" {player} zarabotal {sum(args)}")


calculate_total("Даулет", 10, 20, 50)
calculate_total("Анна", 100, 500)

def build_profile(username, **kwargs):
    print(username)
    for key, value in kwargs.items():
        print(f"{key} = {value}")

build_profile("Neo", role="Избранный", city="Zion", skill="Kung-Fu")
build_profile("Trinity", status="Online")