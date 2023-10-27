from gtts import gTTS
import os
import socket

# Define the server address (usually the IP of your Raspberry Pi)
# server_ip = '192.168.137.8' # eathernet
# server_ip = '192.168.43.15'    #Aman Gupta
server_ip = '192.168.1.15' #madhya airtel
#server_ip = '127.0.0.1'
server_port = 1026

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server address and port
server_socket.bind((server_ip, server_port))

# Listen for incoming connections
server_socket.listen(1)

print(f"Listening on {server_ip}:{server_port}")

# Accept a connection from a client
client_socket, client_address = server_socket.accept()

# Receive and print data from the client
data = client_socket.recv(1024)
text_var = data.decode('utf-8')
print(f"Received data: {text_var}")
tts = gTTS(text_var)
tts.save('output.mp3')
os.system(f"mpg123 output.mp3")

# Close the sockets
client_socket.close()
server_socket.close()

from tkinter import *
def shift():
    x1,y1,x2,y2 = canvas.bbox("marquee")
    if(x2<0 or y1<0): #reset the coordinates
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height()//2
        canvas.coords("marquee",x1,y1)
    else:
        canvas.move("marquee", -2, 0)
    canvas.after(1000//fps,shift)
############# Main program ###############
root=Tk()
root.title('Inderr')
root.wm_attributes("-zoomed", True)
canvas=Canvas(root,bg='blue')
canvas.pack(fill=BOTH, expand=1)
# text_var="Hey there Delilah!,What's it like in New York City."
text=canvas.create_text(0,-2000,text=text_var,font=('Times New Roman',60,'bold'),fill='red',tags=("marquee",),anchor='w')
x1,y1,x2,y2 = canvas.bbox("marquee")
width = x2-x1
height = y2-y1
canvas['width']=width
canvas['height']=height
fps=40    #Change the fps to make the animation faster/slower
shift()
root.mainloop()