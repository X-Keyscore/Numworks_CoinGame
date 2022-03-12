from math import*
I=print
a=True
S=False
f=str
T=len
E=None
from kandinsky import*
from ion import*
from l import*
I("By Lyncix | Release 2.0")
H="2.0"
w={"background":w(0,0,0),"title":w(255,191,0),"text":w(108,52,131),"text-active":w(64,224,208),"player":w(64,224,208),"enemy":w(255,87,34),"platform":w(108,52,131),"coin":w(255,255,0)}
y=[{"name":"Pyramid","platform":[{"x":1,"y":12,"width":4},{"x":6,"y":12,"width":4},{"x":11,"y":12,"width":4},{"x":16,"y":12,"width":4},{"x":4,"y":10,"width":3},{"x":9,"y":10,"width":3},{"x":14,"y":10,"width":3},{"x":6,"y":8,"width":4},{"x":11,"y":8,"width":4},{"x":9,"y":6,"width":3}],"enemy":[{"x":9,"y":11,"move":-3},{"x":14,"y":9,"move":2},{"x":9,"y":7,"move":-2}],"coin":[{"x":1,"y":11},{"x":6,"y":11},{"x":14,"y":11},{"x":19,"y":11},{"x":4,"y":9},{"x":10,"y":9},{"x":16,"y":9},{"x":6,"y":7},{"x":14,"y":7},{"x":10,"y":5}]},{"name":"Pyramid reverse","platform":[{"x":9,"y":12,"width":3},{"x":6,"y":10,"width":4},{"x":11,"y":10,"width":4},{"x":4,"y":8,"width":3},{"x":9,"y":8,"width":3},{"x":14,"y":8,"width":3},{"x":1,"y":6,"width":4},{"x":6,"y":6,"width":4},{"x":11,"y":6,"width":4},{"x":16,"y":6,"width":4}],"enemy":[{"x":9,"y":11,"move":-3},{"x":14,"y":9,"move":2},{"x":9,"y":7,"move":-2}],"coin":[{"x":10,"y":13},{"x":6,"y":11},{"x":14,"y":11},{"x":4,"y":9},{"x":10,"y":9},{"x":16,"y":9},{"x":1,"y":7},{"x":6,"y":7},{"x":14,"y":7},{"x":19,"y":7}]},{"name":"flower","platform":[{"x":8,"y":12,"width":2},{"x":11,"y":12,"width":2},{"x":5,"y":10,"width":1},{"x":7,"y":10,"width":7},{"x":15,"y":10,"width":1},{"x":6,"y":8,"width":2},{"x":9,"y":8,"width":3},{"x":13,"y":8,"width":2},{"x":8,"y":6,"width":1},{"x":10,"y":6,"width":1},{"x":12,"y":6,"width":1},{"x":10,"y":4,"width":1}],"enemy":[{"x":9,"y":11,"move":-1},{"x":11,"y":11,"move":1},{"x":8,"y":9,"move":4},{"x":11,"y":7,"move":-2}],"coin":[{"x":8,"y":11},{"x":12,"y":11},{"x":5,"y":9},{"x":15,"y":9},{"x":6,"y":7},{"x":14,"y":7},{"x":8,"y":5},{"x":12,"y":5},{"x":10,"y":3}]},{"name":"Space Invaders","platform":[{"x":7,"y":12,"width":1},{"x":13,"y":12,"width":1},{"x":7,"y":10,"width":7},{"x":5,"y":8,"width":4},{"x":12,"y":8,"width":4},{"x":5,"y":6,"width":1},{"x":8,"y":6,"width":5},{"x":15,"y":6,"width":1},{"x":8,"y":4,"width":1},{"x":12,"y":4,"width":1}],"enemy":[{"x":9,"y":9,"move":-2},{"x":11,"y":9,"move":2},{"x":5,"y":7,"move":3},{"x":15,"y":7,"move":-3},{"x":8,"y":5,"move":4}],"coin":[{"x":7,"y":11},{"x":13,"y":11},{"x":8,"y":9},{"x":12,"y":9},{"x":5,"y":5},{"x":10,"y":5},{"x":15,"y":5},{"x":8,"y":3},{"x":12,"y":3}]}]
def W():
 q(0.15)
def O(a):
 return a*15
