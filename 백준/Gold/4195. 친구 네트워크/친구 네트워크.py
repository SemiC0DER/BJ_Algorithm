#4195 친구 네트워크
import sys
input = lambda : sys.stdin.readline().rstrip()
class Book():
    def __init__(self):
        self.book = {}

    def relation(self, a, b):
        a = self.captain(a)
        b = self.captain(b)
        if a == b:
            print(self.book[a][1])
            return
            
        if a > b: a, b = b, a
        self.book[a][1] += self.book[b][1]
        self.book[b][0] = [a][0]
        print(self.book[a][1])

    def captain(self, name):
        if not name in self.book:
            self.book[name] = [name, 1]
            return name

        if self.book[name][0] != name:
            self.book[name][0] = self.captain(self.book[name][0])

        return self.book[name][0]

T = int(input())
for _ in range(T):
    F = int(input())
    phone = Book()
    for _ in range(F):
        a, b = input().split()
        phone.relation(a, b)