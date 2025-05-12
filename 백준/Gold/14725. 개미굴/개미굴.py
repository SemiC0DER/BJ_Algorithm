#14725 개미굴

class Trie:
    def __init__(self):
        self.root = {}

    def add(self, intel):
        cur = self.root

        for food in intel:
            if food not in cur:
                cur[food] = {}
            cur = cur[food]
        cur[0] = 0

    def travel(self, level, cur):
        if 0 in cur:
            return

        child = sorted(cur)

        for ch in child:
            print("--" * level + ch)
            self.travel(level + 1, cur[ch])

N = int(input())
trie = Trie()
for _ in range(N):
    trie.add(input().split()[1:])
trie.travel(0, trie.root)