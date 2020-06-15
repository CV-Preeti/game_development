import pygame,sys
from pygame.locals import*
import time
import random
import os



white=(255,255,255)
black=(100,0,0)
red=(255,0,0)




pygame.init()
window=pygame.display.set_mode((1000,600))
pygame.display.set_caption('the ping pong game')
screen=pygame.display.get_surface()
bgimg = pygame.image.load(os.path.join("images" ,"brick-wall.jpg"))
bgimg = pygame.transform.scale(bgimg, (1000, 600)).convert_alpha()
Font = pygame.font.SysFont(None,25,bold=True)



clock=pygame.time.Clock()
FPS=5
def showscore(scorevalue,high_score):
    score=Font.render("Score :" + str(scorevalue) +"  Highscore: "+str(high_score),True,(232,56,87))
    screen.blit(score,(500,300))

def messagetoscreen(msg,color,x,y):
    screen_text=Font.render(msg,True,color)
    screen.blit(screen_text,(x,y))
def welcome():
    gameexit = False
    while not gameexit:
        pygame.mixer.music.load(os.path.join("images","058. Inspirational Pop - AShamaluevMusic.mp3"))
        pygame.mixer.music.play()
        screen.fill((233,210,229))
        messagetoscreen("Welcome to Ping Pong Game", black, 260, 250)
        messagetoscreen("Press Space Bar To Play", black, 242, 270)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameexit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    
                    gameloop()


        pygame.display.update()
        clock.tick(60)


    

def gameloop():
    rect_x=500
    rect_y=580
    changeofpixel_x=10
    changeofpixel_y=10
    gameexit=False
    scorevalue=0
    ball_x=round(random.randrange(10,960-20))
    count=0
    ball_y=round(random.randrange(10,560-20))
    ball_speed_x=5
    ball_speed_y=5 
    i=1
    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt", "w") as f:
            f.write("0")

    with open("highscore.txt", "r") as f:
         high_score = f.read()
    while not gameexit:

        
        if ball_x >1000:
            ball_x=980
        if ball_y>600:
            ball_y=580
        if ball_x <0:
            ball_x=0
        if ball_y<0:
            ball_y=0
        
                    
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameexit=True
                pygame.mixer.music.stop()
                with open("highscore.txt", "w") as f:
                    f.write(str(high_score))
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.mixer.music.stop()
                    pygame.quit()
                    with open("highscore.txt", "w") as f:
                        f.write(str(high_score))
                leftArrow=event.key==pygame.K_LEFT
                rightArrow=event.key==pygame.K_RIGHT
               
                if leftArrow:
                    rect_x -= 30
                    print("leftarrow")
                elif rightArrow:
                    rect_x +=30
                    print("righttarrow")
                
     
        
        
    
        screen.fill(white)
        screen.blit(bgimg,(0,0))
        pygame.draw.rect(screen,(255,0,0),(ball_x,ball_y,20,20))
        showscore(scorevalue,high_score)
        
        pygame.draw.rect(screen,black,(rect_x,rect_y,100,20))
        pygame.display.update()
        ball_x=ball_x + ball_speed_x 
        ball_y=ball_y + ball_speed_y 
        print([int(ball_x),int(ball_y)])
        
          
        if ball_x >=rect_x and ball_x <=rect_x + 100:
            if ball_y >= 560:
                
                count=count+1
                scorevalue= count*count
                if scorevalue >int((high_score)):
                    high_score = scorevalue
                if ball_speed_x >0:
                    ball_speed_x=changeofpixel_x + 2*i
                    ball_speed_y= - (changeofpixel_y + 2*i)
                    i=i+1
                else:
                    ball_speed_x = -(changeofpixel_x + 2*i)
                    ball_speed_y= -(changeofpixel_y + 2*i)
                    i=i+1
                

        if ball_x >=980 :
            
            
            if ball_speed_y>0:
                ball_speed_x=-(changeofpixel_x+2*i)
                ball_speed_y = changeofpixel_y + 2*i
                i=i+1
            else:
                ball_speed_x = -(changeofpixel_x + 2*i)
                ball_speed_y= -(changeofpixel_y + 2*i)
                i=i+1
        if ball_y<=0 :
            
            
            if ball_speed_x>0:
                ball_speed_x=changeofpixel_x +2*i
                ball_speed_y= changeofpixel_y+ 2 *i
                i=i+1
            else:
                ball_speed_x= -(changeofpixel_x + 2*i)
                ball_speed_y = changeofpixel_y + 2*i
                i=i+1
        if ball_x <=0:
            
            
            if ball_speed_y >0:
                ball_speed_x= (changeofpixel_x + 2*i)
                ball_speed_y= changeofpixel_y + 2*i
                i=i+1
            else:
                ball_speed_x= changeofpixel_x + 2*i
                ball_speed_y= -(changeofpixel_y + 2*i)
                i=i+1

        if  ball_y >=580:
           
            
            if ball_speed_x >0:
                ball_speed_x=changeofpixel_x + 2*i
                ball_speed_y= - (changeofpixel_y + 2*i)
                i=i+1
            else:
                ball_speed_x = -(changeofpixel_x + 2*i)
                ball_speed_y= -(changeofpixel_y + 2*i)
                i=i+1 
        
        
        pygame.display.update()        
        clock.tick(FPS)   

        
        

    pygame.quit()
    quit()
welcome()


   
   
   
   
   
   
   
   
   





    
