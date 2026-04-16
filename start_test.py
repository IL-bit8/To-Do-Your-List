import os
import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import time # 记录时间
import winsound
import threading

class ToDo:
    def __init__(self, window, name, time, audio=lambda: winsound.Beep(1000, 1000)):
        self.window = window
        self.name = name
        self.time = time
        self.times_up = False
        self.sound = audio
        self.thread = threading.Thread(target=self.sound)
        self.thread.daemon = True
    
    def __str__(self):
        return self.name + " - " + ("Time's up!" if self.times_up else time.strftime("%H:%M:%S", time.gmtime(self.time)))
    
    def process_timer(self):
        if self.time > 0:
            self.time -= 1
        elif not self.times_up:
            self.times_up = True
            self.thread.start()

class ToDoListApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("To-Do Your List")
        self.window.geometry("800x800")
        # 加入标签
        self.label = tk.Label(self.window, text="Welcome to To-Do Your List!", font=("Arial", 32))
        self.label.pack(pady=20)

        self.to_do_list = []
        self.to_do_listbox = tk.Listbox(self.window, font=("Consolas", 15), height=20, width=60)

        self.button_create_to_do = tk.Button(self.window, text="New To-Do", command=self.create_to_do_window)

        self.button_create_to_do.pack(pady=20)
        self.to_do_listbox.pack(pady=20)

        self.loop()

        # 启动主循环
        self.window.mainloop()

    def loop(self):
        self.to_do_listbox.delete(0, tk.END)
        for todo in self.to_do_list:
            todo.process_timer()
            self.to_do_listbox.insert(tk.END, todo)
        self.window.after(1000, self.loop)

    def create_to_do_window(self):
        func_window = tk.Tk()
        func_window.title("New To-Do")
        func_window.geometry("400x500")
        func_window.resizable(False, False)
        tk.Label(func_window, text="Task Content", font=("Arial", 14)).place(x=20, y=20)
        input_task = tk.Entry(func_window, font=("Arial", 14), width=30)
        input_task.place(x=20, y=50)
        label_time = tk.Label(func_window, text="Timer", font=("Arial", 14))
        label_time.place(x=20, y=100)
        input_time_h = ttk.Combobox(func_window, values=[i for i in range(24)], font=("Arial", 14), width=5)
        input_time_h.place(x=20, y=130)
        input_time_h.current(0)
        tk.Label(func_window, text=":", font=("Arial", 14)).place(x=110, y=130)
        input_time_m = ttk.Combobox(func_window, values=[i for i in range(60)], font=("Arial", 14), width=5)
        input_time_m.place(x=130, y=130)
        input_time_m.current(0)
        tk.Label(func_window, text=":", font=("Arial", 14)).place(x=220, y=130)
        input_time_s = ttk.Combobox(func_window, values=[i for i in range(60)], font=("Arial", 14), width=5)
        input_time_s.place(x=240, y=130)
        input_time_s.current(10)
        tk.Label(func_window, text="Ring Audio:", wraplength=300, font=("Arial", 14)).place(x=20, y=180)
        label_audio = tk.Label(func_window, text="Default", wraplength=300, font=("Arial", 14))
        label_audio.place(x=20, y=220)
        button_file = tk.Button(func_window, text="Browse File", command=lambda: self.open_file(label_audio))
        button_file.place(x=20, y=300)
        button_confirm = tk.Button(func_window, text="Create", command=lambda: self.create_to_do(input_task.get(), label_audio.cget("text"), input_time_h.get(), input_time_m.get(), input_time_s.get()))
        button_confirm.place(x=20, y=360)
        
    def open_file(self, label_audio):
        file_path = filedialog.askopenfilename(title="Select a audio file (*.wav)", filetypes=(("Audio Files", "*.wav"), ("All Files", "*.*")))
        if file_path:
            label_audio.config(text=f"{file_path}")
    
    def create_to_do(self, name, audio, h, m, s):
        if not name:
            messagebox.showerror("Blank Input", "Please input task name")
            return
        int_h = int_m = int_s = 0;
        try:
            int_h = int(h)
            int_m = int(m)
            int_s = int(s)
            if 0 <= int_h and 0 <= int_m < 60 and 0 <= int_s < 60:
                time = int_h * 3600 + int_m * 60 + int_s
                if audio != "Default":
                    todo = ToDo(self.window, name, time, lambda: winsound.PlaySound(audio, winsound.SND_FILENAME))
                else:
                    todo = ToDo(self.window, name, time)
                self.to_do_list.append(todo)
            else:
                messagebox.showerror("Invalid Time Range", "0 <= Hour, 0 <= Minute < 60, 0 <= Second < 60")
        except:
            messagebox.showerror("Invalid Input", "Please input valid integer as time")



