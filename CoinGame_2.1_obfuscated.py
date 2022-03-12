from math import*
p=print
b=True
r=False
H=str
k=len
O=None
from kandinsky import*
from ion import*
from time import*
p("By Lyncix | Release 2.1")
N="2.1"
L={"background":L(0,0,0),"title":L(255,191,0),"text":L(108,52,131),"text-active":L(64,224,208),"player":L(64,224,208),"enemy":L(255,87,34),"platform":L(108,52,131),"coin":L(255,255,0)}
C=[{"name":"Pyramid","platform":[[1,12,4],[6,12,4],[11,12,4],[16,12,4],[4,10,3],[9,10,3],[14,10,3],[6,8,4],[11,8,4],[9,6,3]],"enemy":[[9,11,-3],[14,9,2],[9,7,-2]],"coin":[[1,11],[6,11],[14,11],[19,11],[4,9],[10,9],[16,9],[6,7],[14,7],[10,5]]},{"name":"Pyramid reverse","platform":[[9,12,3],[6,10,4],[11,10,4],[4,8,3],[9,8,3],[14,8,3],[1,6,4],[6,6,4],[11,6,4],[16,6,4]],"enemy":[[9,11,-3],[14,9,2],[9,7,-2]],"coin":[[10,13],[6,11],[14,11],[4,9],[10,9],[16,9],[1,7],[6,7],[14,7],[19,7]]},{"name":"flower","platform":[[8,12,2],[11,12,2],[5,10,1],[7,10,7],[15,10,1],[6,8,2],[9,8,3],[13,8,2],[8,6,1],[10,6,1],[12,6,1],[10,4,1]],"enemy":[[9,11,-1],[11,11,1],[8,9,4],[11,7,-2]],"coin":[[8,11],[12,11],[5,9],[15,9],[6,7],[14,7],[8,5],[12,5],[10,3]]},{"name":"Space Invaders","platform":[[7,12,1],[13,12,1],[7,10,7],[5,8,4],[12,8,4],[5,6,1],[8,6,5],[15,6,1],[8,4,1],[12,4,1]],"enemy":[[9,9,-2],[11,9,2],[5,7,3],[15,7,-3],[8,5,4]],"coin":[[7,11],[13,11],[8,9],[12,9],[5,5],[10,5],[15,5],[8,3],[12,3]]}]
def T():
 U(0.15)
def h(a):
 return a*15
