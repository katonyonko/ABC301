import io
import sys

_INPUT = """\
6
DD??S
????????????????????????????????????????
?D??S
"""

def solve(test):
  mod=998244353
  S=input()
  dp=[0]*((len(S)+1)*29)
  def idx(i,j): return i*29+j
  dp[0]=1
  s=set()
  for i in range(len(S)):
    if S[i]=='?':
      for j in range(27):
        dp[idx(i+1,j+1)]=(dp[idx(i+1,j+1)]+(26-j)*dp[idx(i,j)])%mod
        dp[idx(i+1,j)]=(dp[idx(i+1,j)]+(26+j)*dp[idx(i,j)])%mod
    elif ord('a')<=ord(S[i])<=ord('z'): dp[idx(i+1,j)]=(dp[idx(i+1,j)]+dp[idx(i,j)])%mod
    else:
      pass
    if S[i]=='?':
      dp[idx(i+1,28)]=(dp[idx(i+1,28)]+26*dp[idx(i,27)])%mod
      dp[idx(i+1,27)]=(dp[idx(i+1,27)]+26*dp[idx(i,27)])%mod
    elif ord('a')<=ord(S[i])<=ord('z'): dp[idx(i+1,28)]=(dp[idx(i+1,28)]+dp[idx(i,27)])%mod
    else: dp[idx(i+1,27)]=(dp[idx(i+1,27)]+dp[idx(i,27)])%mod
    if S[i]=='?':
      dp[idx(i+1,28)]=(dp[idx(i+1,28)]+26*dp[idx(i,28)])%mod
    elif ord('a')<=ord(S[i])<=ord('z'): dp[idx(i+1,28)]=(dp[idx(i+1,28)]+dp[idx(i,28)])%mod
    if ord('A')<=ord(S[i])<=ord('Z'): s.add(S[i])
  ans=sum([dp[len(S)*29+j] for j in range(29)]%mod)
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
main(1)