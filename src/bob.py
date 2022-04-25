# TODO: add powerups(idk yet), respawning enemies, loot cubes, add impossible obstacles, enemies that jump
import time
import pygame

pygame.init()
myfont=pygame.font.SysFont("Times New Roman",50)
myfontLevels = pygame.font.SysFont("Roboto Mono", 60)
bluecolor=(0,0,255)
redcolor=(255,0,0)
pinkcolor=(255,0,255)
greencolor=(0,255,0)
blackcolor=(0,0,0)
aquacolor = (0,255,255)
done=False
score = 0
(width, height) = (pygame.display.Info().current_w, pygame.display.Info().current_h)
(objWidth,objHeight) = (50,50)
(enemyWidth,enemyHeight) = (45,45)
clock=pygame.time.Clock()
x=10
enemyX = 1200
y=(height-objHeight)
enemyY=(height-enemyHeight)
screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
pygame.key.set_repeat(25)
enemy = pygame.draw.rect(screen,pinkcolor,pygame.Rect(enemyX,enemyY,enemyWidth,enemyHeight))
player = pygame.draw.rect(screen,bluecolor,pygame.Rect(x,y,objWidth,objHeight))
coinHeight = 25
coinWidth = 25
coinX = 335
coinY = 400
coin = pygame.draw.rect(screen,redcolor,pygame.Rect(coinX,coinY,coinWidth,coinHeight))
(pinkPlatformX, pinkPlatformY, pinkPlatformWidth, pinkPlatformHeight) = (750,600,100,10)
pinkPlatform = pygame.draw.rect(screen,pinkcolor,pygame.Rect(pinkPlatformX, pinkPlatformY, pinkPlatformWidth, pinkPlatformHeight))
redPlatformH = 10
redPlatformW = 100
redPlatformY = 700
redPlatformX = 500
redPlatform = pygame.draw.rect(screen,redcolor,pygame.Rect(redPlatformX, redPlatformY,redPlatformW,redPlatformH))
greenPlatformX = 300
greenPlatformY = 550
greenPlatformLimit = 75
greenPlatformLimit2 = 700
(greenPlatformWidth, greenPlatformHeight) = (100,10)
greenPlatform = pygame.draw.rect(screen,greencolor,pygame.Rect(greenPlatformX,greenPlatformY,greenPlatformWidth,greenPlatformHeight))
greenPlatformSpeed = 10
(bluePlatformX,bluePlatformY,bluePlatformWidth,bluePlatformHeight) = (900, 560, 100, 10)
bluePlatformSpeed = 20
bluePlatformLimit = 300
bluePlatformLimit2 = 550
bluePlatform = pygame.draw.rect(screen,bluecolor,pygame.Rect(bluePlatformX,bluePlatformY,bluePlatformWidth,bluePlatformHeight))
ded = False
# level 0 = tutorial
level = 0
#Start screen
start = True
# Program starts
time.sleep(2)

background_colour = (255,255,255)

pygame.display.set_caption('Bob alpha')
screen.fill(background_colour)
pygame.display.flip()
running = True
jump = 0
pygame.mixer.music.load('lofiHipHop.mp3')
pygame.mixer.music.play(1)

enemySpeed=6

def resetLevel():
    global level, jump
    global greenPlatformX,greenPlatformY,greenPlatformSpeed
    global pinkPlatformX,pinkPlatformY
    global coinX,coinY
    global enemyX
    level = 0
    jump = 0
    (greenPlatformX,greenPlatformY,greenPlatformSpeed) = (300,550,10)
    (pinkPlatformX,pinkPlatformY) = (750,600)
    (coinX,coinY) = (335,400)
    enemyX = 1200


