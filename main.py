import sys

import pygame
import random
from entity.objects import Werewolf, Model, Area, Robber


# --- Настройки ---
def get_area_structure(area):
    structure = {}
    for i in range(16):
        structure[(80 * i, 0)] = area.models[1].image
        structure[(80 * i, 640)] = area.models[1].image
    for i in range(1, 8):
        for j in range(16):
            structure[(80 * j, 80 * i)] = area.models[0].image
    return structure


def get_wall_structure():
    wall_model = Model(pygame.image.load("source/bg-brick-3.png")).image
    main_wall_model = Model(pygame.image.load("source/bg-brick-2.png")).image
    wall = {
        (4 * 80, 1 * 80): wall_model,
        (4 * 80, 2 * 80): wall_model,
        (4 * 80, 5 * 80): wall_model,
        (4 * 80, 6 * 80): wall_model,
        (4 * 80, 7 * 80): wall_model,
        (8 * 80, 3 * 80): wall_model,
        (8 * 80, 4 * 80): wall_model,
        (11 * 80, 5 * 80): wall_model,
        (11 * 80, 6 * 80): wall_model,
        (11 * 80, 7 * 80): wall_model,
        (12 * 80, 1 * 80): wall_model,
        (12 * 80, 2 * 80): wall_model,
        (0, 0): main_wall_model,
        (1 * 80, 0): main_wall_model,
        (2 * 80, 0): main_wall_model,
        (3 * 80, 0): main_wall_model,
        (4 * 80, 0): main_wall_model,
        (5 * 80, 0): main_wall_model,
        (6 * 80, 0): main_wall_model,
        (7 * 80, 0): main_wall_model,
        (8 * 80, 0): main_wall_model,
        (9 * 80, 0): main_wall_model,
        (10 * 80, 0): main_wall_model,
        (11 * 80, 0): main_wall_model,
        (12 * 80, 0): main_wall_model,
        (13 * 80, 0): main_wall_model,
        (14 * 80, 0): main_wall_model,
        (15 * 80, 0): main_wall_model,
        (16 * 80, 0): main_wall_model,
        (0, 8 * 80): main_wall_model,
        (1 * 80, 8 * 80): main_wall_model,
        (2 * 80, 8 * 80): main_wall_model,
        (3 * 80, 8 * 80): main_wall_model,
        (4 * 80, 8 * 80): main_wall_model,
        (5 * 80, 8 * 80): main_wall_model,
        (6 * 80, 8 * 80): main_wall_model,
        (7 * 80, 8 * 80): main_wall_model,
        (8 * 80, 8 * 80): main_wall_model,
        (9 * 80, 8 * 80): main_wall_model,
        (10 * 80, 8 * 80): main_wall_model,
        (11 * 80, 8 * 80): main_wall_model,
        (12 * 80, 8 * 80): main_wall_model,
        (13 * 80, 8 * 80): main_wall_model,
        (14 * 80, 8 * 80): main_wall_model,
        (15 * 80, 8 * 80): main_wall_model,
        (16 * 80, 8 * 80): main_wall_model
    }

    return wall


def draw_area(structure, display):
    for cords in structure:
        display.blit(structure[cords], cords)

def spaven_enemy():
    randomEnemy = random.randint(4, 7)
    enemies = []
    for i in range(randomEnemy):
        x = random.randint()
        y = random.randint()

WIDTH, HEIGHT = 1280, 720
FPS = 60

# --- Инициализация ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Soul Knight")
clock = pygame.time.Clock()

running = True

player = Werewolf(
    10,
    None,
    [
        Model(pygame.image.load("source/character/wolf1.png")),
        Model(pygame.image.load("source/character/wolf2.png")),
        Model(pygame.image.load("source/character/wolf3.png")),
        Model(pygame.image.load("source/character/wolf4.png")),
        Model(pygame.image.load("source/character/wolf5.png"))
    ],
    6 * 80,
    4 * 80 + 40
)

enemy = Robber(
    5,
    None,
    [
        Model(pygame.image.load("source/character/wolf1.png")),
        Model(pygame.image.load("source/character/wolf2.png")),
        Model(pygame.image.load("source/character/wolf3.png")),
        Model(pygame.image.load("source/character/wolf4.png")),
        Model(pygame.image.load("source/character/wolf5.png"))
    ],
    80,
    4 * 80
)

# --- Состояние клавиш ---
keys = {
    "w": False,
    "a": False,
    "s": False,
    "d": False
}

direction = {
    "w": "up",
    "a": "left",
    "s": "down",
    "d": "right"
}

area = Area(
    0,
    0,
    [
        Model(pygame.image.load("source/bg-brick-1.png")),
        Model(pygame.image.load("source/bg-brick-2.png"))
    ]
)
map = get_area_structure(area)
wall = get_wall_structure()
# --- Основной цикл ---
while running:
    dt = clock.tick(FPS) / 1000  # delta time (секунды)

    # --- Обработка событий ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # --- Клавиатура ---
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                keys["w"] = True
            if event.key == pygame.K_a:
                keys["a"] = True
            if event.key == pygame.K_s:
                keys["s"] = True
            if event.key == pygame.K_d:
                keys["d"] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys["w"] = False
            if event.key == pygame.K_a:
                keys["a"] = False
            if event.key == pygame.K_s:
                keys["s"] = False
            if event.key == pygame.K_d:
                keys["d"] = False

        # --- Мышь ---
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            mouse_button = event.button

            print(f"Mouse click at {mouse_pos}, button {mouse_button}")

    active_directions = []
    for active_button in keys:
        if keys[active_button]:
            active_directions.append(direction.get(active_button))
    player.move(active_directions, wall)
    enemy.move_to_player(player.get_cords(), wall)
    screen.fill((255, 255, 255))
    draw_area(map, screen)
    draw_area(wall, screen)
    screen.blit(player.get_active_model().image, player.get_cords())
    screen.blit(enemy.get_active_model().image, enemy.get_cords())
    pygame.display.flip()

# --- Завершение ---
pygame.quit()
sys.exit()