"""
        # 加入第一次按钮被按下的文本框
        self.scrolled_text = None
        # 加入第一次按下的判断
        self.clicked_bool = False

        # 记录时间
        self.time = 0

        self.button_start = tk.Button(self.window, text="开始一个代办事项", command=self.get_input)
        self.button_ifclick = tk.Button(self.window, text="判断是否点击按钮", command=self.if_clicked)
        # 用户命令行输入
        self.user_input_label = tk.Label(self.window, text="请输入任务内容,时间:", font=("Arial", 14))
        self.user_input_buff = 0

        self.task_entry = tk.Entry(self.window, font=("Arial", 14), width=30)
        self.task_entry.pack(pady=5)

        self.user_input_label.pack(pady=(10,0))
        self.button_start.pack(pady=20)
        self.button_ifclick.pack(pady=20)
        # 启动主循环
        self.window.mainloop()  

    def get_input(self):
        # 获取从 "1.0" (第一行第0个字符) 到 tk.END (文本末尾) 的所有内容
        content = self.task_entry.get()
        if content.isdigit():  # 判断是否非负整数
            self.clicked_bool = True
            self.user_input_buff = int(content)
        else:
            self.scrolled_text.insert(tk.END, "请输入有效的整数秒数！\n")
            self.scrolled_text.see(tk.END)
            self.clicked_bool = False

    #加入倒计时计算
    def time_last(self):
        if self.time == 0:
            self.time = time.time()
        else:
            last_time = time.time() - self.time
            self.scrolled_text.insert(tk.END, f"距离上次按钮被按下已经过去了 {last_time:.2f} 秒！\n")
            self.scrolled_text.insert(tk.END, f"距离设定完成还剩已经过去了 {self.user_input_buff - last_time:.2f} 秒！\n")
            self.scrolled_text.see(tk.END)
            self.time = time.time()
            if (self.user_input_buff - last_time) <= 0:
                self.buzzer(time_up=True)
                self.scrolled_text.insert(tk.END, "时间到，我开始响铃了！\n")
            else:
                self.buzzer(time_up=False)

    # 加入蜂鸣器开始响起来
    def buzzer(self, time_up):
        if time_up:
            self.scrolled_text.insert(tk.END, "时间到！\n")
            self.scrolled_text.see(tk.END)
            # 这里可以加入蜂鸣器的代码，例如使用winsound模块在Windows上发出声音
            winsound.Beep(1000, 1000)  # 发出1000Hz的声音，持续1000毫秒
        else:
            self.user_input_buff -= 1
            self.window.after(1000, self.buzzer)  # 每隔1秒调用一次buzzer函数

    # 加入按钮就开始生成日志文本-倒计时
    def if_clicked(self,scrolled_text=None):
        if self.clicked_bool == False:
            return
        if self.scrolled_text == None:
            self.scrolled_text = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, font=("Consolas", 100), width=40, height=10)
            self.scrolled_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.time_last()
        self.scrolled_text.insert(tk.END, "按钮被按下了！\n")
        self.scrolled_text.see(tk.END)
"""


if __name__ == "__main__":
    app = ToDoListApp()