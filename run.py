import tkinter as tk
import tkinter.font as font
from os import path
from PIL import Image, ImageTk

current_dir = path.dirname(path.realpath(__file__))

def startGUI():
    # creating a GUI window
    homeWindow = tk.Tk()

    # Getting the screen width and height
    screen_width = homeWindow.winfo_screenwidth()
    screen_height = homeWindow.winfo_screenheight()

    # Getting the center of the screen
    x_axis = (screen_width/2)
    y_axis = (screen_height/2)

    # Button Sizes
    btnSize_x = screen_width * .15
    btnSize_y = screen_height * .30

    # Calculating the sizes of button and distance
    amtRows = 2
    amtBtns = 4

    spacing_X = (screen_width/(amtBtns+1))*0.50
    spacing_y = (screen_width/(amtRows+1))*0.18

    # Buttons
    createButton(homeWindow, "Old Fashioned", homeWindow.destroy, "oldfash.png", spacing_X, spacing_y*0.5, btnSize_x, btnSize_y)
    createButton(homeWindow, "Moscow Mule", homeWindow.destroy, "mosmule.png", 2*spacing_X + btnSize_y, spacing_y*0.5, btnSize_x, btnSize_y)
    createButton(homeWindow, "Negroni", homeWindow.destroy, "neg.png", 3*spacing_X + 2*btnSize_y, spacing_y*0.5, btnSize_x, btnSize_y)
    createButton(homeWindow, "Mojito", homeWindow.destroy, "moj.png", 4*spacing_X + 3*btnSize_y, spacing_y*0.5, btnSize_x, btnSize_y)

    createButton(homeWindow, "Whiskey Sour", homeWindow.destroy, "wsour.png", spacing_X, 2*spacing_y + btnSize_y, btnSize_x, btnSize_y)
    createButton(homeWindow, "Daiquiri", homeWindow.destroy, "dai.png", 2*spacing_X + btnSize_y, 2*spacing_y + btnSize_y, btnSize_x, btnSize_y)
    createButton(homeWindow, "Margarita", homeWindow.destroy, "mar.png", 3*spacing_X + 2*btnSize_y, 2*spacing_y + btnSize_y, btnSize_x, btnSize_y)
    createButton(homeWindow, "Manhattan", homeWindow.destroy, "man.png", 4*spacing_X + 3*btnSize_y, 2*spacing_y + btnSize_y, btnSize_x, btnSize_y)


    homeWindow.configure(background='#282828')
    homeWindow.attributes('-fullscreen', True)
    homeWindow.mainloop()


def createButton(window: tk.Tk, btnTitle: str, command, pictureFileName: str, posX: int, posY: int, btnSizeX: int, btnSizeY: int):
    btnTitle = btnTitle.upper()

    img = Image.open(getImagePath(pictureFileName)).resize((200,200), Image.ANTIALIAS)
    photoImg = ImageTk.PhotoImage(img)

    # Need this for garbage collection
    label = tk.Label(window, image=photoImg)
    label.image=photoImg

    # Fonts
    btnFont = font.Font(family='Courier New', size=40, weight='bold')

    btn = tk.Button(
        window,
        text = btnTitle,
        width= btnSizeX,
        height= btnSizeY,
        bg = "#3E3E3E",
        fg = "#07A66D",
        image=photoImg,
        command= command,
        compound= tk.TOP,
        font=btnFont,
        wraplength=400,
        justify=tk.CENTER,
        borderwidth=0,
        pady=50,
    )

    btn.place(x=posX, y=posY)


def getImagePath(name):
    return path.join(current_dir, "Images", name)


if __name__ == "__main__":
    startGUI()