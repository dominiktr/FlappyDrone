import sys, pygame, random, base64
#import time
from pygame.math import Vector2
pygame.init()
pygame.display.set_icon(pygame.image.load("drone.png"))

pygame.display.set_caption("FlappyDrone")

screendim=(1280,720)
screen = pygame.display.set_mode(screendim)

font = pygame.font.SysFont("Comic Sans", 80)
font0 = pygame.font.SysFont("Comic Sans", 20)
font1 = pygame.font.SysFont("Comic Sans", 35)
font2 = pygame.font.SysFont("Comic Sans", 65)
font3 = pygame.font.SysFont("Comic Sans", 60)
font4 = pygame.font.SysFont("Comic Sans", 40)
font5 = pygame.font.SysFont("Comic Sans", 15)
points = 0
step = 1

bg = pygame.image.load("bg.png")
bgpos = bg.get_rect()

bg1 = pygame.image.load("bg.png")
bgpos1 = bg1.get_rect()

def drawbg():
    if bgpos.x > -2470:
        if bgpos1.x <= -2469:
            bgpos1.x -= step
            screen.blit(bg1, bgpos1)
        bgpos.x -= step
        screen.blit(bg, bgpos)
        if bgpos.x == -2470:
            bgpos1.x = 1280
    elif bgpos1.x > -2470:
        if bgpos.x == -2470:
            bgpos1.x = 1280
        bgpos1.x -= step
        bgpos.x -= step
        screen.blit(bg, bgpos)
        screen.blit(bg1, bgpos1)
    else:
        bgpos.x = 1280
        bgpos1.x -= step
        bgpos.x -= step
        screen.blit(bg, bgpos)
        screen.blit(bg1, bgpos1)


def about():
    deltamenu = 0
    clockmenu = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and pygame.key == pygame.K_ESCAPE:
                sys.exit(0)
        deltamenu += clockmenu.tick() / 1000.0
        while deltamenu > 1 / 60:
            deltamenu = 0
            screen.fill((0, 0, 0))

            drawbg()
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(315, 140, 650, 440))
            pygame.draw.rect(screen, (33, 33, 33), pygame.Rect(320, 145, 640, 430)) #230

            #screen.blit(font1.render("About", True, (255, 255, 255)), (590, 240))
            screen.blit(font0.render("App author:", True, (255, 255, 255)), (340, 155))
            screen.blit(font0.render("Dominik Tracz", True, (255, 255, 255)), (470, 155)) #240

            screen.blit(font0.render("Background:", True, (255, 255, 255)), (340, 185)) #270
            screen.blit(font5.render("Author: LUM3N", True,(255, 255, 255)), (340, 205))#290
            screen.blit(font5.render("License: Pixabay License", True, (255, 255, 255)), (340, 220))#305
            screen.blit(font5.render("https://pixabay.com/pl/photos/przeciwmgielne-las-ciemny-gloomy-1535201/", True,(255, 255, 255)), (340, 235))#320

            screen.blit(font0.render("Icon && drone texture:", True, (255, 255, 255)), (340, 255))
            screen.blit(font5.render("Author: sinisamaric1", True, (255, 255, 255)), (340, 275))
            screen.blit(font5.render("License: Pixabay License", True, (255, 255, 255)), (340, 290))
            screen.blit(font5.render("https://pixabay.com/pl/vectors/drone-ikona-kamery-powietrze-1750345/", True,(255, 255, 255)), (340, 305))

            screen.blit(font0.render("Wood texture:", True, (255, 255, 255)), (340, 325))
            screen.blit(font5.render("Author: Warlev", True, (255, 255, 255)), (340, 345))
            screen.blit(font5.render("License: CC BY 4.0", True, (255, 255, 255)), (340, 360))
            screen.blit(font5.render("https://commons.wikimedia.org/wiki/File:CEDAR_TREE_BARK.png", True,(255, 255, 255)), (340, 375))

            screen.blit(font0.render("Ingame music:", True, (255, 255, 255)), (340, 395))
            screen.blit(font5.render('Title: "The Great Mundane: 2"', True, (255, 255, 255)), (340, 415))
            screen.blit(font5.render("Author: INTO INFINITY art exhibition by DUBLAB and Creative Commons", True, (255, 255, 255)), (340, 430))
            screen.blit(font5.render("License: CC BY-NC 3.0", True, (255, 255, 255)), (340, 445))
            screen.blit(font5.render("https://soundcloud.com/wearecc/the-great-mundane-2", True, (255, 255, 255)),(340, 460))

            screen.blit(font0.render("Menu music:", True, (255, 255, 255)), (340, 480))
            screen.blit(font5.render('Title: "Unrecognizable Now: 3"', True, (255, 255, 255)), (340, 500))
            screen.blit(font5.render("Author: INTO INFINITY art exhibition by DUBLAB and Creative Commons", True, (255, 255, 255)), (340, 515))
            screen.blit(font5.render("License: CC BY-NC 3.0", True, (255, 255, 255)), (340, 530))
            screen.blit(font5.render("https://soundcloud.com/wearecc/unrecognizable-now-3", True, (255, 255, 255)),(340, 545))

            menurect = pygame.Rect(800, 525, 150, 40)
            pygame.draw.rect(screen, (0, 0, 0), menurect)
            pygame.draw.rect(screen, (33, 33, 33), pygame.Rect(805, 530, 140, 30))
            screen.blit(font0.render("Menu (M)", True, (255, 255, 255)), (830, 535))


            pygame.display.flip()

            if pygame.mouse.get_pressed()[0] == 1:
                if menurect.collidepoint(pygame.mouse.get_pos()):
                    #time.sleep(0.2)
                    pygame.mixer.music.stop()
                    menu()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_p]:
                pygame.mixer.music.stop()
                game()
            if keys[pygame.K_m]:
                pygame.mixer.music.stop()
                menu()
            if keys[pygame.K_ESCAPE]:
                sys.exit(0)

