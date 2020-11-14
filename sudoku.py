bo = [
        [0, 7, 5, 0, 9, 0, 0, 0, 6],
        [0, 2, 3, 0, 8, 0, 0, 4, 0],
        [8, 0, 0, 0, 0, 3, 0, 0, 1],
        [5, 0, 0, 7, 0, 2, 0, 0, 0],
        [0, 4, 0, 8, 0, 6, 0, 2, 0],
        [0, 0, 0, 9, 0, 1, 0, 0, 3],
        [9, 0, 0, 4, 0, 0, 0, 0, 7],
        [0, 6, 0, 0, 7, 0, 5, 8, 0],
        [7, 0, 0, 0, 1, 0, 3, 9, 0]
    ]

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def find_empty(bo):
    for r in range(9):
        for c in range(9):
            if bo[r][c] == 0:
                return r, c

    return None, None

def check_valid(bo, num, row, col):
    # rows
    row_val = bo[row]
    if num in row_val:
        return False

    # cols
    cols_val = [bo[i][col] for i in range(9)]
    if num in cols_val:
        return False

    # squares
    row_sq = (row // 3) * 3
    col_sq = (col // 3) * 3

    for r in range(row_sq, row_sq + 3):
        for c in range(col_sq, col_sq + 3):
            if bo[r][c] == num:
                return False
        
    return True

def solve_puzzle(bo):

    row, col = find_empty(bo)

    if row is None:
        return True

    for num in range(1, 10):
        if check_valid(bo, num, row, col):
            bo[row][col] = num

            if solve_puzzle(bo):
                return True
    
        bo[row][col] = 0

    return False


print_board(bo)
solve_puzzle(bo)
print('\n\n')
print_board(bo)
