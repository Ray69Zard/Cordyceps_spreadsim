#NOTE: GO TO LLINE 137 OF THIS CODE TO CHANGE ALL THE PARAMETERS, Happy Pandemic!!!!!

import pygame
import random
import math
import sys
import numpy as np
from matplotlib import pyplot

pygame.init()


WIDTH = 1000
HEIGHT = 750
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))

COLOR={"grey":(35,35,40),"light_grey":(70,70,90),"white":(255,248,240),"red":(239,71,111),"blue":(17,138,178),"green":(0,255,0)}
COLOR_DEFINITIONS ={"background": COLOR["grey"],
         "healthy": COLOR["white"],
         "infected": COLOR["red"],
         "immune": COLOR["blue"],
         "dead": COLOR["grey"]}

def moving_average(l,k=7):
    avg=[0 for i in range(k//2)]
    for i in range(k//2,len(l)-k//2):
        sub=l[i-k//2:i+k//2+1]
        avg.append(sum(sub)/len(sub))
    return avg + [0 for i in range(k//2)]

class Cell():
    def __init__(self,row,col):
        self.row=row
        self.col=col
        self.Test_Sample=[]

    def get_neighboring_cells(self, n_rows, n_cols):
        index = self.row*n_cols + self.col
        N= index - n_cols if self.row > 0 else None
        S= index + n_cols if self.row < n_rows - 1 else None
        W= index - 1 if self.col > 0 else None
        E= index + 1 if self.col < n_cols - 1 else None
        NW= index - n_cols - 1 if self.row > 0 and self.col > 0 else None
        NE= index - n_cols + 1 if self.row > 0 and self.col < n_cols - 1 else None
        SW= index + n_cols - 1 if self.row < n_rows - 1 and self.col > 0 else None
        SE= index + n_cols + 1 if self.row < n_rows - 1 and self.col < n_cols - 1 else None
        return [i for i in [index,N,S,E,W,NW,NE,SE,SW] if i]
class Grid():
    def __init__(self, Test_Sample, h_size=20, v_size=20):
        self.h_size = h_size
        self.v_size = v_size
        self.n_rows = HEIGHT // v_size
        self.n_cols = WIDTH // h_size
        self.cells = []

        for row in range(self.n_rows):
            for col in range(self.n_cols):
                self.cells.append(Cell(row, col))
        self.store_people(Test_Sample)

    def store_people(self, Test_Sample):
        for p in Test_Sample:
            row = min(int(p.y / self.v_size), self.n_rows - 1)
            col = min(int(p.x / self.h_size), self.n_cols - 1)
            index = row * self.n_cols + col
            self.cells[index].Test_Sample.append(p)


    def show(self,width=1):
        for c in self.cells:
            x=c.col* self.h_size
            y=c.row* self.v_size
            rect = pygame.Rect(x,y,self.h_size,self.v_size)
            pygame.draw.rect(SCREEN,COLOR["light_grey"],rect,width=width)
        

class Person():
    def __init__(self):
        self.x=random.uniform(0,WIDTH)
        self.y=random.uniform(0,HEIGHT)
        self.dx=0
        self.dy=0
        self.state="healthy"
        self.recovery_counter=0
        self.immunity_counter=0
    def show(self,size=5):
         if self.state == "healthy":
             color = COLOR_DEFINITIONS["healthy"]
         elif self.state == "infected":
            color = COLOR_DEFINITIONS["infected"]
         elif self.state == "immune":
             color = COLOR_DEFINITIONS["immune"]
         elif self.state == "dead":
             color = COLOR_DEFINITIONS["dead"]
        
         pygame.draw.circle(SCREEN,color,(self.x,self.y),size)
    def move(self,speed= 0.01):
        #position vector adjustment
        self.x += self.dx
        self.y += self.dy
        #avoid going out of screen
        if self.x >=WIDTH:
            self.x=WIDTH-1
            self.dx *=-1
        if self.y >= HEIGHT:
            self.y=HEIGHT-1
            self.dy *= -1
        if self.x <=0:
            self.x =1
            self.dx *=-1
        if self.y <=0:
            self.y=1
            self.dy *=-1
        
        #velocity vector adjustment
        self.dx += random.uniform(-speed,speed)
        self.dy += random.uniform(-speed,speed)
        
    def get_infected(self,value=1000):
        self.state= "infected"
        self.recovery_counter = value

    def recover(self,value= 2000):
        self.recovery_counter -=1
        if self.recovery_counter ==0:
            self.state= "immune"
            self.immunity_counter=value
            
    def lose_immunity(self):
        self.immunity_counter -=1
        if self.immunity_counter ==0:
            self.state="healthy"

    def die(self,probability=0.00001):
        if random.uniform(0,1) < probability:
            self.state = "dead"

class Pandemic():
    def __init__(self,n_people=2000,size=4,speed=0.04,infect_dist=5,recover_time=400,immune_time=1500000000000000000000000000000000000000000000000000000000000000000000000000000000000000,
                 prob_catch=0.1,prob_death=0.00095):
        self.Test_Sample=[Person() for i in range(n_people)]
        self.size=size
        self.speed=speed
        self.infect_dist=infect_dist
        self.recover_time=recover_time
        self.immune_time=immune_time
        self.prob_catch=prob_catch
        self.prob_death=prob_death
        self.grid=Grid(self.Test_Sample)
        self.Test_Sample[0].get_infected(self.recover_time)
        self.record=[]
        self.over=False
        #for p in self.Test_Sample:
            #p.get_infected(self.recover_time)

    def update_grid(self):
        self.grid= Grid(self.Test_Sample)

    def slowly_infect_people(self):
         for p in self.Test_Sample:
             if p.state == "infected":
                 for other in self.Test_Sample:
                     if other.state == "healthy":
                         dist= math.sqrt((p.x-other.x)**2 + (p.y-other.y)**2)
                         if dist<self.infect_dist:
                             other.get_infected()

    def efficiently_infect_people(self):
        for c in self.grid.cells:

            states=[p.state for p in c.Test_Sample]
            if states.count("infected")==0:
                continue
            people_in_area = []
            for index in c.get_neighboring_cells(self.grid.n_rows,self.grid.n_cols):
                people_in_area += self.grid.cells[index].Test_Sample
                infected_people = [p for p in people_in_area if p.state == "infected"]
                healthy_people = [p for p in people_in_area if p.state == "healthy"]

                if len(healthy_people)== 0:
                    continue
                for i in infected_people:
                    for h in healthy_people:
                        dist= math.sqrt((i.x-h.x)**2 + (i.y-h.y)**2)
                        if dist<self.infect_dist:
                            if random.uniform(0,1)<self.prob_catch:
                                h.get_infected(self.recover_time)
                        
    def run(self):   
        self.update_grid()
        self.efficiently_infect_people()

        for p in self.Test_Sample:
            if p.state == "infected":
                p.die(self.prob_death)
                p.recover(self.immune_time)
            elif p.state == "immune":
                p.lose_immunity()
            p.move(self.speed)
            p.show(self.size)
    def statistics(self):
        states = [p.state for p in self.Test_Sample]
        n_infected=states.count("infected")
        n_dead= states.count("dead")
        n_healthy=states.count("healthy")
        self.record.append([n_infected,n_dead,n_healthy])
        if n_infected ==0:
            self.over=True
    def Conclusion(self):
        time_index= range(1,len(self.record)+1)
        infected=[r[0] for r in self.record]
        dead= [r[1] for r in self.record]
        healthy=[r[2] for r in self.record]

        newly_dead = [0]
        for i in range(1,len(dead)):
            newly_dead.append(dead[i]-dead[i-1])
        newly_dead= moving_average(newly_dead,20)
        fig,ax = pyplot.subplots()
        ax.plot(time_index,infected,color="red")
        ax.plot(time_index,healthy,color="green")
        ax.set_xlabel("Period")
        ax.set_ylabel("People currently infected & healthy",color="black")
        #ax.set_ylabel("People currently healthy",color="green")
        
        ax2 =ax.twinx()
        ax2.plot(time_index,dead,color="black")
        ax2.set_ylabel("Total Deaths",color="black")
        pyplot.show()
        
        
        

pandemic= Pandemic()
#game loop
clock = pygame.time.Clock()
font=pygame.font.Font('freesansbold.ttf',32)
running= True
stopping= False
while running and not pandemic.over:
    if not stopping:

        SCREEN.fill(COLOR_DEFINITIONS["background"])
        pandemic.update_grid()
        pandemic.run()
        pandemic.statistics()
        clock.tick()
        clock_string = str(math.floor(clock.get_fps()))
        text=font.render(clock_string,True,COLOR["blue"],COLOR_DEFINITIONS["background"])
        text_box= text.get_rect(topleft =(10,10))
        SCREEN.blit(text,text_box)
        pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RETURN:
                stopping = False
                pandemic=Pandemic()
            if event.key == pygame.K_SPACE:
                stopping = not stopping

pandemic.Conclusion()


pygame.quit()
quit()
