import io
import sys

_INPUT = """\
6
3 3 5
S.G
o#o
.#.
3 3 1
S.G
.#o
o#.
5 10 2000000
S.o..ooo..
..o..o.o..
..o..ooo..
..o..o.o..
..o..ooo.G
3 3 2
S.G
o#o
.#.
"""

def solve(test):
  from collections import deque
  def bfs(G,s):
    inf=10**30
    D=[inf]*len(G)
    D[s]=0
    dq=deque()
    dq.append(s)
    while dq:
      x=dq.popleft()
      for y in G[x]:
        if D[y]>D[x]+1:
          D[y]=D[x]+1
          dq.append(y)
    return D

  H,W,T=map(int,input().split())
  A=[input() for _ in range(H)]
  kasi=[]
  for i in range(H):
    for j in range(W):
      if A[i][j]=='S': s=i*W+j
      elif A[i][j]=='G': g=i*W+j
      elif A[i][j]=='o': kasi.append(i*W+j)
  G=[[] for _ in range(H*W)]
  for i in range(H):
    for j in range(W):
      for k,l in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
        if 0<=k<H and 0<=l<W and A[k][l]!='#': G[i*W+j].append(k*W+l)
  l=[]
  tmp=[s,g]+kasi
  for i in range(len(tmp)):
    tmp2=bfs(G,tmp[i])
    l.append([tmp2[tmp[j]] for j in range(len(tmp))])
  ans=-1
  if l[0][1]<=T: ans=max(ans,0)
  dp=[1<<30]*((1<<len(kasi))*len(kasi))
  for i in range(len(kasi)):
    dp[(1<<i)*len(kasi)+i]=l[0][2+i]
  for i in range(1<<len(kasi)):
    for j in range(len(kasi)):
      if (i>>j)&1==0: continue
      if dp[i*len(kasi)+j]+l[2+j][1]<=T: ans=max(ans,sum([(i>>k)&1 for k in range(len(kasi))]))
      for k in range(len(kasi)):
        if (i>>k)&1==0: dp[(i+(1<<k))*len(kasi)+k]=min(dp[(i+(1<<k))*len(kasi)+k],dp[i*len(kasi)+j]+l[2+j][2+k])
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