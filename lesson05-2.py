"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

list_homework5 = ['Lesson05\n', 'Homework\n', '5\n']
with open("file2.txt", 'w+') as file_obj:
    file_obj.writelines(list_homework5)
with open("file2.txt") as file_obj:
    lines = 0
    letters = 1
    for line in file_obj:
        for n in line:
            if n == " ":
                letters += 1
        lines += 1
        print(f"Количество слов в строке № {lines} равно {letters} \n")
        letters = 1
    print(f"Количество строк: {lines}")

"""
file file2.txt:
Lesson05
Homework
5

"""