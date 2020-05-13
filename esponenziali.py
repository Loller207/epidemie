import turtle

ninja = turtle.Turtle()
ninja.hideturtle()
ninja.speed(0)

screen = turtle.Screen()
screen.setup(1.0,1.0)

i=0
b = 0
c = 200
l = 600
ninja.up()
ninja.goto(-l,-c)
ninja.down()

font=("Arial", 20, "normal")

ninja.forward(1500)
ninja.backward(2000)
ninja.forward(500)
ninja.left(90)
ninja.forward(1000)
ninja.backward(1500)
ninja.forward(500)

ninja.pensize(0.5)

for k in range(1, 21, 1):
    ninja.seth(90)
    ninja.up()
    ninja.goto(-l,-c)
    ninja.down()
    ninja.forward(20*k)
    ninja.seth(0)
    ninja.forward(1500)
    ninja.backward(1500)
    ninja.up()
    ninja.backward(20)
    y = ninja.ycor()
    x = ninja.xcor()
    ninja.goto(x,y-7.5)
    ninja.write(k*5,font)

ninja.up()
ninja.goto(-l,-c)
ninja.down()
ninja.pencolor("black")
ninja.dot(4)
ninja.pensize(0.1)

dati = open("esponenziale.txt","r")

for file in dati:
    if b==0:
        pop = int(file)
        b = 1
    elif b==1:
        y = float(file)
        y = (y*100*400)/pop
        ninja.goto(i-l,y-c)
        i = i + 7.5
        ninja.dot(4)
dati.close()

ninja.up()
ninja.goto(-l,-c)
ninja.down()
ninja.pencolor("red")
ninja.dot(4)
ninja.pensize(0.1)

dati = open("logica.txt","r")
b=0
i=0
for file in dati:
    if b==0:
        pop = int(file)
        b = 1
    elif b==1:
        y = int(file)
        y = (y*400)/pop
        ninja.goto(i-l,y-c)
        i = i + 7.5
        ninja.dot(4)
dati.close()

dati = open("morte.txt","r")
a = dati.readline()
tm = int(a)
tm = tm/100
dati.close()

ninja.up()
ninja.goto(-l,-c)
ninja.down()
ninja.pencolor("green")
ninja.dot(4)
ninja.pensize(1)

dati = open("guariti.txt","r")
b=0
i=0
for file in dati:
    if b==0:
        pop = int(file)
        b = 1
    elif b==1:
        y = int(file)
        y = y * (1-tm)
        y = (y*400)/pop
        ninja.goto(i-l,y-c)
        i = i + 7.5
        ninja.dot(4)
dati.close()

ninja.up()
ninja.goto(-l,-c)
ninja.down()
ninja.pencolor("grey")
ninja.dot(4)
ninja.pensize(0.8)

dati = open("guariti.txt","r")
b=0
i=0
for file in dati:
    if b==0:
        pop = int(file)
        b = 1
    elif b==1:
        y = int(file)
        y = y * tm
        y = (y*400)/pop
        ninja.goto(i-l,y-c)
        i = i + 7.5
        ninja.dot(4)
dati.close()

ninja.up()
ninja.goto(-l,-c)
ninja.down()
ninja.pencolor("blue")
ninja.dot(4)
ninja.pensize(1)

dati = open("contagi.txt","r")
b=0
i=0
for file in dati:
    if b==0:
        pop = int(file)
        b = 1
    elif b==1:
        y = int(file)
        y = (y*400)/pop
        ninja.goto(i-l,y-c)
        i = i + 7.5
        ninja.dot(4)
dati.close()

screen.exitonclick()
exit()



