# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)
    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sea(canvas, scene_width, scene_height)
    draw_sky(canvas, scene_width, scene_height)
    mr_fisherman(canvas)

    draw_grid(canvas, scene_width, scene_height, 50)


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_grid(canvas, width, height, interval):
    text_pos = 10
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill="red")
        draw_text(canvas, x, text_pos, f"{x}", fill="green1")

    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, fill="red")
        draw_text(canvas, text_pos, y, f"{y}", fill="green1")


def draw_sky(canvas, width, height):
    draw_rectangle(canvas, 0, height / 3, width, height, width=0, fill="sky blue")
    draw_oval(canvas, 0, 470, 100, 500, outline="ghostWhite", fill="ghostWhite")
    draw_oval(canvas, 80, 460, 250, 500, outline="ghostWhite", fill="ghostWhite")
    draw_oval(canvas, 350, 470, 550, 500, outline="ghostWhite", fill="ghostWhite")
    draw_oval(canvas, 450, 460, 590, 490, outline="ghostWhite", fill="ghostWhite")

    mr_sun(canvas)
    birdy_birdy(canvas)


def mr_sun(canvas):
    draw_oval(canvas, 700, 400, 900, 600, outline="gold1", fill="gold1")
    draw_line(canvas, 700, 490, 650, 490, fill="gold1")
    draw_line(canvas, 715, 455, 650, 425, fill="gold1")
    draw_line(canvas, 735, 425, 690, 370, fill="gold1")
    draw_line(canvas, 770, 410, 750, 340, fill="gold1")


def birdy_birdy(canvas):
    draw_arc(canvas, 50, 400, 100, 450, start=0, extent=180)
    draw_arc(canvas, 100, 400, 150, 450, start=0, extent=180)

    draw_arc(canvas, 200, 350, 250, 400, start=0, extent=180)
    draw_arc(canvas, 250, 350, 300, 400, start=0, extent=180)


def draw_sea(canvas, width, height):
    draw_rectangle(canvas, 0, 0, width, height / 3, width=0, fill="dodgerBlue1")
    draw_oval(canvas, 300, 50, 720, 300,  width=1, fill="tan4")
    fish(canvas)


def mr_fisherman(canvas):
    draw_oval(canvas, 500, 250, 550, 300, width=0, fill="tan")
    draw_oval(canvas, 510, 275, 515, 280, fill="black")
    draw_oval(canvas, 535, 275, 540, 280, fill="black")
    draw_arc(canvas, 515, 300, 535, 260, start=230, extent=90)
    draw_rectangle(canvas, 500, 168, 550, 250, width=0, fill="tan")

    fishing_rod(canvas)


def fishing_rod(canvas):
    draw_line(canvas, 500, 240, 454, 200, fill="black")
    draw_line(canvas, 545, 240, 460, 191, fill="black")
    draw_line(canvas, 250, 300, 465, 190, width=8, fill="gray49")
    draw_line(canvas, 250, 300, 150, 80)


def fish(canvas):
    draw_oval(canvas, 80, 60, 150, 95, width=0, fill="gold1")
    draw_oval(canvas, 130, 80, 135, 85, fill="black")
    draw_polygon(canvas, 50, 60, 50, 90, 80, 75, outline="gold1", fill="gold1")

    draw_oval(canvas, 230, 50, 330, 95, width=0, fill="turquoise4")
    draw_oval(canvas, 300, 70, 310, 75, fill="black")
    draw_polygon(canvas, 200, 50, 200, 90, 230, 70, outline="turquoise4", fill="turquoise4")

    draw_oval(canvas, 680, 50, 750, 70, width=0, fill="yellow1")
    draw_oval(canvas, 690, 60, 695, 65, fill="black")
    draw_polygon(canvas, 780, 50, 780, 75, 750, 60, outline="yellow1", fill="yellow1")

# Call the main function so that
# this program will start executing.
main()