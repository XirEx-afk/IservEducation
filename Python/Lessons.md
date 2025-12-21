# Мой конспект

## Мой первый калькулятор:
```
print("Введите первое число:")
a = int(input())
print("Введите второе число:")
b = int(input())
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
```
## Преобразование чисел:
```
print(type(str(55)))
print(type(str(0.32)))

print(type(float(432)))
print(type(float(23)))

print(type(int(6.44)))
print(type(int(23.32)))
```
## Сколько тебе лет:
```
print("Введите ваш год рождения:")
birth_year = int(input())
print("Введите текущий год:")
current_year = int(input())

age = current_year - birth_year
print(f"В этом году вам исполнилось {age} лет")
```
## Дополнительные операторы деления:
```
print("Результат остаточного деления числа 435 на 23 =", 435 % 23)
print("Результат остаточного деления числа 543 на 246 =", 543 % 246)
print("Результат целочисленного деления числа 400 на 20 =", 400 // 20)
```
## Проверка возвраста:
```
myAge = int(input("Введите ваш возвраст:"))
if(myAge < 18):
    print("Вы не совершенолетний!")
else:
    print("Вы совершенолетний")
```
# Работа с условными конструкциями:
*Условные операторы if/else/elif
```
myAge = int(input("Введите ваш возвраст"))
if (myAge < 6):
    print("Вы ребёнок")
elif (myAge >= 13 and myAge < 20):
    print("Вы подросток")
else:
    print("Вы уже взрослый")
```
## Продавец:
```
book = 100
a = int(input("Введите свой бюджет:"))
if a >= 100:
    print("у вас достаточно денег, оформите покупку?")
else:
    print("У вас не хватает денег, можете купить другую книгу")
```

## Мой первый проект: "Определитель возвраста"
```
current_year = 2025
current_month = 10
current_day = 5
birth_year = int(input("Введите ваш год рождения:"))
birth_month = int(input("Введите ваш месяц рождения:"))
birth_day = int(input("Введите ваш день рождения:"))
age = current_year - birth_year
if(current_month > birth_month):
    print("Вам", age, "лет")
elif(current_month == birth_month):
    if(current_day >= birth_day):
        print("Вам", age, "лет")
    else:
        print("Вам", age - 1, "лет")
else:
    print("Вам", age - 1, "лет")
```

# 4 урок:
```
age = 0

while age < 18:
    print(f"Мне {age} лет. Я ребёнок")
    age += 1
print("Пора в качалку!")

i = 0
while i < 5:
    print("Привет")
    i += 1

a = 1
b = "Волтер"
while a < 11:
    print(a,b)
    a += 1
```

## Задача №2
```
price = 20
allMoney = 110

while allMoney >= price:
    print("Вы купили товар")
    allMoney -= price
    print(f"У вас осталось {allMoney} рублей")
print("У вас недостаточно денег на счёте")
```

## Задача №3 "Работа с циклом while"
```
print("Игра - Отгадай число\n")
randomNumber = 34
inputNumber = int(input("Угадай какое число я загадал (1-100): "))

while randomNumber != inputNumber:
    if randomNumber < inputNumber:
        print("Загаданное число меньше")
    else:
        print("Загаданное число больше")
    inputNumber = int(input("Попробуй ещё раз"))
print("Ты отгадал")
```
# Цикл "for"
```
for i in range(0,51):
    print("Hello world")
```
## Задача №4
```
summa = 0
N = int(input("Введите число"))
for i in range(1,N + 1):
    summa += i
print(summa)
```
# Урок 6
## Практическая работа с циклом WHILE:
```
a = 1
c = 1
while c != 0:
    a *= c
    c = int(input("Введите число: "))
print(a)
```

## Практика с циклом FOR
```
for i in range(1,101):
    if i % 3 != 0 and i % 5 != 0:
        print(i)
```

## Практическая работа со СПИСКОМ:
```
## №1
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
fruits.insert(1, 'lemon')
fruits.pop(2)
print(fruits)

## №2
grades = [85, 90, 78, 92, 88, 76, 95, 89, 100, 72]
print(max(grades)),print(min(grades))
summa = sum(grades)
print(summa)
print(summa / len(grades))
print(grades.sort())
```

