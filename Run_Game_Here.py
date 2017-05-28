#J Preston Harvey jph8rw
#George Wilson gaw8cf

import pygame
import gamebox
import random

state = 'intro'
counter = 0
timer = 0
timer2 = 0
camera = gamebox.Camera(600,800)

walls = []
powerup_speed = []
powerup_clear = []
powerup_wrap = []
coins1 = []
coins2 = []
coins3 = []
coins4 = []

powerup_bomb = []
points = 0
wall_left = gamebox.from_color(0,400,'cyan',15,800)
wall_right = gamebox.from_color(600,400,'cyan',15,800)
colors = ['green','cyan','yellow','magenta','orange','blue1','chartreuse1','deeppink1']
sheet = gamebox.load_sprite_sheet('http://www.williammalone.com/articles/create-html5-canvas-javascript-sprite-animation/images/coin-sprite-animation-sprite-sheet.png',1,10)
#sheet = gamebox.load_sprite_sheet('ball_sprite.png',8,12)
frame = 0
ball = gamebox.from_color(300,100,'red',21,21)
highscore = 0
game_sound = gamebox.load_sound("arcade_music.wav")
coin_sound = gamebox.load_sound('coin_sound.wav')
bomb_sound = gamebox.load_sound('bomb_sound.wav')
splat_sound = gamebox.load_sound('splat_sound.wav')
speed_sound = gamebox.load_sound('speed_sound.wav')
wrap_sound = gamebox.load_sound('paddle.wav')
end_game_timer = 0


