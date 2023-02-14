import turtle
import pandas

printer = turtle.Turtle()
printer.penup()
printer.hideturtle()
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

score = 0
answer_archive = []
game_is_on = True

data = pandas.read_csv('50_states.csv')


def get_coord(ans):
    new_x = int(data[data.state == ans].x)
    new_y = int(data[data.state == ans].y)
    output = (new_x, new_y)
    return output


answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
while game_is_on:
    if answer_state in list(data.state) and answer_state not in answer_archive:
        score += 1
        answer_archive.append(answer_state)
        coordinate = get_coord(answer_state)
        printer.goto(coordinate)
        printer.write(f"{answer_state}")
        if score == 50:
            print("Game has ended, you have won!")
            game_is_on = False
        else:
            answer_state = screen.textinput(title=f"{score}/50 States Correct",
                                            prompt="What's another state's name?").title()
    elif answer_state in answer_archive:
        answer_state = screen.textinput(title=f"\"{answer_state}\" is Repeated",
                                        prompt="What's another state's name?").title()
    elif answer_state == "Exit":
        missing_state = [state for state in list(data.state) if state not in answer_archive]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break
    else:
        answer_state = screen.textinput(title=f"\"{answer_state}\" is Wrong",
                                        prompt="What's another state's name?").title()

screen.exitonclick()
