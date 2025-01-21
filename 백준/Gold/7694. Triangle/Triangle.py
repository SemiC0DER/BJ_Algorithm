#7694 Triangle

import sys
input = sys.stdin.readline

'''
Pick의 정리: I(격자점) + B/2(경계점) - 1 = S(넓이)
'''

def triangle_area(x1, y1, x2, y2, x3, y3):
    return abs(x1 * y2 + x2 * y3 + x3 * y1 - x1 * y3 - x2 * y1 - x3 * y2) // 2

def edge_points(x1, y1, x2, y2):
    x = abs(x1 - x2)
    y = abs(y1 - y2)
    return gcd(x, y) - 1

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def triangle_points(x1, y1, x2, y2, x3, y3):
    area = triangle_area(x1, y1, x2, y2, x3, y3)
    bp = 3 + edge_points(x1, y1, x2, y2) + edge_points(x2, y2, x3, y3) + edge_points(x3, y3, x1, y1)

    return area + 1 - bp // 2

while True:
    x1, y1, x2, y2, x3, y3 = map(int, input().split())

    if x1 == y1 == x2 == y2 == x3 == y3 == 0:
        break

    print(triangle_points(x1, y1, x2, y2, x3, y3))