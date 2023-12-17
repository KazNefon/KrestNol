# создаём поле
def draw_field(spots):
    board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
             f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
             f"|{spots[7]}|{spots[8]}|{spots[9]}|")
    print(board)


# проверяем кто ходит
def check_turn(turn):
    if turn % 2 == 0:
        return "O"
    else:
        return "X"


# проверяем на победу
def check_win(dict):
    if (spots[1] == spots[2] == spots[3]) \
            or (spots[4] == spots[5] == spots[6]) \
            or (spots[7] == spots[8] == spots[9]):
        return True
    elif (spots[1] == spots[4] == spots[7]) \
            or (spots[2] == spots[5] == spots[8]) \
            or (spots[3] == spots[6] == spots[9]):
        return True
    elif (spots[1] == spots[5] == spots[9]) \
            or (spots[3] == spots[5] == spots[7]):
        return True
    else:
        return False


spots = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", }

playing, finish = True, False
turn = 0
prev_turn = -1
# игровой цикл
while playing:
    draw_field(spots)
    if prev_turn == turn:
        print("Была выбрана недоступная ячейка, пожалуйста выберите другую")
    prev_turn = turn
    print(" Ход игрока: " + str((turn % 2) + 1) + "\n"
                                                  " Пожалуйста выберите ячейку или нажмите q для выхода")

    choice = input()

    if str.isdigit(choice) and int(choice) in spots:
        if not spots[int(choice)] in {"X", "O"}:
            turn += 1
            spots[int(choice)] = check_turn(turn)
    if check_win(spots): playing, finish = False, True
    if turn > 8:
        playing = False
if finish:
    if check_turn(turn) == "X":
        print("Игрок 1 победил!")
    else:
        print("Игрок 2 победил!")
else:
    print("Ничья")
