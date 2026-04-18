import os
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import time # 记录时间
import winsound

base_dir = os.path.dirname(os.path.abspath(__file__))

class Config(dict):
    def __init__(self):
        self.load()

    def load(self):
        with open(base_dir + "/config.txt", 'r', encoding='utf-8') as f:
            for line in f:
                key, value = line.split('=');
                self[key] = value.strip()
        self.selected_lang = Language(self["selected_lang"])
        ringtone = self["selected_ringtone"]
        self.selected_ringtone = None if ringtone == "default" else Ringtone(ringtone)
    
    def save(self):
        with open(base_dir + "/config.txt", 'w', encoding='utf-8') as f:
            for key in self:
                f.write(f"{ key }={ self[key] }\n")

class Language(dict):
    def __init__(self, file):
        with open(base_dir + "/lang/" + file, 'r', encoding='utf-8') as f:
            for line in f:
                key, value = line.split('=');
                self[key] = value.strip()

class Ringtone:
    def __init__(self, file):
        self.name = file
        self.file = base_dir + "/sounds/" + file

class ToDoListApp:
    def __init__(self):
        self.config = Config()

        self.lang = self.config.selected_lang
        with os.scandir(base_dir + "/sounds") as files:
            self.ringtone_list = ["default"] + [file.name for file in files if file.is_file() and file.name.endswith(".wav")]
        
        self.translable_widgets = {}

        self.window = tk.Tk()
        self.window.title("To-Do Your List")
        self.window.geometry("1000x800")
        # 加入标签
        self.label = self.translable_widget(tk.Label(self.window, font=("Arial", 32)), "title")
        self.label.pack(pady=20)
        # 加入第一次按钮被按下的文本框
        self.scrolled_text = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, font=("Consolas", 12), width=50, height=10)
        self.scrolled_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        # 加入第一次按下的判断
        self.clicked_bool = False

        # 记录时间
        self.time = 0

        self.translable_widget(tk.Label(self.window, font=("Arial", 14)), "set_language").pack(pady=5)
        self.lang_combobox = ttk.Combobox(self.window, values=["zh", "en"])
        self.lang_combobox.current(0)
        self.lang_combobox.pack(pady=10)
        self.lang_combobox.bind("<<ComboboxSelected>>", self.on_set_lang)

        self.translable_widget(tk.Label(self.window, font=("Arial", 14)), "set_ringtone").pack(pady=5)
        self.ringtone_combobox = ttk.Combobox(self.window, values=self.ringtone_list)
        self.ringtone_combobox.current(0)
        self.ringtone_combobox.pack(pady=10)
        self.ringtone_combobox.bind("<<ComboboxSelected>>", self.on_set_ringtone)

        self.button_start = self.translable_widget(tk.Button(self.window, command=self.get_input), "button_start")
        self.button_if_click = self.translable_widget(tk.Button(self.window, command=self.if_clicked), "button_if_click")
        self.button_end = self.translable_widget(tk.Button(self.window, command=self.window.quit), "button_quit")
        # 用户命令行输入
        self.user_input_label = self.translable_widget(tk.Label(self.window, font=("Arial", 14)), "label_user_input")
        self.user_input_label.pack(pady=(10,0))
        self.user_input_buff = 0

        self.task_entry = tk.Entry(self.window, font=("Arial", 14), width=30)
        self.task_entry.pack(pady=5)

        self.button_start.pack(pady=20)
        self.button_if_click.pack(pady=20)
        self.button_end.pack(pady=20)
        # 启动主循环
        self.window.mainloop()

    def on_set_lang(self, event):
        self.config["selected_lang"] = event.widget.get() + ".txt"
        self.config.save()
        self.config.load()
        self.lang = self.config.selected_lang
        for widget in self.translable_widgets:
            (key, args) = self.translable_widgets[widget]
            widget.config(text=self.translate(key, *args))
    
    def on_set_ringtone(self, event):
        self.config["selected_ringtone"] = event.widget.get()
        self.config.save()
        self.config.load()

    def get_input(self):
        # 获取从 "1.0" (第一行第0个字符) 到 tk.END (文本末尾) 的所有内容
        content = self.task_entry.get()
        if content.isdigit():  # 判断是否非负整数
            self.clicked_bool = True
            self.user_input_buff = int(content)
            self.start_auto_countdown() 
        else:
            self.scrolled_text.insert(tk.END, self.translate("invalid_input") + "\n")
            self.scrolled_text.see(tk.END)
            self.clicked_bool = False

    def start_auto_countdown(self):
        # 自动倒计时，每秒减少 user_input_buff，到0时响铃
        if self.user_input_buff > 0:
            self.scrolled_text.insert(tk.END, self.translate("time_left", self.user_input_buff) + "\n")
            self.scrolled_text.see(tk.END)
            self.user_input_buff -= 1
            # 1秒后再调用自己
            self.window.after(1000, self.start_auto_countdown)
        else:
            # 倒计时结束，响铃
            self.scrolled_text.insert(tk.END, self.translate("time_up_buzzer") + "\n")
            self.scrolled_text.see(tk.END)
            winsound.Beep(1000, 1000)

    #加入倒计时计算
    def time_last(self):
        if self.time == 0:
            self.time = time.time()
        else:
            last_time = time.time() - self.time
            self.scrolled_text.insert(tk.END, self.translate("time_elapsed", f"{last_time:.2f}") + "\n")
            self.scrolled_text.insert(tk.END, self.translate("time_behind", f"{self.user_input_buff - last_time:.2f}") + "\n")
            self.scrolled_text.see(tk.END)
            self.time = time.time()
            if (self.user_input_buff - last_time) <= 0:
                self.buzzer(time_up=True)
                self.scrolled_text.insert(tk.END, self.translate("time_up_ring") + "\n")
                winsound.Beep(1000, 1000)

            else:
                self.buzzer(time_up=False)

    # 加入蜂鸣器开始响起来
    def buzzer(self, time_up):
        if time_up:
            self.scrolled_text.insert(tk.END, self.translate("time_up") + "\n")
            self.scrolled_text.see(tk.END)
            # 这里可以加入蜂鸣器的代码，例如使用winsound模块在Windows上发出声音
            winsound.Beep(1000, 1000)  # 发出1000Hz的声音，持续1000毫秒
        else:
            self.user_input_buff -= 1
            self.window.after(1000, lambda: self.buzzer(time_up))  # 每隔1秒调用一次buzzer函数

    # 加入按钮就开始生成日志文本-倒计时
    def if_clicked(self,scrolled_text=None):
        if self.clicked_bool == False:
            return
        self.time_last()
        self.scrolled_text.insert(tk.END, self.translate("button_pressed") + "\n")
        self.scrolled_text.see(tk.END)

    def translable_widget(self, widget: tk.Label | tk.Button, key, *args):
        widget.config(text=self.translate(key, *args))
        self.translable_widgets[widget] = (key, args)
        return widget

    def translate(self, key, *args):
        return self.lang[key].format(*args) if key in self.lang else key


class ToDo:
    def __init__(self, name, time, sound):
        self.name = name
        self.time = time
        self.sound = sound
    
    def __str__(self):
        return self.name + " : " + str(self.time)

if __name__ == "__main__":
    app = ToDoListApp()