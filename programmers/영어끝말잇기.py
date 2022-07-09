
n = 2
words = ["hello", "one", "even", "never", "now", "world", "draw"]

def solution(n, words):
    history = set()
    before = words[0]
    history.add(words[0])
    for idx, word in enumerate(words):
        if idx == 0:
            continue
        if word in history or before[-1] != word[0] or len(word) == 1:
            return [idx%n+1, idx//n+1]
        else:
            history.add(word)
            before = word
    return [0, 0]



if __name__ == "__main__":
    print(solution(n, words))