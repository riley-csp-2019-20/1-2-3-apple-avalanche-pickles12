#   a123_apple_1.py
import turtle as trtl
import time
import random as rand
apple_image = "apple.gif" # Store the file name of your shape
ground_height = -200
apple_letter_x_offset = -25
apple_letter_y_offset = -50


screen_width = 400
screen_lenght = 400
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] 


wn = trtl.Screen()
wn.addshape(apple_image) # Make the screen aware of the new file
wn.setup(width=1.0, height=1.0)

wn.bgpic("tree.gif")
apple = trtl.Turtle()
apple.penup()
wn.tracer(False)

#new code
def reset_apple(active_apple):
  length_of_list = len(letters)
  if (length_of_list != 0):
    index = rand.randint(0,length_of_list)
    #active_apple.goto(rand.randint(-(screen_width)/2), (screen_width)/2), rand.randint(-(screen_height_)/2, (screen_height)/2))
    draw_apple(active_apple, letters.pop(index))


# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple, letter):
  active_apple.shape(apple_image)
  active_apple.showturtle()
  draw_letter(active_apple, letter)
  wn.update()

def drop_apple():
  wn.tracer(True)
  apple.goto(apple.xcor(), ground_height)
  apple.clear()
  apple.hideturtle()
  wn.tracer(False)
  reset_apple(apple)


def draw_letter(active_apple, letter):
  active_apple.color("white")
  remember_position = active_apple.position()
  active_apple.setpos(active_apple.xcor() + apple_letter_x_offset,active_apple.ycor() + apple_letter_y_offset)
  active_apple.write(letter, font=("Arial", 74, "bold"))
  active_apple.setpos(remember_position)

draw_apple(apple, "A")
wn.onkeypress(drop_apple, "a")

wn.listen()
trtl.mainloop()