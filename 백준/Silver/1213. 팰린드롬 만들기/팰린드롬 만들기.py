#1213 팰린드롬 만들기

def make_palindrome(s):
    alphabet = [0] * 26
    n = len(s)
    odd = None
    palindrome = []

    for i in range(n):
        alphabet[ord(s[i]) - 65] += 1

    for i in range(26):
        if alphabet[i] % 2 == 1:
            if n % 2 == 0:
                print("I'm Sorry Hansoo")
                return
            else:
                if odd is None:
                    odd = i
                else:
                    print("I'm Sorry Hansoo")
                    return
    
    if n % 2 == 0:
        for i in range(26):
            if alphabet[i] == 0:
                continue
            for _ in range(alphabet[i] // 2):
                palindrome.append(chr(i + 65))

        palindrome.extend(palindrome[::-1])

        print(''.join(palindrome))
    else:
        for i in range(26):
            if alphabet[i] == 0:
                continue
            for _ in range(alphabet[i] // 2):
                palindrome.append(chr(i + 65))

        palindrome.append(chr(odd + 65))

        palindrome.extend(reversed(palindrome[:-1]))

        print(''.join(palindrome))

make_palindrome(input())