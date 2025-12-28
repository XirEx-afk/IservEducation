class Car:
    def __init__(self, name, color, power):
        self.name = name
        self.color = color
        self.power = power
        self.mileage = 0
        self.is_running = False
    
    def printInfo(self):
        print("="*10)
        print(f"Название машины: {self.name}")
        print(f"Цвет: {self.color}")
        print(f"Мощность: {self.power}")
        print(f"Пробег: {self.mileage}")
        print(f"Машина: {self.is_running}")
        print("="*10)

    def start_engine(self):
        if self.is_running:
            print("Двигатель уже заведён!")
            return
        self.is_running = True
        print("Двигатель запущен")

# class Cat:
#     def __init__(self, name, color, breed):
#         self.name = name
#         self.color = color
#         self.breed = breed
    
#     def printInfo(self):
#         print("="*10)
#         print(f"Имя кошки: {self.name}")
#         print(f"Цвет кошки: {self.color}")
#         print(f"Порода: {self.breed}")
#         print("="*10)

#     def say(self):
#         print("Ахмэд сказал - Мээуу жи есть да")