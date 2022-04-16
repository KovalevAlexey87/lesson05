"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

str_obj = "1 2 3 4 5"
res = 0

with open('5_output.txt', 'w+', encoding='utf-8') as file_obj:
    file_obj.write(str_obj)

with open("5_output.txt", encoding='utf-8') as file_obj:
    content = file_obj.read().split(" ")
    for n in content:
        res = res + int(n)
    print(f"Сумма чисел = {res}")

"""
file 5_output.txt:
1 2 3 4 5
"""