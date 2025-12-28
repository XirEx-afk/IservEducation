from animals import*

def info(object):
    object.printInfo()

def animalSpeak(object):
    object.speak()

cat = Cat("Гав", 3, "Бенгальская")
dog = Dog("Бобик", 2, "Хаски")
newcat =  HomeCat("Муся", 4, "Сибирская", "Рыжая", "Вова")

newcat.printInfo()
info(newcat)
animalSpeak(newcat)

# from hospital import Doctor

# doc = Doctor("Айболит", [])
# doc.get_activity()
