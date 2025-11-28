import random

# Лабиринт 5x5 (0 - стена, 1 - проход, M - монстр, S - меч, K - ключ, T - ловушка, E - выход)
lab = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 'M', 0],
    [0, 1, 0, 1, 0],
    [0, 'K', 'T', 'S', 0],
    [0, 0, 0, 0, 0]
]

# Позиция игрока
x, y = 1, 1
health = 100
has_sword = False
has_key = False

# Игровой цикл
while health > 0:
    # Показываем лабиринт
    for i in range(5):
        for j in range(5):
            if i == x and j == y:
                print('P', end=' ')  # Игрок
            else:
                print(lab[i][j], end=' ')
        print()
    
    # Проверяем текущую клетку
    cell = lab[x][y]
    
    if cell == 'M':
        if has_sword:
            print("Вы победили монстра мечом!")
            lab[x][y] = 1
        else:
            print("Монстр атакует! Нужен меч.")
            health -= 30
    
    elif cell == 'S':
        print("Вы нашли меч!")
        has_sword = True
        lab[x][y] = 1
    
    elif cell == 'K':
        print("Вы нашли ключ!")
        has_key = True
        lab[x][y] = 1
    
    elif cell == 'T':
        print("Ловушка! -20 здоровья")
        health -= 20
        lab[x][y] = 1
    
    elif cell == 'E':
        print("Победа! Вы вышли из лабиринта!")
        break
    
    print(f"Здоровье: {health}, Меч: {'есть' if has_sword else 'нет'}, Ключ: {'есть' if has_key else 'нет'}")
    
    # Движение
    move = input("Куда идти? (wasd): ").lower()
    new_x, new_y = x, y
    
    if move == 'w': new_x -= 1
    elif move == 's': new_x += 1
    elif move == 'a': new_y -= 1
    elif move == 'd': new_y += 1
    
    # Проверка возможности хода
    if lab[new_x][new_y] != 0:
        x, y = new_x, new_y
    else:
        print("Туда нельзя!")

if health <= 0:
    print("Вы погибли!")