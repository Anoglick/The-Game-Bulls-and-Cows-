# Функция, которая "упаковывает" значения в словарь, 
# где "ключ" - цифра одного из игрока, а "значение" - индекс цифры 
def packing(nums: str):
    if len(nums) != 4:
        return "Некорректный запрос: Число должно состоять из 4 цифр!"

    if not nums.isdigit():
        return "Некорректный запрос: Допустимы только цифры!"

    # Наш словарь
    values = {n: i for i, n in enumerate(nums)}

    # Преобразуем список цифр в множество, чтобы проверить уникальность
    uniq_values = set(nums)
    
    if len(nums) != len(uniq_values):
        return "Некорректный запрос: Допустимы только уникальные цифры!"
    
    return values

# Логика самой игры
def game(player_1, player_2):
    bulls, cows = 0, 0

    # Проходимся по ключам второго игрока (цифрам его числа)
    for key in player_2.keys():
        if player_2[key] == player_1.get(key, -1):
            bulls += 1
        elif key in player_1:
            cows += 1
    
    # Встроенная функция, отвечающая за выбор окончания слов
    def pluralize(count, singular, plural_1, plural_2):
        if count == 1:
            return f"{count} {singular}"
        elif 2 <= count <= 4:
            return f"{count} {plural_1}"
        else:
            return f"{count} {plural_2}"

    bulls_str = pluralize(bulls, "бык", "быка", "быков")
    cows_str = pluralize(cows, "корова", "коровы", "коров")

    return f"{bulls_str}, {cows_str}"

# Валидация ввода игрока
def get_valid_input(prompt):
    while True:
        # Запрашиваем ввод и проверяем его с помощью функции packing
        result = packing(input(prompt))
        if isinstance(result, str):  # Если введено некорректное число, то выводим причину
            print(result)
        else:
            return result