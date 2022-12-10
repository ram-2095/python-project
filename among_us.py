import turtle

bc = 'red'
bs = ''
gc = 'skyblue'
gs = ''

ft = turtle.Turtle()


""" draws body """
ft.pensize(15)
ft.speed(5)
ft.begin_fill()
ft.fillcolor("red")

    # right side
ft.right(90)
ft.forward(50)
ft.right(180)
ft.circle(40 , -180)
ft.right(180)
ft.forward(200)

    # head curve
ft.right(180)
ft.circle(100 , -180)

    # left side
ft.backward(20)
ft.left(15)
ft.circle(500 , -20)
ft.backward(20)
ft.circle(40 , -180)
ft.left(7)
ft.backward(50)

    # hip
ft.up()
ft.left(90)
ft.forward(10)
ft.right(90)
ft.down()
ft.right(240)
ft.circle(50,-70)
ft.end_fill()

