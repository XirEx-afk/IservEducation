# lst1 = [23, 57, 13, 67, 75]
# new_lst1 = []
# for i in lst1:
#     new_lst1.append(i ** 2)

# results1 = sum(new_lst1)
# print(results1)

# lst2 = [14, 49, 6, 64]
# new_lst2 = []
# for i in lst2:
#     new_lst2.append(i ** 2)

# results2 = sum(new_lst2)
# print(results2)

# lst3 = [8, 90, 55, 83, 1, 22]
# new_lst3 = []
# for i in lst3:
#     new_lst3.append(i ** 2)

# results3 = sum(new_lst3)
# print(results3)

# def sum_squares_nums(lst):
#     new_lst = []
#     for i in lst:
#         new_lst.append(i ** 2)

#     results = sum(new_lst)
#     return results
# lst1 = [23, 57, 13, 67, 75]
# result1 = sum_squares_nums(lst1)
# print(result1)

# lst2 = [14, 49, 6, 64]
# result2 = sum_squares_nums(lst1)
# print(result2)

# lst3 = [8, 90, 55, 83, 1, 22]
# result3 = sum_squares_nums(lst1)
# print(result3)


# Функция с параметрами
# def exam_result(russian, math, informatics):
#     total = russian + math + informatics

#     if 0 <= total and total <= 120:
#         print('Плохо')
#     elif 121 <= total and total <= 210:
#         print('Хорошо')
#     elif 211 <= total and total <= 300:
#         print('Отлично')
#     else:
#         print('Введены некорректные значения')
# exam_result(67, 72, 80)

# # Задача №1 создание пароля
# import random
# import string

# def password_generation(lenPas, isNums, isUpAlpha):
#     symbols = string.ascii_lowercase
#     password  = ""

#     if isUpAlpha:
#         symbols += string.ascii_uppercase
#     if isNums:
#         symbols += '1234567890'
    
#     for _ in range(lenPas):
#         password += random.choice(symbols)
#     return password
# print("---Программа для генерации пароля---")
# lenPas = int(input("Введите длину пароля: "))
# isNums = input("Нужны ли цифры в пароле? Y/n: ")
# isUpAlpha = input("Нужны ли большие буквы в пароле Y/n: ")

# if isNums.lower() == "y":
#     isNums = True
# else:
#     isNums = False
# if isUpAlpha.lower() == "y":
#     isUpAlpha = True
# else:
#     isUpAlpha = False
# password = password_generation(lenPas, isNums, isUpAlpha)
# print(password)


# def isEeven(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False

# num = int(input("Введите ваше число: "))

# if(isEeven(num)):
#     print("Число чётное")
# else:
#     print("Число нечётное")


# def CountGlassSymbols(text):
#     glassSymbol = "уеыаоэяиюё"
#     count = 0
#     for i in text:
#         if glassSymbol.find(i) != -1:
#             count += 1
#     return count
# string = "всем привет, я крутая строка!"
# print(f"В строке \"{string}\" {CountGlassSymbols(string)} гласных букв")


# def SumOfDigits(number):
#     strNum = str(number)
#     sumDigits = 0
#     for i in strNum:
#         sumDigits += int(i)
#     return sumDigits
# print(f"Сумма цифр в числе 1234 равна {SumOfDigits(1234)}")