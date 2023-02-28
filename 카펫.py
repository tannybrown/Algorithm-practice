def solution(brown, yellow):
    total = brown + yellow
    row = 3
    while 1 :
        if not (total % row) :
            col = total // row
            if 2 * (row + col) - 4 == brown :
                return [col,row]
        row += 1
    return answer
