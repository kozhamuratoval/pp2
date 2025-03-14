import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moving Red Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)


BALL_RADIUS = 25
ball_x = SCREEN_WIDTH // 2 
ball_y = SCREEN_HEIGHT // 2
MOVE_DISTANCE = 20

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            new_x = ball_x
            new_y = ball_y
            
            if event.key == pygame.K_UP:
                new_y -= MOVE_DISTANCE
            elif event.key == pygame.K_DOWN:
                new_y += MOVE_DISTANCE
            elif event.key == pygame.K_LEFT:
                new_x -= MOVE_DISTANCE
            elif event.key == pygame.K_RIGHT:
                new_x += MOVE_DISTANCE
            
            if (BALL_RADIUS <= new_x <= SCREEN_WIDTH - BALL_RADIUS and
                BALL_RADIUS <= new_y <= SCREEN_HEIGHT - BALL_RADIUS):
                ball_x = new_x
                ball_y = new_y

    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()