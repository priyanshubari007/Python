import pygame, random,math 

pygame.init()


screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Space Invaders")


bg = pygame.image.load("space.jpg")
player_img = pygame.image.load("rocket.png")
enemy_img = pygame.image.load("alien.png")
bullet_img = pygame.image.load("bullet.png")
icon = pygame.image.load("ufo.webp")
pygame.display.set_icon(icon)

player_x, player_y = 370, 380
player_speed = 0


enemies = []
for i in range(6):
    enemies.append([
        random.randint(0, 736),
        random.randint(50, 150),
        4
    ])

bullet_x, bullet_y = 0, 380
bullet_state = "ready"

score = 0
font = pygame.font.SysFont(None, 40)


def show_score():
        txt = font.render("Score : " +str(score), True, (253,255,255))
        screen.blit(txt,  (10,10))

def collision(ex, ey, bx, by):
        return math.sqrt((ex-bx)**2 + (ey-by)**2) < 27
    
running = True
while running:

        screen.blit(bg, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_speed = -5
                if event.key == pygame.K_RIGHT:
                    player_speed = 5
                if event.key == pygame.K_SPACE and bullet_state == "ready":
                    bullet_x = player_x
                    bullet_state = "fire"

            if event.type == pygame.KEYDOWN:
                player_speed = 0

        player_x += player_speed
        player_x = max(0, min(player_x, player_y))
        screen.blit(player_img, (player_x, player_y))

        if bullet_state == "fire":
            screen.blit(bullet_img, (bullet_x+16, bullet_y))
            bullet_y -= 10

        if bullet_y <= 0:
            bullet_y = 380
            bullet_state = "ready"
        for e in enemies:
            e[0] += e[2]

            if e[0] <= 0 or e[0] >= 736:
                e[2] *= -1
                e[1] += 40
            if collision(e[0], e[1], bullet_x, bullet_y):
               score += 1
               bullet_y = 300
               bullet_state = "ready"
               e[0] = random.randint(0, 736)
               e[1] = random.randint(50, 150)

            screen.blit(enemy_img, (e[0], e[1]))

        show_score()
        pygame.display.update()
