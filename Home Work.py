print('-_- Крестики-нолики -_-')

field = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

win_comb = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

def print_field():
    print(field[0], field[1], field[2], '            7 8 9')
    print(field[3], field[4], field[5], '  Схема ->  4 5 6') # Схема для игры на numpad.
    print(field[6], field[7], field[8], '            1 2 3')

def step_maps(step, symbol):  # Я понимаю, что это странно, но я не смог придумать ничего другого.
    if step == 1:
        field[6] = symbol
    elif step == 2:
        field[7] = symbol
    elif step == 3:
        field[8] = symbol
    elif step == 4:
        field[3] = symbol
    elif step == 5:
        field[4] = symbol
    elif step == 6:
        field[5] = symbol
    elif step == 7:
        field[0] = symbol
    elif step == 8:
        field[1] = symbol
    elif step == 9:
        field[2] = symbol

def chek(symbol):
    valid = False
    while not valid:
        try:
            step = int(input(f"Ход игрока {symbol}: "))
        except ValueError:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if 1 <= step <= 9:
            if str(field[step - 1]) not in "XO":
                valid = True
            else:
                print('Эта ячейка уже занята!')
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")

    return step

def get_result():
    win = ""
    for i in win_comb:
        if field[i[0]] == "X" and field[i[1]] == "X" and field[i[2]] == "X":
            win = "X"
        if field[i[0]] == "0" and field[i[1]] == "0" and field[i[2]] == "0":
            win = "0"

    return win

def main():
    counter = 1
    win = False
    while not win:
        print("_______________________")
        print_field()
        if counter % 2 == 0:
            symbol = "X"
            step_maps(chek(symbol), symbol)
        else:
            symbol = "0"
            step_maps(chek(symbol), symbol)
        counter += 1
        tmp = get_result()
        if tmp == "X":
            print(tmp, "выиграл!")
            print("\n")
            break
        elif tmp == "0":
            print("__________")
            print(f"{tmp} выиграл!")
            break
        if counter == 9:
            print("Ничья!")
            break
    print_field()

main()

