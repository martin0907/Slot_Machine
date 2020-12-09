from playsound import playsound
import pygame
import random
import time
import sys
import os

pygame.font.init()
width, height = 830, 530
pygame.display.set_caption("Slot Machine by Martin Taborsky")
screen = pygame.display.set_mode((width, height))
background = pygame.transform.scale(pygame.image.load(os.path.join("img","img5.jpg")),(width, height))
frame = pygame.image.load(os.path.join("img","frame1.1.3.png"))
win_one_frame = pygame.image.load(os.path.join('img','win_frame.png'))
win_two_frame = pygame.image.load(os.path.join('img','win_frame_green.png'))
flashing_IMG = [win_one_frame, win_two_frame]
clock = pygame.time.Clock()
color_dark = (32, 163, 32)
color_win = (255,0,0)
fps = 7
wavFile = 'img/slot_sound.wav'
ITEMS = ["seven.png","bar.png","cherry.png","diamond.png",
        "grapes.png","bell.png","lemon.png","melon.png",
        "orange.png","plum.png","shoes.png"]

IMG = []
for x in range(len(ITEMS)):
    IMG.append(pygame.image.load(os.path.join("images/" + str(ITEMS[x]))))

reel_one_num = list([x for x in range(len(ITEMS))])
reel_two_num = list([x for x in range(len(ITEMS))])
reel_three_num = list([x for x in range(len(ITEMS))])
reel_four_num = list([x for x in range(len(ITEMS))])
reel_five_num = list([x for x in range(len(ITEMS))])
random.shuffle(reel_three_num)
random.shuffle(reel_five_num)

class Money:
    def __init__(self, money, bet, win):
        self.bet = bet
        self.win = win
        self.money = money

    def increase_bet(self):
        self.bet += 10
        if self.bet > 100:
            self.bet = 100
    
    def dicrease_bet(self):
        self.bet -= 10
        if self.bet < 10:
            self.bet = 10
    
    def win_rate(self, cost,coordinate, coordinate_two, coordinate_three, coordinate_four=None,coordinate_five=None):
        start = 0
        playsound(wavFile, False)
        self.win = (self.bet * cost)
        self.money += self.win
        win_font = pygame.font.SysFont('arial', 26)
        while start < 6:
            screen.blit(flashing_IMG[0], coordinate)
            screen.blit(flashing_IMG[0], coordinate_two)
            screen.blit(flashing_IMG[0], coordinate_three)
            if coordinate_four and coordinate_five != None:
                screen.blit(flashing_IMG[0], coordinate_four)
                screen.blit(flashing_IMG[0], coordinate_five)
            flashing_IMG.append(flashing_IMG[0])
            flashing_IMG.pop(0)
            text_money = win_font.render(f"$: {self.money}" , True , (0,0,0))
            text_win = win_font.render(f"Win: {self.win}" , True , (0,0,0))
            text_bet = win_font.render(f"Bet: {self.bet}" , True , (0,0,0))
            screen.blit(text_money,(80,404))
            screen.blit(text_bet,(330,404))
            screen.blit(text_win,(490,404))
            pygame.display.update()
            clock.tick(fps)
            start += 1