def z(Q):
 B=y[Q]
 s={"player":{"x":0,"y":13},"enemyTime":monotonic(),"enemy":[],"coin":[]}
 for J in B['enemy']:
  s['enemy'].append({"x":J['x'],"y":J['y'],"action":"+"})
 for x in B['coin']:
  s['coin'].append({"x":x['x'],"y":x['y']})
 def r(w,x1,y1,x2,y2):
  b(x1*15,y1*15,15,15,w['background'])
  b(x2*15,y2*15,15,15,w['player'])
 def j(B,x,y):
  h=0
  for N in B['platform']:
   D=N['x']-1
   A=N['x']+(N['width'])
   v=N['y']-1
   if(D<x<A and v==y):
    h=h+1
  if(h>=1):
   return a
  else:
   return S
 def i(B,x,y):
  h=0
  if(-1<x<21 and y==13):
   h=1
  else:
   for N in B['platform']:
    D=N['x']-1
    A=N['x']+(N['width'])
    v=N['y']-1
    if(D<x<A and v==y):
     h=h+1
  if(h==1):
   return S
  else:
   return a
 def p(w,B,s):
  J=[]
  if((s['enemyTime']+1)<monotonic()):
   i=0
   l=monotonic()
   for M in s['enemy']:
    d=B['enemy'][i]
    Y=d['x']
    e=d['y']
    m=d['move']
    G=M['x']
    U=M['y']
    R=M['action']
    b(G*15,U*15,15,15,w['background'])
    t=[(+1),(-1)]
    if(m<0):
     t.reverse()
    if(m==0):
     rX=G
     rY=U
     R="+"
    elif(Y==G):
     rX=G+t[0]
     rY=U
     R="+"
    elif((Y+m)==G):
     rX=G+t[1]
     rY=U
     R="-"
    elif(R=="+"):
     rX=G+t[0]
     rY=U
     R="+"
    elif(R=="-"):
     rX=G+t[1]
     rY=U
     R="-"
    b(rX*15,rY*15,15,15,w['enemy'])
    J.append({"x":rX,"y":rY,"action":R})
    i=i+1
  else:
   l=s['enemyTime']
   J=s['enemy']
  return{"player":s['player'],"enemyTime":l,"enemy":J,"coin":s['coin']}
 def C(s):
  for M in s['enemy']:
   if(M['x']==s['player']['x']and M['y']==s['player']['y']):
    return a
 def P(s):
  i=0
  for k in s['coin']:
   if(k['x']==s['player']['x']and k['y']==s['player']['y']):
    return i
   i=i+1
 def n(Q):
  b(0,0,320,222,w['background'])
  c("Menu",0,0,w['title'],w['background'])
  c("x:"+f(s['player']['x'])+" y:"+f(s['player']['y']),225,0,w['title'],w['background'])
  c("Level:"+f(Q+1)+" ("+y[Q]['name']+")",0,30,w['text'],w['background'])
  c("Pièces restantes:"+f(T(s['coin'])),0,50,w['text'],w['background'])
  c("Pièces récupérées:"+f(X),0,70,w['text'],w['background'])
  c("OK:retour",1,201,w['text'],w['text-active'])
  c(H,280,201,w['title'],w['background'])
  g=a
  while(g==a):
   if(keydown(KEY_OK)):
    g=S
 def K():
  b(0,0,320,222,w['background'])
  b(O(0),O(14),O(22),O(1),w['platform'])
  for N in B['platform']:
   b(N['x']*15,N['y']*15,N['width']*15,15,w['platform'])
  b(O(s['player']['x']),O(s['player']['y']),O(1),O(1),w['player'])
  for x in s['coin']:
   b(x['x']*15,x['y']*15,15,15,w['coin'])
  for J in s['enemy']:
   b(J['x']*15,J['y']*15,15,15,w['enemy'])
 K()
 X=0
 u=a
 while(u==a):
  c("Level:"+f(Q+1),5,5,w['text'],w['background'])
  c("Pièces:"+f(X),5,20,w['text'],w['background'])
  if(keydown(KEY_LEFT)and s['player']['x']>0):
   r(w,s['player']['x'],s['player']['y'],s['player']['x']-1,s['player']['y'])
   s['player']['x']=s['player']['x']-1
   if(P(s)!=E):
    s['coin'].pop(P(s))
    X=X+1
   W()
  elif(keydown(KEY_RIGHT)and s['player']['x']<20):
   r(w,s['player']['x'],s['player']['y'],s['player']['x']+1,s['player']['y'])
   s['player']['x']=s['player']['x']+1
   if(P(s)!=E):
    s['coin'].pop(P(s))
    X=X+1
   W()
  elif(keydown(KEY_UP)and s['player']['y']>0):
   r(w,s['player']['x'],s['player']['y'],s['player']['x'],s['player']['y']-2)
   s['player']['y']=s['player']['y']-2
   if(P(s)!=E):
    s['coin'].pop(P(s))
    X=X+1
   W()
   if not(j(B,s['player']['x'],s['player']['y'])):
    q(0.4)
    r(w,s['player']['x'],s['player']['y'],s['player']['x'],s['player']['y']+2)
    s['player']['y']=s['player']['y']+2
  elif(keydown(KEY_HOME)):
   n(Q)
   K()
  if(i(B,s['player']['x'],s['player']['y'])==a):
   r(w,s['player']['x'],s['player']['y'],s['player']['x'],s['player']['y']+2)
   s['player']['y']=s['player']['y']+2
  for x in s['coin']:
   b(x['x']*15,x['y']*15,15,15,w['coin'])
  s=p(w,B,s)
  if(C(s)):
   b(O(0),O(13),O(1),O(1),w['player'])
   s['player']['x']=0;s['player']['y']=13
   z(0)
  if(P(s)!=E):
   s['coin'].pop(P(s))
   X=X+1
  if(T(s['coin'])==0):
   Q=Q+1
   z(Q)
z(0)
# Created by pyminifier (https://github.com/liftoff/pyminifier)

