def chess_board(rows,columns):
    return [['X' if (r+c) % 2  else 'O' for c in  range(columns)] 
            for r in range(rows)]


print(chess_board(4,4))