# TO DO - function to change level
def nextLevel():
    global level, x, y, jump
    global greenPlatformX, greenPlatformY, greenPlatformSpeed, greenPlatformLimit, greenPlatformLimit2
    global pinkPlatformX, pinkPlatformY
    global coin, coinX, coinY
    global bluePlatform, bluePlatformX, bluePlatformY, bluePlatformWidth, bluePlatformHeight
    level += 1
    # Reset player position and jump
    (x,y) = (0, height-objHeight)
    time.sleep(0.05)
    jump = 0
    if level == 1:
        (greenPlatformX, greenPlatformY) = (600,600)
        greenPlatformSpeed = 0
        (pinkPlatformX, pinkPlatformY) = (350,450)
        (coinX, coinY) = (925,400)

    if level == 2:
        (greenPlatformX, greenPlatformY) = (200,600)
        greenPlatformSpeed = 4
        (greenPlatformLimit, greenPlatformLimit2) = (50,1000)
        (pinkPlatformX, pinkPlatformY) = (600, 550)
        jump = 250

    if level == 3:
        (bluePlatformX, bluePlatformY) = (1100,550)

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
  keyPressed=pygame.key.get_pressed()

  # Clear screen
  screen.fill((255,255,255))

  # Draw fixed objects on screen
  img = pygame.image.load('moyai.png')
  screen.blit(img, (100,100))
  img2 = pygame.image.load('doggy.jpeg')
  screen.blit(img2, (1200,300))
  text1=myfont.render("Bob",1,bluecolor)
  screen.blit(text1,(1200,10))
  text2=myfont.render("prototype",1,bluecolor)
  screen.blit(text2,(1200,60))
  text3=myfont.render("Points:" + str(score),1,redcolor)
  screen.blit(text3,(100,10))
  pygame.draw.rect(screen,redcolor,redPlatform)
  pygame.draw.rect(screen,pinkcolor,pinkPlatform)
  pygame.draw.rect(screen,greencolor,greenPlatform)
  if level == 3 or level == 1:
    bluePlatform = pygame.draw.rect(screen,bluecolor,bluePlatform)
  img4 = pygame.image.load('start.png')


  if level == 0:
      text4=myfontLevels.render("Tutorial",1,aquacolor)
      screen.blit(text4,(600,20))
  else:
      text5 = myfontLevels.render("Level:" + str(level),1, aquacolor)
      screen.blit(text5,(600,20))

  # Check keys
  if keyPressed[pygame.K_a]:
    x=max(x-5,0);
  if keyPressed[pygame.K_d]:
    x=min(x+5,width-objWidth);
  if keyPressed[pygame.K_ESCAPE]:
    done = True
  if keyPressed[pygame.K_SPACE]:
    if (x >= redPlatformX - objWidth and x <= redPlatformX + redPlatformW and y == redPlatformY - objHeight) \
       or (x >= greenPlatformX - objWidth and x <= greenPlatformX + greenPlatformWidth and y == greenPlatformY - objHeight) \
       or (x >= bluePlatformX - objWidth and x <= bluePlatformX + bluePlatformWidth and y == bluePlatformY - objHeight) \
       or (y == height - objHeight):
        jump = 200

  # ded
  if ded == True:
    screen.blit(img3,(0,0))
    (x,y) = (10,height - objHeight)
    screen.blit(img3, (0,0))
    pygame.display.update()
    button = pygame.Rect(550, 700, 450, 300 )
    mouseClicks = pygame.mouse.get_pressed()
    if mouseClicks == (1,0,0) and button.collidepoint( pygame.mouse.get_pos() ):
        resetLevel()
        ded = False
    else:
       continue

  # Start screen
  if start == True:
    screen.blit(img4, (0,0))
    controlsButton = pygame.Rect(500,400,450,300)
    playButton = pygame.Rect(500,350,450,200)
    returnButton = pygame.Rect(30,30,450,50)
    mouseClicks = pygame.mouse.get_pressed()
    pygame.display.update()
    if mouseClicks == (1,0,0) and controlsButton.collidepoint(pygame.mouse.get_pos()):
        pass
    if mouseClicks == (1,0,0) and playButton.collidepoint(pygame.mouse.get_pos()):
        resetLevel()
        start = False
    else:
      continue

  # Jump
  if jump > 0:
    y=max(y-10,0)
    jump -= 10
  # green platform
  elif x >= greenPlatformX - objWidth and x <= greenPlatformX+greenPlatformWidth and y <= greenPlatformY - objHeight:
    y=min(y+7,greenPlatformY - objHeight)

  elif x >= bluePlatformX - objWidth and x <= bluePlatformX+bluePlatformWidth and y <= bluePlatformY - objHeight:
    y=min(y+7,bluePlatformY - objHeight)

  # red platform
  elif x >= redPlatformX - objWidth and x <= redPlatformX + redPlatformW and y <= redPlatformY - objHeight:
    y=min(y+7,redPlatformY-objHeight)

  # floor
  elif y < height - objHeight:
    y=min(y+7,height-objHeight)

  player = pygame.draw.rect(screen,bluecolor,pygame.Rect(x,y,objWidth,objHeight))

  # Pink Platform
  img3 = pygame.image.load('Death.png')
  pinkPlatform = pygame.draw.rect(screen,pinkcolor,pygame.Rect(pinkPlatformX, pinkPlatformY, pinkPlatformWidth, pinkPlatformHeight))
  if pygame.Rect.colliderect(player, pinkPlatform) == True:
    ded = True

  # Coin
  coin = pygame.draw.rect(screen,redcolor,pygame.Rect(coinX, coinY,coinWidth,coinHeight))
  if pygame.Rect.colliderect(player, coin) == True:
      time.sleep(0.1)
      nextLevel()

  # Move enemy
  if enemy:
      enemyX = enemyX + enemySpeed
      if enemyX >= width-enemyWidth:
          enemySpeed = -6
      elif enemyX <= 0:
          enemySpeed = 6
      enemy = pygame.draw.rect(screen,pinkcolor,pygame.Rect(enemyX,enemyY,enemyWidth,enemyHeight))

      if pygame.Rect.colliderect(player, enemy):
          if y == height-objHeight:
              (x,y) = (10,height-objHeight)
              ded = True
          else:
              score += 1
              enemy = None

  # Move greenPlatform
  if greenPlatform:
      greenPlatformX = greenPlatformX + greenPlatformSpeed
      if greenPlatformX <= greenPlatformLimit or greenPlatformX >= greenPlatformLimit2 - greenPlatformWidth:
          greenPlatformSpeed *= -1
      greenPlatform = pygame.draw.rect(screen,greencolor,pygame.Rect(greenPlatformX,greenPlatformY,greenPlatformWidth,greenPlatformHeight))

  if bluePlatform and level == 3:
      bluePlatformY = bluePlatformY + bluePlatformSpeed
      if bluePlatformY <= bluePlatformLimit or bluePlatformY >= bluePlatformLimit2 - bluePlatformHeight:
          bluePlatformSpeed *= -1
      bluePlatform = pygame.draw.rect(screen,bluecolor,pygame.Rect(bluePlatformX,bluePlatformY,bluePlatformWidth,bluePlatformHeight))

  pygame.display.update()
  clock.tick(60)
