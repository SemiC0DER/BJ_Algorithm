#1973 놀라운 문자열

while (word:= input()) != '*':
    sg = ''
    for i in range(1, len(word)):
        d = set()
        for j in range(0, len(word) - i):
            s_word = word[j] + word[j + i]
            if s_word in d:
                sg = 'NOT '
                break
            d.add(s_word)
    print(f"{word} is {sg}surprising.")