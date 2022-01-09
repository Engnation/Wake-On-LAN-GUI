#from tkinter import *
from tkinter import Tk, Label, Frame, BOTTOM, LEFT, Button #base class for tkinter
from wakeonlan import BROADCAST_IP, send_magic_packet

root = Tk()

topFrame = Frame(root) # creates a blank rectangle frame
topFrame.pack() #.pack method places the item in the main window
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

my_label = Label(root, text="Python Wake on LAN Application", bg ="red",fg="white")
my_label.pack()

button1 = Button(topFrame, text="Button 1", fg="red")
button2 = Button(topFrame, text="Button 2", fg="blue")
button3 = Button(topFrame, text="Button 3", fg="green")
button4 = Button(bottomFrame, text="Wake Server", fg="purple")

#button1.pack(side=LEFT)
#button2.pack(side=LEFT)
#button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop() #runs the window event loop so the window stays open

#Send magic packet to wake up target machine

target_1 = open("Target_MAC","r")
target_2 = open("Target_IP","r")
mac_address = str(target_1.read())
ip_address = str(target_2.read())

#print(type(magic_packet))
print(mac_address)

send_magic_packet(mac_address,ip_address = ip_address,port=7)

print('Magic Packet Sent')
