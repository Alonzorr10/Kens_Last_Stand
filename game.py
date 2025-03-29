import random
import math
import pygame
from pygame import mixer

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ken's Last Stand")

# Colors for background
WHITE = (255, 255, 255)
BACKGROUND = (240, 240, 240)
BUTTON_COLOR = (100, 100, 255)
BUTTON_HOVER_COLOR = (150, 150, 255)
TEXT_COLOR = (0, 0, 0)
TITLE_TEXT_COLOR = (255, 255, 255)

game_state = "Menu"
font = pygame.font.Font(None, 30)
title_font = pygame.font.SysFont('Comic-Sans', 45)
clock = pygame.time.Clock()

class FloatingObject:
    def __init__(self, x=None, y=None):
        self.radius = random.randint(10, 30)  # Base radius
        circSize = random.randint(2, 7)  # Scaling factor
        self.scaled_radius = self.radius * circSize  # Final object size

        # Load and scale image
        filenames = ["Assets/KenSprite1.png", "Assets/KenSprite2.png", "Assets/KenSprite3.png"]
        random_image = random.choice(filenames)
        self.image = pygame.image.load(random_image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.scaled_radius, self.scaled_radius))

        # Set initial position
        self.x = x if x is not None else random.randint(self.scaled_radius, WIDTH - self.scaled_radius)
        self.y = y if y is not None else random.randint(self.scaled_radius, HEIGHT - self.scaled_radius)

        # Get rect for accurate positioning
        self.rect = self.image.get_rect(center=(self.x, self.y))

        # Movement properties
        self.speed = random.uniform(0.5, 2.0)
        self.angle = random.uniform(0, 2 * math.pi)

    def update(self):
        """Move floating object with slight random variation in direction."""
        self.angle += random.uniform(-0.1, 0.1)
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed

        # Keep object within bounds
        if self.x < self.scaled_radius or self.x > WIDTH - self.scaled_radius:
            self.angle = math.pi - self.angle
        if self.y < self.scaled_radius or self.y > HEIGHT - self.scaled_radius:
            self.angle = -self.angle

        # Update rect position
        self.rect.center = (self.x, self.y)

    def draw(self, surface):
        """Draw the floating object."""
        surface.blit(self.image, self.rect.topleft)

    def is_clicked(self, mouse_pos):
        """Check if mouse click is within object radius."""
        mx, my = mouse_pos
        radius = self.image.get_width() // 2  # More accurate radius
        distance = math.sqrt((mx - self.x) ** 2 + (my - self.y) ** 2)
        return distance <= radius

floaters = [FloatingObject()]
button_rect = pygame.Rect(WIDTH // 2 - 75, HEIGHT // 2, 150, 50)

def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def end_screen(score):
    """Game over screen with replay option."""
    global game_state
    while game_state == "End":
        screen.fill(WHITE)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        button_color = BUTTON_HOVER_COLOR if button_rect.collidepoint(mouse_x, mouse_y) else BUTTON_COLOR

        draw_text("Game Over", title_font, TEXT_COLOR, 230, 100)
        pygame.draw.rect(screen, button_color, button_rect)
        draw_text("Play Again?", font, TEXT_COLOR, WIDTH // 2 - 55, HEIGHT // 2 + 14)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
                game_state = "game"

        pygame.display.flip()
        clock.tick(60)

def menu_screen():
    """Main menu screen."""

    mixer.music.load('Assets/funky town low quality.mp3')
    mixer.music.play(-1)
    global game_state
    bg_img = pygame.image.load("Assets/KenSprite1.png")
    bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))
    
    while game_state == "Menu":
        screen.blit(bg_img, (0, 0))
        mouse_x, mouse_y = pygame.mouse.get_pos()
        button_color = BUTTON_HOVER_COLOR if button_rect.collidepoint(mouse_x, mouse_y) else BUTTON_COLOR

        draw_text("Ken's Last Stand", title_font, TITLE_TEXT_COLOR, 230, 100)
        pygame.draw.rect(screen, button_color, button_rect)
        draw_text("Start Game", font, TEXT_COLOR, WIDTH // 2 - 55, HEIGHT // 2 + 14)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
                mixer.music.load('Assets/funky town low quality.mp3')
                mixer.music.stop
                game_state = "game"

        pygame.display.flip()
        clock.tick(60)

menu_screen()
running = True
counter = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            mouse_pos = pygame.mouse.get_pos()

            if(counter % 10 == 0):
                ken_Sound = mixer.Sound('Assets/good boy.mp3')
                ken_Sound.play()

            # Check if a floater was clicked
            clicked_object = next((floater for floater in floaters if floater.is_clicked(mouse_pos)), None)
            if clicked_object:
                game_state = "End"
                end_screen(score)
            else:
                #score += 1
                floaters.append(FloatingObject(mouse_pos[0], mouse_pos[1]))

            if game_state == "End":
                end_screen()

    screen.fill(BACKGROUND)
    score = 0
    for floater in floaters:
        score += 1
        floater.update()
        floater.draw(screen)
        BACKGROUND = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        floater.speed += random.uniform(0.05, 0.05)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()