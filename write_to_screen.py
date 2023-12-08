from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import socket
import sys
import struct

import tkinter as tk
from tkinter import *

# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)

# Create a UD socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = '/tmp/CoreFxPipe_testpipe'
print('connecting to {}'.format(server_address))

try:
    sock.connect(server_address)
except socket.error as msg:
    print(msg)
    sys.exit(1)

# Define a function to update the label
def update_label(label):
    message = sock.recv(128)
    if message:
        #label.config(text="Last Word: " + str(message.decode()))
        label.config(text= str(message.decode()))
    # Call this function again after 100ms
    label.after(100, lambda: update_label(label))

# Create the Tkinter root object
root = tk.Tk()
root.title("Last Word Heard...")
root.geometry("1500x1000")
root.configure(bg='#E73E55')

# Create the label and place it in the center of the window
label = tk.Label(root, fg="#F8C9D3", font=('Arial', 200), background="#E73E55",)
label.place(relx=0.5, rely=0.5, anchor=CENTER)

# Start updating the label
update_label(label)

# Start the Tkinter event loop
root.mainloop()

# Close the socket when the program exits
sock.close()