## Практика с библиотекой MATH:
```
import math
part_1_1 = math.cos(math.pi/3) + math.log2(16)
print(part_1_1)
part_1_2 = sum([math.factorial(n) + 1 for n in range(0,4)])
part_1 = part_1_1 * part_1_2
print(part_1_2)
part_2 = (math.sqrt(25) - abs(-5)) ** math.sin(math.pi/2)
print(part_2)
part_3 = (3 ** 2 + 4 ** 2) / 5 * (math.tan(0) + 1)
print(part_3)
result = part_1 + part_2 - part_3
print(result)
```

# Практика с библиотекой RANDOM:
```
import random
for i in range(5):
    rand_num =  random.randint(1,100)
    print(rand_num)
```
## Игра УГАДАЙ ЧИСЛО
```
import random
life = 5
rand_num = random.randint(1,50)
isWin = False
print("Было загадано число от 1 до 50. Попробуй угадать!")
while life != 0:
    num = int(input("Введите число:"))
    if num == rand_num:
        print("Вы победили!")
        isWin = True
        break
    elif num < rand_num:
        print("Загаданное число больше.")
        life -= 1
    elif num > rand_num:
        print("Загаданное число меньше.")
        life -= 1
if(not isWin):
    print("Вы проиграли :(")
```

## Работа с библеотекой TURTLE
```
import turtle

screen = turtle.Screen()
screen.setup(600,600)
screen.bgcolor("lightblue")
screen.title("Весёлый смайлик - Изучаем Turtle")
t = turtle.Turtle()
t.speed(5)
t.width(3)
t.penup()
t.goto(0, -100)
t.pendown()
t.color("black", "yellow")
t.begin_fill()
t.circle(100)
t.end_fill()

# Левый глаз
t.penup()
t.goto(-40,30)
t.pendown()
t.color("black", "white")
t.begin_fill()
t.circle(20)
t.end_fill()
t.penup()
t.goto(-40,40)
t.pendown()
t.color("black", "black")
t.begin_fill()
t.circle(10)
t.end_fill()

# Правый глаз
t.penup()
t.goto(40,30)
t.pendown()
t.color("black", "white")
t.begin_fill()
t.circle(20)
t.end_fill()
t.penup()
t.goto(40,40)
t.pendown()
t.color("black", "black")
t.begin_fill()
t.circle(10)
t.end_fill()

# Улыбка
t.penup()
t.goto(-60,-20)
t.pendown()
t.color("black")
t.width(5)
t.setheading(-60)
t.circle(70,120)

# Скрываем черепашку
t.hideturtle()
screen.exitonclick()
```

# Функция с параметрами:
```
# Функция с параметрами
def exam_result(russian, math, informatics):
    total = russian + math + informatics

    if 0 <= total and total <= 120:
        print('Плохо')
    elif 121 <= total and total <= 210:
        print('Хорошо')
    elif 211 <= total and total <= 300:
        print('Отлично')
    else:
        print('Введены некорректные значения')
exam_result(67, 72, 80)
```

## Задача №1 создание пароля
```
import random
import string

def password_generation(lenPas, isNums, isUpAlpha):
    symbols = string.ascii_lowercase
    password  = ""

    if isUpAlpha:
        symbols += string.ascii_uppercase
    if isNums:
        symbols += '1234567890'
    
    for _ in range(lenPas):
        password += random.choice(symbols)
    return password
print("---Программа для генерации пароля---")
lenPas = int(input("Введите длину пароля: "))
isNums = input("Нужны ли цифры в пароле? Y/n: ")
isUpAlpha = input("Нужны ли большие буквы в пароле Y/n: ")

if isNums.lower() == "y":
    isNums = True
else:
    isNums = False
if isUpAlpha.lower() == "y":
    isUpAlpha = True
else:
    isUpAlpha = False
password = password_generation(lenPas, isNums, isUpAlpha)
print(password)
```

## Задача: Какая сумма у чисел:
```
def SumOfDigits(number):
    strNum = str(number)
    sumDigits = 0
    for i in strNum:
        sumDigits += int(i)
    return sumDigits
print(f"Сумма цифр в числе 1234 равна {SumOfDigits(1234)}")
```

# Первое приложение
```

```