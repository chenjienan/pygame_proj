import pygame
import sys

pygame.init()
windowSize = (800, 600)


screen = pygame.display.set_mode(windowSize)

my_font = pygame.font.SysFont("Myriad Pro", 48)

# greetings = my_font.render("Python", 1, (255, 0, 0), (0, 0, 0))

# load images
greetings = pygame.image.load('sprite.png')
greetings_size = greetings.get_size()

# sound mixer
pygame.mixer.init()
sound = pygame.mixer.Sound('crash.wav')

x, y = 0, 0
direction_x, direction_y = 1, 1

pygame.mouse.set_visible(0)

clock = pygame.time.Clock()

while True:

    clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RIGHT:
                x += 3
            if e.key == pygame.K_LEFT:
                x -= 3
            if e.key == pygame.K_UP:
                y -= 3
            if e.key == pygame.K_DOWN:
                y += 3

    screen.fill((0, 0, 0))
    screen.blit(greetings, (x, y))

    mouse_pos = pygame.mouse.get_pos()
    x, y = mouse_pos

    if x + greetings_size[0] > 800:
        x = 800 - greetings_size[0]
        sound.stop()
        sound.play()

    if y + greetings_size[1] > 600:
        y = 600 - greetings_size[1]

    # x += 3 * direction_x
    # y += 3 * direction_y

    # if x + greetings_size[0] > 800 or x <= 0:
    #     direction_x *= -1

    # if y + greetings_size[1] > 600 or y <= 0:
    #     direction_y *= -1
    
    pygame.display.update()