import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def createplot(x, y):
    sns.set(style="white")

    # Get data
    d = pd.read_csv("heart.csv")

    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=(10, 7))

    # Draw the dot plot
    sns.stripplot(data=d, x=x, y=y, hue="target")

    return f


if __name__ == "__main__":

    root = tkinter.Tk()
    root.wm_title("Embedding in Tk")

    label = tkinter.Label(root, text="Matplotlib with Seaborn in Tkinter")
    label.pack()

    fig = create_plot("age", 'sex')

    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack()


    tkinter.mainloop()