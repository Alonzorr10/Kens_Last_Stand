import sys
import pygame

pygame.init()


pygame.display.set_caption("Ken's Last Stand")

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600

text_font = pygame.font.SysFont(None, 30)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    print("Drawing Text: ", text)
    screen.blit(img, (x, y))

player = pygame.Rect((300, 250, 50, 50))

if __name__ == "__main__":
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while(True):
        screen.fill((255, 255, 255))
        draw_text("I love Ken", text_font, (0, 0, 0), 255, 155)

        pygame.draw.rect(screen, (250, 0, 0), player)
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
