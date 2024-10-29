import turtle

screen = turtle.Screen()
screen.title("Us States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answwer_state = screen.textinput(title="Guess the State", prompt="Whar's another state's name? ")


turtle.mainloop()


