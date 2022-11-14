import tkinter as tk
from os import path
from PIL import Image, ImageTk

current_dir = path.dirname(path.realpath(__file__))


def startGUI():
    # creating a GUI window
    homeWindow = tk.Tk()

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~placing of Tkinter window at center
    # Getting the screen width and height
    screen_width = homeWindow.winfo_screenwidth()
    screen_height = homeWindow.winfo_screenheight()

    # Getting the center of the screen
    x_axis = (screen_width/2)
    y_axis = (screen_height/2)

    # Debug Only exit button
    exitBtn = tk.Button(
        homeWindow,
        text=current_dir,
        width=2,
        height=2,
        bg="red",
        fg="black",
        command=homeWindow.destroy,
    )
    exitBtn.place(x=30,y=30)

    createButton(homeWindow, "Test", "img1.png", 60, 60)


    homeWindow.configure(background='#282828')
    homeWindow.attributes('-fullscreen', True)
    homeWindow.mainloop()


def createButton(window, name, pictureFileName, posX, posY):

    img = Image.open(getImagePath(pictureFileName)).resize((50,50), Image.ANTIALIAS)
    photoImg = ImageTk.PhotoImage(img)
    # Need this for garbage collection
    label = tk.Label(window, image=photoImg)
    label.image=photoImg

    btn = tk.Button(
        window,
        text = name,
        width= 100,
        height= 100,
        bg = "#3E3E3E",
        fg = "#07A66D",
        image=photoImg,
        command= window.destroy,
        compound= tk.TOP,
    )

    btn.place(x=posX, y=posY)


def getImagePath(name):
    return path.join(current_dir, "Images", name)


if __name__ == "__main__":
    startGUI()