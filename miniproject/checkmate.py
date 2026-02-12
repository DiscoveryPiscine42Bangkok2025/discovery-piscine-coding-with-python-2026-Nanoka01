def checkmate(board):
    if not board:
        print("Error")
        return

    rows = board.split("\n")

    size = len(rows)

    # ตรวจว่าเป็นกระดานสี่เหลี่ยมจัตุรัส
    for row in rows:

        if len(row) != size:
            print("Error")
            return

    
    have_king = False
    king_pos = None
    p_pos = None
    b_pos = None
    r_pos = None
    q_pos = None
    
    for i in range(size):
        for j in range(size):

            # หา King
            if rows[i][j] == "K":
                if not have_king :
                    have_king = True
                    king_pos = (i, j)
                else:
                    print("Error")
                    return
            # หา Pawn
            if rows[i][j] == "P":
                p_pos = (i,j)
                
            # หา Bishop
            if rows[i][j] == "B":
                b_pos = (i,j)
            
            # หา Rook
            if rows[i][j] == "R":
                r_pos = (i,j)
            
            # หา Rook
            if rows[i][j] == "Q":
                q_pos = (i,j)

    if not have_king:
        print("Error")
        return

    
    if p_pos:
        p_r, p_c = p_pos

        
        pawn_moves = [(-1, -1), (-1, 1)]
        for dr, dc in pawn_moves:
            r = p_r + dr
            c = p_c + dc
            if rows[r][c] == "K" and 0 <= r < size and 0 <= c < size:
                print("Success")
                have_king = False
                return
    
    if b_pos:
        b_r, b_c = b_pos

        bishop_move = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in bishop_move:
            r = b_r + dr
            c = b_c + dc
            while 0 <= r < size and 0 <= c < size:
                if rows[r][c] == "K":
                    print("Success")
                    have_king = False
                    return
                
                if rows[r][c] != ".":
                        break                  
                r += dr
                c += dc
    if r_pos:
        r_r, r_c = r_pos

        rook_move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in rook_move:
            r = r_r + dr
            c = r_c + dc
            while 0 <= r < size and 0 <= c < size:
                if rows[r][c] == "K":
                    print("Success")
                    have_king = False
                    return
                
                if rows[r][c] != ".":
                        break                  
                r += dr
                c += dc
    
    if q_pos:
        q_r, q_c = q_pos

        queen_move = [(-1, 0), (1, 0), (0, -1), (0, 1),(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in queen_move:
            r = q_r + dr
            c = q_c + dc
            while 0 <= r < size and 0 <= c < size:
                if rows[r][c] == "K":
                    print("Success")
                    have_king = False
                    return
                
                if rows[r][c] != ".":
                        break                  
                r += dr
                c += dc

    if have_king:
        print("Fail")