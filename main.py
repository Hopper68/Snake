from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# File change 3

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")

# This turns the tracer off to halt turtle animation to later be rendered with screen.update()
screen.tracer(0)

# Creates scoreboard object
scoreboard = Scoreboard()

# Creates snake object from Snake class in snake.py
snake = Snake()

# Creates food object from the Food class in food.py
food = Food()

# Turn on key listener for arrow keys, bound to snake.[direction]
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True

while game_is_on:
    # This restarts display previously set by screen.tracer(0).  This delays display until after code execution of loop below
    screen.update()

    # with time module imported, this tells processing to sleep for .1 seconds
    time.sleep(.1)

    # Can now invoke the move method of snake object
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        ## Removed these and using reset function added to scoreboard instead
        # game_is_on = False  # Exists while loop to end game
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail (avoid detecting collision with head or will error on start)
    for segment in snake.segments[1:]:  # Defines range of loop using slicing, by looping through all segments except the first one (segments[0]).
        if snake.head.distance(segment) < 10:
            ## Removed these and using reset function added to scoreboard instead
            # game_is_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
