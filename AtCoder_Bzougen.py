import io
import sys

_INPUT = """\
10
9
10
3
100
100
90
80
10
30
10



"""
sys.stdin = io.StringIO(_INPUT)
n = int(input())
s = []
s.append(int(input())) #appendは末尾に要素を追加
for i in range(n-1):
    s.append(int(input()))
    dir = s[-1]-s[-2]
    if dir > 0:
        print("up "+str(dir))
    elif dir == 0:
        print("stay")
    else:
        print("down "+str(abs(dir)))


