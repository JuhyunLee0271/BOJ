def solution(dirs):
    dx = {'U': 0, 'D': 0, 'L': -1, 'R':1}
    dy = {'U': 1, 'D': -1, 'L': 0, 'R':0}
    
    start = (0, 0)
    path = set()
    
    for d in dirs:
        _x, _y = start
        x, y = _x + dx[d], _y + dy[d]
        if -5 <= x <= 5 and -5 <= y <= 5:
            path.add(tuple(sorted([(_x, _y,), (x, y)])))
            start = x, y
        
    return len(path)