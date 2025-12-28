from car import *

# Машина
# car1 = Car("Lada Granta", "Черный", 200)
# car2 = Car("Kia K5", "Белый", 500)

# car1.printInfo()
# car2.printInfo()


# Кот
# cat1 = Cat("Ахмэд", "Черная", "Таджитская")

# cat1.printInfo()
# cat1.say()


# Перекраска машины
# car1 = Car("Kia Rio", "Чёрный", 350)
# car1.printInfo()

# name=car1.name
# print(name)
# car1.color = "Белый"
# car1.printInfo()

car1 = Car("Kia Rio", "Чёрный", 350)
car1.printInfo()

name = getattr(car1, "name")
print(name)

setattr(car1, "color", "Белый")
car1.printInfo()
car1.start_engine()
car1.start_engine()