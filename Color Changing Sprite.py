import pygame

def main():
    pygame.init()
    screen_width, screen_height = 500, 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('color changing sprite')

    colors = (
        'red': pygame.Color('red')
        'green': pygame.Color('green')
        'blue': pygame.Color('blue')
        'yellow': pygame.Color('yellow')
        'white': pygame.Color('white')
    )
    current_color = colors['white']

    x, y = 30, 30
    sprite_width, sprite_height = 60, 60

    clock = pygame.time.Clock()

    done = False