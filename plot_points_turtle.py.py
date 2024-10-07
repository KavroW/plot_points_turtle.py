import turtle

x1 = int(input('Enter the first x value: '))
y1 = int(input('Enter the first y value: '))
x2 = int(input('Enter the second x value: '))
y2 = int(input('Enter the second y value: '))
turtle.home()
turtle.hideturtle()
turtle.color('red')
turtle.up()
turtle.goto(x1,y1)
turtle.down()
turtle.dot(10)
turtle.color('black')
turtle.write(f'({x1},{y1})')
turtle.color('red')
turtle.goto(x2,y2)
turtle.down()
turtle.dot(10)
turtle.color('black')
turtle.write(f'({x2},{y2})')
turtle.exitonclick()



