# Задача 2: Найдите сумму цифр трехзначного числа.

number = int(input('Введите трёхзначное число: '))
a = number // 100
b = number // 10 % 10
c = number % 10
print (a + b + c)