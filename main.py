#import das bibliotecas
import pygame
import tools
from pygame.locals import *
from sys import exit
from random import randint

#inicio do pygame
pygame.init()

#default volume
sound = 0.50
counter_volume = 5

# som da cobra comendo
music_eat = pygame.mixer.Sound('settings/music/eat.wav')

# songs
default = 'settings/music/default.mp3'
song_tension = 'settings/music/tension.mp3'
song_gamer_over = 'settings/music/game_over.wav'
sleep_songs = 0
stop_songs = 0
up = False

# definições da tela
width = 640
height = 480

# posição da cobra
snake_x = width / 2
snake_y = height / 2

# posição da maçãn x 600, 20 y 430, 120
apple_x = randint(20, 600)
apple_y = randint(120, 430)


# definição de font
font = pygame.font.SysFont('arial', 16, True, False)

#definição da pontuação
score = 0

# setando as configurações da tela
display = pygame.display.set_mode((width, height))

#nome da janela
pygame.display.set_caption('Snake Game')

# taxa de frames
fps = pygame.time.Clock()
clock = 0
time = 0

#dificuldade
speed = 10
level1 = 2

#corpo da cobra
body_snake = []
snake_length = 10

#definições de controle
direction_x = 20
direction_y = 0

tools.start_songs(default)

gamer_over = False

# definiçoes de tempo de tela
sleep_volume = 0
stop_volume = 0
volume_display = False

#loop principal
while True:

    #velocidade do jogo
    fps.tick(20)
    clock += 1

    #mensagem de pontuação
    message = f'Pontos: {score}'

    #mensagem de volume
    message_volume = 'Volume: ' + ' | ' * counter_volume + f'{counter_volume}0'

    #mensagem de gamer_over
    message_gamer_over = 'Gamer Over!'
    message_maca = f'{score} Maças coletadas'


    #mensagem do relogio
    message_clock = f'Time: {clock / 60:.0f} : {clock % 60:.0f}'

    #restart
    message_restart = 'Aperte R para reiniciar o jogo'


    #formatando mensagem
    text_score = font.render(message, True, (0, 0, 0))
    text_volume = font.render(message_volume, True, (0, 0, 0))
    text_gamer_over = font.render(message_gamer_over, True, (255, 0, 0))
    text_clock = font.render(message_clock, True, (0, 0, 0))
    text_maca = font.render(message_maca, True, (0, 255, 0))

    text_restart = font.render(message_restart, True, (255, 0, 0))

    #prencimento de tela na cor preta
    display.fill((255, 255, 255))

    #loop que monitora o evento de fechamento da janela
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()


    # comandos
    if event.type == pygame.KEYDOWN:
        if event.key == K_LEFT:
            if direction_x == speed:
                pass
            else:
                direction_x = -speed
                direction_y = 0
        if event.key == K_RIGHT:
            if direction_x == -speed:
                pass
            else:
                direction_x = speed
                direction_y = 0
        if event.key == K_UP:
            if direction_y == speed:
                pass
            else:
                direction_x = 0
                direction_y = -speed
        if event.key == K_DOWN:
            if direction_y == -speed:
                pass
            else:
                direction_x = 0
                direction_y = speed

    snake_x = snake_x + direction_x
    snake_y = snake_y + direction_y

    #teclas de volume
    if pygame.key.get_pressed()[K_KP_PLUS]:
        if counter_volume < 10:
            counter_volume += 1
            sound += 0.10
        if counter_volume == 10:
            sound = 1
        tools.songs_volume(sound)
        volume_display = True
    if pygame.key.get_pressed()[K_KP_MINUS]:
        if counter_volume > 0:
            counter_volume -= 1
            sound -= 0.10
        if counter_volume == 0:
            sound -= 0
        tools.songs_volume(sound)
        volume_display = True

    # posição da cobra
    snake = pygame.draw.rect(display, (0, 255, 0), (snake_x, snake_y, 20, 20))

    # posição da maçan
    apple = pygame.draw.rect(display, (255, 0, 0), (apple_x, apple_y, 20, 20))


# paredes
    line_right = pygame.draw.rect(display, (0, 0, 0,), (630, 60, 5, 410))
    line_lift = pygame.draw.rect(display, (0, 0, 0,), (5, 60, 5, 410))
    line_top = pygame.draw.rect(display, (0, 0, 0), (5, 60, 630, 5))
    line_floor = pygame.draw.rect(display, (0, 0, 0), (5, 470, 630, 5))

    # verificador de colizão
    if snake.colliderect(apple):

        # redefinição da posição da maçan
        apple_x = randint(40, 600)
        apple_y = randint(50, 430)

        #adicionando pontuação
        score += 1

        #play no music_eat
        music_eat.play()

        #almentando o tamanho da cobra
        snake_length += 1
        up = True

    #lista da posição atual head
    head_snake = []
    head_snake.append(snake_x)
    head_snake.append(snake_y)

    # lista do corpo da cobra evolução
    body_snake.append(head_snake)

# condição de derrota
    if body_snake.count(head_snake) > 1 or snake.colliderect(line_top) or snake.colliderect(line_lift) or snake.colliderect(line_right) or snake.colliderect(line_floor):
        tools.start_songs(song_gamer_over)
        gamer_over = True
        time = clock
        message_life = f'Tempo de Vida {time / 60:.0f} : {time % 60:.0f}'
        text_life = font.render(message_life, True, (0, 0, 0))
        while gamer_over:
            display.fill((255, 255, 255))
            display.blit(text_gamer_over, (270, 130))
            display.blit(text_maca, (250, 170))
            display.blit(text_life, (240, 200))
            display.blit(text_restart, (220, 250))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

                # reset do jogo
                if event.type == pygame.KEYDOWN:
                    if event.key == K_r:
                        score = 0
                        snake_length = 10
                        snake_x = width / 2
                        snake_y = height / 2
                        head_snake = []
                        body_snake = []
                        apple_x = randint(40, 600)
                        apple_y = randint(50, 430)
                        clock = 0
                        gamer_over = False
                        tools.start_songs(default)
            pygame.display.update()

    #limima o tamanho da cobra
    if len(body_snake) > snake_length:
        del body_snake[0]

    # evolução da cobra
    tools.snake_evolution(body_snake, display)

    #render da message
    display.blit(text_score, (10, 10))
    display.blit(text_clock, (10, 25))

    # cliar volume na tela
    if volume_display:
        display.blit(text_volume, (10, 40))
        if sleep_volume == 0:
            sleep_volume = clock
        stop_volume = sleep_volume + 10

    # apagar volume da tela
    if clock == stop_volume:
        tools.clear(text_volume)
        sleep_volume = 0
        volume_display = False

    #up dificuldade
    if up:
        if score == 25:
            speed += 2
            up = False
        if score == 50:
            speed += 3
            up = False
        if score == 75:
            speed += 4
            up = False


    # atualização da tela
    pygame.display.update()
