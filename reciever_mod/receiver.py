from gtts import gTTS
import os
import socket
import pickle
import json
import math
from decouple import config
from tkinter import *
import threading
from datetime import datetime, timedelta

from . import helper_fun as chf
from .tk_window import DisplayDesign
from .constants import *

SERVER_IP = config('IP',None)
SERVER_PORT = int(config('PORT',None))
# import pickle

# data = b'\x80\x04\x95.\x06\x00\x00\x00\x00\x00\x00}\x94(\x8c\x05train\x94}\x94(\x8c\x04name\x94\x8c\x12Rajya Rani Express\x94\x8c\x06number\x94M\x91V\x8c\x0cfrom_station\x94\x8c\x0fBhopal Junction\x94\x8c\nto_station\x94\x8c\x05Damoh\x94u\x8c\x08stations\x94]\x94(}\x94(h\x03\x8c\x0fBhopal Junction\x94\x8c\x04abbr\x94\x8c\x03BPL\x94\x8c\x08distance\x94N\x8c\x05order\x94K\x01\x8c\restimate_time\x94N\x8c\ndelay_time\x94\x8c\x08datetime\x94\x8c\x04time\x94\x93\x94C\x06\x117\x00\x00\x00\x00\x94\x85\x94R\x94\x8c\x03lat\x94\x8c\x07decimal\x94\x8c\x07Decimal\x94\x93\x94\x8c\t23.266717\x94\x85\x94R\x94\x8c\x03lon\x94h\x1d\x8c\t77.412920\x94\x85\x94R\x94\x8c\thalt_time\x94Nu}\x94(h\x03\x8c\x07Vidisha\x94h\x0e\x8c\x03BHS\x94h\x10Nh\x11K\x02h\x12h\x16C\x06\x12 \x00\x00\x00\x00\x94\x85\x94R\x94h\x13h\x16C\x06\x12"\x00\x00\x00\x00\x94\x85\x94R\x94h\x1ah\x1d\x8c\t23.522687\x94\x85\x94R\x94h!h\x1d\x8c\t77.815174\x94\x85\x94R\x94h%K\x02u}\x94(h\x03\x8c\x0bGanj Basoda\x94h\x0e\x8c\x03BAQ\x94h\x10Nh\x11K\x03h\x12h\x16C\x06\x13\x02\x00\x00\x00\x00\x94\x85\x94R\x94h\x13h\x16C\x06\x13\x03\x00\x00\x00\x00\x94\x85\x94R\x94h\x1ah\x1d\x8c\t23.846135\x94\x85\x94R\x94h!h\x1d\x8c\t77.944559\x94\x85\x94R\x94h%K\x02u}\x94(h\x03\x8c\x0cMandi Bamora\x94h\x0e\x8c\x04MABA\x94h\x10Nh\x11K\x04h\x12h\x16C\x06\x13\x1b\x00\x00\x00\x00\x94\x85\x94R\x94h\x13h\x16C\x06\x13\x1c\x00\x00\x00\x00\x94\x85\x94R\x94h\x1ah\x1d\x8c\t24.053588\x94\x85\x94R\x94h!h\x1d\x8c\t78.082580\x94\x85\x94R\x94h%K\x02u}\x94(h\x03\x8c\x04Bina\x94h\x0e\x8c\x04BINA\x94h\x10Nh\x11K\x05h\x12h\x16C\x06\x137\x00\x00\x00\x00\x94\x85\x94R\x94h\x13h\x16C\x06\x14\x00\x00\x00\x00\x00\x94\x85\x94R\x94h\x1ah\x1d\x8c\t24.172716\x94\x85\x94R\x94h!h\x1d\x8c\t78.184876\x94\x85\x94R\x94h%K\x02u}\x94(h\x03\x8c\x06Khurai\x94h\x0e\x8c\x03KYE\x94h\x10Nh\x11K\x06h\x12h\x16C\x06\x14\x1e\x00\x00\x00\x00\x94\x85\x94R\x94h\x13h\x16C\x06\x14 \x00\x00\x00\x00\x94\x85\x94R\x94h\x1ah\x1d\x8c\t24.053327\x94\x85\x94R\x94h!h\x1d\x8c\t78.330431\x94\x85\x94R\x94h%K\x02u}\x94(h\x03\x8c\x06Saugor\x94h\x0e\x8c\x03SGO\x94h\x10Nh\x11K\x07h\x12h\x16C\x06\x15\x16\x00\x00\x00\x00\x94\x85\x94R\x94h\x13h\x16C\x06\x15\x19\x00\x00\x00\x00\x94\x85\x94R\x94h\x1ah\x1d\x8c\t23.847723\x94\x85\x94R\x94h!h\x1d\x8c\t78.744192\x94\x85\x94R\x94h%K\x02u}\x94(h\x03\x8c\x08Makronia\x94h\x0e\x8c\x04MKRN\x94h\x10Nh\x11K\x08h\x12h\x16C\x06\x15$\x00\x00\x00\x00\x94\x85\x94R\x94h\x13h\x16C\x06\x15&\x00\x00\x00\x00\x94\x85\x94R\x94h\x1ah\x1d\x8c\t23.866749\x94\x85\x94R\x94h!h\x1d\x8c\t78.809547\x94\x85\x94R\x94h%K\x02u}\x94(h\x03\x8c\nGaneshganj\x94h\x0e\x8c\x03GAJ\x94h\x10Nh\x11K\th\x12h\x16C\x06\x16\x03\x00\x00\x00\x00\x94\x85\x94R\x94h\x13h\x16C\x06\x16\x05\x00\x00\x00\x00\x94\x85\x94R\x94h\x1ah\x1d\x8c\t23.895494\x94\x85\x94R\x94h!h\x1d\x8c\t79.073202\x94\x85\x94R\x94h%K\x02u}\x94(h\x03\x8c\x08Patharia\x94h\x0e\x8c\x03PHA\x94h\x10Nh\x11K\nh\x12h\x16C\x06\x16\x12\x00\x00\x00\x00\x94\x85\x94R\x94h\x13h\x16C\x06\x16\x14\x00\x00\x00\x00\x94\x85\x94R\x94h\x1ah\x1d\x8c\t23.905831\x94\x85\x94R\x94h!h\x1d\x8c\t79.192505\x94\x85\x94R\x94h%K\x02u}\x94(h\x03\x8c\x05Damoh\x94h\x0e\x8c\x03DMO\x94h\x10Nh\x11K\x0bh\x12h\x16C\x06\x16-\x00\x00\x00\x00\x94\x85\x94R\x94h\x13Nh\x1ah\x1d\x8c\t23.835631\x94\x85\x94R\x94h!h\x1d\x8c\t79.431790\x94\x85\x94R\x94h%K\x02ue\x8c\x0cnext_station\x94}\x94(h\x03\x8c\x06Saugor\x94h\x1ah\x1d\x8c\t23.847723\x94\x85\x94R\x94h!h\x1d\x8c\t78.744192\x94\x85\x94R\x94h\x11K\x07h\x10G@\x07Z\x1bZ5wAu\x8c\rcurr_location\x94}\x94(h\x1ah\x1d\x8c\t23.846099\x94\x85\x94R\x94h!h\x1d\x8c\t78.738281\x94\x85\x94R\x94u\x8c\x05speed\x94K\x00\x8c\x07late_by\x94K\x00u.'

