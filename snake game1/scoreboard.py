from turtle import *
from snake import Snake

ALIGMENT = "center"
FONT = ("Courier",21 ,"normal")


class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data :
           self.h_score=int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} HIGH SCORE  : {self.h_score}", align = ALIGMENT , font=FONT)

    def reset(self):
        if self.score > self.h_score :
            self.h_score = self.score
            with open("data.txt", mode = "w") as data :
                data.write(f"{self.h_score}")
        self.score = 0 
        self.update_scoreboard()

    def incrise_score(self):
        self.score += 1
        self.update_scoreboard()

   



    





    
    
        
    


