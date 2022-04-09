# ex_1.1
print("Hello!")
a = input("Enter your name: ")
num_1 = int(input("Enter number_1: "))
num_2 = int(input("Enter number_2: "))
print("multiplication result", a, ":", num_1 * num_2)
print("subtraction result", a, ":", num_1 - num_2)
print("addition result", a, ":", num_1 + num_2)
print("goodbye")

# ex_1.2
num = int(input("Enter number: "))
if num > 0:
    sec = num % 60
    min1 = num // 60 % 60
    clok = num // 3600
    print(f"Convert to hours:minutes:seconds {clok:02}:{min1:02}:{sec:02}")
else:
    print("Enter a positive number!")

# ex_1.3
num = input("Enter number: ")
num_2 = int(num + num)
num_3 = int(num * 3)
sum_1 = int(num) + num_2 + num_3
print(f"результат: {num} + {num_2} + {num_3} = {sum_1}")

# ex_1.4 Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
num = int(input("Enter number > 0: "))
i = 0
while num > 0:
    num_2 = num % 10
    if num_2 < 1:
        break
    num = num // 10
    if i < num_2:
        i = num_2
if i <= 0:
    print("Ввели неверное число!")
else:
    print("Самая большая цифра в числе:", i)

#   или 2-й вариант решения задачи (ex_1.4.1)
a = int(input("Enter number > 0: "))
i = 0
while a > 0:
    isc = a % 10
    a = a // 10
    if isc > i:
        i = isc
print("Самая большая цифра в числе:", i)

# ex_1.5
revenue = int(input("Введите прибыль: "))
firm_cost = int(input("Введите убыток: "))
if revenue > firm_cost:
    rentab = (revenue - firm_cost) / firm_cost
    numb_empl = int(input("Введите численность сотрудников фирмы: "))
    reven_pers = revenue / numb_empl
    print(f"рентабельность выручки {rentab:.2f}, численность сотрудников фирмы {numb_empl}")
    print(f"прибыль фирмы в расчёте на одного сотрудника равна: {reven_pers:.3f}")
elif revenue < firm_cost:
    print(f'издержки больше выручки в: {(firm_cost - revenue) // revenue} раз')
else:
    print('нужен аудитор!')

# ex_1.6
a_start = int(input("В первый день результат составил (км): "))
b_end = int(input("Планируемый результат (км): "))
i = 0
while a_start < b_end + a_start * .1:
    i += 1
    print(f"{i}-й день: {a_start:.2f}")
    a_start = a_start * 1.1
print(f'Ответ: на {i} день спортсмен достиг результата — не менее {b_end} км.')
