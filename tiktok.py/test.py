import os
import time
import tkinter as tk

class TimerApp(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master=None)
        self.grid()
        self.create_widgets()
        self.elapsed = 0
        self.refresh_timer()
        self.after_id = None  # used to determine and control if timer is running

    def create_widgets(self):
        self.timer = tk.StringVar()
        self.timer.set('')
        self.timer_label = tk.Label(self, textvariable=self.timer)
        self.timer_label.grid(row=1, column=2)

        self.button1 = tk.Button(self, text="Start", command=self.start_clock)
        self.button1.grid(row=2, column=0, columnspan=2)
        self.button2 = tk.Button(self, text="Stop", command=self.stop_clock)
        self.button2.grid(row=2, column=2, columnspan=2)
        self.button3 = tk.Button(self, text="Clear", command=self.clear_clock)
        self.button3.grid(row=2, column=4, columnspan=2)

app = TimerApp()
app.master.title('Timer')
app.mainloop()