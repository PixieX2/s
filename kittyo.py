class Ball:
    def __init__(self,color, msg):
        self.color = color
        self.msg = msg

    def Bounce(self):
        print("i bounced")

    def __str__(self):
        return self.msg
        





red_ball = Ball("red", "helloings im a ball")
print(red_ball)
red_ball.Bounce()
