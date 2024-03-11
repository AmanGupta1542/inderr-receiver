import tkinter as tk
import time
from .constants import *
import math

STATIONS0 = [
    {
        'name': 'Bhopal Junction',
        'abbr': 'BPL',
        'total_distance': 53.4,
        'raw_distance': 53.4,
        'order': 1,
        'estimate_time': 'Start',
        'delay_time': '-'
    },
    {
        'name': 'Vidisha',
        'abbr': "BHS",
        'total_distance': 92.9,
        'raw_distance': 39.5,
        'order':2,
        'estimate_time': '6:32 p.m.',
        'delay_time': '-'
    },
    {
        'name': 'Ganj Basoda',
        'abbr': "BAQ",
        'total_distance': 121.3,
        'raw_distance': 28.4,
        'order':3,
        'estimate_time': '7:02 p.m.',
        'delay_time': '-'
    },
    {
        'name': 'Mandi Bamora',
        'abbr': "MABA",
        'total_distance': 138.7,
        'raw_distance': 17.4,
        'order':4,
        'estimate_time': '7:27 p.m.',
        'delay_time': '-'
    },
    {
        'name': 'Bina',
        'abbr': "BINA",
        'total_distance': 160.4,
        'raw_distance': 21.7,
        'order':5,
        'estimate_time': '7:55 p.m.',
        'delay_time': '-'
    },
    {
        'name': 'Khurai',
        'abbr': "KYE",
        'total_distance': 213.2,
        'raw_distance': 52.8,
        'order':6,
        'estimate_time': '8:30 p.m.',
        'delay_time': '-'
    },
    {
        'name': 'Saugor',
        'abbr': "SGO",
        'total_distance': 220.3,
        'raw_distance': 7.1,
        'order':7,
        'estimate_time': '9:22 p.m.',
        'delay_time': '-'
    },
    {
        'name': 'Makronia',
        'abbr': "MKRN",
        'total_distance': 251.3,
        'raw_distance': 31,
        'order':8,
        'estimate_time': '9:36 p.m.',
        'delay_time': '-'
    },
    {
        'name': 'Ganeshganj',
        'abbr': "GAJ",
        'total_distance': 264.2,
        'raw_distance': 12.9,
        'order':9,
        'estimate_time': '10:03 p.m.',
        'delay_time': '-'
    },
    {
        'name': 'Patharia',
        'abbr': "PHA",
        'total_distance': 290.3,
        'raw_distance': 26.1,
        'order':10,
        'estimate_time': '10:18 p.m.',
        'delay_time': '-'
    },
    {
        'name': 'Damoh',
        'abbr': "DMO",
        'total_distance': 0,
        'raw_distance': 0,
        'order':11,
        'estimate_time': '10:45 p.m.',
        'delay_time': '-'
    }
]
STATIONS1 = [
    {
        'name': 'station 1',
        'abbr': 'stat',
        'delay_time': '-',
        'estimate_time': '12:00AM',
        'raw_distance': 100.0,
        'order': 1
    },
    {
        'name': 'station 2',
        'abbr': 'stat',
        'delay_time': '-',
        'estimate_time': '12:00AM',
        'raw_distance': 120.0,
        'order':2
    },
    {
        'name': 'station 3',
        'abbr': 'stat',
        'delay_time': '-',
        'estimate_time': '12:00AM',
        'raw_distance': 100.0,
        'order':3
    },
    {
        'name': 'station 4',
        'abbr': 'stat',
        'delay_time': '-',
        'estimate_time': '12:00AM',
        'raw_distance': 200.0,
        'order':4
    },
    {
        'name': 'station 5',
        'abbr': 'stat',
        'delay_time': '-',
        'estimate_time': '12:00AM',
        'raw_distance': 80.0,
        'order':5
    }
]
STATIONS = [
    {
        'name': 'Bhopal Junction',
        'abbr': 'BPL',
        'total_distance': 53.4,
        'distance': 53.4,
        'order': 1,
        'estimate_time': 'Start',
        'delay_time': '-'
    },
    {
        'name': 'Vidisha',
        'abbr': "BHS",
        'total_distance': 92.9,
        'distance': 39.5,
        'order':2,
        'estimate_time': '6:32 p.m.',
        'delay_time': '-'
    },
    {
        'name': 'Ganj Basoda',
        'abbr': "BAQ",
        'total_distance': 121.3,
        'distance': 28.4,
        'order':3,
        'estimate_time': '7:02 p.m.',
        'delay_time': '-'
    },
    {
        'name': 'Mandi Bamora',
        'abbr': "MABA",
        'total_distance': 138.7,
        'distance': 17.4,
        'order':4,
        'estimate_time': '7:27 p.m.',
        'delay_time': '-'
    },
    {
        'name': 'Bina',
        'abbr': "BINA",
        'total_distance': 160.4,
        'distance': 21.7,
        'order':5,
        'estimate_time': '7:55 p.m.',
        'delay_time': '-'
    },
    {
        'name': 'Khurai',
        'abbr': "KYE",
        'total_distance': 213.2,
        'distance': 52.8,
        'order':6,
        'estimate_time': '8:30 p.m.',
        'delay_time': '-'
    },
    {
        'name': 'Saugor',
        'abbr': "SGO",
        'total_distance': 220.3,
        'distance': 7.1,
        'order':7,
        'estimate_time': '9:22 p.m.',
        'delay_time': '-'
    },
    {
        'name': 'Makronia',
        'abbr': "MKRN",
        'total_distance': 251.3,
        'distance': 31,
        'order':8,
        'estimate_time': '9:36 p.m.',
        'delay_time': '-'
    },
    {
        'name': 'Ganeshganj',
        'abbr': "GAJ",
        'total_distance': 264.2,
        'distance': 12.9,
        'order':9,
        'estimate_time': '10:03 p.m.',
        'delay_time': '-'
    },
    {
        'name': 'Patharia',
        'abbr': "PHA",
        'total_distance': 290.3,
        'distance': 26.1,
        'order':10,
        'estimate_time': '10:18 p.m.',
        'delay_time': '-'
    },
    {
        'name': 'Damoh',
        'abbr': "DMO",
        'total_distance': 0,
        'distance': 0,
        'order':11,
        'estimate_time': '10:45 p.m.',
        'delay_time': '-'
    }
]
STATIONS = [
    {
        'name': 'station 1',
        'abbr': 'stat',
        'delay_time': '-',
        'estimate_time': '12:00AM',
        'distance': 100.0,
        'order': 1
    },
    {
        'name': 'station 2',
        'abbr': 'stat',
        'delay_time': '-',
        'estimate_time': '12:00AM',
        'distance': 120.0,
        'order':2
    },
    {
        'name': 'station 3',
        'abbr': 'stat',
        'delay_time': '-',
        'estimate_time': '12:00AM',
        'distance': 100.0,
        'order':3
    },
    {
        'name': 'station 4',
        'abbr': 'stat',
        'delay_time': '-',
        'estimate_time': '12:00AM',
        'distance': 200.0,
        'order':4
    },
    {
        'name': 'station 5',
        'abbr': 'stat',
        'delay_time': '-',
        'estimate_time': '12:00AM',
        'distance': 80.0,
        'order':5
    }
]

