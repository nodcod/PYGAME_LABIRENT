import turtle
import math
import random
import sys



wn = turtle.Screen()
wn.bgcolor("black")
wn.title("LABİRENT OYUNU")
wn.setup(800,800)



#register shapes
resimler = ["karaktersag.gif","karaktersol.gif",
            "duvar.gif","dusmansag.gif","dusmansol.gif","row.gif","puan.gif"]

for resim in resimler :
    turtle.register_shape(resim)
    

#deneme





    
#deneme
#Creat pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 0
class Bitir(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        self.goto(x, y)
        

class Carpma1(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("row.gif")
        self.speed(0)
        self.goto(x, y)



class deneme(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        self.gold = 0
        
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("karaktersag.gif")
        self.color("red")
        self.penup()
        self.speed(0)

    def go_up(self):
        #Calculate the spot to move to
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 27

        #checkif the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
       
    def go_down(self):
        #Calculate the spot to move to
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 27

        #checkif the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
      
    def go_left(self):
        #Calculate the spot to move to
        move_to_x = player.xcor() - 27
        move_to_y = player.ycor()
        self.shape("karaktersol.gif")
        

        #checkif the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        

    def go_right(self):
        #Calculate the spot to move to
        move_to_x = player.xcor() + 27
        move_to_y = player.ycor()

        self.shape("karaktersag.gif")

        #checkif the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def is_collision(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a **2) + (b ** 2))

        if distance < 5:
             return True
        else:
            return False
  #HAZİNE      
class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("puan.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)
        
    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

#DÜŞMAN
class dusman(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("dusmansol.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.direction = random.choice(["up", "down", "left", "right"])

    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 27
        elif self.direction == "down":
            dx = 0
            dy = -27
        elif self.direction == "left":
            dx = -27
            dy = 0
            self.shape("dusmansol.gif")
        elif self.direction == "right":
            dx = 27
            dy = 0
            self.shape("dusmansag.gif")
        else:
            dx = 0
            dy = 0
        #Calculate the stop to move to
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        #check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            #choose a different direction
            self.direction = random.choice(["up","down","left","right"])

        #set timer to move next time
        turtle.ontimer(self.move, t=random.randint(100,300))
        
    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()




#Create levels list
    
levels = [""]

#Define first level

level_1 = [
    "11111111111111111111111111",
    "1C00L11111D3000000000L1111",
    "10000AA00A000A1111D0001111",
    "1000000001D00A1111D00AA0O1",
    "1000000001D0001A0000003001",
    "111111000100011A0000000011",
    "111111000100B11111A00A1111",
    "11111100010000B111O0001111",
    "1O011100000000B111A00A1111",
    "10011100111111111110A11111",
    "100000000A1111111111111111",
    "10000000000000000A11111AO1",
    "11111111111A00000A1111A001",
    "11111111111100000011110001",
    "1111O01111111111A000000001",
    "111D0000000000000000000001",
    "111D3000000000A11111111111",
    "1110A00AA0000A111111111111",
    "111111111A00000000000000L1",
    "113O0A111A00000000000000L1",
    "11000111111111111100L11111",
    "11000A11111111111100011111",
    "11000000000A1111A0000000A1",
    "11111030000000000000000OA1", 
    "1O00000AA00000000AA0000A01",
    "11111111111111111112221111",
]
#Add a treasures list
treasures = []
# düşman listesi
dusmanlar = []
#BİTİRDİN
bitirdin = []
#çarpma
carptın = []
carptın1 = []
carptın2 = []
carptın3 = []
#Add maze to mazes list
levels.append(level_1)

#Create level setup function
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            #Get the character at each x,y cordinate
            #Note the order of y and x in the next line
            character = level[y][x]
            #calcuate the screen x, y coordinates
            screen_x = -370 + (x*27)
            screen_y = 370 - (y*27)

    
            


            #Check if it isan X (represtening a wall)
            if character == "1":
                pen.goto(screen_x, screen_y)
                pen.shape("square")
                pen.stamp()
                #Add coordinates to wall list
                walls.append((screen_x, screen_y))
               
            #Check if it is a C (representing the player)
            if character == "C":
                player.goto(screen_x, screen_y)

            if character == "O":
                treasures.append(Treasure(screen_x, screen_y))

            # check if it is a 3 (representing düşman)
            if character == "3":
                dusmanlar.append(dusman(screen_x, screen_y))
                
                
            # check if it is a 2 (oyunu bitirme)
            if character == "2":
                bitirdin.append(Bitir(screen_x, screen_y))

            
               
            if character == "A":
                pen.shape("row.gif")
                carptın1.append(Carpma1(screen_x, screen_y))
                
            
                
                
                
                
                
                
               
                                


#Create class instances
pen = Pen()
player = Player()


#Create wall coordinate list
walls = []


#Set up the level
setup_maze(levels[1])


#Keyboard binding
turtle.listen()
turtle.onkey(player.go_left,"a")
turtle.onkey(player.go_right,"s")
turtle.onkey(player.go_up,"w")
turtle.onkey(player.go_down,"z")

#Turn off screen updates
wn.tracer(0)

#start moving dusmanlar
for dusman in dusmanlar:
    turtle.ontimer(dusman.move, t= 250)

#Main game loop

while True:
    #Check for player collision with treasure
    #Iterate through treasure list
    for treasure in treasures:
        if player.is_collision(treasure):
            #add the treasure gold to the player gold
            player.gold = treasure.gold
            print ("SKOR:{}".format(player.gold))
            #destroy the treasure
            treasure.destroy()
            #remove the treasure from the treasures list
            treasures.remove(treasure)
    for dusman in dusmanlar:
        if player.is_collision(dusman):
            print ("ÖLDÜN")
            turtle.Screen == exit()
    for bitir in bitirdin:
        if player.is_collision(bitir):
            print ("oyun bitti")
            turtle.Screen == exit() 

    
    for Carpma1 in carptın1:
       if player.is_collision(Carpma1):
            print ("Duvara Çarptın")
            turtle.Screen == exit()
    
       
    #update screen
    wn.update()
    
    































            

    






