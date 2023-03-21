import pygame

# Initialization of the Game
pygame.init()
width = 1100
height = 600
screen = pygame.display.set_mode((width, height)) # Width by Height

# Player Stuff
player_img = pygame.image.load('stick.png')
player_X = 10
player_Y_default = height/2 - 100
player_Y_dif = 0

# Ball Stuff
ball_img = pygame.image.load('ball.png')
ball_X = width/2 - 15
ball_Y = height/2 - 15
ball_dir_X = -3
ball_dir_Y = 3

# Player2 Stuff
player2_img = pygame.image.load('stick.png')
player2_X = width-10-27
player2_Y_default = height/2 - 100
player2_Y_dif = 0

def player(y_val):
    screen.blit(player_img, (player_X, y_val))
    
def player2(y_val):
    screen.blit(player2_img, (player2_X, y_val))

def ball():
    screen.blit(ball_img, (ball_X, ball_Y))


def game_over(win):
    global ball_dir_X
    global ball_dir_Y
    global ball_X
    global ball_Y
    print(win)
    ball_X = width/2 - 15
    ball_Y = height/2 - 15
    ball_dir_X = -1
    ball_dir_Y = 1

def calc_ball():
    global ball_dir_X
    global ball_dir_Y
    global ball_X
    global ball_Y
    if ball_Y == 10:
        ball_dir_Y *= -1
    elif ball_Y == height-10-30:
        ball_dir_Y *= -1
    if ball_X <= 37 and ball_Y >= player_Y_default+player_Y_dif-30 and ball_Y <= player_Y_default+player_Y_dif+200 and ball_dir_X < 0:
        ball_dir_X *= -1
    if ball_X >= 1000 and ball_Y >= player2_Y_default+player2_Y_dif-11 and ball_Y <= player2_Y_default+player2_Y_dif+200-19 and ball_dir_X > 0:
        ball_dir_X *= -1
    
    
    ball_X+=ball_dir_X
    ball_Y+=ball_dir_Y
    if (ball_X < 30):
        game_over(False)
    elif (ball_X > player2_X+30):
        game_over(True)
    ball_Y = min(ball_Y, height-10-30)
    ball_Y = max(ball_Y, 10)

def move_up(y_val):
    global player_Y_dif
    if player_Y_dif-y_val >= -player_Y_default+10:
        player_Y_dif -= y_val

def move_down(y_val):
    global player_Y_dif
    if player_Y_dif+y_val <= player_Y_default-10:
        player_Y_dif += y_val

def move_up2(y_val):
    global player2_Y_dif
    if player2_Y_dif-y_val >= -player2_Y_default+10:
        player2_Y_dif -= y_val

def move_down2(y_val):
    global player2_Y_dif
    if player2_Y_dif+y_val <= player2_Y_default-10:
        player2_Y_dif += y_val


game_on = True

while game_on:
    screen.fill((255,225,226))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_on=False
    
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_w]:
        move_up(4)
    elif key_input[pygame.K_s]:
        move_down(4)
    elif key_input[pygame.K_UP]:
        move_up2(4)
    elif key_input[pygame.K_DOWN]:
        move_down2(4)
    
    if key_input[pygame.K_5]:
        game_on=False
    player(player_Y_default+player_Y_dif)
    player2(player2_Y_default+player2_Y_dif)
    calc_ball()
    ball()
    pygame.display.update()