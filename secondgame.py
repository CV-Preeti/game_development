import pygame,sys
import time
import random
pygame.mixer.init()
pygame.init()
white=(255,255,255)
black=(100,0,0)
red=(255,0,0)

window=pygame.display.set_mode((1000,600))
pygame.display.set_caption('snake game')
Font = pygame.font.SysFont(None,25,bold=True)
screen=pygame.display.get_surface()
screen.fill(white)


clock=pygame.time.Clock()
FPS=5
blocksize=20
nopixel=0
def levelmsg():
    msg=Font.render("level-2" ,True,(100,0,0))
    screen.blit(msg,(500,10))
def showscore(score_value):
    score=Font.render("Score :" + str(score_value),True,(232,56,87))
    screen.blit(score,(10,10))


def snake( blocksize,snakelist):
    for size in snakelist:
        pygame.draw.rect(screen,black,(size[0],size[1],blocksize,20))

def messagetoscreen(msg,color):
    screen_text=Font.render(msg,True,color)
    screen.blit(screen_text,(500,300))

def gameloop():
    gameover=False
    gameexit=False
    lead_x=500
    lead_y=300
    change_pixel_of_x=0
    change_pixel_of_y=0
    snakelist=[]
    snakelength=1
    score_value=0
    randomApplex=round(random.randrange(10,800-blocksize))
    randomAppley= round(random.randrange(10,400-blocksize))

    while not gameexit:
        
        while gameover==True:
            screen.fill(white)
            messagetoscreen('Game Over,press c to continue',black)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    gameover=False
                    gameexit=True
                    
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_c:
                        gameloop()
                    if event.key==pygame.K_q:
                        gameexit=True
                        gameover=False
                    
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameexit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                leftArrow=event.key==pygame.K_LEFT
                rightArrow=event.key==pygame.K_RIGHT
                upArrow=event.key==pygame.K_UP
                downArrow=event.key==pygame.K_DOWN
                if leftArrow:
                    change_pixel_of_x =-blocksize
                    change_pixel_of_y=nopixel
                    print("leftarrow")
                elif rightArrow:
                    change_pixel_of_x=blocksize
                    change_pixel_of_y=nopixel
                elif upArrow:
                    change_pixel_of_y =-blocksize
                    change_pixel_of_x=nopixel
                elif downArrow:
                    change_pixel_of_y=blocksize
                    change_pixel_of_x=nopixel
            
            
                
        lead_x +=change_pixel_of_x
        lead_y +=change_pixel_of_y
        screen.fill(white)
        if lead_x >= 1000 or lead_x < 0 or lead_y >=600 or lead_y < 0:
                gameover=True
                pygame.mixer.music.load("C:\Users\sapna\Desktop\chandachamke_whistle.mp3")
                pygame.mixer.music.play()
        
        

        Applethickness=20
        levelmsg()
        showscore(score_value)
        print([int(randomApplex),int(randomAppley)])
        print(["lead",int(lead_x),int(lead_y)])
        pygame.draw.rect(screen,red,(randomApplex,randomAppley,Applethickness,Applethickness))
        
        allspriteslist=[]
        allspriteslist.append(lead_x)
        allspriteslist.append(lead_y)
        snakelist.append(allspriteslist)
        
        if abs(lead_x-randomApplex)<20:
            if abs(lead_y-randomAppley)<20:
                randomApplex=round(random.randrange(10,800-blocksize))
                randomAppley=round(random.randrange(10,400-blocksize))
                snakelength +=1
                score_value=snakelength*snakelength
                

        if len(snakelist)>snakelength:
            del snakelist[0]
        

        snake(blocksize, snakelist)
        pygame.display.update()
        
        clock.tick(FPS)

    pygame.quit()
    quit()
gameloop()















            














 





















