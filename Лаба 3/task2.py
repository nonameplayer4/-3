# TODO Напишите функцию find_common_participants
def find_common_participants(s1, s2, separator=','):
    s1_new = s1.split(separator) #хотел сделать множественное присваивание
    s2_new = s2.split(separator) #но получилась супер длинная строка
    merger = set(s1_new).intersection(s2_new) #находим общих участников
    return list(merger) #попросили вернуть список

participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group))