# deserialized_data = pickle.loads(data)

# print(deserialized_data)

class Detail:
    def __init__(self, data1, data2, stations, next_station, rem_distance=0):
        ''' data will be in {'curr_location': 'lat': 23.455, 'lon': 33.223, 'datetime': datetime object} format'''
        # distance in km
        self.stations = stations
        self.next_station = next_station
        self.instant_distance, self.rm_distance = self.haversine_distance(data1['curr_location']['lat'], data1['curr_location']['lon'], data2['curr_location']['lat'], data2['curr_location']['lon'], rem_distance)
        self.seconds = self.calc_time_diff(data1['datetime'], data2['datetime'])
        self.instant_speed = self.calc_speed()
        
        self.total_traveled_distance = None

        # To calculate total time store departure time and subtract it with current time stamp and convert return data in hours, 
        # then avg_speed = total_traveled_distance/total_time_taken

    def haversine_distance(self, lat1, lon1, lat2, lon2, remain_dis):
        # Convert Decimal values to float
        lat1, lon1, lat2, lon2 = map(float, [lat1, lon1, lat2, lon2])

        R = 6371  # Radius of the Earth in kilometers
        d_lat = math.radians(lat2 - lat1)
        d_lon = math.radians(lon2 - lon1)

        a = (
            math.sin(d_lat / 2) * math.sin(d_lat / 2) +
            math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
            math.sin(d_lon / 2) * math.sin(d_lon / 2)
        )
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        distance = R * c
        print('distance calculation done')
        rm_distance = float(self.next_station['distance']) - (float(distance)+remain_dis)
        print(rm_distance)
        return (distance,rm_distance)
    
    def calc_time_diff(self, start_time, end_time):
        """
        Calculate the time difference in seconds between two datetime objects.
        
        Args:
            start_time (datetime): The starting datetime.
            end_time (datetime): The ending datetime.
        
        Returns:
            int: The time difference in seconds.
        """
        time_diff = end_time - start_time
        return time_diff.total_seconds()
    
    def calc_speed(self):
        time_diff_hours = self.seconds/3600
        # distance in km, time in hour, so speed in km/h
        speed = self.instant_distance / time_diff_hours  # Speed in kilometers per hour
        return speed
    

