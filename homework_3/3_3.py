# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

word = input("Введите слово: ")
word_letters = [x for x in word.lower()]
eng_point_1 = ("a", "e", "i", "o", "u", "l", "n", "s", "t", "r")
eng_point_2 = ("d", "g")
eng_point_3 = ("b", "c", "m", "p")
eng_point_4 = ("f", "h", "v", "w", "y")
eng_point_5 = ("k")
eng_point_8 = ("j", "x")
eng_point_10 = ("q", "z")
rus_point_1 = ("а", "в", "е", "и", "н", "о", "р", "с", "т")
rus_point_2 = ("д", "к", "л", "м", "п", "у")
rus_point_3 = ("б", "г", "ё", "ь", "я")
rus_point_4 = ("й", "ы")
rus_point_5 = ("ж", "з", "х", "ц", "ч")
rus_point_8 = ("ш", "э", "ю")
rus_point_10 = ("ф", "щ", "ъ")
count = 0

for i in word_letters:
    if i in eng_point_1:
        count += 1
    if i in eng_point_2:
        count += 2
    if i in eng_point_3:
        count += 3
    if i in eng_point_4:
        count += 4
    if i in eng_point_5:
        count += 5
    if i in eng_point_8:
        count += 8
    if i in eng_point_10:
        count += 10
    if i in rus_point_1:
        count += 1
    if i in rus_point_2:
        count += 2
    if i in rus_point_3:
        count += 3
    if i in rus_point_4:
        count += 4
    if i in rus_point_5:
        count += 5
    if i in rus_point_8:
        count += 8
    if i in rus_point_10:
        count += 10
print(count)