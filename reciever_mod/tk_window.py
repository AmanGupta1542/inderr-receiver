from tkinter import *
from time import strftime
from datetime import datetime

from .constants import *
from .stations import StationDesign

class DisplayDesign():
    def __init__(self, *args, **kwargs):
        self.data_dict = None
        self.root = root = Tk()
        self.root.title("Inderr")
        # self.root.state("zoomed")
        self.root.wm_attributes("-fullscreen", True)
        self.root.geometry("1300x677")
        self.root.protocol("WM_DELETE_WINDOW", self.prevent_close)
        self.root.configure(bg='blue')

        self.WINDOW_WIDTH = self.root.winfo_screenwidth()
        self.WINDOW_HEIGHT = self.root.winfo_screenheight()
        self.station_obj = None

    def prevent_close(self):
        print("Window can not be closed")

    def main_frame(self):

        self.header_frame = Frame(self.root, highlightbackground=HEADER_BG_COLOR, highlightthickness=HIGHLIGHTTHICKNESS, bg=HEADER_BG_COLOR)
        self.header_frame.pack_propagate(False)
        self.header_frame.configure(width=self.WINDOW_WIDTH, height=60)
        self.footer_frame = Frame(self.root)
        # self.footer_frame = Frame(self.root, highlightbackground=HEADER_BG_COLOR, highlightthickness=HIGHLIGHTTHICKNESS, bg=HEADER_BG_COLOR)
        self.footer_frame.pack_propagate(False)
        self.footer_frame.configure(width=self.WINDOW_WIDTH, height=400)
        self.body_frame = Frame(self.root)
        # self.body_frame = Frame(self.root, highlightbackground="blue", highlightthickness=HIGHLIGHTTHICKNESS)
        self.header_frame.pack()
        self.body_frame.pack(fill="both", expand=True)
        # self.body_frame.configure(width=self.WINDOW_WIDTH, height=self.WINDOW_HEIGHT* 0.6)
        self.footer_frame.pack(side = BOTTOM)
        height_of_footer_frame = self.footer_frame.winfo_reqheight()
        print(f"Height of self.footer_frame: {height_of_footer_frame}")

    def sub_frames(self):
        
        self.header()
        self.body()
        self.footer()


    def header(self):
        print(self.WINDOW_WIDTH, self.WINDOW_HEIGHT* 0.6)

        def shift():
            x1, y1, x2, y2 = canvas.bbox("marquee")
            if x2 < 0:
                # Reset the coordinates to start from the right edge at the bottom
                x1 = canvas.winfo_width()
                y1 = 25  # Adjust this value to control the height from the bottom
                canvas.coords("marquee", x1, y1)
            else:
                canvas.move("marquee", -2, 0)
            canvas.after(1000 // fps, shift)
        # wel_message = Label(self.header_frame, text="Welcome to Indian railway")
        # wel_message.place(x=10, y=50)

        # Canvas for the marquee
        canvas = Canvas(self.header_frame, bg=HEADER_BG_COLOR, bd=0, highlightthickness=0, relief='ridge')
        canvas.pack(fill=BOTH, expand=1)

        text_var = "Welcome to the Indian Railways"
        text = canvas.create_text(0, 25, text=text_var, font=('Times New Roman', 30, 'bold'), fill=HEADER_TEXT_COLOR, tags=("marquee",), anchor='w')

        x1, y1, x2, y2 = canvas.bbox("marquee")
        width = x2 - x1
        height = y2 - y1
        canvas['width'] = width
        canvas['height'] = height
        fps = 100  # Change the fps to make the animation faster/slower
        shift()

    def body(self):
        
        self.data_left_frame = Frame(self.body_frame, highlightbackground=BODY_TABLE_BOARDER_COLOR, highlightthickness=HIGHLIGHTTHICKNESS)
        self.data_right_frame = Frame(self.body_frame, highlightbackground=BODY_TABLE_BOARDER_COLOR, highlightthickness=HIGHLIGHTTHICKNESS)
        self.data_left_frame.pack_propagate(False)
        self.data_left_frame.configure(width=self.WINDOW_WIDTH/2, height=200)
        self.data_left_frame.pack(side = LEFT)
        self.data_right_frame.pack_propagate(False)
        self.data_right_frame.configure(width=self.WINDOW_WIDTH/2, height=200)
        self.data_right_frame.pack(side = LEFT)

        self.w1 = Label(self.data_left_frame, text="The next stations is", font=(FONT_TYPE, 30, 'bold'))
        self.w1.pack()
        self.w2 = Label(self.data_left_frame, text=self.data_dict['next_station']['name'], font=(FONT_TYPE, 30, 'bold'))
        self.w2.pack()

        self.t1 = Frame(self.data_right_frame, highlightbackground=BODY_TABLE_BOARDER_COLOR, highlightthickness=HIGHLIGHTTHICKNESS)
        self.t1.pack(fill=BOTH, expand =1)
        self.speed_l = Label(self.t1, text=f"Speed ", font=(FONT_TYPE, FONT_SIZES['h1'], 'bold'))
        self.speed_l.pack(side = LEFT, padx=10)

        self.speed_r = Label(self.t1, text=f"{self.data_dict['speed']}", font=(FONT_TYPE, FONT_SIZES['h1'], 'bold'))
        self.speed_r.pack(side = RIGHT, padx=10)
        

        ################################
        # time = Label(self.data_right_frame, text="Time - 12:11AM", font=(FONT_TYPE, FONT_SIZES['h3'], 'bold'))
        self.t2 = Frame(self.data_right_frame, highlightbackground=BODY_TABLE_BOARDER_COLOR, highlightthickness=HIGHLIGHTTHICKNESS)
        self.t2.pack(fill=BOTH, expand =1)
        self.time_l = Label(self.t2, text=f"Time ", font=(FONT_TYPE, FONT_SIZES['h1'], 'bold'))
        self.time_l.pack(side = LEFT, padx=10)

        self.time_r = Label(self.t2, font=(FONT_TYPE, FONT_SIZES['h1'], 'bold'))
        self.time_r.pack(side = RIGHT, padx=10)
        
        def update_time():
            now = strftime("%H:%M:%S")
            self.time_r.config(text=now)

            # now = datetime.now()
            # # Format the date and time
            # formatted_date_time = now.strftime("%d-%m-%Y %H:%M:%S %p") 
            # time.config(text=formatted_date_time)

            self.data_right_frame.after(1000, update_time)
        update_time()
        ################################

        
        self.late = Label(self.data_right_frame, text=f"Late by {self.data_dict['late_by']}", font=(FONT_TYPE, FONT_SIZES['h1'], 'bold'))
        self.late.pack(fill=BOTH,side = LEFT, padx=10)
        # frame = Frame(self.data_right_frame, height=100,width=150,bg="black")
        # frame.pack()

    def footer(self):
        self.station_obj = StationDesign(self.footer_frame, self.footer_frame.winfo_reqheight(), self.footer_frame.winfo_reqwidth(), self.data_dict['stations'])
        
        # self.stat = Label(self.footer_frame, text="Stations detail", width=self.WINDOW_WIDTH)
        # self.stat.pack()

    def run(self, data):
        self.data_dict = data
        self.main_frame()
        self.sub_frames()
        self.root.mainloop()

    def update_data(self, data):
        self.data_dict = data
        # try:
        print('station_obj : is none')
        if self.station_obj is not None:
            print('station object created')
            self.w2.config(text=data['next_station']['name'])
            inst_speed = round(data['next_station']['instant_speed'], 2)
            inst_speed_str = str(inst_speed)+" km/h"
            self.speed_r.config(text=inst_speed_str)
            # late_by_txt = 'Early By '+str(round(data['late_by'], 2))+ 'minutes' if data['late_by'] < 0 else 'Late By '+str(round(data['late_by'], 2))+ 'minutes'
            late_stat = data['next_station']['late_by']
            self.late.config(text=late_stat)
            if 'late' in late_stat.lower():
                color = 'red'
            else:
                color = 'blue'
            self.late.config(fg=color)
            self.station_obj.update_train_location(data)
        # except Exception as e:
            # print(e)


# if __name__ == "__main__":
#     DisplayDesign(data_dict={'next_station': 'Saugor'})
