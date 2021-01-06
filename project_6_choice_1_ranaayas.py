import turtle as tu

tu.bgcolor("lightgrey")
box1 = "a"
box2 = "a"
box3 = "a"
box4 = "a"
box5 = "a"
box6 = "a"
box7 = "a"
box8 = "a"
box9 = "a"
go = 0

def grid():
    tu.ht()
    tu.color('navy')
    tu.pensize(3)
    tu.speed(400)
    tu.pu()
    tu.goto(-150, -50)
    tu.pd()
    tu.forward(300)
    tu.pu()
    tu.goto(-150, 50)
    tu.pd()
    tu.forward(300)
    tu.pu()
    tu.goto(-50, 150)
    tu.right(90)
    tu.pd()
    tu.forward(300)
    tu.pu()
    tu.goto(50, 150)
    tu.right
    tu.pd()
    tu.forward(300)
    tu.pu()

    tu.pu()
    tu.setposition(-150, -150)
    tu.pd()
    tu.right(180)
    tu.forward(300)
    tu.pu()
    tu.setposition(-150, -150)
    tu.pd()
    tu.right(90)
    tu.forward(300)
    tu.pu()
    tu.setposition(150, -150)
    tu.pd()
    tu.left(90)
    tu.forward(300)
    tu.pu()
    tu.setposition(150, 150)
    tu.pd()
    tu.left(90)
    tu.forward(300)
    tu.pu()
    tu.setposition(-120,160)
    tu.write("Tic-Tac-Toe", font=("Comic Sans", 40, "bold"))


def numbering():
    tu.pensize(3)
    tu.speed(7)
    tu.setposition(-130, 130)
    tu.write("1", font= 15)
    tu.setposition(-130, 30)
    tu.write("4", font= 15)
    tu.setposition(-130, -70)
    tu.write("7", font= 15)
    tu.setposition(-30, 130)
    tu.write("2", font= 15)
    tu.setposition(-30, 30)
    tu.write("5", font= 15)
    tu.setposition(-30, -70)
    tu.write("8", font= 15)
    tu.setposition(70, 130)
    tu.write("3", font= 15)
    tu.setposition(70, 30)
    tu.write("6", font= 15)
    tu.setposition(70, -70)
    tu.write("9", font= 15)

def drawo():
    tu.color("goldenrod")
    tu.speed(20)
    tu.pendown()
    tu.circle(30)
    tu.penup()
    tu.home()


def drawx():
    tu.color("steelblue")
    tu.speed(50)
    tu.left(45)
    tu.pendown()
    tu.forward(30)
    tu.backward(60)
    tu.forward(30)
    tu.left(90)
    tu.forward(30)
    tu.backward(60)
    tu.forward(30)
    tu.penup()
    tu.home()


def movex():
        global box1
        global box2
        global box3
        global box4
        global box5
        global box6
        global box7
        global box8
        global box9
        movex = input("Player X's move: ")
        if (movex == 1):
            tu.goto(-100,100)
            drawx()
            box1 = "x"
        if (movex == 2):
            tu.goto(0,100)
            drawx()
            box2 = "x"
        if (movex == 3):
            tu.goto(100,100)
            drawx()
            box3 = "x"
        if (movex == 4):
            tu.goto(-100,0)
            drawx()
            box4 = "x"
        if (movex == 5):
            tu.goto(-0,0)
            drawx()
            box5 = "x"
        if (movex == 6):
            tu.goto(100,0)
            drawx()
            box6 = "x"
        if (movex == 7):
            tu.goto(-100,-100)
            drawx()
            box7 = "x"
        if (movex == 8):
            tu.goto(0,-100)
            drawx()
            box8 = "x"
        if (movex == 9):
            tu.goto(100,-100)
            drawx()
            box9 = "x"
        winnerx()

def moveo():
    global box1
    global box2
    global box3
    global box4
    global box5
    global box6
    global box7
    global box8
    global box9
    moveo = input("Player O's move: ")
    if (moveo == 1):
        tu.goto(-100, 75)
        drawo()
        box1 = "o"
    if (moveo == 2):
        tu.goto(0, 75)
        drawo()
        box2 = "o"
    if (moveo == 3):
        tu.goto(100, 75)
        drawo()
        box3 = "o"
    if (moveo == 4):
        tu.goto(-100, -25)
        drawo()
        box4 = "o"
    if (moveo == 5):
        tu.goto(0, -25)
        drawo()
        box5 = "o"
    if (moveo == 6):
        tu.goto(100, -25)
        drawo()
        box6 = "o"
    if (moveo == 7):
        tu.goto(-100, -125)
        drawo()
        box7 = "o"
    if (moveo == 8):
        tu.goto(0, -125)
        drawo()
        box8 = "o"
    if (moveo == 9):
        tu.goto(100, -125)
        drawo()
        box9 = "o"
    winnero()

def winnerx():
    global go
    if (box1 == "x" and box2 == "x" and box3 == "x"):
        print("Player X wins!")
        go = 1
    if (box4 == "x" and box5 == "mx" and box6 == "x"):
        print ("Player X wins!")
        go = 1
    if (box7 == "x" and box8 == "x" and box9 == "x"):
        print ("Player X wins!")
        go = 1
    if (box1 == "x" and box4 == "x" and box7 == "x"):
        print ("Player X wins!")
        go = 1
    if (box2 == "x" and box5 == "x" and box8 == "x"):
        print ("Player X wins!")
        go = 1
    if (box3 == "x" and box6 == "x" and box9 == "x"):
        print ("Player X wins!")
        go = 1
    if (box1 == "x" and box5 == "x" and box9 == "x"):
        print ("Player X wins!")
        go = 1
    if (box3 == "x" and box5 == "x" and box7 == "x"):
        print ("Player X wins!")
        go = 1

def winnero():
    global go
    if (box1 == "o" and box2 == "o" and box3 == "o"):
        print ("Player O wins!")
        go = 1
    if (box4 == "o" and box5 == "o" and box6 == "o"):
        print ("Player O wins!")
        go = 1
    if (box7 == "o" and box8 == "o" and box9 == "o"):
        print ("Player O wins!")
        go = 1
    if (box1 == "o" and box4 == "o" and box7 == "o"):
        print ("Player O wins!")
        go = 1
    if (box2 == "o" and box5 == "o" and box8 == "o"):
        print ("Player O wins!")
        go = 1
    if (box3 == "o" and box6 == "o" and box9 == "o"):
        print ("Player O wins!")
        go = 1
    if (box1 == "o" and box5 == "o" and box7 == "o"):
        print ("Player O wins!")
        go = 1
    if (box3 == "o" and box5 == "o" and box7 == "o"):
        print ("Player O wins!")
        go = 1

def loop():
    global go
    chk = 0
    while (go==0 and chk<5):
        movex()
        chk=chk+1
        if(chk<5 and go==0):
            moveo()
    if (go == 0):
            print "It's a tie!"

def main():
    grid()
    numbering()
    loop()

main()

tu.exitonclick()