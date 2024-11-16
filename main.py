from logic import game, get_valid_input

def main():
    # Сохраняем числа игроков
    nums_player_1 = get_valid_input("1 Игрок вводит 4 уникальные цифры: ")
    nums_player_2 = get_valid_input("2 Игрок вводит 4 уникальные цифры: ")

    while True:
        player_1 = get_valid_input("Ходит 1 игрок: ")
        if player_1 == nums_player_2:  # Если игрок 1 угадал число игрока 2
            print("Игрок 1 угадал число!")
            break

        print(game(player_1, nums_player_2))  # Проверяем, сколько быков и коров у игрока 2

        player_2 = get_valid_input("Ходит 2 игрок: ")
        if player_2 == nums_player_1:  # Если игрок 2 угадал число игрока 1
            print("Игрок 2 угадал число!")
            break

        print(game(nums_player_1, player_2))

if __name__ == "__main__":
    main()