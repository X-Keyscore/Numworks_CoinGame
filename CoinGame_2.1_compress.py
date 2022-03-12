from math import *
from kandinsky import *
from ion import *
from time import *
d = draw_string
f = fill_rect
c = color
k = keydown
print("By Lyncix | Release 2.1")
release = "2.1"
cs = {
  "bg": c(0,0,0),
  "t": c(255,191,0),
  "te": c(108,52,131),
  "tea": c(64,224,208),
  "p": c(64,224,208),
  "e": c(255,87,34),
  "pl": c(108,52,131),
  "c": c(255,255,0)
}
l = [
   {
    "name": "Pyramid",
    "platform": [
      [1,12,4],[6,12,4],
      [11,12,4],[16,12,4],
      [4,10,3],[9,10,3],
      [14,10,3],[6,8,4],
      [11,8,4],[9,6,3]
    ],
    "enemy": [
      [9,11,-3],[14,9,2],
      [9,7,-2]
    ],
    "coin": [
      [1,11],[6,11],[14,11],
      [19,11],[4,9],[10,9],
      [16,9],[6,7],[14,7],
      [10,5]
    ]
  },
  {
    "name": "Pyramid reverse",
    "platform": [
      [9,12,3],[6,10,4],
      [11,10,4],[4,8,3],
      [9,8,3],[14,8,3],
      [1,6,4],[6,6,4],
      [11,6,4],[16,6,4]
    ],
    "enemy": [
      [9,11,-3],[14,9,2],
      [9,7,-2]
    ],
    "coin": [
      [10,13],[6,11],[14,11],
      [4,9],[10,9],[16,9],
      [1,7],[6,7],[14,7],
      [19,7]
    ]
  },
  {
    "name": "flower",
    "platform": [
      [8,12,2],[11,12,2],
      [5,10,1],[7,10,7],
      [15,10,1],[6,8,2],
      [9,8,3],[13,8,2],
      [8,6,1],[10,6,1],
      [12,6,1],[10,4,1]
    ],
    "enemy": [
      [9,11,-1],[11,11,1],
      [8,9,4],[11,7,-2]
    ],
    "coin": [
      [8,11],[12,11],[5,9],
      [15,9],[6,7],[14,7],
      [8,5],[12,5],[10,3]
    ]
  },
  {
    "name": "Space Invaders",
    "platform": [
      [7,12,1],[13,12,1],[7,10,7],
      [5,8,4],[12,8,4],[5,6,1],
      [8,6,5],[15,6,1],[8,4,1],
      [12,4,1]
    ],
    "enemy": [
      [9,9,-2],[11,9,2],
      [5,7,3],[15,7,-3],
      [8,5,4]
    ],
    "coin": [
      [7,11],[13,11],[8,9],
      [12,9],[5,5],[10,5],
      [15,5],[8,3],[12,3]
    ]
  }
]
def w():
  sleep(0.15)
def conv(a):
  return a*15
