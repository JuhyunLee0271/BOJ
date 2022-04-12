def solution(genres, plays):
    answer = []
    temp_dict = dict()
    for genre, play in zip(genres, plays):
        if genre not in temp_dict:
            temp_dict[genre] = play
        else:
            temp_dict[genre] = temp_dict[genre] + play

    temp = sorted(list(temp_dict.items()), key=lambda x: -x[1])
    genre_dict, i = dict(), 0
    for i in range(len(temp)):
        genre_dict[temp[i][0]] = i
        i += 1

    result = [[] for _ in range(len(genre_dict))]
    for i in range(len(plays)):
        result[genre_dict[genres[i]]].append([i, plays[i]])

    for i in range(len(result)):
        result[i].sort(key=lambda x:(-x[1], x[0]))

    for i in range(len(result)):
        for j in range(0, min(len(result[i]), 2)):
            answer.append(result[i][j][0])

    return answer