class Receiver:
    fps = 80
    def __init__(self, text_var=''):
        self.time_coord_1 = None
        self.time_coord_2 = None
        self.recieved_data = None
        self.station_initialized = False
        # self.output_audio('abc aman')
        self.tk_data_dict = {
            'next_station': '',
            'current_speed': '',
            'late_by': '',
            'stations': ''
            }
        
        self.distance = 0
        self.seconds = 0
        self.instant_speed = 0
        self.remaining_distance = 0
        self.avg_speed = 0
        # self.root=Tk()
        # self.root.protocol("WM_DELETE_WINDOW", self.prevent_close)
        # Header
        # self.header_label = Label(self.root, text='New',font=('Times New Roman',30,'bold'), bg='blue', fg='white')
        # self.header_label.pack(side='top', fill='x')

        # self.canvas = Canvas(self.root,bg='blue', highlightthickness=0)
        # self.canvas.pack(fill=BOTH, expand=1)
        # self.canva_text=self.canvas.create_text(0,0,text='Welcome to Indian Railway',font=('Times New Roman',30,'bold'),fill='yellow',tags=("marquee",),anchor='w')
        
    def prevent_close(self):
        print("Window can not be closed")

    def output_audio(self, text):
        try:
            # Get the current timestamp
            current_timestamp = datetime.now()

            # Format the timestamp as a string (adjust the format as needed)
            timestamp_str = current_timestamp.strftime("%Y-%m-%d_%H-%M-%S")

            tts = gTTS(text)
            tts.save(f"output_{timestamp_str}.mp3")
            os.system(f"mpg123 output_{timestamp_str}.mp3")
        except Exception as e:
            print(f"Error: {e}")


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
        self.dd = DisplayDesign()
        while self.recieved_data is None:
            pass
        # self.stations = self.recieved_data.get('stations', None)
        # if self.station_initialized:
        #     print('Updatinig Display Window')
        #     self.dd.update_data(self.recieved_data)
        # else:
        print('Initializing Display Window')
        self.station_initialized = True
        self.dd.run(self.recieved_data)
        # self.dd.run()
        # self.root.title('Inderr')
        # # self.root.wm_attributes("-zoomed", True)
        # self.root.wm_attributes("-fullscreen", True)

        # x1,y1,x2,y2 = self.canvas.bbox("marquee")
        # width = x2-x1
        # height = y2-y1
        # self.canvas['width']=width
        # self.canvas['height']=height
        # fps=60    #Change the fps to make the animation faster/slower
        # self.shift()
        # self.root.mainloop()

    def update_text(self, text_var):
        self.canvas.itemconfig(self.canva_text, text=text_var)
        x1,y1,x2,y2 = self.canvas.bbox("marquee")
        width = x2-x1
        self.canvas['width']=width
        self.canvas.coords("marquee",width,y1)

    def calc_late_by(self):
        remaining_distance = self.remaining_distance
        avg_speed = self.avg_speed # in kmph
        instent_speed = self.instant_speed # in kmph
        time = remaining_distance/avg_speed # in hours
        totaL_time_to_reach = datetime.now() + timedelta(hours=time)
        next_station = list(filter(lambda x: x.get('name') == self.recieved_data['next_station']['name'], self.recieved_data['stations']))[0]
        # convert next station arrived(estimate_time ) string in python datetime obj
        next_stat_time = datetime.strptime(next_station['estimate_time'], '%H:%M')
        time_difference  = totaL_time_to_reach - next_stat_time
        minutes_difference = time_difference.total_seconds() / 60
        res = minutes_difference
        print(res)
        return res
    
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
        received_data = b''
        print('while start')
        # while True:
        #     # print(received_data)
        #     chunk = client_socket.recv(4096)
        #     if not chunk:
        #         break
        #     received_data+=chunk
        try:
            data = client_socket.recv(4096)
            # timestamp
            # text_var = data.decode('utf-8')
            print('while end')
            deserialized_data = pickle.loads(data)
            self.recieved_data = deserialized_data
            if(self.time_coord_1 is None):
                print("time_coord_1 is none")
                self.time_coord_1 = {'curr_location' :deserialized_data['curr_location'], 'datetime': datetime.now()} # {'curr_location': 'lat': 23.455, 'lon': 33.223, 'datetime': datetime object}
            else :
                print("time_coord_1 is not none")
                # store coordinates in second variable and perform calculatations
                self.time_coord_2 = {'curr_location' :deserialized_data['curr_location'], 'datetime': datetime.now()} # {'curr_location': 'lat': 23.455, 'lon': 33.223, 'datetime': datetime object}
                print('detail start')
                detail = Detail(self.time_coord_1, self.time_coord_2, deserialized_data['stations'], deserialized_data['next_station'], self.remaining_distance)
                print('detail end')
                self.time_coord_1 = self.time_coord_2

                self.distance += detail.instant_distance # in km
                self.seconds += detail.seconds # in seconds
                self.instant_speed = detail.instant_speed
                print('detail end1')
                self.remaining_distance = detail.rm_distance
                print('detail end2')

                self.avg_speed = self.distance / (self.seconds/3600)

                print("***************  DATA START  ***************")
                print("Total Distance", self.distance)
                print("Total Seconds", self.seconds)
                print("Instance Speed", self.instant_speed)
                print("Remaining Distance", self.remaining_distance)
                print("Average Speed", self.avg_speed)
                print("***************  DATA END  ***************")

                deserialized_data['speed'] = detail.instant_speed
                deserialized_data['late_by'] = self.calc_late_by()
            print(deserialized_data)
            # text = data.decode()
            # deserialized_data = json.loads(text)
            # deserialized_data = pickle.loads(data, encoding='utf-8')
            # deserialized_data = json.loads(received_data.decode('utf-8'))
            # print(f"Received data: {deserialized_data}")
            
                #     {
                #     'next_station': text_var,
                #     'current_speed': '20km/h',
                #     'late_by': '30 minutes',
                #     'stations': ''
                #     }
                # )
            # self.update_text(text_var)
            if self.station_initialized:
                print('Updatinig Display Window')
                self.dd.update_data(self.recieved_data)
            # header_label1 = Label(self.root, text='The next Station is',font=('Times New Roman',30,'bold'), bg='blue', fg='white')
            # header_label1.place(relx=0.5, rely=0.4, anchor='center')
            # header_label2 = Label(self.root, text=text_var[20:],font=('Times New Roman',40,'bold'), bg='blue', fg='yellow')
            # header_label2.place(relx=0.5, rely=0.5, anchor='center')
            # call output audio function
            self.output_audio(NEXT_STATION_PREFIX+self.recieved_data['next_station']['name'])

            # Close the sockets
            client_socket.close()
            server_socket.close()
            # tk_window(text_var)
        except pickle.UnpicklingError as e:
            print("Error occur while unpickling : ", e)
        # except Exception as e:
            # print("An unknown error occur : ", e)

    def recieve_loop(self):
        while True:
            self.recieve()

    def main(self):
        self.t1 = threading.Thread(target=self.recieve_loop)
        self.t1.start()
        
        self.tk_window()
