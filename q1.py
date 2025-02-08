import pygame
import random

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game Setup")

player_size = 20
player_x, player_y = width // 5, height // 5
speed = 10

objects = []

running = True
show_instr = True
clk = pygame.time.Clock()
font = pygame.font.Font(None,36)

def spawn_object():
    while True:
        objx = random.randint(0, width - player_size)
        objy = random.randint(0, height - player_size)
        obj_rect = pygame.Rect(objx, objy, player_size, player_size)
        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)

        if not obj_rect.colliderect(player_rect):
            return objx, objy 

while running:
    screen.fill('#000000')

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYDOWN:
            if show_instr and e.key == pygame.K_s:
                show_instr = False
            elif e.key == pygame.K_f:
                running = False
            elif not show_instr and e.key == pygame.K_SPACE:
                objects.append(spawn_object())

    if show_instr:
        instructions = [
            "1. Use arrow keys to move the box (blue)",
            "2. Click the space bar to spawn new objects (green)",
            "3. Click F to finish",
            "4. Click S to start"
        ]

        for i, text in enumerate(instructions):
            render_text = font.render(text, True, pygame.Color("#FFFFFF")) 
            text_rect = render_text.get_rect(topleft=(2, i*30)) 
            screen.blit(render_text, text_rect) 
            
    else:

        keys = pygame.key.get_pressed()

        new_x, new_y = player_x, player_y

        if keys[pygame.K_LEFT]:
            new_x = max(0, player_x - speed)
        if keys[pygame.K_RIGHT]:
            new_x = min(width - player_size, player_x + speed)
        if keys[pygame.K_UP]:
            new_y = max(0, player_y - speed)
        if keys[pygame.K_DOWN]:
            new_y = min(height - player_size, player_y + speed)

        new_player_rect = pygame.Rect(new_x, new_y, player_size, player_size)

        collision = False
        for obj in objects:
            obj_rect = pygame.Rect(obj[0], obj[1], player_size, player_size)
            if new_player_rect.colliderect(obj_rect):
                collision = True
                break

        if not collision:
            player_x, player_y = new_x, new_y

        pygame.draw.rect(screen, "#12f8f5", (player_x, player_y, player_size, player_size))

        for obj in objects:
            pygame.draw.rect(screen, "#3cf812", (obj[0], obj[1], player_size, player_size))

    pygame.display.flip()
    clk.tick(30)

pygame.quit()
