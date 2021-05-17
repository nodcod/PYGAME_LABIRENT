import pygame
class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100
       

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "BAŞLA"
        self.startx, self.starty = self.mid_w, self.mid_h + 5
        self.levelsx, self.levelsy = self.mid_w, self.mid_h + 40
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 70
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 100
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
  
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('ANA MENÜ', 60, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 50)
            self.game.draw_text("BAŞLA", 30, self.startx, self.starty)
            self.game.draw_text("AYARLAR (SOON)", 30, self.levelsx, self.levelsy)
            self.game.draw_text("OYNANIŞ", 30, self.optionsx, self.optionsy)
            self.game.draw_text("YAPIMCILAR", 30, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'BAŞLA':
                self.cursor_rect.midtop = (self.levelsx + self.offset, self.levelsy)
                self.state = 'level'
            elif self.state == 'level':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'BAŞLA'
        elif self.game.UP_KEY:
            if self.state == 'BAŞLA':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.levelsx + self.offset, self.levelsy)
                self.state = 'level'
            elif self.state == 'level':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'BAŞLA'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'BAŞLA':
                self.game.playing = True
            elif self.state == 'levels':
                self.game.curr_menu = self.game.levels
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False

class levelsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'AYARLAR'
        self.levelssx, self.levelssy = self.mid_w, self.mid_h + 40
        

  
class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'SES'
        self.oynanıs2x, self.voly = self.mid_w, self.mid_h - 95
        self.oynanıs3x, self.vol2y = self.mid_w, self.mid_h - 80
        self.oynanıs4x, self.vol3y = self.mid_w, self.mid_h - 65
        self.oynanıs5x, self.vol4y = self.mid_w, self.mid_h - 50
        self.oynanıs6x, self.vol5y = self.mid_w, self.mid_h - 35
        self.oynanıs7x, self.vol6y = self.mid_w, self.mid_h - 20
        self.oynanıs8x, self.vol7y = self.mid_w, self.mid_h - 5
        self.oynanıs9x, self.vol8y = self.mid_w, self.mid_h +10
        self.oynanıs10x, self.vol9y = self.mid_w, self.mid_h + 25
        self.oynanıs11x, self.vol10y = self.mid_w, self.mid_h + 40
        self.oynanısx, self.oynanısy = self.mid_w, self.mid_h + 90
        self.cursor_rect.midtop = (self.oynanıs2x + self.offset, self.voly)

    def display_menu(self):
        
        
        while self.run_display:
            self.game.check_events()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('OYUN MANTIĞI', 24, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 114)
            self.game.draw_text("KARAKTERİMİZ BAŞLANGIÇ NOKTASINDAN ÇIKIŞ NOKTASI", 15, self.oynanıs2x, self.voly)
            self.game.draw_text("OLAN BEYAZ KAPIYA DOĞRU İLERLERKEN BİRDEN FAZLA", 15, self.oynanıs3x, self.vol2y)
            self.game.draw_text("DÜŞMAN ETKENİ İLE KARŞILAŞACAKTIR, DÜŞMANLAR İLE", 15, self.oynanıs4x, self.vol3y)
            self.game.draw_text("TEMAS HALİNDE OYUNCU YANAR VE OYUN KAPANIR.", 15, self.oynanıs5x, self.vol4y)
            self.game.draw_text("DUVAR BLOKLARIN BAZI NOKTALARINDA BULUNAN MAYINLARA", 15, self.oynanıs6x, self.vol5y)
            self.game.draw_text("TEMAS HALİNDE OYUNCU YANAR VE OYUN BİTER.", 15, self.oynanıs7x, self.vol6y)
            self.game.draw_text("DUVAR BLOKLARIN BAZI KISIMLARINA GİZLENMİŞ OLAN", 15, self.oynanıs8x, self.vol7y)
            self.game.draw_text("HAZİNELERE ULAŞILDIĞINDA İSE OYUNCUYA TERMİNALDE", 15, self.oynanıs9x, self.vol8y)
            self.game.draw_text("+100 PUAN SKOR EKLENİR. OYUNCU BEYAZ KAPIYA ULAŞIP", 15, self.oynanıs10x, self.vol9y)
            self.game.draw_text("ÇIKIŞ YAĞTIĞINDA OYUNU KAZANIR VE OYUN BİTER", 15, self.oynanıs11x, self.vol10y)
            self.game.draw_text('OYNANIŞ', 24, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 1 - 70)
            self.game.draw_text("KONTROLLER: YUKARI: W  / AŞAĞI : Z  / SAĞ   : A / SOL   : S ", 15, self.oynanısx, self.oynanısy)
            self.draw_cursor()
            self.blit_screen()

    


class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('YAPIMCILAR', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('MEHMET MERT / ENES ÇAVDAR', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.blit_screen()