def menu():
    pygame.mixer.music.load("menu.wav")
    pygame.mixer.music.play(-1)
    try:
        best = str(base64.b64decode(str(open("FlyDroneDATA.dat", 'r').readlines())))
        best = best.replace("'","").replace("b","")
        if best == "":
            best = "0"
    except:
        best = "0"
    finally:
        deltamenu = 0
        clockmenu = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and pygame.key == pygame.K_ESCAPE:
                    sys.exit(0)
            deltamenu += clockmenu.tick() / 1000.0
            while deltamenu > 1 / 60:
                deltamenu = 0
                screen.fill((0, 0, 0))

                drawbg()
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(315, 225, 650, 270))
                pygame.draw.rect(screen, (33, 33, 33), pygame.Rect(320, 230, 640, 260))

                screen.blit(font4.render("Hello!", True, (255, 255, 255)), (495, 250))

                screen.blit(font1.render("Best score:", True, (255, 255, 255)), (340, 360))
                screen.blit(font1.render(str(best), True, (255, 255, 255)), (530, 360))

                playrect = pygame.Rect(770, 315, 150, 40)
                pygame.draw.rect(screen, (0, 0, 0), playrect)
                pygame.draw.rect(screen, (33, 33, 33), pygame.Rect(775, 320, 140, 30))
                screen.blit(font0.render("Let's play! (P)", True, (255, 255, 255)), (780, 317))

                aboutrect = pygame.Rect(770, 370, 150, 40)
                pygame.draw.rect(screen, (0, 0, 0), aboutrect)
                pygame.draw.rect(screen, (33, 33, 33), pygame.Rect(775, 375, 140, 30))
                screen.blit(font0.render("About (A)", True, (255, 255, 255)), (800, 372))

                exitrect = pygame.Rect(770, 425, 150, 40)
                pygame.draw.rect(screen, (0, 0, 0), exitrect)
                pygame.draw.rect(screen, (33, 33, 33), pygame.Rect(775, 430, 140, 30))
                screen.blit(font0.render("Exit (Esc)", True, (255, 255, 255)), (800, 428))

                pygame.display.flip()

                if pygame.mouse.get_pressed()[0] == 1:
                    if playrect.collidepoint(pygame.mouse.get_pos()):
                        pygame.mixer.music.stop()
                        game()
                    if aboutrect.collidepoint(pygame.mouse.get_pos()):
                        about()
                    if exitrect.collidepoint(pygame.mouse.get_pos()):
                        sys.exit(0)
                keys = pygame.key.get_pressed()
                if keys[pygame.K_p]:
                    pygame.mixer.music.stop()
                    game()
                if keys[pygame.K_a]:
                    about()
                if keys[pygame.K_ESCAPE]:
                    sys.exit(0)


