import re
while True:
    reg = re.compile('[^а-яА-Я ^a-zA-Z ]')
    a = " "
    def changer(word):
        stc = input(word)
        if not stc.isdigit():
            for ltr in ['і', 'е', 'у', 'ї', 'а', 'о', 'є', 'я', 'и', 'ю', 'e', 'y', 'u', 'i', 'o', 'a', 'э', 'ы']:
                stc = stc.replace(ltr, "*")
            qty = stc.count("*")
            return print(stc, qty)
        else:
            return print("Ви ввели числові значення, а не текст.")
    answer = changer("Введіть речення, або текст: ")
    if input('Спробувати ще раз?\nТак - введіть будь-яке значення.\nНі - введіть "n".') == "n":
        break



