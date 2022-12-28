import customtkinter as ctk
import re
import PIL as p

class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = ctk.CTkToplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = ctk.CTkLabel(tw, text=self.text, fg_color='#333333', text_color='white', width=190, height=100, corner_radius=10, font=("tahoma", 12))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def CreateToolTip(self, text, row, column, padx=0, pady=0, size=(15, 14)):
    my_image = ctk.CTkImage(light_image=p.Image.open("inforev.png"), dark_image=p.Image.open("inforev.png"), size=size)
    label = ctk.CTkLabel(self, text='', image=my_image)
    label.grid(row=row, column=column, padx=padx, pady=pady)
    toolTip = ToolTip(label)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    label.bind('<Enter>', enter)
    label.bind('<Leave>', leave)