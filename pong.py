import pygame

pygame.init()
running = True

window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

clock = pygame.time.Clock()

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()