DISTANCE_BW_ST_IN_PX = 250
STATION_STRT_PX = 400

# Function to add a new key-value pair
def add_key_value(station):
    station['distance'] = station['raw_distance']+50
    return station

# Use map to apply the function to each dictionary in the list
STATIONS = list(map(add_key_value, STATIONS0))

class StationDesign(tk.Frame):
    def __init__(self, root, height, width, stations):
        self.stations = stations
        self.root = root
        # self.root.title("Horizontal Line and Circle Design")
        self.screen_width = width
        self.screen_height = height
        # self.station_capacity = math.ceil((width - STATION_STRT_PX)/DISTANCE_BW_ST_IN_PX)
        self.station_capacity = 0

        print("screen_width ", self.screen_width)
        print("screen_height ", self.screen_height)
        # print("station_capacity ", self.station_capacity)
        self.shift_call = 0
        # Create a Canvas
        self.canvas = tk.Canvas(root, width=self.screen_width, height=self.screen_height)
        self.canvas.config(highlightthickness=2, highlightbackground=FOOTER_TEXT_COLOR)
        self.canvas.pack()

        self.start_point = 5
        self.x = STATION_STRT_PX
        self.y = int(self.screen_height/2)
        self.circle_radius = 5
        self.line_width = 150
        self.next_x = None

        # Draw horizontal line, circle, and another horizontal line
        self.draw_station_circle()
        self.draw_station_name()
        self.create_train()
        # self.move_train()
        # self.canvas.after(1000, self.move_train)
        self.move_train()

    def draw_station_circle(self):
        self.station_points = []
        for station in self.stations:
            self.line_width = DISTANCE_BW_ST_IN_PX
            if station['order'] ==1:
                station['x_coord'] = self.x
                station['y_coord'] = self.y
                self.station_points.append(self.x)
                print('tag', station['name']+' circle')
                self.draw_circle(self.x, self.y, self.circle_radius, tag=station['abbr']+"_circle") # drawing a circle to represent station
                self.draw_horizontal_line(self.x+self.circle_radius, self.y, self.line_width, tag=station['abbr']+"_line")
                self.next_x = self.x+self.circle_radius+self.line_width
                
            elif station['order'] == len(self.stations):
                # self.draw_circle(self.x+self.circle_radius+self.line_width+self.circle_radius, self.y, self.circle_radius)
                self.draw_circle(self.next_x+self.circle_radius, self.y, self.circle_radius, tag=station['abbr']+"_circle") # drawing a circle to represent station
                self.station_points.append(self.next_x)
                station['x_coord'] = self.next_x
                station['y_coord'] = self.y
            else :
                self.station_points.append(self.next_x)
                station['x_coord'] = self.next_x
                station['y_coord'] = self.y
                self.draw_circle(self.next_x+self.circle_radius, self.y, self.circle_radius, tag=station['abbr']+"_circle") # drawing a circle to represent station
                self.draw_horizontal_line(self.next_x+(self.circle_radius*2), self.y, self.line_width, tag=station['abbr']+"_line")
                self.next_x = self.next_x+(self.circle_radius*2)+self.line_width
        print(self.next_x)
        print(self.station_points)
        print(self.stations)
        for i in range(len(self.station_points)):
            if self.station_points[i] >= self.screen_width:
                self.station_capacity = i
                break
        if self.station_capacity == 0:
            self.station_capacity = len(self.stations)
        print(self.station_capacity)

    def create_train(self):
        
        self.p = self.x - self.start_point
        self.q = self.y - 5
        # self.circle = self.canvas.create_oval(5, 20, 15, 30, fill="red")
        self.train = self.canvas.create_oval(self.p, self.q, self.x+self.circle_radius, self.y +5, fill="red", tag='train')
        # pass
        # self.train = self.draw_circle(self.x, self.y, self.circle_radius, fill='red')

    def shift_stations_left(self, current_station_index):
        print('shifting call')
        self.p = self.station_points[1]
        print(self.p)
        print(self.q)
        print(self.p+10)
        print(self.q+10)


        print('remaining stations are : ', len(self.station_points)-(current_station_index))
        self.canvas.delete("train")
        remove_stat_points = self.station_capacity - 1 if self.shift_call == 0 else self.station_capacity - 2 # station_capacity -1 = 5-1
        print(remove_stat_points)
        print('old',self.station_points)
        if(len(self.station_points)> self.station_capacity-1):
            for i in range(remove_stat_points):
                print(i)
                self.station_points.pop()
        print('new',self.station_points)
        cond = (self.shift_call*(self.station_capacity-2))
        for i in range((self.shift_call*(self.station_capacity-2)) +1 , cond+self.station_capacity):
            print('deleted, ', self.stations[i]['abbr'])
            self.canvas.delete(self.stations[i]['abbr'])
            self.canvas.delete(self.stations[i]['abbr']+"_dt")
            self.canvas.delete(self.stations[i]['abbr']+"_et")
        
        r = (self.station_capacity-1) if len(self.station_points) > (self.station_capacity-1) else (len(self.station_points)) # 11 > 5
        for i in range(r):
            ind = ((self.shift_call*(self.station_capacity-2))+self.station_capacity+i)-1
            self.ind = ind
            print('index', ind)
            print(len(self.stations))
            print('created, ', self.stations[ind]['abbr'])
            x_coord = self.station_points[i]+(self.circle_radius*2)+self.line_width if (i+1 == r and len(self.station_points)<=len(self.station_points)) else self.station_points[i+1]
            print(x_coord)
            if x_coord not in self.station_points:
                print('draw last circle')
                # self.canvas.create_line(x_coord+(self.circle_radius*2), self.y, x_coord+(self.circle_radius*2)+self.line_width, self.y, width=2, fill="black", tags=self.stations[ind]['abbr']+"_line")
                # self.draw_horizontal_line(x_coord+(self.circle_radius*2), self.y, self.line_width, tag=self.stations[ind]['abbr']+"_line")
                # self.draw_circle(x_coord+self.circle_radius, self.y, self.circle_radius, tag=self.stations[ind]['abbr']+"_circle") # drawing a circle to represent station
                self.station_points.append(x_coord)
            self.canvas.create_text(x_coord, self.y+20, text=self.stations[ind]['abbr'], font=('Times New Roman', 15, 'bold'), fill=FOOTER_TEXT_COLOR, tags=self.stations[ind]['abbr'])
            self.canvas.create_text(x_coord, self.y-20, text=self.stations[ind]['delay_time'], font=('Times New Roman', 15, 'bold'), fill=FOOTER_TEXT_COLOR, tags=self.stations[ind]['abbr']+"_dt")
            self.canvas.create_text(x_coord, self.y-40, text=self.stations[ind]['estimate_time'], font=('Times New Roman', 15, 'bold'), fill=FOOTER_TEXT_COLOR, tags=self.stations[ind]['abbr']+"_et")
            
        
        total_leave_station = 0
        print('self.shift_call', self.shift_call)
        for i in range(self.shift_call+1):
            if i==0:
                total_leave_station = total_leave_station+self.station_capacity
            else:
                total_leave_station = total_leave_station+(self.station_capacity-2)
            
        last_created_stat_count = len(self.stations) - total_leave_station
        is_last_round = last_created_stat_count <= (self.station_capacity - 1)
        print(last_created_stat_count)
        print(is_last_round)
        if is_last_round:
            print('stations len', len(self.stations))
            for i in range(last_created_stat_count+1, len(self.stations)):
                print(i)
                self.canvas.delete(self.stations[i]['abbr']+"_line")
                if i+1 < len(self.stations):
                    self.canvas.delete(self.stations[i+1]['abbr']+"_circle") #err

        if self.shift_call == 0:
            self.canvas.delete(self.stations[0]['abbr']+"_line")
            self.draw_horizontal_line(self.station_points[0]+self.circle_radius, self.y, self.line_width, tag=self.stations[0]['abbr']+"_line", dash=(20,10))
        
        # self.canvas.delete(self.stations[0]['abbr']+'_circle')
        self.train = self.canvas.create_oval(self.p, self.q, self.p + 10, self.q + 10, fill="red", tag='train')
        # self.canvas.coords(self.train, self.p, self.q, self.p + 10, self.q + 10)
        self.shift_call = self.shift_call +1

    def check_station_screen_size(self, current_x_coord):
        print('checking')
        current_station_index = self.station_points.index(current_x_coord)
        print(self.station_points)
        # try:
        if current_station_index+1 == len(self.station_points) :
            if len(self.stations) > self.station_capacity:
                if self.ind+1 == len(self.stations):
                    print('Reach Destination')
                    return False
                else:
                    self.shift_stations_left(current_station_index)
                    return True
            else:
                print('Reach Destination')
                return False
        else:
            next_station_x_y = self.station_points[current_station_index+1]
            if next_station_x_y >= self.screen_width:
                self.shift_stations_left(current_station_index)
            return True
        # except IndexError as e:
        #     # if getting index error - list out of range, that means that is the last station
        #     print(e)
        #     print('Reach Destination')
        #     return False




    def move_train(self):
        if(self.p != self.next_x):
            # print(self.p, self.next_x)
            self.p += .1
            self.p = round(self.p, 1)
            # self.q += 1
            # print(self.p)
            move_train_forward = True
            if self.p in self.station_points:
                print(self.screen_width)
                print(self.p)
                move_train_forward = self.check_station_screen_size(self.p)
                print(self.station_points)
                time.sleep(1)
            # Move the circle by dx and dy
            # self.canvas.coords(self.train, self.x, self.y, self.x + 1, self.y + 10)
            self.canvas.coords(self.train, self.p, self.q, self.p + 10, self.q + 10)
            if move_train_forward:
                self.canvas.after(1, self.move_train) # increase value to slow dot move speed

    def draw_station_name(self):
        i = 0
        self.canvas.create_text(self.x-300, self.y-40, text="ET", font=('Times New Roman', 18, 'bold'))
        self.canvas.create_text(self.x-300, self.y-20, text="DT", font=('Times New Roman', 18, 'bold'))
        self.canvas.create_text(self.x-300, self.y+20, text="Station", font=('Times New Roman', 18, 'bold'))

        for station in self.stations:
            # if station['order'] != len(self.stations):
            #     self.canvas.create_text((self.station_points[i]+self.station_points[i+1])/2, self.y+15, text=round((station['distance']-50), 1))
            self.canvas.create_text(self.station_points[i], self.y+20, text=station['abbr'], font=('Times New Roman', 15, 'bold'), fill=FOOTER_TEXT_COLOR, tags=station['abbr'])
            self.canvas.create_text(self.station_points[i], self.y-20, text=f"{'End' if station['delay_time'] is None else station['delay_time']}", font=('Times New Roman', 15, 'bold'), fill=FOOTER_TEXT_COLOR, tags=station['abbr']+"_dt")
            self.canvas.create_text(self.station_points[i], self.y-40, text=f"{'Start' if station['estimate_time'] is None else station['estimate_time']}", font=('Times New Roman', 15, 'bold'), fill=FOOTER_TEXT_COLOR, tags=station['abbr']+"_et")
            i+=1


    def draw_horizontal_line(self, x1, y1, length, tag=None, dash=None):
        x2 = x1 + length
        if tag:
            self.canvas.create_line(x1, y1, x2, y1, width=2, fill="black", tags=tag, dash=dash)
        else:
            self.canvas.create_line(x1, y1, x2, y1, width=2, fill="black")

    def draw_circle(self, x, y, radius, fill=None, tag=None):
        x1, y1 = x - radius, y - radius
        x2, y2 = x + radius, y + radius
        print('draw circle', x1,y1,x2,y2)
        if fill:
            if tag:
                self.canvas.create_oval(x1, y1, x2, y2, outline="black", fill=fill, tags=tag)
            else:
                self.canvas.create_oval(x1, y1, x2, y2, outline="black", fill=fill)
        else:
            if tag:
                self.canvas.create_oval(x1, y1, x2, y2, outline="black", fill=fill, tags=tag)
            else:
                self.canvas.create_oval(x1, y1, x2, y2, outline="black")
    
    def update_train_location(self, data):
        # data will be 
        # data = {
        #     'next_station': {'name': 'Vidisha', 'lat': Decimal('23.522687'), 'lon': Decimal('77.815174'), 'order': 2, 'distance': 49.70376998384893}, 
        #     'curr_location': {'lat': Decimal('23.270723'), 'lon': Decimal('77.414528')}, 
        #     'speed': 0, 
        #     'late_by': 0
        # }
        pass
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = HorizontalLineCircleDesignApp(root)
#     root.mainloop()
