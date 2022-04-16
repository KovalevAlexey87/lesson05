"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

homework5 = []
while True:
    line = input("Введите числа: ")
    if line == '':
        print(homework5)
        exit()
    else:
        newline = line + '\n'
        homework5.append(newline)
    with open("file1.txt", "w", ) as file_obj:
        file_obj.writelines(homework5)
