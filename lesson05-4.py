"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

text = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
new_file = []
with open("4_input.txt", 'r', encoding='utf-8') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(text[i[0]] + '  ' + i[1])
    print(new_file)
with open("4_output.txt", 'w') as file_obj_2:
    file_obj_2.writelines(new_file)

"""
file 4_input.txt:
One — 1
Two — 2
Three — 3
Four — 4
"""
