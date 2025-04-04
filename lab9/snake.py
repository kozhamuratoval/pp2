import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
background_color = (204, 51, 255)

dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Enhanced Snake Game")

clock = pygame.time.Clock()
snake_block = 10
initial_speed = 15
snake_speed = 15
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

wall_thickness = 20
play_area = {
    'x_min': wall_thickness,
    'x_max': dis_width - wall_thickness,
    'y_min': wall_thickness,
    'y_max': dis_height - wall_thickness
}

def draw_walls():
    pygame.draw.rect(dis, blue, [0, 0, dis_width, wall_thickness])
    pygame.draw.rect(dis, blue, [0, dis_height - wall_thickness, dis_width, wall_thickness])
    pygame.draw.rect(dis, blue, [0, 0, wall_thickness, dis_height])
    pygame.draw.rect(dis, blue, [dis_width - wall_thickness, 0, wall_thickness, dis_height])

def generate_food(snake_list):
    while True:
        foodx = round(random.randrange(play_area['x_min'], play_area['x_max'] - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(play_area['y_min'], play_area['y_max'] - snake_block) / 10.0) * 10.0
        
        food_overlaps = False
        for segment in snake_list:
            if segment[0] == foodx and segment[1] == foody:
                food_overlaps = True
                break
                
        if not food_overlaps:
            return foodx, foody

def display_score(score, level):
    score_text = score_font.render(f"Score: {score}", True, black)
    level_text = score_font.render(f"Level: {level}", True, black)
    dis.blit(score_text, [10, wall_thickness + 5])
    dis.blit(level_text, [dis_width - 150, wall_thickness + 5])

def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def display_message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():
    game_over = False
    game_close = False
    
    x1 = play_area['x_min'] + (play_area['x_max'] - play_area['x_min']) // 2
    y1 = play_area['y_min'] + (play_area['y_max'] - play_area['y_min']) // 2
    x1_change = 0
    y1_change = 0
    
    snake_list = []
    length_of_snake = 1
    score = 0
    level = 1
    foods_eaten_in_level = 0
    foods_needed_for_next_level = 3  
    
    foodx, foody = generate_food(snake_list)
    
    while not game_over:
        # Game over screen
        while game_close:
            dis.fill(background_color)
            display_message("Game Over! Press Q-Quit or C-Play Again", white)
            display_score(score, level)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        # Reset game state
                        snake_speed = 15
                        gameLoop()
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change <= 0:  # Prevent 180-degree turn
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change >= 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change <= 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change >= 0:
                    y1_change = snake_block
                    x1_change = 0
        
        # Update snake position
        x1 += x1_change
        y1 += y1_change
        
        # Check for wall collision
        if (x1 >= play_area['x_max'] or x1 < play_area['x_min'] or 
            y1 >= play_area['y_max'] or y1 < play_area['y_min']):
            game_close = True
        
        # Draw game elements
        dis.fill(background_color)
        draw_walls()
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        
        # Update snake
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        
        # Check for self-collision
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True
        
        draw_snake(snake_block, snake_list)
        display_score(score, level)
        pygame.display.update()
        
        # Check if food was eaten
        if x1 == foodx and y1 == foody:
            foodx, foody = generate_food(snake_list)
            length_of_snake += 1
            score += 1
            foods_eaten_in_level += 1
            
            # Level progression
            if foods_eaten_in_level >= foods_needed_for_next_level:
                level += 1
                snake_speed += 2  # Increase speed
                foods_eaten_in_level = 0
                foods_needed_for_next_level += 1  # Make next level slightly harder
        
        clock.tick(snake_speed)
    
    pygame.quit()
    quit()

# Start the game
gameLoop()