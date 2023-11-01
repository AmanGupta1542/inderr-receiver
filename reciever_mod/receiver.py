from gtts import gTTS
import os
import socket
from decouple import config
from tkinter import *
import threading

from . import helper_fun as chf

SERVER_IP = config('IP',None)
SERVER_PORT = int(config('PORT',None))

class Receiver:
    fps = 80
    def __init__(self, text_var=''):
        self.root=Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.prevent_close)
        # Header
        # self.header_label = Label(self.root, text='New',font=('Times New Roman',30,'bold'), bg='blue', fg='white')
        # self.header_label.pack(side='top', fill='x')

        self.canvas = Canvas(self.root,bg='blue', highlightthickness=0)
        self.canvas.pack(fill=BOTH, expand=1)
        self.canva_text=self.canvas.create_text(0,0,text='Welcome to Indian Railway',font=('Times New Roman',30,'bold'),fill='yellow',tags=("marquee",),anchor='w')
        
    def prevent_close(self):
        print("Window can not be closed")

    def output_audio(self, text):
        tts = gTTS(text)
        tts.save('output.mp3')
        os.system(f"mpg123 output.mp3")


    def shift(self):
        x1,y1,x2,y2 = self.canvas.bbox("marquee")
        if(x2<0 or y1<0): #reset the coordinates
            x1 = self.canvas.winfo_width()
            y1 = self.canvas.winfo_height()-300
            self.canvas.coords("marquee",x1,y1)
        else:
            self.canvas.move("marquee", -2, 0)
        self.canvas.after(1000//Receiver.fps, self.shift)

    def tk_window(self, text_var=''):
        
        self.root.title('Inderr')
        # self.root.wm_attributes("-zoomed", True)
        self.root.wm_attributes("-fullscreen", True)

        x1,y1,x2,y2 = self.canvas.bbox("marquee")
        width = x2-x1
        height = y2-y1
        self.canvas['width']=width
        self.canvas['height']=height
        fps=60    #Change the fps to make the animation faster/slower
        self.shift()
        self.root.mainloop()

    def update_text(self, text_var):
        self.canvas.itemconfig(self.canva_text, text=text_var)
        x1,y1,x2,y2 = self.canvas.bbox("marquee")
        width = x2-x1
        self.canvas['width']=width
        self.canvas.coords("marquee",width,y1)

    def recieve(self):

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
        # self.update_text(text_var)
        header_label1 = Label(self.root, text='The next Station is',font=('Times New Roman',30,'bold'), bg='blue', fg='white')
        header_label1.place(relx=0.5, rely=0.4, anchor='center')
        header_label2 = Label(self.root, text=text_var[20:],font=('Times New Roman',40,'bold'), bg='blue', fg='yellow')
        header_label2.place(relx=0.5, rely=0.5, anchor='center')
        # call output audio function
        self.output_audio(text_var)

        # Close the sockets
        client_socket.close()
        server_socket.close()
        # tk_window(text_var)

    def recieve_loop(self):
        while True:
            self.recieve()

    def main(self):
        self.t1 = threading.Thread(target=self.recieve_loop)
        self.t1.start()
        
        self.tk_window()