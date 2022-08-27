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

# definições da tela
width = 640
height = 480

# posição da cobra
snake_x = width / 2
snake_y = height / 2

# posição da maçãn
apple_x = randint(40, 600)
apple_y = randint(50, 430)

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

#dificuldade
speed = 10

#corpo da cobra
body_snake = []
snake_length = 10

#definições de controle
direction_x = 20
direction_y = 0

tools.songs()

gamer_over = False

#loop principal
while True:

    #velocidade do jogo
    fps.tick(speed)

    #mensagem de pontuação
    message = f'Pontos: {score}'

    #mensagem de volume
    message_volume = 'Volume: ' + ' | ' * counter_volume + f'{counter_volume}0'

    #mensagem de gamer_over
    message_gamer_over = f'Gamer Over! Pontuação {score} Presione a Tecla R para jogar Novamente'


    #formatando mensagem
    text_score = font.render(message, True, (0, 0, 0))
    text_volume = font.render(message_volume, True, (0, 0, 0))
    text_gamer_over = font.render(message_gamer_over, True, (255, 0, 0))
    ret_text = text_gamer_over.get_rect()

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
        tools.songs(sound)
    if pygame.key.get_pressed()[K_KP_MINUS]:
        if counter_volume > 0:
            counter_volume -= 1
            sound -= 0.10
        if counter_volume == 0:
            sound -= 0
        tools.songs(sound)

    # posição da cobra
    snake = pygame.draw.rect(display, (0, 255, 0), (snake_x, snake_y, 20, 20))

    # posição da maçan
    apple = pygame.draw.rect(display, (255, 0, 0), (apple_x, apple_y, 20, 20))

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

    #lista da posição atual head
    head_snake = []
    head_snake.append(snake_x)
    head_snake.append(snake_y)

    # lista do corpo da cobra evolução
    body_snake.append(head_snake)

    if body_snake.count(head_snake) > 1:
        tools.songs(sound=sound, music=song_gamer_over)
        gamer_over = True
        while gamer_over:
            display.fill((255, 255, 255))
            ret_text.center = (width // 2, height // 2)
            display.blit(text_gamer_over, ret_text)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
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
                        gamer_over = False
                        tools.songs(sound=sound, music=default)
            pygame.display.update()

    #limima o tamanho da cobra
    if len(body_snake) > snake_length:
        del body_snake[0]

    tools.snake_evolution(body_snake, display)

    #render da message
    display.blit(text_score, (10, 10))
    display.blit(text_volume, (10, 25))

    # atualização da tela
    pygame.display.update()
