from math import *
from kandinsky import *
from ion import *
from time import *
print("By Lyncix | Release 2.0")
release = "2.0"
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
      { "x": 1, "y": 12, "width": 4 },
      { "x": 6, "y": 12, "width": 4 },
      { "x": 11, "y": 12, "width": 4 },
      { "x": 16, "y": 12, "width": 4 },
      { "x": 4, "y": 10, "width": 3 },
      { "x": 9, "y": 10, "width": 3 },
      { "x": 14, "y": 10, "width": 3 },
      { "x": 6, "y": 8, "width": 4},
      { "x": 11, "y": 8, "width": 4},
      { "x": 9, "y": 6, "width": 3}
    ],
    "enemy": [
      { "x": 9, "y": 11, "move": -3 },
      { "x": 14, "y": 9, "move": 2 },
      { "x": 9, "y": 7, "move": -2 }
    ],
    "coin": [
      { "x": 1, "y": 11 },
      { "x": 6, "y": 11 },
      { "x": 14, "y": 11 },
      { "x": 19, "y": 11 },
      { "x": 4, "y": 9 },
      { "x": 10, "y": 9 },
      { "x": 16, "y": 9 },
      { "x": 6, "y": 7 },
      { "x": 14, "y": 7 },
      { "x": 10, "y": 5 }
    ]
  },
  {
    "name": "Pyramid reverse",
    "platform": [
      { "x": 9, "y": 12, "width": 3 },
      { "x": 6, "y": 10, "width": 4 },
      { "x": 11, "y": 10, "width": 4 },
      { "x": 4, "y": 8, "width": 3 },
      { "x": 9, "y": 8, "width": 3 },
      { "x": 14, "y": 8, "width": 3 },
      { "x": 1, "y": 6, "width": 4 },
      { "x": 6, "y": 6, "width": 4 },
      { "x": 11, "y": 6, "width": 4 },
      { "x": 16, "y": 6, "width": 4 }
    ],
    "enemy": [
      { "x": 9, "y": 11, "move": -3 },
      { "x": 14, "y": 9, "move": 2 },
      { "x": 9, "y": 7, "move": -2 }
    ],
    "coin": [
      { "x": 10, "y": 13 },
      { "x": 6, "y": 11 },
      { "x": 14, "y": 11 },
      { "x": 4, "y": 9 },
      { "x": 10, "y": 9 },
      { "x": 16, "y": 9 },
      { "x": 1, "y": 7 },
      { "x": 6, "y": 7 },
      { "x": 14, "y": 7 },
      { "x": 19, "y": 7 }
    ]
  },
  {
    "name": "flower",
    "platform": [
      { "x": 8, "y": 12, "width": 2 },
      { "x": 11, "y": 12, "width": 2 },
      { "x": 5, "y": 10, "width": 1 },
      { "x": 7, "y": 10, "width": 7 },
      { "x": 15, "y": 10, "width": 1 },
      { "x": 6, "y": 8, "width": 2 },
      { "x": 9, "y": 8, "width": 3 },
      { "x": 13, "y": 8, "width": 2 },
      { "x": 8, "y": 6, "width": 1 },
      { "x": 10, "y": 6, "width": 1 },
      { "x": 12, "y": 6, "width": 1 },
      { "x": 10, "y": 4, "width": 1 }
    ],
    "enemy": [
      { "x": 9, "y": 11, "move": -1 },
      { "x": 11, "y": 11, "move": 1 },
      { "x": 8, "y": 9, "move": 4 },
      { "x": 11, "y": 7, "move": -2 }
    ],
    "coin": [
      { "x": 8, "y": 11 },
      { "x": 12, "y": 11 },
      { "x": 5, "y": 9 },
      { "x": 15, "y": 9 },
      { "x": 6, "y": 7 },
      { "x": 14, "y": 7 },
      { "x": 8, "y": 5 },
      { "x": 12, "y": 5 },
      { "x": 10, "y": 3 }
    ]
  },
  {
    "name": "Space Invaders",
    "platform": [
      { "x": 7, "y": 12, "width": 1 },
      { "x": 13, "y": 12, "width": 1 },
      { "x": 7, "y": 10, "width": 7 },
      { "x": 5, "y": 8, "width": 4 },
      { "x": 12, "y": 8, "width": 4 },
      { "x": 5, "y": 6, "width": 1 },
      { "x": 8, "y": 6, "width": 5 },
      { "x": 15, "y": 6, "width": 1 },
      { "x": 8, "y": 4, "width": 1 },
      { "x": 12, "y": 4, "width": 1 }
    ],
    "enemy": [
      { "x": 9, "y": 9, "move": -2 },
      { "x": 11, "y": 9, "move": 2 },
      { "x": 5, "y": 7, "move": 3 },
      { "x": 15, "y": 7, "move": -3 },
      { "x": 8, "y": 5, "move": 4 }
    ],
    "coin": [
      { "x": 7, "y": 11 },
      { "x": 13, "y": 11 },
      { "x": 8, "y": 9 },
      { "x": 12, "y": 9 },
      { "x": 5, "y": 5 },
      { "x": 10, "y": 5 },
      { "x": 15, "y": 5 },
      { "x": 8, "y": 3 },
      { "x": 12, "y": 3 }
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
    "player": { "x": 0, "y": 13 },
    "enemyTime": monotonic(),
    "enemy": [],
    "coin": []
  }
  for enemy in level['enemy']:
    var['enemy'].append({"x": enemy['x'], "y": enemy['y'], "action": "+"})
  for coin in level['coin']:
    var['coin'].append({"x": coin['x'], "y": coin['y']})
  def playerMove(color, x1, y1, x2, y2):
      fill_rect(x1*15, y1*15, 15, 15, color['background'])
      fill_rect(x2*15, y2*15, 15, 15, color['player'])
  def platformHitbox(level, x, y):
    result = 0
    for platform in level['platform']:
      platformXmin = platform['x'] - 1
      platformXmax = platform['x'] + (platform['width'])
      platformY = platform['y'] - 1
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
        platformXmin = platform['x'] - 1
        platformXmax = platform['x'] + (platform['width'])
        platformY = platform['y'] - 1
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
        fixeX = levelEnemy['x']
        fixeY = levelEnemy['y']
        move = levelEnemy['move']
        modularX = varEnemy['x']
        modularY = varEnemy['y']
        action = varEnemy['action']
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
        enemy.append({"x": rX, "y": rY, "action": action})
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
      if (varEnemy['x'] == var['player']['x'] and varEnemy['y'] == var['player']['y']):
        return True
  def touchCoin(var):
    i = 0
    for varCoin in var['coin']:
      if (varCoin['x'] == var['player']['x'] and varCoin['y'] == var['player']['y']):
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
      fill_rect(platform['x']*15, platform['y']*15, platform['width']*15, 15, color['platform'])
    fill_rect(conv(var['player']['x']), conv(var['player']['y']), conv(1), conv(1), color['player'])
    for coin in var['coin']:
      fill_rect(coin['x']*15, coin['y']*15, 15, 15, color['coin'])
    for enemy in var['enemy']:
      fill_rect(enemy['x']*15, enemy['y']*15, 15, 15, color['enemy'])
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
      fill_rect(coin['x']*15, coin['y']*15, 15, 15, color['coin'])
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
