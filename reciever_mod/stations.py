import tkinter as tk
from .constants import *

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

# Function to add a new key-value pair
def add_key_value(station):
    station['distance'] = station['raw_distance']+50
    return station

# Use map to apply the function to each dictionary in the list
STATIONS = list(map(add_key_value, STATIONS0))

class StationDesign(tk.Frame):
    def __init__(self, root, height, width):
        self.root = root
        # self.root.title("Horizontal Line and Circle Design")
        self.screen_width = width
        self.screen_height = height

        print("screen_width ", self.screen_width)
        print("screen_height ", self.screen_height)

        # Create a Canvas
        self.canvas = tk.Canvas(root, width=self.screen_width, height=self.screen_height)
        self.canvas.config(highlightthickness=2, highlightbackground=FOOTER_TEXT_COLOR)
        self.canvas.pack()

        self.start_point = 5
        self.x = 400
        self.y = int(self.screen_height/2)
        self.circle_radius = 5
        self.line_width = 150
        self.next_x = None

        # Draw horizontal line, circle, and another horizontal line
        self.draw_shape()
        self.draw_station_name()
        self.create_train()
        # self.move_train()
        self.canvas.after(1000, self.move_train)

    def draw_shape(self):
        self.station_points = []
        for station in STATIONS:
            self.line_width = 250
            if station['order'] ==1:
                self.station_points.append(self.x)
                self.draw_circle(self.x, self.y, self.circle_radius)
                self.draw_horizontal_line(self.x+self.circle_radius, self.y, self.line_width)
                self.next_x = self.x+self.circle_radius+self.line_width
                
            elif station['order'] == len(STATIONS):
                # self.draw_circle(self.x+self.circle_radius+self.line_width+self.circle_radius, self.y, self.circle_radius)
                self.draw_circle(self.next_x+self.circle_radius, self.y, self.circle_radius)
                self.station_points.append(self.next_x)
            else :
                self.station_points.append(self.next_x)
                self.draw_circle(self.next_x+self.circle_radius, self.y, self.circle_radius)
                self.draw_horizontal_line(self.next_x+(self.circle_radius*2), self.y, self.line_width)
                self.next_x = self.next_x+(self.circle_radius*2)+self.line_width
        print(self.next_x)
        print(self.station_points)

    def create_train(self):
        
        self.p = self.x - self.start_point
        self.q = self.y - 5
        # self.circle = self.canvas.create_oval(5, 20, 15, 30, fill="red")
        self.train = self.canvas.create_oval(self.p, self.q, self.x+self.circle_radius, self.y +5, fill="red")
        # pass
        # self.train = self.draw_circle(self.x, self.y, self.circle_radius, fill='red')

    def move_train(self):
        if(self.p != self.next_x):
            # print(self.p, self.next_x)
            self.p += .1
            self.p = round(self.p, 1)
            # self.q += 1
            # print(self.x)
            # Move the circle by dx and dy
            # self.canvas.coords(self.train, self.x, self.y, self.x + 1, self.y + 10)
            self.canvas.coords(self.train, self.p, self.q, self.p + 10, self.q + 10)

            self.canvas.after(10, self.move_train)

    def draw_station_name(self):
        i = 0
        self.canvas.create_text(self.x-300, self.y-40, text="ET", font=('Times New Roman', 18, 'bold'))
        self.canvas.create_text(self.x-300, self.y-20, text="DT", font=('Times New Roman', 18, 'bold'))
        self.canvas.create_text(self.x-300, self.y+20, text="Station", font=('Times New Roman', 18, 'bold'))

        for station in STATIONS:
            # if station['order'] != len(STATIONS):
            #     self.canvas.create_text((self.station_points[i]+self.station_points[i+1])/2, self.y+15, text=round((station['distance']-50), 1))
            self.canvas.create_text(self.station_points[i], self.y+20, text=station['abbr'], font=('Times New Roman', 15, 'bold'), fill=FOOTER_TEXT_COLOR)
            self.canvas.create_text(self.station_points[i], self.y-20, text=station['delay_time'], font=('Times New Roman', 15, 'bold'), fill=FOOTER_TEXT_COLOR)
            self.canvas.create_text(self.station_points[i], self.y-40, text=station['estimate_time'], font=('Times New Roman', 15, 'bold'), fill=FOOTER_TEXT_COLOR)
            i+=1


    def draw_horizontal_line(self, x1, y1, length):
        x2 = x1 + length
        self.canvas.create_line(x1, y1, x2, y1, width=2, fill="black")

    def draw_circle(self, x, y, radius, fill=None):
        x1, y1 = x - radius, y - radius
        x2, y2 = x + radius, y + radius
        print('draw circle', x1,y1,x2,y2)
        if fill:
            self.canvas.create_oval(x1, y1, x2, y2, outline="black", fill=fill)
        else:
            self.canvas.create_oval(x1, y1, x2, y2, outline="black")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = HorizontalLineCircleDesignApp(root)
#     root.mainloop()
