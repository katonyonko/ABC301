import io
import sys

_INPUT = """\
6
4
2 5 1 2
6
3 4 5 6 5 4
"""

def solve(test):
  N=int(input())
  A=list(map(int,input().split()))
  ans=[A[0]]
  for i in range(N-1):
    if A[i]<A[i+1]:
      for j in range(A[i]+1,A[i+1]): ans.append(j)
    else:
      for j in range(A[i]-1,A[i+1],-1): ans.append(j)
    ans.append(A[i+1])
  if test==0:
    print(*ans)
  else:
    return None

def random_input():
  from random import randint,shuffle
  N=randint(1,10)
  M=randint(1,N)
  A=list(range(1,M+1))+[randint(1,M) for _ in range(N-M)]
  shuffle(A)
  return (" ".join(map(str, [N,M]))+"\n"+" ".join(map(str, A))+"\n")*3

def simple_solve():
  return []

def main(test):
  if test==0:
    solve(0)
  elif test==1:
    sys.stdin = io.StringIO(_INPUT)
    case_no=int(input())
    for _ in range(case_no):
      solve(0)
  else:
    for i in range(1000):
      sys.stdin = io.StringIO(random_input())
      x=solve(1)
      y=simple_solve()
      if x!=y:
        print(i,x,y)
        print(*[line for line in sys.stdin],sep='')
        break

#0:提出用、1:与えられたテスト用、2:ストレステスト用
main(0)