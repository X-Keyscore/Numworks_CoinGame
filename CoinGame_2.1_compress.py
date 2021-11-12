from math import *
from kandinsky import *
from ion import *
from time import *
print("By Lyncix | Release 2.1")
release = "2.1"
color = {
  "background": color(0,0,0),
  "title": color(255,191,0),
  "text": color(108,52,131),
  "text-active": color(64,224,208),
  "player": color(64,224,208),
  "enemy": color(255,87,34),
  "platform": color(108,52,131),
  "coin": color(255,255,0)
}
levels = [
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
def waiting():
  sleep(0.15)
def conv(a):
  return a*15
def game(levelId):
  level = levels[levelId]
  var = {
    "player": {"x":0,"y":13},
    "enemyTime": monotonic(),
    "enemy": [],
    "coin": []
  }
  for enemy in level['enemy']:
    var['enemy'].append([enemy[0],enemy[1],"+"])
  for coin in level['coin']:
    var['coin'].append([coin[0],coin[1]])
  def playerMove(color, x1, y1, x2, y2):
      fill_rect(x1*15, y1*15, 15, 15, color['background'])
      fill_rect(x2*15, y2*15, 15, 15, color['player'])
  def platformHitbox(level, x, y):
    result = 0
    for platform in level['platform']:
      platformXmin = platform[0] - 1
      platformXmax = platform[0] + (platform[2])
      platformY = platform[1] - 1
      if (platformXmin < x < platformXmax and platformY == y):
        result = result + 1
    if (result >= 1):
      return True
    else:
      return False
  def playerDrop(level, x, y):
    result = 0
    if (-1 < x < 21 and y == 13):
      result = 1
    else:
      for platform in level['platform']:
        platformXmin = platform[0] - 1
        platformXmax = platform[0] + (platform[2])
        platformY = platform[1] - 1
        if (platformXmin < x < platformXmax and platformY == y):
          result = result + 1
    if (result == 1):
      return False
    else:
      return True
  def enemyMove(color, level, var):
    enemy = []
    if ((var['enemyTime'] + 1) < monotonic()):
      i = 0
      time = monotonic()
      for varEnemy in var['enemy']:
        levelEnemy = level['enemy'][i]
        fixeX = levelEnemy[0]
        fixeY = levelEnemy[1]
        move = levelEnemy[2]
        modularX = varEnemy[0]
        modularY = varEnemy[1]
        action = varEnemy[2]
        fill_rect(modularX*15, modularY*15, 15, 15, color['background'])
        operation = [(+1), (-1)]
        if (move < 0):
          operation.reverse()
        if (move == 0):
          rX = modularX
          rY = modularY
          action = "+"
        elif (fixeX == modularX):
          rX = modularX + operation[0]
          rY = modularY
          action = "+"
        elif ((fixeX + move) == modularX):
          rX = modularX + operation[1]
          rY = modularY
          action = "-"
        elif (action == "+"):
          rX = modularX + operation[0]
          rY = modularY
          action = "+"
        elif (action == "-"):
          rX = modularX + operation[1]
          rY = modularY
          action = "-"
        fill_rect(rX*15, rY*15, 15, 15, color['enemy'])
        enemy.append([rX,rY,action])
        i = i + 1
    else:
      time = var['enemyTime']
      enemy = var['enemy']
    return {
      "player": var['player'],
      "enemyTime": time,
      "enemy": enemy,
      "coin": var['coin']
    }
  def touchEnemy(var):
    for varEnemy in var['enemy']:
      if (varEnemy[0] == var['player']['x'] and varEnemy[1] == var['player']['y']):
        return True
  def touchCoin(var):
    i = 0
    for varCoin in var['coin']:
      if (varCoin[0] == var['player']['x'] and varCoin[1] == var['player']['y']):
        return i
      i = i + 1
  def menu(levelId):
    fill_rect(0, 0, 320, 222, color['background'])
    draw_string("Menu", 0, 0, color['title'], color['background'])
    draw_string("x:"+ str(var['player']['x']) + " y:" + str(var['player']['y']), 225, 0, color['title'], color['background'])
    draw_string("Level:" + str(levelId + 1) + " (" + levels[levelId]['name'] + ")", 0, 30, color['text'], color['background'])
    draw_string("Pièces restantes:" + str(len(var['coin'])), 0, 50, color['text'], color['background'])
    draw_string("Pièces récupérées:" + str(wallet), 0, 70, color['text'], color['background'])
    draw_string("OK:retour", 1, 201, color['text'], color['text-active'])
    draw_string(release, 280, 201, color['title'], color['background'])
    menuLoop = True
    while (menuLoop  == True):
      if (keydown(KEY_OK)):
        menuLoop = False
  def init():
    fill_rect(0, 0, 320, 222, color['background'])
    fill_rect(conv(0), conv(14), conv(22), conv(1), color['platform'])
    for platform in level['platform']:
      fill_rect(platform[0]*15, platform[1]*15, platform[2]*15, 15, color['platform'])
    fill_rect(conv(var['player']['x']), conv(var['player']['y']), conv(1), conv(1), color['player'])
    for coin in var['coin']:
      fill_rect(coin[0]*15, coin[1]*15, 15, 15, color['coin'])
    for enemy in var['enemy']:
      fill_rect(enemy[0]*15, enemy[1]*15, 15, 15, color['enemy'])
  init()
  wallet = 0
  gameLoop = True
  while (gameLoop == True):
    draw_string("Level:" + str(levelId + 1),5,5, color['text'], color['background'])
    draw_string("Pièces:" + str(wallet),5,20, color['text'], color['background'])
    if (keydown(KEY_LEFT) and var['player']['x'] > 0):
      playerMove(color, var['player']['x'], var['player']['y'], var['player']['x']-1, var['player']['y'])
      var['player']['x'] = var['player']['x'] - 1
      if (touchCoin(var) != None):
        var['coin'].pop(touchCoin(var))
        wallet = wallet + 1
      waiting()
    elif (keydown(KEY_RIGHT) and var['player']['x'] < 20):
      playerMove(color, var['player']['x'], var['player']['y'], var['player']['x']+1, var['player']['y'])
      var['player']['x'] = var['player']['x'] + 1
      if (touchCoin(var) != None):
        var['coin'].pop(touchCoin(var))
        wallet = wallet + 1
      waiting()
    elif (keydown(KEY_UP) and var['player']['y'] > 0):
      playerMove(color, var['player']['x'], var['player']['y'], var['player']['x'], var['player']['y']-2)
      var['player']['y'] = var['player']['y'] - 2
      if (touchCoin(var) != None):
        var['coin'].pop(touchCoin(var))
        wallet = wallet + 1
      waiting()
      if not (platformHitbox(level, var['player']['x'], var['player']['y'])):
        sleep(0.4)
        playerMove(color, var['player']['x'], var['player']['y'], var['player']['x'], var['player']['y']+2)
        var['player']['y'] = var['player']['y'] + 2
    elif (keydown(KEY_HOME)):
      menu(levelId)
      init()
    if (playerDrop(level, var['player']['x'], var['player']['y']) == True):
      playerMove(color, var['player']['x'], var['player']['y'], var['player']['x'], var['player']['y']+2)
      var['player']['y'] = var['player']['y'] + 2
    for coin in var['coin']:
      fill_rect(coin[0]*15, coin[1]*15, 15, 15, color['coin'])
    var = enemyMove(color, level, var)
    if (touchEnemy(var)):
      fill_rect(conv(0), conv(13), conv(1), conv(1), color['player'])
      var['player']['x'] = 0; var['player']['y'] = 13
      game(0)
    if (touchCoin(var) != None):
      var['coin'].pop(touchCoin(var))
      wallet = wallet + 1
    if (len(var['coin']) == 0):
        levelId = levelId + 1
        game(levelId)
game(0)