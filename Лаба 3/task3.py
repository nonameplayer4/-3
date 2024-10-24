# TODO  Напишите функцию count_letters
def count_letters(str_):
    s = str_.lower() # просто str_.lower() не сработал, пришлось создать новую переменную s
    dict_ = {}
    for i in range(len(s)):
        if s[i].isalpha(): # проверка на букву
            if s[i] in dict_:
                dict_[s[i]] += 1
            else:
                dict_[s[i]] = 1 #изначально у меня тут был 0, и я 3 часа искал ошибку, теперь здесь единица
    return dict_

# TODO Напишите функцию calculate_frequency
def calculate_frequency(dictionary: dict):
    sum = 0
    for _ in dictionary: #считаем общее кол-во 'встречаний' букв
        sum += dictionary[_]
    for elem in dictionary:
        dictionary[elem] = dictionary[elem] / sum
    return dictionary

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""


# TODO Распечатайте в столбик букву и её частоту в тексте
for i in calculate_frequency(count_letters(main_str)):
    print(f'{i}: {calculate_frequency(count_letters(main_str))[i]:.2f}')