def e(i):
 l=C[i]
 B={"player":{"x":0,"y":13},"enemyTime":monotonic(),"enemy":[],"coin":[]}
 for n in l['enemy']:
  B['enemy'].append([n[0],n[1],"+"])
 for F in l['coin']:
  B['coin'].append([F[0],F[1]])
 def X(L,x1,y1,x2,y2):
  V(x1*15,y1*15,15,15,L['background'])
  V(x2*15,y2*15,15,15,L['player'])
 def M(l,x,y):
  A=0
  for f in l['platform']:
   G=f[0]-1
   q=f[0]+(f[2])
   g=f[1]-1
   if(G<x<q and g==y):
    A=A+1
  if(A>=1):
   return b
  else:
   return r
 def S(l,x,y):
  A=0
  if(-1<x<21 and y==13):
   A=1
  else:
   for f in l['platform']:
    G=f[0]-1
    q=f[0]+(f[2])
    g=f[1]-1
    if(G<x<q and g==y):
     A=A+1
  if(A==1):
   return r
  else:
   return b
 def d(L,l,B):
  n=[]
  if((B['enemyTime']+1)<monotonic()):
   i=0
   P=monotonic()
   for J in B['enemy']:
    I=l['enemy'][i]
    o=I[0]
    w=I[1]
    u=I[2]
    x=J[0]
    a=J[1]
    s=J[2]
    V(x*15,a*15,15,15,L['background'])
    W=[(+1),(-1)]
    if(u<0):
     W.reverse()
    if(u==0):
     rX=x
     rY=a
     s="+"
    elif(o==x):
     rX=x+W[0]
     rY=a
     s="+"
    elif((o+u)==x):
     rX=x+W[1]
     rY=a
     s="-"
    elif(s=="+"):
     rX=x+W[0]
     rY=a
     s="+"
    elif(s=="-"):
     rX=x+W[1]
     rY=a
     s="-"
    V(rX*15,rY*15,15,15,L['enemy'])
    n.append([rX,rY,s])
    i=i+1
  else:
   P=B['enemyTime']
   n=B['enemy']
  return{"player":B['player'],"enemyTime":P,"enemy":n,"coin":B['coin']}
 def E(B):
  for J in B['enemy']:
   if(J[0]==B['player']['x']and J[1]==B['player']['y']):
    return b
 def y(B):
  i=0
  for z in B['coin']:
   if(z[0]==B['player']['x']and z[1]==B['player']['y']):
    return i
   i=i+1
 def K(i):
  V(0,0,320,222,L['background'])
  c("Menu",0,0,L['title'],L['background'])
  c("x:"+H(B['player']['x'])+" y:"+H(B['player']['y']),225,0,L['title'],L['background'])
  c("Level:"+H(i+1)+" ("+C[i]['name']+")",0,30,L['text'],L['background'])
  c("Pièces restantes:"+H(k(B['coin'])),0,50,L['text'],L['background'])
  c("Pièces récupérées:"+H(m),0,70,L['text'],L['background'])
  c("OK:retour",1,201,L['text'],L['text-active'])
  c(N,280,201,L['title'],L['background'])
  D=b
  while(D==b):
   if(keydown(KEY_OK)):
    D=r
 def j():
  V(0,0,320,222,L['background'])
  V(h(0),h(14),h(22),h(1),L['platform'])
  for f in l['platform']:
   V(f[0]*15,f[1]*15,f[2]*15,15,L['platform'])
  V(h(B['player']['x']),h(B['player']['y']),h(1),h(1),L['player'])
  for F in B['coin']:
   V(F[0]*15,F[1]*15,15,15,L['coin'])
  for n in B['enemy']:
   V(n[0]*15,n[1]*15,15,15,L['enemy'])
 j()
 m=0
 R=b
 while(R==b):
  c("Level:"+H(i+1),5,5,L['text'],L['background'])
  c("Pièces:"+H(m),5,20,L['text'],L['background'])
  if(keydown(KEY_LEFT)and B['player']['x']>0):
   X(L,B['player']['x'],B['player']['y'],B['player']['x']-1,B['player']['y'])
   B['player']['x']=B['player']['x']-1
   if(y(B)!=O):
    B['coin'].pop(y(B))
    m=m+1
   T()
  elif(keydown(KEY_RIGHT)and B['player']['x']<20):
   X(L,B['player']['x'],B['player']['y'],B['player']['x']+1,B['player']['y'])
   B['player']['x']=B['player']['x']+1
   if(y(B)!=O):
    B['coin'].pop(y(B))
    m=m+1
   T()
  elif(keydown(KEY_UP)and B['player']['y']>0):
   X(L,B['player']['x'],B['player']['y'],B['player']['x'],B['player']['y']-2)
   B['player']['y']=B['player']['y']-2
   if(y(B)!=O):
    B['coin'].pop(y(B))
    m=m+1
   T()
   if not(M(l,B['player']['x'],B['player']['y'])):
    U(0.4)
    X(L,B['player']['x'],B['player']['y'],B['player']['x'],B['player']['y']+2)
    B['player']['y']=B['player']['y']+2
  elif(keydown(KEY_HOME)):
   K(i)
   j()
  if(S(l,B['player']['x'],B['player']['y'])==b):
   X(L,B['player']['x'],B['player']['y'],B['player']['x'],B['player']['y']+2)
   B['player']['y']=B['player']['y']+2
  for F in B['coin']:
   V(F[0]*15,F[1]*15,15,15,L['coin'])
  B=d(L,l,B)
  if(E(B)):
   V(h(0),h(13),h(1),h(1),L['player'])
   B['player']['x']=0;B['player']['y']=13
   e(0)
  if(y(B)!=O):
   B['coin'].pop(y(B))
   m=m+1
  if(k(B['coin'])==0):
   i=i+1
   e(i)
e(0)
# Created by pyminifier (https://github.com/liftoff/pyminifier)

