from gtts import gTTS
import os
import socket
from decouple import config
from tkinter import *

from . import helper_fun as chf

SERVER_IP = config('IP',None)
SERVER_PORT = int(config('PORT',None))

    
def output_audio(text):
    tts = gTTS(text)
    tts.save('output.mp3')
    os.system(f"mpg123 output.mp3")



def tk_window(text_var=''):
    
    def shift():
        x1,y1,x2,y2 = canvas.bbox("marquee")
        if(x2<0 or y1<0): #reset the coordinates
            x1 = canvas.winfo_width()
            y1 = canvas.winfo_height()//2
            canvas.coords("marquee",x1,y1)
        else:
            canvas.move("marquee", -2, 0)
        canvas.after(1000//fps,shift)

    root=Tk()
    root.title('Inderr')
    root.wm_attributes("-zoomed", True)
    canvas=Canvas(root,bg='blue')
    canvas.pack(fill=BOTH, expand=1)
    text=canvas.create_text(0,-2000,text=text_var,font=('Times New Roman',60,'bold'),fill='red',tags=("marquee",),anchor='w')
    x1,y1,x2,y2 = canvas.bbox("marquee")
    width = x2-x1
    height = y2-y1
    canvas['width']=width
    canvas['height']=height
    fps=60    #Change the fps to make the animation faster/slower
    shift()
    root.mainloop()


def recieve():

    # tk_window()

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Bind the socket to the server address and port
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((SERVER_IP, SERVER_PORT))
    except OSError as e:
        print(e)

    # Listen for incoming connections
    server_socket.listen(1)

    print(f"Listening on {SERVER_IP}:{SERVER_PORT}")

    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()

    # Receive and print data from the client
    data = client_socket.recv(1024)
    text_var = data.decode('utf-8')
    print(f"Received data: {text_var}")

    # call output audio function
    output_audio(text_var)

    # Close the sockets
    client_socket.close()
    server_socket.close()
    # tk_window(text_var)