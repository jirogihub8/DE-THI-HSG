import sys
input = sys.stdin.readline
a = int(input())
b = int(input())
th2=(a - 1) + (b - 1) + 2 * (min(a, b) - 1)
if a==b:
    th2-=1
print(th2)
