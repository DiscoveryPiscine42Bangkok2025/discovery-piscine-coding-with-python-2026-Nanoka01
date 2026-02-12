def checkmate(board):

    rows = board.split("\n")
    size = len(rows)

    # หา King
    king_row = -1
    king_col = -1

    for i in range(size):
        for j in range(len(rows[i])):
            if rows[i][j] == "K":
                king_row = i
                king_col = j

    if king_row == -1:
        print("Fail")
        return

    # -------------------------
    # ตรวจ Pawn (P)
    # Pawn กินเฉียงขึ้น
    if king_row - 1 >= 0:
        if king_col - 1 >= 0:
            if rows[king_row - 1][king_col - 1] == "P":
                print("Success")
                return

        if king_col + 1 < size:
            if rows[king_row - 1][king_col + 1] == "P":
                print("Success")
                return

    # -------------------------
    # ตรวจ Rook (R)
    # เช็คขึ้น
    i = king_row - 1
    while i >= 0:
        if rows[i][king_col] != ".":
            if rows[i][king_col] == "R" or rows[i][king_col] == "Q":
                print("Success")
                return
            break
        i -= 1

    # เช็คลง
    i = king_row + 1
    while i < size:
        if rows[i][king_col] != ".":
            if rows[i][king_col] == "R" or rows[i][king_col] == "Q":
                print("Success")
                return
            break
        i += 1

    # เช็คซ้าย
    j = king_col - 1
    while j >= 0:
        if rows[king_row][j] != ".":
            if rows[king_row][j] == "R" or rows[king_row][j] == "Q":
                print("Success")
                return
            break
        j -= 1

    # เช็คขวา
    j = king_col + 1
    while j < size:
        if rows[king_row][j] != ".":
            if rows[king_row][j] == "R" or rows[king_row][j] == "Q":
                print("Success")
                return
            break
        j += 1

    # -------------------------
    # ตรวจ Bishop (B)
    # ทแยงบนซ้าย
    i = king_row - 1
    j = king_col - 1
    while i >= 0 and j >= 0:
        if rows[i][j] != ".":
            if rows[i][j] == "B" or rows[i][j] == "Q":
                print("Success")
                return
            break
        i -= 1
        j -= 1

    # ทแยงบนขวา
    i = king_row - 1
    j = king_col + 1
    while i >= 0 and j < size:
        if rows[i][j] != ".":
            if rows[i][j] == "B" or rows[i][j] == "Q":
                print("Success")
                return
            break
        i -= 1
        j += 1