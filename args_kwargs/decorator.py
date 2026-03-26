def smart_logger(func):
    def wrapper(*args, **kwargs):
        print(" Умный дом: начинаю действие...")
        result = func(*args, **kwargs)
        print(" Действие завершено!\n")         
        return result
    
    return wrapper


@smart_logger
def turn_on_lights(room, brightness):
    print(f" Включаю свет: {room}, яркость {brightness}%")


@smart_logger
def boil_kettle(temperature, mode="Standard"):
    print(f" Грею воду до {temperature}°C в режиме {mode}")



turn_on_lights("Кухня", brightness=80)
boil_kettle(90, mode="Tea")

def urgent(func):
    def wrapper(*args, **kwargs):
        print("СРОЧНО! БРОСАЙ ВСЕ ДЕЛА!")
        result = func(*args, **kwargs)
        print("ПОЧЕМУ ТАК ДОЛГО?!")
        return result
    return wrapper

@urgent
def write_report(topic):
    print(f"Пишу скучный отчет на тему: {topic}...")

@urgent
def drink_coffee():
    print(" Пью кофе...")


write_report("Финансы")
drink_coffee()

def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        result = func(*args, **kwargs)
        return result
    return wrapper


@do_twice
def say_hello(name):
    print(f" Привет, {name}!")

@do_twice
def attack(damage):
    print(f" Нанесен удар силой {damage} урона!")


say_hello("Даулет")
attack(50)