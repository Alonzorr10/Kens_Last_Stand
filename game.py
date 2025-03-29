import random
import math
import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Floating object")

#colors for background 
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BACKGROUND = (240, 240, 240)
gradient = random.randrange(5, 11)
clock = pygame.time.Clock()
x = 650
y = 250

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


clock = pygame.time.Clock()
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




