from math import *
from kandinsky import *
from ion import *
from time import *
'''
Game type = Platformer
Editeur = Lyncix
Game version = 1.0.0
Version dev = V12
'''
# =====[ Constantes ]=====
# [ color ]
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
# [ levels ]
levels = [
  {
    "name": "Default",
    "platform": [
      { "x": 1, "y": 12, "width": 4, "height": 1 },
      { "x": 6, "y": 12, "width": 4, "height": 1 },
      { "x": 11, "y": 12, "width": 4, "height": 1 },
      { "x": 16, "y": 12, "width": 4, "height": 1 },
      { "x": 4, "y": 10, "width": 3, "height": 1 },
      { "x": 9, "y": 10, "width": 3, "height": 1 },
      { "x": 14, "y": 10, "width": 3, "height": 1 },
      { "x": 6, "y": 8, "width": 4, "height": 1},
      { "x": 11, "y": 8, "width": 4, "height": 1},
      { "x": 9, "y": 6, "width": 3, "height": 1}
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
    "name": "Default reverse",
    "platform": [
      { "x": 9, "y": 12, "width": 3, "height": 1 },
      { "x": 6, "y": 10, "width": 4, "height": 1 },
      { "x": 11, "y": 10, "width": 4, "height": 1 },
      { "x": 4, "y": 8, "width": 3, "height": 1 },
      { "x": 9, "y": 8, "width": 3, "height": 1 },
      { "x": 14, "y": 8, "width": 3, "height": 1 },
      { "x": 1, "y": 6, "width": 4, "height": 1 },
      { "x": 6, "y": 6, "width": 4, "height": 1 },
      { "x": 11, "y": 6, "width": 4, "height": 1 },
      { "x": 16, "y": 6, "width": 4, "height": 1 }
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
  }
]

# =====[ Functions globales ]=====
# Fonction pour l'attente qui réduit les FPS
def timeTouch():
  sleep(0.15)

# Fonction qui convertit en position système
def conv(a):
  return a*15

# Boîte de dialogue
def alert(color, text):
  fill_rect(0, 0, 320, 222, color['background'])
  draw_string(text, 0, 0, color['text'], color['background'])
  draw_string("OK", 1, 201, color['text'], color['text-active'])
  loop = True
  while (loop  == True):
    if (keydown(KEY_OK)):
      loop = False
  return True

# =====[ HOME ]=====
def home():
  # Affichage de la couleur de fond
  fill_rect(0, 0, 320, 222, color['background'])
  # Affichage du texte
  draw_string("Bienvenue", 0, 0, color['title'], color['background'])
  draw_string("Start", 0, 30, color['text-active'], color['background'])
  draw_string("EXE:validé", 1, 201, color['text'], color['text-active'])
  draw_string("By: Lyncix", 215, 200, color['text'], color['background'])

  # Sélection de démarrage
  homeLoop = True
  select = 1
  while (homeLoop  == True):
    if (keydown(KEY_EXE)):
      homeLoop = False
      return 0

# =====[ GAME ]=====
def game(levelId):

  # Récupération des infos sur le level dans une variable
  level = levels[levelId]

  # Variable de position
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

  # [ Functions ]

  # ==========[ ENGINE ]==========

  # Move player
  def playerMove(color, x1, y1, x2, y2):
      fill_rect(x1*15, y1*15, 15, 15, color['background'])
      fill_rect(x2*15, y2*15, 15, 15, color['player'])

  # Fonctions qui permet de dire si le joueur atterrit sur une plat-formes ou pas
  def platformHitbox(level, x, y):
    result = 0
    # Je boucle les données des plat-formes
    for platform in level['platform']:
      # Récupération les positions
      platformXmin = platform['x'] - 1
      platformXmax = platform['x'] + (platform['width'])
      platformY = platform['y'] - 1
      # Conditions pour vérification
      if (platformXmin < x < platformXmax and platformY == y):
        result = result + 1
    # Conditions pour vérification finale
    if (result >= 1):
      return True
    else:
      return False
    
  # Cette fonction a pour but de dire si le joueur tombe
  def playerDrop(level, x, y):
    result = 0
    if (-1 < x < 21 and y == 13):
      result = result + 1
    else:
      # Je boucle les données des plat-formes
      for platform in level['platform']:

        # Récupération des positions
        platformXmin = platform['x'] - 1
        platformXmax = platform['x'] + (platform['width'])
        platformY = platform['y'] - 1

        # Conditions pour vérification
        if (platformXmin < x < platformXmax and platformY == y):
          result = result + 1

    # Conditions pour vérification finale
    if (result == 1):
      return False
    else:
      return True

  # Move enemys
  def enemyMove(color, level, var):

    # Définition de la variable enemy qui va stocker les données finales
    enemy = []

    # Condition pour réguler la vitesse de déplacement des ennemis
    if ((var['enemyTime'] + 1) < monotonic()):
      i = 0
      time = monotonic()

      # Je boucle chaque enemy
      for varEnemy in var['enemy']:

        # Je récupère les données de base
        levelEnemy = level['enemy'][i]

        # Assignation des valeurs
        fixeX = levelEnemy['x']
        fixeY = levelEnemy['y']
        move = levelEnemy['move']
        modularX = varEnemy['x']
        modularY = varEnemy['y']
        action = varEnemy['action']

        # Effacement de l'ennemi de la position actuel
        fill_rect(modularX*15, modularY*15, 15, 15, color['background'])

        # Condition pour savoir le mode opératoire à utiliser
        operation = [(+1), (-1)]
        if (move < 0):
          operation.reverse()

        # Condition pour changer la position de l'ennemi
        if (fixeX == modularX):
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

        # Affichage de l'ennemi à sa nouvelle position
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
    # Je boucle chaque enemy
    for varEnemy in var['enemy']:
      if (varEnemy['x'] == var['player']['x'] and varEnemy['y'] == var['player']['y']):
        return True

  def touchCoin(var):
    # Je boucle chaque pièce
    i = 0
    for varCoin in var['coin']:
      if (varCoin['x'] == var['player']['x'] and varCoin['y'] == var['player']['y']):
        return i
      i = i + 1

  # =====[ END ENGINE ]=====

  # [ Menu ]
  def menu(levelId):

    # Affichage de la couleur de fond
    fill_rect(0, 0, 320, 222, color['background'])
    # Affichage du texte
    draw_string("Menu", 0, 0, color['title'], color['background'])
    draw_string("x:"+ str(var['player']['x']) + " y:" + str(var['player']['y']), 225, 0, color['title'], color['background'])
    draw_string("Level:" + str(levelId + 1), 0, 30, color['text'], color['background'])
    draw_string("Pièces:" + str(len(var['coin'])), 0, 50, color['text'], color['background'])
    draw_string("Ennemis:" + str(len(var['enemy'])), 0, 70, color['text'], color['background'])
    draw_string("OK:retour", 1, 201, color['text'], color['text-active'])
    # Action
    menuLoop = True
    while (menuLoop  == True):
      if (keydown(KEY_OK)):
        menuLoop = False

  # [ Initialisation ]
  def init():
    # Background color
    fill_rect(0, 0, 320, 222, color['background'])
    # Positionnement du sol
    fill_rect(conv(0), conv(14), conv(22), conv(1), color['platform'])
    # Positionnement des plate-formes
    for platform in level['platform']:
      fill_rect(platform['x']*15, platform['y']*15, platform['width']*15, platform['height']*15, color['platform'])
    # Spawn player
    fill_rect(conv(var['player']['x']), conv(var['player']['y']), conv(1), conv(1), color['player'])
    # Spawn enemy
    for enemy in var['enemy']:
      fill_rect(enemy['x']*15, enemy['y']*15, 15, 15, color['enemy'])
    # Spawn coin
    for coin in var['coin']:
      fill_rect(coin['x']*15, coin['y']*15, 15, 15, color['coin'])

  # ==========[ GAME ]==========
  init()

  # [ Event ]
  wallet = 0
  gameLoop = True
  while (gameLoop == True):
    #draw_string(str(var['player']['x']),5,5, color['text'], color['background'])
    #draw_string(str(var['player']['y']),5,20, color['text'], color['background'])
    draw_string("Level:" + str(levelId + 1),5,5, color['text'], color['background'])
    draw_string("Coins:" + str(wallet),5,20, color['text'], color['background'])

    if (keydown(KEY_LEFT) and var['player']['x'] > 0):
      playerMove(color, var['player']['x'], var['player']['y'], var['player']['x']-1, var['player']['y'])
      var['player']['x'] = var['player']['x'] - 1
      # Teste si touche une piece
      if (touchCoin(var) != None):
        var['coin'].pop(touchCoin(var))
        wallet = wallet + 1

      # Attente pour réduction FPS
      timeTouch()
    elif (keydown(KEY_RIGHT) and var['player']['x'] < 20):
      playerMove(color, var['player']['x'], var['player']['y'], var['player']['x']+1, var['player']['y'])
      var['player']['x'] = var['player']['x'] + 1
      # Teste si touche une piece
      if (touchCoin(var) != None):
        var['coin'].pop(touchCoin(var))
        wallet = wallet + 1

      # Attente pour réduction FPS
      timeTouch()
    elif (keydown(KEY_UP)):
      playerMove(color, var['player']['x'], var['player']['y'], var['player']['x'], var['player']['y']-2)
      var['player']['y'] = var['player']['y'] - 2
      # Teste si touche une piece
      if (touchCoin(var) != None):
        var['coin'].pop(touchCoin(var))
        wallet = wallet + 1

      # Attente pour réduction FPS
      timeTouch()
      if not (platformHitbox(level, var['player']['x'], var['player']['y'])):
        sleep(0.4)
        playerMove(color, var['player']['x'], var['player']['y'], var['player']['x'], var['player']['y']+2)
        var['player']['y'] = var['player']['y'] + 2
    elif (keydown(KEY_HOME)):
      menu(levelId)
      init()

    # Gravity
    # Je teste si le joueur ne tombe pas
    if (playerDrop(level, var['player']['x'], var['player']['y']) == True):
      playerMove(color, var['player']['x'], var['player']['y'], var['player']['x'], var['player']['y']+2)
      var['player']['y'] = var['player']['y'] + 2

    # Spawn coin
    for coin in var['coin']:
      fill_rect(coin['x']*15, coin['y']*15, 15, 15, color['coin'])

    # Move enemy
    var = enemyMove(color, level, var)

    # Touch enemy
    if (touchEnemy(var)):
      fill_rect(conv(0), conv(13), conv(1), conv(1), color['player'])
      var['player']['x'] = 0; var['player']['y'] = 13
      game(levelId)

    # Teste si toutes les pièces ont été ramassé
    if (len(var['coin']) == 0):
        levelId = levelId + 1
        game(levelId)

levelId = home()
game(levelId)
