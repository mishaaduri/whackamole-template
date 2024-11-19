import pygame

import random


pygame.init()


SCREEN_WIDTH, SCREEN_HEIGHT = 640, 512  # 20 * 32, 16 * 32
GRID_SIZE = 32
GRID_ROWS, GRID_COLS = SCREEN_HEIGHT // GRID_SIZE, SCREEN_WIDTH // GRID_SIZE


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Whack-a-Mole")


mole_image = pygame.image.load("mole.png")  
mole_rect = mole_image.get_rect(topleft=(0, 0)) r

def draw_grid():
    for x in range(0, SCREEN_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (SCREEN_WIDTH, y))

def move_mole():
    row = random.randrange(GRID_ROWS)
    col = random.randrange(GRID_COLS)
    mole_rect.topleft = (col * GRID_SIZE, row * GRID_SIZE)

running = True
while running:
    screen.fill(WHITE)
    draw_grid()
    screen.blit(mole_image, mole_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if mole_rect.collidepoint(event.pos):
                move_mole()  

    pygame.display.flip()

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()
    


if __name__ == "__main__":
    main()
