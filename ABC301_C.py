import io
import sys

_INPUT = """\
6
ch@ku@ai
choku@@i
ch@kud@i
akidu@ho
aoki
@ok@
aa
bb
"""

def solve(test):
  S=input()
  T=input()
  s,t=[0]*26+[S.count('@')],[0]*26+[T.count('@')]
  for i in range(len(S)):
    if S[i]!='@': s[ord(S[i])-ord('a')]+=1
  for i in range(len(T)):
    if T[i]!='@': t[ord(T[i])-ord('a')]+=1
  for i in range(26):
    tmp=min(s[i],t[i])
    s[i]-=tmp; t[i]-=tmp
  ans='Yes'
  l=set(list('atcoder'))
  for i in range(26):
    if chr(i+ord('a')) not in l and (s[i]>0 or t[i]>0): ans='No'
  if s[-1]<sum(t[:-1]) or t[-1]<sum(s[:-1]): ans='No'
  if test==0:
    print(ans)
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