class Machine(Money):
    random.shuffle(reel_one_num)
    random.shuffle(reel_two_num)
    random.shuffle(reel_four_num)
    def __init__(self, money, bet, win):
        super().__init__(money, bet, win)
        self.bet = bet
        self.win = win
        self.money = money
        self.reel_one_stop = True
        self.reel_two_stop = True
        self.reel_three_stop = True
        self.reel_four_stop = True
        self.reel_five_stop = True
        self.reel_one_count = random.randint(6,9)
        self.reel_two_count = random.randint(10,13)
        self.reel_three_count = random.randint(14,16)
        self.reel_four_count = random.randint(17,19)
        self.reel_five_count = random.randint(20,23)
        self.reel_help_count = 24
        self.spin_count = 0
        self.mouse_klick_count = 0
        self.start = False

    def spin(self):
        time.sleep(.04)
        if self.reel_one_stop == False:
            screen.blit(IMG[reel_one_num[2]],(90,60))
            screen.blit(IMG[reel_one_num[1]],(90,170))
            screen.blit(IMG[reel_one_num[0]],(90,280))
            reel_one_num.append(reel_one_num[0])    
            reel_one_num.pop(0)
        
        if self.reel_two_stop == False:
            screen.blit(IMG[reel_two_num[2]],(230,60))
            screen.blit(IMG[reel_two_num[1]],(230,170))
            screen.blit(IMG[reel_two_num[0]],(230,280))
            reel_two_num.append(reel_two_num[0])    
            reel_two_num.pop(0)

        if self.reel_three_stop == False:
            screen.blit(IMG[reel_three_num[2]],(365,60))
            screen.blit(IMG[reel_three_num[1]],(365,170))
            screen.blit(IMG[reel_three_num[0]],(365,280))
            reel_three_num.append(reel_three_num[0])    
            reel_three_num.pop(0)
        
        if self.reel_four_stop == False:
            screen.blit(IMG[reel_four_num[2]],(500,60))
            screen.blit(IMG[reel_four_num[1]],(500,170))
            screen.blit(IMG[reel_four_num[0]],(500,280))
            reel_four_num.append(reel_four_num[0])    
            reel_four_num.pop(0)

        if self.reel_five_stop == False:
            screen.blit(IMG[reel_five_num[2]],(640,60))
            screen.blit(IMG[reel_five_num[1]],(640,170))
            screen.blit(IMG[reel_five_num[0]],(640,280))
            reel_five_num.append(reel_five_num[0])    
            reel_five_num.pop(0)

        time.sleep(.04)
        screen.blit(frame,(65,40))
        screen.blit(IMG[reel_one_num[2]],(90,60))
        screen.blit(IMG[reel_one_num[1]],(90,170))
        screen.blit(IMG[reel_one_num[0]],(90,280))

        screen.blit(IMG[reel_two_num[2]],(230,60))
        screen.blit(IMG[reel_two_num[1]],(230,170))
        screen.blit(IMG[reel_two_num[0]],(230,280))

        screen.blit(IMG[reel_three_num[2]],(365,60))
        screen.blit(IMG[reel_three_num[1]],(365,170))
        screen.blit(IMG[reel_three_num[0]],(365,280))

        screen.blit(IMG[reel_four_num[2]],(500,60))
        screen.blit(IMG[reel_four_num[1]],(500,170))
        screen.blit(IMG[reel_four_num[0]],(500,280))

        screen.blit(IMG[reel_five_num[2]],(640,60))
        screen.blit(IMG[reel_five_num[1]],(640,170))
        screen.blit(IMG[reel_five_num[0]],(640,280))

    def time_to_stop(self):
        self.spin_count += 1
        if self.spin_count == self.reel_one_count:
            self.reel_one_stop = True
        if self.spin_count == self.reel_two_count:
            self.reel_two_stop = True
        if self.spin_count == self.reel_three_count:
            self.reel_three_stop = True
        if self.spin_count == self.reel_four_count:
            self.reel_four_stop = True
        if self.spin_count == self.reel_five_count:
            self.reel_five_stop = True
        if self.spin_count == self.reel_help_count: 
            pass
            if self.start:
                if (IMG[reel_one_num[2]] == IMG[reel_two_num[2]]) and (IMG[reel_one_num[2]] == IMG[reel_three_num[2]]):
                    super().win_rate(2,(90,60),(230,60),(365,60))
                if (IMG[reel_one_num[2]] == IMG[reel_two_num[1]]) and (IMG[reel_one_num[2]] == IMG[reel_three_num[1]]):
                    super().win_rate(2,(90,60),(230,170),(365,170))
                if (IMG[reel_one_num[2]] == IMG[reel_two_num[0]]) and (IMG[reel_one_num[2]] == IMG[reel_three_num[0]]):
                    super().win_rate(3,(90,60),(230,280),(365,280))
                if (IMG[reel_one_num[1]] == IMG[reel_two_num[2]]) and (IMG[reel_one_num[1]] == IMG[reel_three_num[2]]):
                    super().win_rate(3,(90,170),(230,60),(365,60))
                if (IMG[reel_one_num[1]] == IMG[reel_two_num[1]]) and (IMG[reel_one_num[1]] == IMG[reel_three_num[1]]):
                    super().win_rate(3,(90,170),(230,170),(365,170))
                if (IMG[reel_one_num[1]] == IMG[reel_two_num[0]]) and (IMG[reel_one_num[1]] == IMG[reel_three_num[0]]):
                    super().win_rate(4,(90,170),(230,280),(365,280))
                if (IMG[reel_one_num[0]] == IMG[reel_two_num[0]]) and (IMG[reel_one_num[0]] == IMG[reel_three_num[0]]):
                    super().win_rate(4,(90,280),(230,280),(365,280))
                if (IMG[reel_one_num[0]] == IMG[reel_two_num[1]]) and (IMG[reel_one_num[0]] == IMG[reel_three_num[1]]):
                    super().win_rate(1,(90,280),(230,170),(365,170))
                if (IMG[reel_one_num[0]] == IMG[reel_two_num[2]]) and (IMG[reel_one_num[0]] == IMG[reel_three_num[2]]):
                    super().win_rate(5,(90,280),(230,60),(365,60))
                if (IMG[reel_one_num[2]] == IMG[reel_two_num[1]]) and (IMG[reel_one_num[2]] == IMG[reel_three_num[0]]):
                    super().win_rate(6,(90,60),(230,170),(365,280))
                if (IMG[reel_one_num[0]] == IMG[reel_two_num[1]]) and (IMG[reel_one_num[0]] == IMG[reel_three_num[2]]):
                    super().win_rate(7,(90,280),(230,170),(365,60))
                if (IMG[reel_one_num[2]] == IMG[reel_two_num[2]]) and (IMG[reel_one_num[2]] == IMG[reel_three_num[1]]):
                    super().win_rate(6,(90,60),(230,60),(365,170))
                if (IMG[reel_one_num[1]] == IMG[reel_two_num[1]]) and (IMG[reel_one_num[1]] == IMG[reel_three_num[2]]):
                    super().win_rate(5,(90,170),(230,170),(365,60))
                if (IMG[reel_one_num[1]] == IMG[reel_two_num[1]]) and (IMG[reel_one_num[1]] == IMG[reel_three_num[0]]):
                    super().win_rate(4,(90,170),(230,170),(365,280))
                if (IMG[reel_one_num[0]] == IMG[reel_two_num[0]]) and (IMG[reel_one_num[0]] == IMG[reel_three_num[1]]):
                    super().win_rate(3,(90,280),(230,280),(365,170))
                if (IMG[reel_one_num[2]] == IMG[reel_two_num[1]]) and (IMG[reel_one_num[2]] == IMG[reel_three_num[2]]):
                    super().win_rate(2,(90,60),(230,170),(365,60))
                if (IMG[reel_one_num[0]] == IMG[reel_two_num[1]]) and (IMG[reel_one_num[0]] == IMG[reel_three_num[0]]):
                    super().win_rate(1,(90,280),(230,170),(365,280))
                if (IMG[reel_one_num[1]] == IMG[reel_two_num[2]]) and (IMG[reel_one_num[1]] == IMG[reel_three_num[1]]):
                    super().win_rate(2,(90,170),(230,60),(365,170))
                if (IMG[reel_one_num[1]] == IMG[reel_two_num[0]]) and (IMG[reel_one_num[1]] == IMG[reel_three_num[1]]):  
                    super().win_rate(3,(90,170),(230,280),(365,170))
                if (IMG[reel_one_num[0]] == IMG[reel_two_num[0]]) and (IMG[reel_one_num[0]] == IMG[reel_three_num[2]]):
                    super().win_rate(4,(90,280),(230,280),(365,60))
                if (IMG[reel_one_num[2]] == IMG[reel_two_num[2]]) and (IMG[reel_one_num[2]] == IMG[reel_three_num[0]]):
                    super().win_rate(5,(90,60),(230,60),(365,280))
                if (IMG[reel_one_num[2]] == IMG[reel_two_num[0]]) and (IMG[reel_one_num[2]] == IMG[reel_three_num[2]]):
                    super().win_rate(6,(90,60),(230,280),(365,60))
                if (IMG[reel_one_num[0]] == IMG[reel_two_num[2]]) and (IMG[reel_one_num[0]] == IMG[reel_three_num[0]]):
                    super().win_rate(6,(90,280),(230,60),(365,280))
                if (IMG[reel_one_num[1]] == IMG[reel_two_num[1]]) and (IMG[reel_one_num[1]] == IMG[reel_three_num[1]]) and (IMG[reel_one_num[1]] == IMG[reel_four_num[1]]) and (IMG[reel_one_num[1]] == IMG[reel_five_num[1]]):
                    super().win_rate(20,(90,170),(230,170),(365,170),(500,170),(640,170))
                if (IMG[reel_one_num[2]] == IMG[reel_two_num[2]]) and (IMG[reel_one_num[2]] == IMG[reel_three_num[2]]) and (IMG[reel_one_num[2]] == IMG[reel_four_num[2]]) and (IMG[reel_one_num[2]] == IMG[reel_five_num[2]]):
                    super().win_rate(20,(90,60),(230,60),(365,60),(500,60),(640,60))                
                if (IMG[reel_one_num[0]] == IMG[reel_two_num[0]]) and (IMG[reel_one_num[0]] == IMG[reel_three_num[0]]) and (IMG[reel_one_num[0]] == IMG[reel_four_num[0]]) and (IMG[reel_one_num[0]] == IMG[reel_five_num[0]]):
                    super().win_rate(23,(90,280),(230,280),(365,280),(500,280),(640,280))            
                if (IMG[reel_one_num[2]] == IMG[reel_two_num[1]]) and (IMG[reel_one_num[2]] == IMG[reel_three_num[0]]) and (IMG[reel_one_num[2]] == IMG[reel_four_num[1]]) and (IMG[reel_one_num[2]] == IMG[reel_five_num[2]]):
                    super().win_rate(23,(90,60),(230,170),(365,280),(500,170),(640,60))
                if (IMG[reel_one_num[0]] == IMG[reel_two_num[1]]) and (IMG[reel_one_num[0]] == IMG[reel_three_num[2]]) and (IMG[reel_one_num[0]] == IMG[reel_four_num[1]]) and (IMG[reel_one_num[0]] == IMG[reel_five_num[0]]):
                    super().win_rate(25,(90,280),(230,170),(365,60),(500,170),(640,280))
                if (IMG[reel_one_num[2]] == IMG[reel_two_num[2]]) and (IMG[reel_one_num[2]] == IMG[reel_three_num[1]]) and (IMG[reel_one_num[2]] == IMG[reel_four_num[2]]) and (IMG[reel_one_num[2]] == IMG[reel_five_num[2]]):
                    super().win_rate(25,(90,60),(230,60),(365,170),(500,60),(640,60))
                if (IMG[reel_one_num[0]] == IMG[reel_two_num[0]]) and (IMG[reel_one_num[0]] == IMG[reel_three_num[1]]) and (IMG[reel_one_num[0]] == IMG[reel_four_num[0]]) and (IMG[reel_one_num[0]] == IMG[reel_five_num[0]]):
                    super().win_rate(27,(90,280),(230,280),(365,170),(500,280),(640,280))
                if (IMG[reel_one_num[1]] == IMG[reel_two_num[0]]) and (IMG[reel_one_num[1]] == IMG[reel_three_num[0]]) and (IMG[reel_one_num[1]] == IMG[reel_four_num[0]]) and (IMG[reel_one_num[1]] == IMG[reel_five_num[1]]):
                    super().win_rate(27,(90,170),(230,280),(365,280),(500,280),(640,170))
                if (IMG[reel_one_num[1]] == IMG[reel_two_num[2]]) and (IMG[reel_one_num[1]] == IMG[reel_three_num[2]]) and (IMG[reel_one_num[1]] == IMG[reel_four_num[2]]) and (IMG[reel_one_num[1]] == IMG[reel_five_num[2]]):
                    super().win_rate(29,(90,170),(230,60),(365,60),(500,60),(640,60))
                if (IMG[reel_one_num[1]] == IMG[reel_two_num[2]]) and (IMG[reel_one_num[1]] == IMG[reel_three_num[1]]) and (IMG[reel_one_num[1]] == IMG[reel_four_num[2]]) and (IMG[reel_one_num[1]] == IMG[reel_five_num[1]]):
                    super().win_rate(29,(90,60),(230,60),(365,170),(500,60),(640,170))
                if (IMG[reel_one_num[1]] == IMG[reel_two_num[0]]) and (IMG[reel_one_num[1]] == IMG[reel_three_num[1]]) and (IMG[reel_one_num[1]] == IMG[reel_four_num[0]]) and (IMG[reel_one_num[1]] == IMG[reel_five_num[1]]):
                    super().win_rate(31,(90,170),(230,280),(365,170),(500,280),(640,170))
                if (IMG[reel_one_num[2]] == IMG[reel_two_num[1]]) and (IMG[reel_one_num[2]] == IMG[reel_three_num[2]]) and (IMG[reel_one_num[2]] == IMG[reel_four_num[1]]) and (IMG[reel_one_num[2]] == IMG[reel_five_num[2]]):
                    super().win_rate(31,(90,60),(230,170),(365,60),(500,170),(640,60))
                if (IMG[reel_one_num[0]] == IMG[reel_two_num[1]]) and (IMG[reel_one_num[0]] == IMG[reel_three_num[0]]) and (IMG[reel_one_num[0]] == IMG[reel_four_num[1]]) and (IMG[reel_one_num[0]] == IMG[reel_five_num[0]]):
                    super().win_rate(33,(90,280),(230,170),(365,280),(500,170),(640,280))
                if (IMG[reel_one_num[1]] == IMG[reel_two_num[1]]) and (IMG[reel_one_num[1]] == IMG[reel_three_num[2]]) and (IMG[reel_one_num[1]] == IMG[reel_four_num[1]]) and (IMG[reel_one_num[1]] == IMG[reel_five_num[1]]):
                    super().win_rate(33,(90,170),(230,170),(365,60),(500,170),(640,170))
                if (IMG[reel_one_num[1]] == IMG[reel_two_num[1]]) and (IMG[reel_one_num[1]] == IMG[reel_three_num[0]]) and (IMG[reel_one_num[1]] == IMG[reel_four_num[1]]) and (IMG[reel_one_num[1]] == IMG[reel_five_num[1]]):
                    super().win_rate(35,(90,170),(230,170),(365,280),(500,170),(640,170))
                if (IMG[reel_one_num[2]] == IMG[reel_two_num[1]]) and (IMG[reel_one_num[2]] == IMG[reel_three_num[1]]) and (IMG[reel_one_num[2]] == IMG[reel_four_num[1]]) and (IMG[reel_one_num[2]] == IMG[reel_five_num[2]]):
                    super().win_rate(35,(90,60),(230,170),(365,170),(500,60),(640,60))
                if (IMG[reel_one_num[0]] == IMG[reel_two_num[1]]) and (IMG[reel_one_num[0]] == IMG[reel_three_num[1]]) and (IMG[reel_one_num[0]] == IMG[reel_four_num[1]]) and (IMG[reel_one_num[0]] == IMG[reel_five_num[0]]):
                    super().win_rate(37,(90,280),(230,170),(365,170),(500,170),(640,280))
                if (IMG[reel_one_num[2]] == IMG[reel_two_num[1]]) and (IMG[reel_one_num[2]] == IMG[reel_three_num[0]]) and (IMG[reel_one_num[2]] == IMG[reel_four_num[0]]) and (IMG[reel_one_num[2]] == IMG[reel_five_num[0]]):
                    super().win_rate(37,(90,60),(230,170),(365,280),(500,280),(640,280)) 
                if (IMG[reel_one_num[0]] == IMG[reel_two_num[1]]) and (IMG[reel_one_num[0]] == IMG[reel_three_num[2]]) and (IMG[reel_one_num[0]] == IMG[reel_four_num[2]]) and (IMG[reel_one_num[0]] == IMG[reel_five_num[2]]):
                    super().win_rate(39,(90,280),(230,170),(365,60),(500,60),(640,60))
                if (IMG[reel_one_num[2]] == IMG[reel_two_num[0]]) and (IMG[reel_one_num[2]] == IMG[reel_three_num[2]]) and (IMG[reel_one_num[2]] == IMG[reel_four_num[0]]) and (IMG[reel_one_num[2]] == IMG[reel_five_num[2]]):
                    super().win_rate(39,(90,60),(230,280),(365,60),(500,280),(640,60))
                if (IMG[reel_one_num[0]] == IMG[reel_two_num[2]]) and (IMG[reel_one_num[0]] == IMG[reel_three_num[0]]) and (IMG[reel_one_num[0]] == IMG[reel_four_num[2]]) and (IMG[reel_one_num[0]] == IMG[reel_five_num[0]]):
                    super().win_rate(41,(90,280),(230,60),(365,280),(500,60),(640,280))
                if (IMG[reel_one_num[2]] == IMG[reel_two_num[0]]) and (IMG[reel_one_num[2]] == IMG[reel_three_num[0]]) and (IMG[reel_one_num[2]] == IMG[reel_four_num[0]]) and (IMG[reel_one_num[2]] == IMG[reel_five_num[2]]):
                    super().win_rate(41,(90,60),(230,280),(365,280),(500,280),(640,60))
                if (IMG[reel_one_num[0]] == IMG[reel_two_num[2]]) and (IMG[reel_one_num[0]] == IMG[reel_three_num[2]]) and (IMG[reel_one_num[0]] == IMG[reel_four_num[2]]) and (IMG[reel_one_num[0]] == IMG[reel_five_num[0]]):
                    super().win_rate(43,(90,280),(230,60),(365,60),(500,60),(640,280))
                if (IMG[reel_one_num[2]] == IMG[reel_two_num[2]]) and (IMG[reel_one_num[2]] == IMG[reel_three_num[0]]) and (IMG[reel_one_num[2]] == IMG[reel_four_num[2]]) and (IMG[reel_one_num[2]] == IMG[reel_five_num[2]]):
                    super().win_rate(43,(90,60),(230,60),(365,280),(500,60),(640,60)) 
                if (IMG[reel_one_num[0]] == IMG[reel_two_num[0]]) and (IMG[reel_one_num[0]] == IMG[reel_three_num[2]]) and (IMG[reel_one_num[0]] == IMG[reel_four_num[0]]) and (IMG[reel_one_num[0]] == IMG[reel_five_num[0]]):
                    super().win_rate(45,(90,280),(230,280),(365,60),(500,280),(640,280))

