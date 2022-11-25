import pygame

WIDTH = 400
HEIGHT = 300
FPS = 200

BLACK = (0, 0, 0)
GREY = (128, 128, 128)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((100, 80))
        # self.image.fill(BLACK)

        self.image = pygame.image.load("p1_jump.png")
        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.prev_time = pygame.time.get_ticks()
        self.speed_x = 0.5

    def update(self):
        curr_time = pygame.time.get_ticks()
        dt = curr_time - self.prev_time
        self.rect.x += self.speed_x * dt
        if self.rect.right > WIDTH:
            self.speed_x *= -1
            self.rect.right = WIDTH - (self.rect.right - WIDTH)
        if self.rect.left < 0:
            self.speed_x *= -1
            self.rect.left = abs(self.rect.left)
        self.prev_time = curr_time


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GAME")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

arial_font = pygame.font.SysFont("Arial", 20)
text = arial_font.render("quit", True, WHITE)

running = True
while running:
    clock.tick(FPS)
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_SPACE:

        if event.type == pygame.MOUSEBUTTONDOWN:
            if WIDTH / 2 <= mouse_pos[0] <= WIDTH / 2 + 140 and HEIGHT / 2 <= mouse_pos[1] <= HEIGHT / 2 + 40:
                running = False
    #
    all_sprites.update()
    # collisions = pygame.sprite.spritecollide(player, group_of_entites, False)


    screen.fill(GREEN)
    pygame.draw.rect(screen, GREY, [WIDTH / 2, HEIGHT / 2, 140, 40])
    screen.blit(text, (WIDTH / 2 + 50, HEIGHT / 2 + 10))

    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()