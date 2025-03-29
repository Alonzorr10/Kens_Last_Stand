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
    def __init__(self, x = None, y = None):
        self.radius = random.randint(10, 30)
        # Use provided position or random position
        self.x = x if x is not None else random.randint(self.radius, WIDTH - self.radius)
        self.y = y if y is not None else random.randint(self.radius, HEIGHT - self.radius)
        self.speed = random.uniform(0.5, 2.0)
        self.angle = random.uniform(0, 2 * math.pi)
        self.float_offset = 0
        self.float_speed = 0.05
        self.float_amount = 5
        # Load the image
        self.image = pygame.image.load("Assets/KenSprite1.png")
        self.image = pygame.transform.scale(self.image, (self.radius * 2, self.radius * 2))
    def update(self):
        self.angle += random.uniform(-0.1, 0.1)
        
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        if self.x < self.radius or self.x > WIDTH - self.radius:
            self.angle = math.pi - self.angle
        if self.y < self.radius or self.y > HEIGHT - self.radius:
            self.angle = -self.angle
            
    def draw(self, surface):
        #pygame.draw.circle(surface, BLUE, (int(self.x), int(self.y + self.float_offset)), self.radius)
        surface.blit(self.image, (int(self.x - self.radius), (int(self.y + self.float_offset - self.radius))))

floater = FloatingObject()


clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                floater = FloatingObject(mouse_pos[0], mouse_pos[1])
                floaters.append(floater)

    screen.fill(BACKGROUND)

    for floater in floaters:
        floater.update()
        floater.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()