def roll(machine):
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 640 <= mouse[0] <= 640+110 and 398 <= mouse[1] <= 398+80:
                machine.reel_one_stop = False
                machine.reel_two_stop = False
                machine.reel_three_stop = False
                machine.reel_four_stop = False 
                machine.reel_five_stop = False
                machine.spin_count = 0
                machine.win = 0
                machine.start = True
                machine.money -= machine.bet
                machine.mouse_klick_count += 1

                if machine.mouse_klick_count == 5:
                    machine.spin_count = 2
                elif machine.mouse_klick_count == 11:
                    machine.spin_count = 3
                    machine.mouse_klick_count = 0

                if machine.money < 0:
                    pygame.display.quit()
                    pygame.quit()

            if 445 <= mouse[0] <= 445+30 and 405 <= mouse[1] <= 405+30:
                machine.increase_bet()

            if 297 <= mouse[0] <= 297+30 and 405 <= mouse[1] <= 405+30:
                machine.dicrease_bet()        

def main():
    run = True
    machine = Machine(1000,10,0)
    spin_font = pygame.font.SysFont('comicsans', 50)
    win_font = pygame.font.SysFont('arial', 26)
    bet_font = pygame.font.SysFont('arial', 26)
    text_spin = spin_font.render("Spin" , True , (255,255,255))

    while run:
        screen.blit(background,(0,0))
        pygame.draw.rect(screen,color_dark,[640,396,110,80])
        screen.blit(text_spin,(658,418))
        machine.spin()
        machine.time_to_stop()
        roll(machine)
        text_money = win_font.render(f"$: {machine.money}" , True , (0,0,0))
        text_win = win_font.render(f"Win: {machine.win}" , True , (0,0,0))
        text_bet = win_font.render(f"Bet: {machine.bet}" , True , (0,0,0))
        text_bet_plus = spin_font.render("+" , True , (0,0,0))
        text_bet_minus = spin_font.render("-" , True , (0,0,0))
        screen.blit(text_bet_plus,(450,400))
        screen.blit(text_bet_minus,(305,400))
        screen.blit(text_money,(80,404))
        screen.blit(text_bet,(330,404))
        screen.blit(text_win,(490,404))
        pygame.display.update()
        
main()