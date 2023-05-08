import turtle

def generate_tartaglia_triangle(n):
    triangle = [[1]]

    for i in range(1, n):
        row = [1]

        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        row.append(1)
        triangle.append(row)

    return triangle

def draw_tartaglia_triangle(triangle):
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-150, 150)

    for row in triangle:
        x_start = turtle.xcor()
        for cell_value in row:
            turtle.write(cell_value, align="center", font=("Arial", 12, "normal"))
            turtle.forward(30)
        y_start = turtle.ycor() - 30
        turtle.goto(x_start, y_start)

    turtle.hideturtle()
    turtle.done()

tartaglia_triangle = generate_tartaglia_triangle(10)
draw_tartaglia_triangle(tartaglia_triangle)
