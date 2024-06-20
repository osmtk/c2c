import pygame

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)

class DS:
    # button
    cross = 0
    circle = 1
    square = 2
    triangle = 3
    share = 4
    ps = 5
    option = 6
    l3 = 7
    r3 = 8
    l1 = 9
    r1 = 10
    up = 11
    down = 12
    left = 13
    right = 14
    tpad = 15
    # axis
    lx = 0
    ly = 1
    rx = 2
    ry = 3
    l2 = 4
    r2 = 5



while True:
    for event in pygame.event.get():
        if not event:
            continue
        if event.type == pygame.constants.JOYBUTTONDOWN:
            print(event)
        elif event.type == pygame.constants.JOYBUTTONUP:
            print(event)
        elif event.type == pygame.constants.JOYAXISMOTION:
            if event.value < -0.1 or 0.1 < event.value:
                print(event)
                match event.axis:
                    case DS.lx:
                        pass
                    case DS.ly:
                        pass
                    case DS.rx:
                        pass
                    case DS.ry:
                        pass
                    case DS.l2:
                        pass
                    case DS.r2:
                        pass
        elif event.type == pygame.constants.CONTROLLERTOUCHPADMOTION:
            pass
