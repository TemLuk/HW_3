print("Приветсвую тебя, пользователь!")
nickname, sex, age = input('Какой у тебя никнейм?'), input("Твой пол: М/Ж?"), int(input("Сколько тебе лет?"))
# Цикл для никнейма admin
if nickname == 'admin':
    print("Привет, повелитель!")
    if 10 < age < 14 and sex == 'М' or age > 30 and sex == 'М':
        print("Советую Вам посмотреть 'StarWars' или 'Мандалорец'.")
    if 22 < age < 32 and sex == 'Ж':
        print("Советую Вам посмотреть 'Трансформеры'.")
    if 16 > age and sex == 'Ж':
        print("Советую Вам посмотреть 'Инсургент'.")
    if 11 > age and sex == 'М':
        print("Советую Вам посмотреть 'TMNT'.")
# Цикл для никнейма Guido
if nickname == 'Guido':
    print("Огромное спасибо!")
    if 10 < age < 14 and sex == 'М' or age > 30 and sex == 'М':
        print("Советую Вам посмотреть 'StarWars' или 'Мандалорец'.")
    if 22 < age < 32 and sex == 'Ж':
        print("Советую Вам посмотреть 'Трансформеры'.")
    if 16 > age and sex == 'Ж':
        print("Советую Вам посмотреть 'Инсургент'.")
    if 11 > age and sex == 'М':
        print("Советую Вам посмотреть 'TMNT'.")

elif 10 < age < 14 and sex == 'М' or age > 30 and sex == 'М':
    print("Советую Вам посмотреть 'StarWars' или 'Мандалорец'.")
elif 22 < age < 32 and sex == 'Ж':
    print("Советую Вам посмотреть 'Трансформеры'.")
elif 16 > age and sex == 'Ж':
    print("Советую Вам посмотреть 'Инсургент'.")
elif nickname == 'Женя':
    print("Советую Вам посмотреть 'TENET'.")
elif 11 > age and sex == 'М':
    print("Советую Вам посмотреть 'TMNT'.")