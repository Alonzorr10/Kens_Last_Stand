import random
import math
import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ken's Last Stand")

#colors for background 
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BACKGROUND = (240, 240, 240)
BUTTON_COLOR = (100, 100, 255)
BUTTON_HOVER_COLOR = (150, 150, 255)
TEXT_COLOR = (0, 0, 0)
gradient = random.randrange(5, 11)
clock = pygame.time.Clock()
x = 650
y = 250

game_state = "Menu"
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()


class FloatingObject:
    def __init__(self):
        self.radius = 20
        self.x = random.randint(self.radius, WIDTH - self.radius)
        self.y = random.randint(self.radius, HEIGHT - self.radius)
        self.speed = 1.5
        self.angle = random.uniform(0, 2 * math.pi)
        self.float_offset = 0
        self.float_speed = 0.05
        self.float_amount = 5
    def update(self):
        self.angle += random.uniform(-0.1, 0.1)
        
        
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        
        
        if self.x < self.radius or self.x > WIDTH - self.radius:
            self.angle = math.pi - self.angle
        if self.y < self.radius or self.y > HEIGHT - self.radius:
            self.angle = -self.angle
            
        # Floating up and down effect
        #self.float_offset = math.sin(pygame.time.get_ticks() * self.float_speed) * self.float_amount
        
    def draw(self, surface):
        pygame.draw.circle(surface, BLUE, (int(self.x), int(self.y + self.float_offset)), self.radius)

floater = FloatingObject()

button_rect = pygame.Rect(WIDTH // 2 - 75, HEIGHT // 2, 150, 50)

def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def menu_screen():
    global game_state
    while game_state == "Menu":
        screen.fill(WHITE)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        button_color = BUTTON_HOVER_COLOR if button_rect.collidepoint(mouse_x, mouse_y) else BUTTON_COLOR

        pygame.draw.rect(screen, button_color, button_rect)
        draw_text("Start Game", font, TEXT_COLOR, WIDTH // 2 - 50, HEIGHT // 2 + 10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    game_state = "game"  # Switch to game state

        pygame.display.flip()
        clock.tick(60)

menu_screen()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
   
    floater.update()
    
    
    screen.fill(BACKGROUND)
    floater.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()




