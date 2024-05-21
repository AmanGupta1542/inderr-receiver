from tkinter import *
from time import strftime
from datetime import datetime

from .constants import *
from .stations import StationDesign
import sys

class DisplayDesign():
    def __init__(self, *args, **kwargs):
        self.data_dict = None
        try:
            self.root = root = Tk()
        except tk.TclError:
            print("Failed to start Tkinter. Running in non-GUI mode.")
            # Handle non-GUI mode or exit
            sys.exit(1)
        self.root.title("Inderr")
        # self.root.state("zoomed")
        self.root.wm_attributes("-fullscreen", True)
        self.root.geometry("1300x677")
        self.root.protocol("WM_DELETE_WINDOW", self.prevent_close)
        self.root.configure(bg='blue')

        self.WINDOW_WIDTH = self.root.winfo_screenwidth()
        self.WINDOW_HEIGHT = self.root.winfo_screenheight()
        self.station_obj = None
        self.cur_formated_date = datetime.now().strftime("%d-%m-%Y")

    def prevent_close(self):
        print("Window can not be closed")

    def main_frame(self):
        self.new_header = Frame(self.root, highlightbackground=HEADER_BG_COLOR, highlightthickness=HIGHLIGHTTHICKNESS, bg=HEADER_BG_COLOR)
        self.new_header.pack_propagate(False)
        self.header_height = int((self.WINDOW_HEIGHT*20)/100)
        self.new_header.configure(width=self.WINDOW_WIDTH, height=self.header_height)

        self.new_header.pack()
        # Create the inner frame with red background
        # inner_frame_width = int(self.WINDOW_WIDTH * 0.3)
        # self.inner_frame = Frame(self.new_header, bg="red", width=inner_frame_width)
        # self.inner_frame.pack(side=LEFT, fill=Y)

        # # Create a label inside the inner frame
        # label_text = "Label Inside Red Frame"
        # label = Label(self.inner_frame, text=label_text, bg="red", fg="white")
        # label.pack(pady=10)  # Adjust padding as needed

        self.body_frame = Frame(self.root)
        # self.body_frame = Frame(self.root, highlightbackground="blue", highlightthickness=HIGHLIGHTTHICKNESS)
        self.body_frame.pack(fill="both", expand=True)
        # self.body_frame.configure(width=self.WINDOW_WIDTH, height=self.WINDOW_HEIGHT* 0.6)
        # self.footer_frame = Frame(self.root)
        # # self.footer_frame = Frame(self.root, highlightbackground=HEADER_BG_COLOR, highlightthickness=HIGHLIGHTTHICKNESS, bg=HEADER_BG_COLOR)
        # self.footer_frame.pack_propagate(False)
        # self.footer_frame.configure(width=self.WINDOW_WIDTH, height=400)
        # self.footer_frame.pack()
        # height_of_footer_frame = self.footer_frame.winfo_reqheight()
        # print(f"Height of self.footer_frame: {height_of_footer_frame}")
        self.header_frame = Frame(self.root, highlightbackground=HEADER_BG_COLOR, highlightthickness=HIGHLIGHTTHICKNESS, bg=HEADER_BG_COLOR)
        self.header_frame.pack_propagate(False)
        self.header_frame.configure(width=self.WINDOW_WIDTH, height=60)
        self.header_frame.pack()

    def sub_frames(self):
        self.new_header_setup()
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

    def new_header_setup(self):
        # Create the inner frame with red background
        inner_frame_width = int(self.WINDOW_WIDTH * 0.35)
        self.inner_frame = Frame(self.new_header, bg=HEADER_BG_COLOR, width=inner_frame_width)
        self.inner_frame.pack(side=LEFT, fill=Y)
        

        # Create a label inside the inner frame
        label_text = "Bhopal Junction"
        label_font_size = self.calculate_font_size(label_text, inner_frame_width)
        label = Label(self.inner_frame, text=label_text, bg=HEADER_BG_COLOR, fg=HEADER_TEXT_COLOR, font=("Arial", label_font_size, "bold"), wraplength=inner_frame_width)
        label.pack(pady=10, fill="x", expand=True)  # Adjust padding as needed
        # label.configure(wraplength=inner_frame_width)

        inner_frame3_width = 45
        print("arrow frame width", inner_frame3_width)
        self.inner_frame3 = Frame(self.new_header, bg=HEADER_BG_COLOR, width=inner_frame3_width)
        self.inner_frame3.pack(side=LEFT, fill=Y)
        height_inner_frame3 = int(self.header_height //2)
        # Create a canvas covering the entire frame
        canvas = Canvas(self.inner_frame3, bg=HEADER_BG_COLOR, width=inner_frame3_width, bd=0, highlightthickness=0)
        canvas.pack(fill=BOTH, expand=True)
        print("arrow frame width", inner_frame3_width)

        # drawing arrow in the canvas
        canvas.create_line(0, height_inner_frame3, 30, height_inner_frame3, width=10, fill="black")

        # Draw the triangle
        triangle_points = [(30, height_inner_frame3-10), (30, height_inner_frame3+10), (45, height_inner_frame3)]
        canvas.create_polygon(triangle_points, fill="black", outline="black")

        inner_frame2_width = int(self.WINDOW_WIDTH * 0.35)
        self.inner_frame2 = Frame(self.new_header, bg=HEADER_BG_COLOR, width=inner_frame2_width)
        self.inner_frame2.pack(side=LEFT, fill=Y)

        label_text = "Virangana Lakshmibai Jhansi Junction"
        label_text = "Vidisha "
        label_font_size = self.calculate_font_size(label_text, inner_frame2_width)
        label = Label(self.inner_frame2, text=label_text, bg=HEADER_BG_COLOR, fg=HEADER_TEXT_COLOR, font=("Arial", label_font_size, "bold"), wraplength=inner_frame_width)
        label.pack(pady=10, fill="x", expand=True)  # Adjust padding as needed

        
        inner_frame3_width = int(self.WINDOW_WIDTH * 0.25)
        self.inner_frame3 = Frame(self.new_header, bg=HEADER_BG_COLOR, width=inner_frame3_width)
        self.inner_frame3.pack(side=RIGHT, fill=Y)

        label_text1 = datetime.now().strftime("%d-%m-%Y")
        label_font_size = self.calculate_font_size(label_text1, inner_frame3_width)
        self.top_right_label1 = Label(self.inner_frame3, text=self.cur_formated_date, bg=HEADER_BG_COLOR, fg=HEADER_TEXT_COLOR, font=("Arial", label_font_size-7, "bold"))
        self.top_right_label1.pack(pady=10, fill="x", expand=True)
        label_text2 = datetime.now().strftime("%H:%M:%S")
        self.top_right_label2 = Label(self.inner_frame3, text='', bg=HEADER_BG_COLOR, fg=HEADER_TEXT_COLOR, font=("Arial", label_font_size-7, "bold"))
        self.top_right_label2.pack(pady=10, fill="x", expand=True)  # Adjust padding as needed

        label_text3 = "Next Stop"
        label_font_size = self.calculate_font_size(label_text3, inner_frame3_width)
        self.top_right_label3 = Label(self.inner_frame3, text=label_text3, bg=HEADER_BG_COLOR, fg=HEADER_TEXT_COLOR, font=("Arial", label_font_size-18, "bold"))
        self.top_right_label3.pack(pady=10, fill="x", expand=True)
        label_text4 = str(120)+" km"
        self.top_right_label4 = Label(self.inner_frame3, text='', bg=HEADER_BG_COLOR, fg=HEADER_TEXT_COLOR, font=("Arial", label_font_size-18, "bold"))
        self.top_right_label4.pack(pady=10, fill="x", expand=True)  # Adjust padding as needed

        label_text5 = "Speed"
        label_font_size = self.calculate_font_size(label_text5, inner_frame3_width)
        self.top_right_label5 = Label(self.inner_frame3, text=label_text5, bg=HEADER_BG_COLOR, fg=HEADER_TEXT_COLOR, font=("Arial", label_font_size-57, "bold"))
        self.top_right_label5.pack(pady=10, fill="x", expand=True)
        label_text6 = str(120)+" kmph"
        self.top_right_label6 = Label(self.inner_frame3, text='', bg=HEADER_BG_COLOR, fg=HEADER_TEXT_COLOR, font=("Arial", label_font_size-57, "bold"))
        self.top_right_label6.pack(pady=10, fill="x", expand=True)  # Adjust padding as needed
        
        def update_time():
            now = strftime("%H:%M:%S")
            cur_date = datetime.now().strftime("%d-%m-%Y")
            self.top_right_label2.config(text=now)
            if self.cur_formated_date != cur_date:
                self.top_right_label1.config(text=cur_date)

            # now = datetime.now()
            # # Format the date and time
            # formatted_date_time = now.strftime("%d-%m-%Y %H:%M:%S %p") 
            # time.config(text=formatted_date_time)

            self.inner_frame.after(1000, update_time)
        update_time()
        

    def calculate_font_size(self, text, frame_width):
        font_size = 1
        while True:
            label_width = Label(self.inner_frame, text=text, font=("Arial", font_size)).winfo_reqwidth()
            if label_width >= frame_width:
                break
            font_size += 1
        return font_size

    def body(self):
        
        self.data_left_frame = Frame(self.body_frame, bg=HEADER_TEXT_COLOR)
        self.data_right_frame = Frame(self.body_frame, bg=HEADER_TEXT_COLOR)
        self.data_left_frame.pack_propagate(False)
        self.data_left_frame.configure(width=self.WINDOW_WIDTH/2, height=200)
        self.data_left_frame.pack(side = LEFT)
        self.data_right_frame.pack_propagate(False)
        self.data_right_frame.configure(width=self.WINDOW_WIDTH/2, height=200)
        self.data_right_frame.pack(side = LEFT)

        inner_frame2_width = int(self.WINDOW_WIDTH/2)

        label_text = "Next Halting Station"
        label_font_size = self.calculate_font_size(label_text, inner_frame2_width)

        self.w1 = Label(self.data_left_frame, text=label_text, font=(FONT_TYPE, label_font_size, 'bold'), bg=HEADER_TEXT_COLOR, fg=HEADER_BG_COLOR)
        self.w1.pack(padx=20 )
        self.w1.configure(wraplength=self.WINDOW_WIDTH/2)
        self.w1.place(relx=0.5, rely=0.5, anchor="center")

        label_text2 = "Virangana Lakshmibai Jhansi Junction"
        label_font_size2 = self.calculate_font_size(label_text2, inner_frame2_width)
        self.w2 = Label(self.data_right_frame, text=label_text2, font=(FONT_TYPE, label_font_size, 'bold'), bg=HEADER_TEXT_COLOR, fg=HEADER_BG_COLOR)
        self.w2.pack(padx=20 )
        self.w2.configure(wraplength=self.WINDOW_WIDTH/2)
        self.w2.place(relx=0.5, rely=0.5, anchor="center")

        # self.t1 = Frame(self.data_right_frame, highlightbackground=BODY_TABLE_BOARDER_COLOR, highlightthickness=HIGHLIGHTTHICKNESS)
        # self.t1.pack(fill=BOTH, expand =1)
        # self.speed_l = Label(self.t1, text=f"Speed ", font=(FONT_TYPE, FONT_SIZES['h1'], 'bold'))
        # self.speed_l.pack(side = LEFT, padx=10)

        # self.speed_r = Label(self.t1, text=f"{self.data_dict['speed']}", font=(FONT_TYPE, FONT_SIZES['h1'], 'bold'))
        # self.speed_r.pack(side = RIGHT, padx=10)
        

        ################################
        # time = Label(self.data_right_frame, text="Time - 12:11AM", font=(FONT_TYPE, FONT_SIZES['h3'], 'bold'))
        # self.t2 = Frame(self.data_right_frame, highlightbackground=BODY_TABLE_BOARDER_COLOR, highlightthickness=HIGHLIGHTTHICKNESS)
        # self.t2.pack(fill=BOTH, expand =1)
        # self.time_l = Label(self.t2, text=f"Time ", font=(FONT_TYPE, FONT_SIZES['h1'], 'bold'))
        # self.time_l.pack(side = LEFT, padx=10)

        # self.time_r = Label(self.t2, font=(FONT_TYPE, FONT_SIZES['h1'], 'bold'))
        # self.time_r.pack(side = RIGHT, padx=10)
        
        # def update_time():
        #     now = strftime("%H:%M:%S")
        #     self.time_r.config(text=now)

        #     # now = datetime.now()
        #     # # Format the date and time
        #     # formatted_date_time = now.strftime("%d-%m-%Y %H:%M:%S %p") 
        #     # time.config(text=formatted_date_time)

        #     self.data_right_frame.after(1000, update_time)
        # update_time()
        ################################

        
        # self.late = Label(self.data_right_frame, text=f"Late by {self.data_dict['late_by']}", font=(FONT_TYPE, FONT_SIZES['h1'], 'bold'))
        # self.late.pack(fill=BOTH,side = LEFT, padx=10)
        # frame = Frame(self.data_right_frame, height=100,width=150,bg="black")
        # frame.pack()

    def footer(self):
        self.canvas_page = Canvas(self.body_frame, bg="white")
        print("body frame height", self.body_frame.winfo_reqheight())
        print("body frame width", self.body_frame.winfo_reqwidth())
        print("Canva height", self.canvas_page.winfo_reqheight())
        print("Canva width", self.canvas_page.winfo_reqwidth())
        self.canvas_page.pack_propagate(False)
        self.canvas_page.configure(width=self.WINDOW_WIDTH, height=(((self.WINDOW_HEIGHT*80)/100)-60))
        self.canvas_page.pack(expand=True, fill="both")
        self.station_obj = StationDesign(self.canvas_page, self.canvas_page.winfo_reqheight(), self.canvas_page.winfo_reqwidth(), self.data_dict['stations'])
        # self.stat = Label(self.footer_frame, text="Stations detail", width=self.WINDOW_WIDTH)
        # self.stat.pack()
        self.current_page = 1
        self.current_page_head = 1


        self.update_page()

    def update_page(self):
        if self.current_page == 1:
            self.canvas_page.pack(expand=True, fill="both")
            self.data_left_frame.pack_forget()
            self.data_right_frame.pack_forget()
        elif self.current_page == 2:
            self.canvas_page.pack_forget()
            self.data_left_frame.pack(expand=True, fill="both", side="left")
            self.data_right_frame.pack(expand=True, fill="both", side="right")

        self.current_page = 1 if self.current_page == 2 else 2
        # self.current_page = 1
        self.root.after(10000, self.update_page)


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
            self.top_right_label6.config(text=inst_speed_str)
            # late_by_txt = 'Early By '+str(round(data['late_by'], 2))+ 'minutes' if data['late_by'] < 0 else 'Late By '+str(round(data['late_by'], 2))+ 'minutes'
            late_stat = data['next_station']['late_by']
            self.top_right_label4.config(text=round(float(data['next_station']['remaining_distance']), 2))
            # self.late.config(text=late_stat)
            if 'late' in late_stat.lower():
                color = 'red'
            else:
                color = 'blue'
            # self.late.config(fg=color)
            self.station_obj.update_train_location(data, color)
        # except Exception as e:
            # print(e)


# if __name__ == "__main__":
#     DisplayDesign(data_dict={'next_station': 'Saugor'})