def game():
    points = 0

    try:
        best = base64.b64decode(str(open("FlyDroneDATA.dat", 'r').readlines()))
        best = best.replace("'", "").replace("b", "")
        if best == "":
            best = 0
    except:
        best = 0
    finally:

        bird =  pygame.transform.scale(pygame.image.load("drone.png"), (91, 25))

        #birdrect = bird.get_rect()
        #birdrect.x =int(screendim[0]/2)-birdrect.w*3
        #birdrect.y = int(screendim[1]/2)-birdrect.h


        delta = 0
        clock = pygame.time.Clock()


        pos = Vector2(screendim[0]/2-bird.get_rect().w*3, screendim[1]/2-bird.get_rect().h)
        vel: Vector2 = Vector2(0,0)
        acc = Vector2(0,0)
        birdrect = bird.get_rect()


        stumpw = 96
        stumpm = 3
        class stump:
            def __init__(self):
                #n = "building"+str(random.randint(1,6))+".png"
                #self.stump = pygame.image.load(n)
                #self.stumpup = pygame.transform.flip(self.stump, False, True)

                self.stump = pygame.image.load("stump.png")
                self.stumpup = pygame.image.load("stump.png")

                self.randy = random.randint(100,550)
                self.vy = 720 - self.randy+50
                self.stumpv = Vector2(1280, self.vy)
                self.stumpupv = Vector2(1280, -150)
                self.stump = pygame.transform.scale(self.stump, (stumpw, self.randy))
                self.stumpup = pygame.transform.scale(self.stump, (stumpw, 720-self.randy))
                self.stumprect = self.stump.get_rect()
                self.stumpuprect = self.stumpup.get_rect()
                self.stumprect.y = self.stumpv.y
                self.stumpuprect.y = self.stumpupv.y


            def draw(self):
                self.stumpv.x -= step
                self.stumpupv.x -= step
                self.stumprect.x = self.stumpv.x
                self.stumpuprect.x = self.stumpupv.x
                screen.blit(self.stump,self.stumpv)
                screen.blit(self.stumpup, self.stumpupv)




        def gamesummary():
            try:
                best = str(base64.b64decode(str(open("FlyDroneDATA.dat", 'r').readlines()).encode("UTF-8"))).replace("'","").replace("b","")
                best = best.replace("'", "").replace("b", "")
                if best == "":
                    best = 0
            except:
                best = 0
            finally:
                if points > int(best):
                    best = points
                    open("FlyDroneDATA.dat", "w").writelines(str(base64.b64encode(str(best).encode("UTF-8"))).replace("'","").replace("b",""))
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(315, 225, 650, 270))
                pygame.draw.rect(screen, (33, 33, 33), pygame.Rect(320, 230, 640, 260))

                screen.blit(font3.render("You lost!", True, (255, 255, 255)), (520, 250))
                screen.blit(font1.render("Your score:", True, (255, 255, 255)), (340, 330))
                screen.blit(font1.render(str(points), True, (255, 255, 255)), (530, 330))

                screen.blit(font1.render("Best score:", True, (255, 255, 255)), (340, 400))
                screen.blit(font1.render(str(best), True, (255, 255, 255)), (530, 400))

                retryrect = pygame.Rect(770, 325, 150, 40)
                pygame.draw.rect(screen, (0, 0, 0), retryrect)
                pygame.draw.rect(screen, (33, 33, 33), pygame.Rect(775, 330, 140, 30))
                screen.blit(font0.render("Retry! (R)", True, (255, 255, 255)), (800, 327))

                menurect = pygame.Rect(770, 395, 150, 40)
                pygame.draw.rect(screen, (0, 0, 0), menurect)
                pygame.draw.rect(screen, (33, 33, 33), pygame.Rect(775, 400, 140, 30))
                screen.blit(font0.render("Menu (M)", True, (255, 255, 255)), (800, 397))

                if pygame.mouse.get_pressed()[0] == 1:
                    if retryrect.collidepoint(pygame.mouse.get_pos()):
                        pygame.mixer.music.stop()
                        game()
                    if menurect.collidepoint(pygame.mouse.get_pos()):
                        pygame.mixer.music.stop()
                        menu()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_r]:
                    pygame.mixer.music.stop()
                    game()
                if keys[pygame.K_m]:
                    pygame.mixer.music.stop()
                    menu()


        d = stumpw*3
        stumparr = []


        pygame.mixer.music.load("game.wav")
        pygame.mixer.music.play(-1)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and pygame.key == pygame.K_ESCAPE:
                    sys.exit(0)

            delta += clock.tick()/1000.0
            while delta > 1/120:
                delta = 0
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    acc[1]-=2
                elif keys[pygame.K_ESCAPE]:
                    sys.exit(0)

                vel *= 0.9
                vel[1] += 0.7
                vel += acc
                pos += vel
                acc *= 0
                angle = pos.angle_to(Vector2(640, 500))
                birdrect.x = pos[0]
                birdrect.y = pos[1]

                screen.fill((0,0,0))
                drawbg()

                if d == stumpw*stumpm:
                    stumparr.append(stump())
                    d = 0

                for stumpi in stumparr:
                    stumpi.draw()
                    if stumpi.stumprect.colliderect(birdrect) or stumpi.stumpuprect.colliderect(birdrect) or pos[1] >= 660 or pos[1] <= 0:
                        delta1 = 0
                        clock1 = pygame.time.Clock()
                        while True:
                            delta1 += clock1.tick() / 1000.0
                            while delta1 > 1 / 120:
                                delta1 = 0
                                while pos[1] < 660:
                                    acc[1] += 1

                                    vel *= 0.9
                                    vel[1] += 0.7
                                    vel += acc
                                    pos += vel
                                    acc *= 0
                                    angle = pos.angle_to(Vector2(640, 300))
                                    birdrect.x = pos[0]
                                    birdrect.y = pos[1]

                                    screen.fill((0, 0, 0))
                                    drawbg()

                                    if d == stumpw * stumpm:
                                        stumparr.append(stump())
                                        d = 0

                                    for stumpi in stumparr:
                                        stumpi.draw()
                                    screen.blit(pygame.transform.rotate(bird, angle), pos)
                                    pygame.display.flip()
                                    screen.fill((0, 0, 0))
                                    d += step
                                    if pos[1] >= 660:
                                        pos[1] = 660
                                    pos[0] -= 1

                                vel *= 0.9
                                vel[1] += 0.7
                                vel += acc
                                pos += vel
                                acc *= 0
                                angle = pos.angle_to(Vector2(640, 150))
                                birdrect.x = pos[0]
                                birdrect.y = pos[1]

                                screen.fill((0, 0, 0))
                                if d == stumpw * stumpm:
                                    stumparr.append(stump())
                                    d = 0

                                drawbg()

                                for stumpi in stumparr:
                                    stumpi.draw()
                                screen.blit(pygame.transform.rotate(bird, angle), pos)

                                gamesummary()


                                pygame.display.flip()
                                if pos[1] >= 660:
                                    pos[1] = 660
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        sys.exit(0)
                                keys = pygame.key.get_pressed()
                                if keys[pygame.K_ESCAPE]:
                                    sys.exit(0)
                                d += step
                    if stumpi.stumpv.x+48 == pos[0]:
                        points += 1


                screen.blit(pygame.transform.rotate(bird, angle), pos)
                screen.blit(font.render(str(points), True, (255,255,255)), (640,60))
                pygame.display.flip()
                d += step

menu()
