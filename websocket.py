import serial
import time
from tkinter import *
from tkinter import ttk
import math

# line_length = 30
# line_length2 = 25
# center_x = 50
# center_y = 50

ser = serial.Serial('/dev/ttyUSB0', 9600)
ser2 = serial.Serial('/dev/ttyUSB1', 9600)

root = Tk()

frm = ttk.Frame(root, padding=50)
frm.grid()

ttk.Label(frm, text="Speed").grid(column=0, row=10)

ttk.Label(frm, text="Drehzahl").grid(column=0, row=12)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=0)

def label(txt, col, row):
    ttk.Label(frm, text=txt).grid(column=col, row=row)

label("Speed", 0,10)
label("Km/h", 1,11)

label("Drehzahl", 0,12)
label("1000/min", 1,13)

# win = Tk()
# canvas = Canvas(win, width=100, height=100, bg="white")
# canvas.pack()

while True:
    Speed = ser.readline()
    RotationRate = ser2.readline()
    
    # angle_in_radians = int(Speed) * math.pi / 180
    # end_x = center_x + line_length * math.cos(angle_in_radians)
    # end_y = center_y + line_length * math.sin(angle_in_radians)
    # end_x2 = center_x + line_length2 * math.cos(angle_in_radians)
    # end_y2 = center_y + line_length2 * math.sin(angle_in_radians)

    # line=canvas.create_line(center_x,center_y,end_x,end_y, fill="green", width=5)
    # line=canvas.create_line(center_x,center_y,end_x2,end_y2, fill="white", width=5)

    label(Speed.decode(), 0,11)
    label(RotationRate.decode(), 0,13)

    ser.flushInput();ser.flushOutput()
    ser2.flushInput();ser2.flushOutput()
   
    time.sleep(0.1)
    root.update()

# win.mainloop()
root.mainloop()