def tick(keys):
    global state
    global counter
    global timer
    global timer2
    global walls
    global powerup_speed
    global powerup_clear
    global powerup_wrap
    global powerup_bomb
    global colors
    global coins1
    global coins2
    global coins3
    global coins4
    global points
    global frame
    global highscore
    global end_game_timer
    global sheet

    if state == "intro":
        screen = gamebox.from_text(300,100,"Welcome to falldown", "arial", 30, "gold")
        screen2 = gamebox.from_text(300,200,"Press SPACE to start", "arial", 30, "purple")
        camera.clear("black")
        camera.draw(screen)
        camera.draw(screen2)
        camera.display()
        if pygame.K_SPACE in keys:
            points = 0
            state = 'game'

    if state == 'game':
        end_game_timer = 0
        global walls
        global wall
        camera.clear('black')
        counter += 1
        timer -= 1
        timer2 -= 1
        frame += 1
        if frame == 10:
            frame = 0
        if counter >= 60 and ball.yspeed <= 45:
            ball.yspeed += 1
            ball.y = ball.y + ball.yspeed

        camera.draw(gamebox.from_text(50,20,'Points: '+str(points),'arial', 30,'purple'))
        camera.draw(gamebox.from_text(190,20,'High Score: '+str(highscore),'arial',30,'purple'))

        if pygame.K_RIGHT in keys and timer <= 0:
            ball.x += 15
        if pygame.K_LEFT in keys and timer <= 0:
            ball.x -= 15
        if pygame.K_RIGHT in keys and timer >= 0:
            ball.x += 30
        if pygame.K_LEFT in keys and timer >= 0:
            ball.x -= 30



        if counter % 15 == 0:
            choose = random.randint(1,4)
            choose2 = random.randint(1,10)

            if choose == 1:
                color = colors[random.randint(0,len(colors)-1)]
                xval = random.randint(200,400)
                new_wall = gamebox.from_color(xval, 1000,color, 150,15)
                new_wall2 = gamebox.from_color(xval-250, 1000,color, 150,15)
                new_wall3 = gamebox.from_color(xval+250, 1000,color, 150,15)
                walls.append(new_wall)
                walls.append(new_wall2)
                walls.append(new_wall3)
            if choose == 2:
                color = colors[random.randint(0,len(colors)-1)]
                xval = random.randint(200,400)
                new_wall = gamebox.from_color(xval, 1000,color, 250,15)
                new_wall2 = gamebox.from_color(xval-300, 1000,color, 150,15)
                new_wall3 = gamebox.from_color(xval+280, 1000,color, 150,15)
                walls.append(new_wall)
                walls.append(new_wall2)
                walls.append(new_wall3)
            if choose == 3:
                color = colors[random.randint(0,len(colors)-1)]
                xval = random.randint(200,400)
                new_wall = gamebox.from_color(xval, 1000,color, 300,15)
                new_wall2 = gamebox.from_color(xval-275, 1000,color, 75,15)
                new_wall3 = gamebox.from_color(xval+250, 1000,color, 150,15)
                walls.append(new_wall)
                walls.append(new_wall2)
                walls.append(new_wall3)
            if choose == 4:
                color = colors[random.randint(0,len(colors)-1)]
                xval = random.randint(100,400)
                new_wall = gamebox.from_color(xval, 1000,color, 150,15)
                new_wall2 = gamebox.from_color(xval-200, 1000,color, 75,15)
                new_wall3 = gamebox.from_color(xval+300, 1000,color, 75,15)
                new_wall4 = gamebox.from_color(xval+400, 1000,color, 100,15)
                new_wall5 = gamebox.from_color(xval-300, 1000,color, 150,15)
                walls.append(new_wall)
                walls.append(new_wall2)
                walls.append(new_wall3)
                walls.append(new_wall4)
                walls.append(new_wall5)
            if choose2 == 1:
                xval = random.randint(150,450)
                speed = gamebox.from_color(xval,980,'white', 20,20 )
                powerup_speed.append(speed)
            if choose2 == 2:
                xval = random.randint(150,450)
                clear = gamebox.from_color(xval,980, 'orange', 20, 20)
                powerup_clear.append(clear)
            if choose2 == 3:
                xval = random.randint(150,450)
                wrap = gamebox.from_color(xval,980, 'cyan', 20,20)
                powerup_wrap.append(wrap)
            if choose2 == 4:
                xval = random.randint(150,450)
                bomb = gamebox.from_color(xval,980,'brown',20,20)
                powerup_bomb.append(bomb)
        for wall in walls:
            wall.y -= 13
            if ball.touches(wall):
                ball.y = wall.y-13
                ball.yspeed = wall.yspeed
            camera.draw(wall)

        for speed in powerup_speed:
            speed.y -= 13

            camera.draw(speed)
            if ball.touches(speed):
                speed_sound.play()
                powerup_speed = []
                powerup_clear = []
                powerup_wrap = []
                powerup_bomb = []
                timer = 90

        for clear in powerup_clear:
            clear.y -= 13
            camera.draw(clear)
            if ball.touches(clear):
                speed_sound.play()
                walls = []
                powerup_clear = []
                powerup_speed = []
                powerup_wrap = []
                powerup_bomb = []


        for wrap in powerup_wrap:
            wrap.y -= 13
            for wall in walls:
                if (wall.y - wrap.y) <= 10 and (wall.y - wrap.y) >= 0:
                    wrap.y = wall.y - 30
            camera.draw(wrap)
            if ball.touches(wrap):
                wrap_sound.play()
                timer2 = 90
                powerup_clear = []
                powerup_speed = []
                powerup_wrap = []
                powerup_bomb = []

        for bomb in powerup_bomb:
            bomb.y -= 13
            for wall in walls:
                if (wall.y - bomb.y) <= 10 and (wall.y - bomb.y) >= 0:
                    bomb.y = wall.y - 30
            camera.draw(bomb)
            if ball.touches(bomb):
                if points > 5:
                    bomb_sound.play()
                    points -= 5

                else:
                    points = points
                powerup_bomb = []
                powerup_speed = []
                powerup_wrap = []
                powerup_clear = []

        if counter % 60 == 0 or counter == 4:
            xval1 = random.randint(50,550)
            xval2 = random.randint(50,550)
            xval3 = random.randint(50,550)
            xval4 = random.randint(50,550)
            coin1 = gamebox.from_image(xval1,975,sheet[frame])
            coins1.append(coin1)
            coin2 = gamebox.from_image(xval2,1950,sheet[frame])
            coins2.append(coin2)
            coin3 = gamebox.from_image(xval3,1360,sheet[frame])
            coins3.append(coin3)
            coin4 = gamebox.from_image(xval4,1660,sheet[frame])
            coins4.append(coin4)
        for coin in coins1:
            coin.x = coin.x
            coin.y -= 13
            coin = gamebox.from_image(coin.x,coin.y,sheet[frame])
            camera.draw(coin)
            if ball.touches(coin):
                coin_sound.play()
                points += 1
                coins1 = []
        for coin in coins2:
            coin.x = coin.x
            coin.y -= 13
            coin = gamebox.from_image(coin.x,coin.y,sheet[frame])
            camera.draw(coin)
            if ball.touches(coin):
                coin_sound.play()
                points += 1
                coins2 = []
        for coin in coins3:
            coin.x = coin.x
            coin.y -= 13
            coin = gamebox.from_image(coin.x,coin.y,sheet[frame])
            camera.draw(coin)
            if ball.touches(coin):
                coin_sound.play()
                points += 1
                coins3 = []
        for coin in coins4:
            coin.x = coin.x
            coin.y -= 13
            coin = gamebox.from_image(coin.x,coin.y,sheet[frame])
            camera.draw(coin)
            if ball.touches(coin):
                coin_sound.play()
                points += 1
                coins4 = []




        if timer2 >= 0:
            camera.draw(wall_left)
            camera.draw(wall_right)
            if ball.touches(wall_left):
                ball.x = 580
            if ball.touches(wall_right):
                ball.x = 20
        if timer2 <= 0:
            if ball.x >= 600:
                ball.x = 600
            if ball.x <= 0:
                ball.x = 0
        if int(points) >= int(highscore):
            highscore = points
        if pygame.K_b in keys:
            timer2 = 60

        camera.draw(ball)
        camera.display()
        if ball.y >= 790:
            ball.y = 790
            ball.yspeed = 0
        if ball.y <= 0:
            state = 'end'
        if counter == 1:
            game_sound.play()
        if counter % 450 == 0:
            game_sound.play()

    if state == 'end':
        camera.clear('white')
        game_sound.stop()
        if end_game_timer == 0:
            splat_sound.play()
        end_game_timer += 1
        if end_game_timer >= 40:
            splat_sound.stop()
        camera.draw(gamebox.from_text(300,350,"Press SPACE to play again","arial", 40, "gold"))
        camera.draw(gamebox.from_text(300,300,"You scored "+str(points)+" points","arial", 40, "red"))
        camera.draw(gamebox.from_text(80,20,'High Score: '+str(highscore),'arial',30,'purple'))
        camera.display()
        if pygame.K_SPACE in keys:
            walls = []
            timer = 0
            timer2 = 0
            powerup_wrap = []
            powerup_clear = []
            powerup_speed = []
            powerup_bomb = []
            ball.y = 100
            points = 0
            coins1 = []
            coins2 = []
            coins3 = []
            coins4 = []
            state = 'game'
            counter = 0


ticks_per_second = 30

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)