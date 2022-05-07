def solution(board, moves):
    answer = 0
    new_board = [[] for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board)):
            new_board[j].append(board[i][j])
    stack = []
    topIdx = [0] * len(new_board)
    for i in range(len(new_board)):
        for j in range(len(new_board)):
            if new_board[i][j] != 0:
                topIdx[i] = j
                break
    
    for move in moves:
        value = new_board[move-1][topIdx[move-1]]
        if value:
            if stack and stack[-1] == value:
                stack.pop()
                answer += 2
            else:
                stack.append(value)
            new_board[move-1][topIdx[move-1]] = 0
        topIdx[move-1] = min(len(new_board[0])-1, topIdx[move-1]+1)

    return answer