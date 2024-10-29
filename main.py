import turtle
import pandas

screen = turtle.Screen()
screen.title("Us States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
score_keeper = 0
guessed_list = []
score = turtle.Turtle()

while len(guessed_list) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_list)} / 50 States Correct",
                                    prompt="What's another state name? ").title()
    if answer_state == "Exit":
        break
    for each in data.state:
        if each == answer_state:
            score.clear()
            score.hideturtle()
            score.penup()
            score.goto(0, 260)
            score_keeper += 1
            score.write(arg=f"Score: {score_keeper}", align="center",
                        font=("Courier", 20, "bold"))
            guessed_list.append(answer_state)
            tim = turtle.Turtle()
            tim.hideturtle()
            tim.penup()
            country_row = data[data.state == answer_state]
            x = int(country_row["x"])
            y = int(country_row["y"])
            tim.goto(x, y)
            tim.write(arg=answer_state, align="center", font=("Courier", 7, "bold"))

list_not_found = {"not found": []}
for each in data.state:
    if each in guessed_list:
        pass
    else:
        list_not_found["not found"].append(each)
        data_not_found = pandas.DataFrame(list_not_found)
        data_not_found.to_csv("states_to_learn.csv")







