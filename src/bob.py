# TODO: add powerups(idk yet), respawning enemies, loot cubes.
import pygame
import time
pygame.init()
myfont=pygame.font.SysFont("Times New Roman",50)
bluecolor=(0,0,255)
redcolor=(255,0,0)
pinkcolor=(255,0,255)
greencolor=(0,255,0)
blackcolor=(0,0,0)
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
coin = pygame.draw.rect(screen,redcolor,pygame.Rect(335, 400,25,25))
pinkPlatform = pygame.draw.rect(screen,pinkcolor,pygame.Rect(750,600,100,10))
redPlatform = pygame.draw.rect(screen,redcolor,pygame.Rect(500, 700,100,10))
greenPlatformX = 300
greenPlatformY = 550
(greenPlatformWidth, greenPlatformHeight) = (100,10)
greenPlatform = pygame.draw.rect(screen,greencolor,pygame.Rect(greenPlatformX,greenPlatformY,greenPlatformWidth,greenPlatformHeight))
greenPlatformSpeed = 3


# Program starts
time.sleep(2)

background_colour = (0,0,0)

pygame.display.set_caption('Bob alpha')
screen.fill(background_colour)
pygame.display.flip()
running = True
jump = 0
pygame.mixer.music.load('./mp3/lofi_hip_hopchill_beats_lTRiuFIWV54-192k-1645860609450.mp3')
pygame.mixer.music.play(1)

enemySpeed=6

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
  keyPressed=pygame.key.get_pressed()

  # Clear screen
  screen.fill((255,255,255))

  # Draw fixed objects on screen
  img = pygame.image.load('./img/moyai.png')
  screen.blit(img, (100,100))
  img2 = pygame.image.load('./img/doggy.jpeg')
  screen.blit(img2, (1200,300))
  text1=myfont.render("Bob",1,bluecolor)
  text2=myfont.render("prototype",1,bluecolor)
  text3=myfont.render("Points:" + str(score),1,redcolor)
  text4=myfont.render("agognus",1,bluecolor)
  screen.blit(text1,(1200,10))
  screen.blit(text2,(1200,60))
  screen.blit(text3,(100,10))
  screen.blit(text4,(100,200))
  pygame.draw.rect(screen,redcolor,redPlatform)
  pygame.draw.rect(screen,pinkcolor,pinkPlatform)
  pygame.draw.rect(screen,greencolor,greenPlatform)

  # Check keys
  if keyPressed[pygame.K_a]:
    x=max(x-5,0);
  if keyPressed[pygame.K_d]:
    x=min(x+5,width-objWidth);
  if keyPressed[pygame.K_ESCAPE]:
      done = True
  if keyPressed[pygame.K_SPACE]:
      if (x >= 500 - objWidth and x <= 600 and y == 700 - objHeight) or (x >= greenPlatformX - objWidth and x <= greenPlatformX + greenPlatformWidth and y == greenPlatformY - objHeight) or (y == height - objHeight):
          jump = 200

  # Jump
  if jump > 0:
    y=max(y-10,0)
    jump -= 10
  # green platform
  elif x >= greenPlatformX - objWidth and x <= greenPlatformX+greenPlatformWidth and y <= greenPlatformY - objHeight:
    y=min(y+7,greenPlatformY - objHeight)
  # red platform
  elif x >= 500 - objWidth and x <= 600 and y <= 700- objHeight:
    y=min(y+7,700-objHeight)
  # floor
  elif y < height - objHeight:
    y=min(y+7,height-objHeight)

  player = pygame.draw.rect(screen,bluecolor,pygame.Rect(x,y,objWidth,objHeight))

  # Pink Platform
  if pygame.Rect.colliderect(player, pinkPlatform) == True:
    (x,y) = (0,height - objHeight)

  # Coin
  if coin:
    pygame.draw.rect(screen,redcolor,pygame.Rect(335, 400,25,25))
    if pygame.Rect.colliderect(player, coin) == True:
      score += 1
      coin = None

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
          else:
              score += 1
              enemy = None
  # Move greenPlatform
  if greenPlatform:
      greenPlatformX = greenPlatformX + greenPlatformSpeed
      if greenPlatformX >= 700 - greenPlatformWidth:
          greenPlatformSpeed = -3
      elif greenPlatformX <= 75:
          greenPlatformSpeed = 3
      greenPlatform = pygame.draw.rect(screen,greencolor,pygame.Rect(greenPlatformX,greenPlatformY,greenPlatformWidth,greenPlatformHeight))


  pygame.display.update()
  clock.tick(60)
