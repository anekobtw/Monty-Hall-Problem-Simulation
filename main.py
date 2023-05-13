import random

# Количество игроков и количество дверей
num_players = 1000
num_doors = 3

# Счетчики для подсчета результатов
stay_wins = 0
switch_wins = 0

# Запуск симуляции
for i in range(num_players):

    # Генерация позиции приза
    prize_position = random.randint(1, num_doors)

    # Игрок выбирает дверь
    player_choice = random.randint(1, num_doors)

    # Монтаж открывает одну из оставшихся дверей, не содержащих приз, и предлагает игроку поменять свой выбор
    available_doors = [x for x in range(1, num_doors + 1) if x != prize_position and x != player_choice]
    monty_choice = random.choice(available_doors)
    switch_choice = [x for x in range(1, num_doors + 1) if x != player_choice and x != monty_choice][0]

    # Подсчет результатов
    if player_choice == prize_position:
        stay_wins += 1
    elif switch_choice == prize_position:
        switch_wins += 1

# Вывод результатов
print("Победы, если оставить свой выбор: {} из {}".format(stay_wins, num_players))
print("Победы, если поменять свой выбор: {} из {}".format(switch_wins, num_players))
