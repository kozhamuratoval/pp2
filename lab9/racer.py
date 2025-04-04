import pygame, sys
from pygame.locals import *
import random, time

# Initialize pygame
pygame.init()

# Set up the frame rate
FPS = 60
FramePerSec = pygame.time.Clock()

# Define colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen dimensions and game variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5  # Initial enemy speed
SCORE = 0  # Score counter
COINS_COLLECTED = 0  # Coin collection counter
SPEED_INCREASE_THRESHOLD = 5  # Number of coins needed to increase enemy speed

# Load fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Load background image
background = pygame.image.load("Street.png")

# Create game window
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        """Moves the enemy down and respawns it at the top when it goes off-screen."""
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            SCORE += 1  # Increase score when enemy respawns
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        """Handles player movement based on key inputs."""
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

# Coin class with different weights
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Randomly choose coin type (1: normal, 2: silver, 3: gold)
        self.coin_type = random.randint(1, 3)
        
        # Load different coin images based on type
        if self.coin_type == 1:
            original_image = pygame.image.load("coin.png")
            self.weight = 1
            self.image = pygame.transform.scale(original_image, (30, 30))
        elif self.coin_type == 2:
            original_image = pygame.image.load("coin_silver.png")  # You need to have this image
            self.weight = 2
            self.image = pygame.transform.scale(original_image, (35, 35))
        else:  # type 3
            original_image = pygame.image.load("coin_gold.png")  # You need to have this image
            self.weight = 3
            self.image = pygame.transform.scale(original_image, (40, 40))
            
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(-600, 0))

    def move(self):
        """Moves the coin down and respawns it at the top when it goes off-screen."""
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            self.respawn()

    def respawn(self):
        """Respawns the coin with a new random type and position."""
        self.coin_type = random.randint(1, 3)
        if self.coin_type == 1:
            original_image = pygame.image.load("coin.png")
            self.weight = 1
            self.image = pygame.transform.scale(original_image, (30, 30))
        elif self.coin_type == 2:
            original_image = pygame.image.load("coin_silver.png")
            self.weight = 2
            self.image = pygame.transform.scale(original_image, (35, 35))
        else:
            original_image = pygame.image.load("coin_gold.png")
            self.weight = 3
            self.image = pygame.transform.scale(original_image, (40, 40))
            
        self.rect.top = random.randint(-600, 0)
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), self.rect.top)

# Set up Sprites
P1 = Player()
E1 = Enemy()

# Create sprite groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# Create a custom event for adding new coins
ADDCOIN = pygame.USEREVENT + 1
pygame.time.set_timer(ADDCOIN, 2000)  # Add a new coin every 2 seconds

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == ADDCOIN:
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)
    
    # Update game state
    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    coins_text = font_small.render(f"Coins: {COINS_COLLECTED}", True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coins_text, (300, 10))
    
    # Move and draw all sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    
    # Check for collisions between player and coins
    collected_coins = pygame.sprite.spritecollide(P1, coins, True)
    for coin in collected_coins:
        COINS_COLLECTED += coin.weight  # Add coin weight to total
        # Increase speed every SPEED_INCREASE_THRESHOLD coins
        if COINS_COLLECTED % SPEED_INCREASE_THRESHOLD == 0:
            SPEED += 0.5  # Slightly increase speed
    
    # Check for collision between player and enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)
        
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()        
    
    pygame.display.update()
    FramePerSec.tick(FPS)