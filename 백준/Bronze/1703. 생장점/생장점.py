while (tree := list(map(int, input().split()))) != [0]:
    leaf = 1
    i = 1
    for _ in range(tree[0]):
        leaf = leaf * tree[i] - tree[i + 1]
        i += 2
    print(leaf)