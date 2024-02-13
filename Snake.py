import pygame
import sys

# O'yin ekranini o'rnatish
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("To'rtburchak Shakl")

# Ranglar
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Shaklning x, y koordinatalari va o'lchami
shape_x = WIDTH // 2
shape_y = HEIGHT // 2
shape_width = 100
shape_height = 80

# O'yin asosiy sikl
def main():
    running = True
    while running:
        screen.fill(BLACK)

        # Shaklning chizilishi
        pygame.draw.rect(screen, WHITE, (shape_x, shape_y, shape_width, shape_height))

        # Ekran yangilash
        pygame.display.flip()

        # Dasturni to'xtatish uchun tekshirish
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
