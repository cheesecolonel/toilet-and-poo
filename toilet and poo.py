import pygame,random
pygame.init()
window_width,window_height=950,400
displayscreen=pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("toilet and poo")


#set fps
FPS=60
clock=pygame.time.Clock()

#values
player_starting_lives=5
player_velocity=10
coin_starting_velocity=7
coin_add_speed=0.5 #錢幣加速度
buffer_distance=100
score=0
lives=player_starting_lives
coin_velocity=coin_starting_velocity

GREEN=(255,255,255)
DARKGREEN=(0,0,0)
WHITE=(255,255,255)
BLACK=(0,0,0)

font=pygame.font.Font("AttackGraffiti.ttf",32)

score_text=font.render("poo: "+str(score),True,GREEN)
score_text_rect=score_text.get_rect()
score_text_rect.topleft=(10,10)

title_text=font.render("TOILET and POO",True,GREEN)
title_text_rect=title_text.get_rect()
title_text_rect.centerx=window_width//2
title_text_rect.y=10

lives_text=font.render("lives:  "+str(lives),True,GREEN)
lives_text_rect=score_text.get_rect()
lives_text_rect.topright=(window_width-10,10)

gameover_text=font.render("GAMEOVER",True,GREEN)
gameover_text_rect=gameover_text.get_rect()
gameover_text_rect.center=(window_width//2,window_height//2)

continue_text=font.render("press any key to play again",True,GREEN)
continue_text_rect=continue_text.get_rect()
continue_text_rect.center=(window_width//2,window_height//2+32)

coin_sound=pygame.mixer.Sound("fart.mp3")
miss_sound=pygame.mixer.Sound("miss.wav")
miss_sound.set_volume(0.1)
miss_sound.set_volume(0.8)
pygame.mixer.music.load("bgm.mp3")

player_image=pygame.image.load("toilet.png")
player_rect=player_image.get_rect()
player_rect.left=32
player_rect.centery=window_height//2

coin_image=pygame.image.load("poo.png")
coin_rect=player_image.get_rect()
coin_rect.x=window_width+buffer_distance
coin_rect.y=random.randint(64,window_height-32)

pygame.mixer.music.play(-1,0.0)


running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    #key move
    keys=pygame.key.get_pressed()
    if (keys[pygame.K_UP] or keys[pygame.K_w])and player_rect.top>64:
        player_rect.y -=player_velocity
    if (keys[pygame.K_DOWN] or keys[pygame.K_s])and player_rect.bottom<window_height:
        player_rect.y +=player_velocity
    #coin move
    if coin_rect.x<0:
        lives-=1
        miss_sound.play()
        coin_rect.x=window_width+buffer_distance
        coin_rect.y=random.randint(64,window_height-32)
    else:
        coin_rect.x-=coin_velocity

    #check collision
    if player_rect.colliderect(coin_rect):
        score+=1
        coin_sound.play()
        coin_velocity+=coin_add_speed
        coin_rect.x=window_width+buffer_distance
        coin_rect.y=random.randint(64,window_height-32)

    #update text
    score_text=font.render("poo: "+str(score),True,GREEN,DARKGREEN)
    lives_text=font.render("Lives: "+str(lives),True,GREEN,DARKGREEN)
    #gameover
    if lives==0:
        displayscreen.blit(gameover_text,gameover_text_rect)
        displayscreen.blit(continue_text,continue_text_rect)
        pygame.display.update()
        pygame.mixer.music.stop()

        is_paused=True
        while is_paused:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    is_paused=False
                    running=False
                if event.type==pygame.KEYDOWN:
                    score=0
                    lives=player_starting_lives
                    coin_velocity=coin_starting_velocity
                    pygame.mixer.music.play(-1,0.0)
                    is_paused=False

    displayscreen.fill(BLACK)
    displayscreen.blit(score_text,score_text_rect)
    displayscreen.blit(title_text,title_text_rect)
    displayscreen.blit(lives_text,lives_text_rect)
    pygame.draw.line(displayscreen,WHITE,(0,64),(window_width,64),3)
    
    displayscreen.blit(player_image,player_rect)
    displayscreen.blit(coin_image,coin_rect)

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
