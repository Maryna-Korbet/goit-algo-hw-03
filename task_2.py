# An example of a command to run in the terminal: python task_2.py --level 4 (level can be changed)

import turtle
import argparse

def koch_snowflake(t, level, size):
    if level == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, level - 1, size / 3)
            t.left(angle)

def draw_koch_snowflake(level, size=300):
    screen = turtle.Screen()
    screen.title("A Koch snowflake")
    screen.bgcolor("black")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()
    t.color('white')
    t.pensize(5)

    for _ in range(3):  
        koch_snowflake(t, level, size)
        t.right(120)

    screen.mainloop()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Creating a Koch snowflake')
    parser.add_argument('--level', type=int, default=3, help='Recursion level')
    args = parser.parse_args()

    if args.level < 0:
        print("The recursion level must be a positive number")
    else:
        draw_koch_snowflake(args.level)