def game(id):
  le = l[id]
  v = {
    "p": {"x":0,"y":13},
    "et": monotonic(),
    "e": [],
    "c": []
  }
  for en in le['enemy']:
    v['e'].append([en[0],en[1],"+"])
  for cn in le['coin']:
    v['c'].append([cn[0],cn[1]])
  def playerMove(color, x1, y1, x2, y2):
      f(x1*15, y1*15, 15, 15, cs['bg'])
      f(x2*15, y2*15, 15, 15, cs['p'])
  def platformHitbox(le, x, y):
    r = 0
    for p in le['platform']:
      pX = p[0] - 1
      pXm = p[0] + (p[2])
      pY = p[1] - 1
      if (pX < x < pXm and p == y):
        r = r + 1
    return r>=1
  def playerDrop(le, x, y):
    r = 0
    if (-1 < x < 21 and y == 13):
      r = 1
    else:
      for p in le['platform']:
        pX = p[0] - 1
        pXm = p[0] + (p[2])
        pY = p[1] - 1
        if (pX < x < pXm and pY == y):
          r = r + 1
    return not (r==1)
  def enemyMove(color, le, var):
    e = []
    if ((v['eTime'] + 1) < monotonic()):
      i = 0
      time = monotonic()
      for vE in v['e']:
        lE = le['enemy'][i]
        fX = lE[0]
        fY = lE[1]
        m = lE[2]
        mX = vE[0]
        mY = vE[1]
        action = vE[2]
        f(mX*15, mY*15, 15, 15, cs['bg'])
        operation = [(+1), (-1)]
        if (m < 0):
          operation.reverse()
        if (m == 0):
          rX = mX
          rY = mY
          action = "+"
        elif (fX == mX):
          rX = mX + operation[0]
          rY = mY
          action = "+"
        elif ((fX + m) == mX):
          rX = mX + operation[1]
          rY = mY
          action = "-"
        elif (action == "+"):
          rX = mX + operation[0]
          rY = mY
          action = "+"
        elif (action == "-"):
          rX = mX + operation[1]
          rY = mY
          action = "-"
        f(rX*15, rY*15, 15, 15, cs['enemy'])
        enemy.append([rX,rY,action])
        i = i + 1
    else:
      time = v['eTime']
      enemy = v['e']
    return {
      "p": v['p'],
      "et": time,
      "e": enemy,
      "c": v['c']
    }
  def touchEnemy(var):
    for vE in v['e']:
      if (vE[0] == v['p']['x'] and vE[1] == v['p']['y']):
        return True
  def touchCoin(var):
    i = 0
    for varCoin in v['c']:
      if (varCoin[0] == v['p']['x'] and varCoin[1] == v['p']['y']):
        return i
      i = i + 1
  def menu(id):
    f(0, 0, 320, 222, cs['bg'])
    d("Menu", 0, 0, cs['t'], cs['bg'])
    d("x:"+ str(v['p']['x']) + " y:" + str(v['p']['y']), 225, 0, cs['t'], cs['bg'])
    d("le:" + str(id + 1) + " (" + l[id]['name'] + ")", 0, 30, cs['te'], cs['bg'])
    d("Pièces restantes:" + str(len(v['c'])), 0, 50, cs['te'], cs['bg'])
    d("Pièces récupérées:" + str(wallet), 0, 70, cs['te'], cs['bg'])
    d("OK:retour", 1, 201, cs['te'], cs['tea'])
    d(release, 280, 201, cs['t'], cs['bg'])
    menuLoop = True
    while (menuLoop  == True):
      if (k(KEY_OK)):
        menuLoop = False
  def init():
    f(0, 0, 320, 222, cs['bg'])
    f(conv(0), conv(14), conv(22), conv(1), cs['pl'])
    for platform in le['platform']:
      f(platform[0]*15, platform[1]*15, platform[2]*15, 15, cs['pl'])
    f(conv(v['p']['x']), conv(v['p']['y']), conv(1), conv(1), cs['p'])
    for coin in v['c']:
      f(coin[0]*15, coin[1]*15, 15, 15, cs['c'])
    for enemy in v['e']:
      f(enemy[0]*15, enemy[1]*15, 15, 15, cs['e'])
  init()
  wallet = 0
  gameLoop = True
  while (gameLoop == True):
    d("le:" + str(id + 1),5,5, cs['te'], cs['bg'])
    d("Pièces:" + str(wallet),5,20, cs['te'], cs['bg'])
    if (k(KEY_LEFT) and v['p']['x'] > 0):
      playerMove(cs, v['p']['x'], v['p']['y'], v['p']['x']-1, v['p']['y'])
      v['p']['x'] = v['p']['x'] - 1
      if (touchCoin(var) != None):
        v['c'].pop(touchCoin(var))
        wallet = wallet + 1
      w()
    elif (k(KEY_RIGHT) and v['p']['x'] < 20):
      playerMove(cs, v['p']['x'], v['p']['y'], v['p']['x']+1, v['p']['y'])
      v['p']['x'] = v['p']['x'] + 1
      if (touchCoin(var) != None):
        v['c'].pop(touchCoin(var))
        wallet = wallet + 1
      w()
    elif (k(KEY_UP) and v['p']['y'] > 0):
      playerMove(cs, v['p']['x'], v['p']['y'], v['p']['x'], v['p']['y']-2)
      v['p']['y'] = v['p']['y'] - 2
      if (touchCoin(var) != None):
        v['c'].pop(touchCoin(var))
        wallet = wallet + 1
      w()
      if not (platformHitbox(le, v['p']['x'], v['p']['y'])):
        sleep(0.4)
        playerMove(cs, v['p']['x'], v['p']['y'], v['p']['x'], v['p']['y']+2)
        v['p']['y'] = v['p']['y'] + 2
    elif (k(KEY_HOME)):
      menu(id)
      init()
    if (playerDrop(le, v['p']['x'], v['p']['y']) == True):
      playerMove(cs, v['p']['x'], v['p']['y'], v['p']['x'], v['p']['y']+2)
      v['p']['y'] = v['p']['y'] + 2
    for coin in v['c']:
      f(coin[0]*15, coin[1]*15, 15, 15, cs['c'])
    var = enemyMove(cs, le, var)
    if (touchEnemy(var)):
      f(conv(0), conv(13), conv(1), conv(1), cs['p'])
      v['p']['x'] = 0; v['p']['y'] = 13
      game(0)
    if (touchCoin(var) != None):
      v['c'].pop(touchCoin(var))
      wallet = wallet + 1
    if (len(v['c']) == 0):
        id = id + 1
        game(id)
game(0)