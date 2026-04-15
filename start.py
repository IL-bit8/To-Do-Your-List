import os
import tkinter as tk
from tkinter import scrolledtext
import time # 记录时间
import winsound

class ToDoListApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("To-Do Your List")
        self.window.geometry("1000x800")
        # 加入标签
        self.label = tk.Label(self.window, text="Welcome to To-Do Your List!", font=("Arial", 32))
        self.label.pack(pady=20)
        # 加入第一次按钮被按下的文本框
        self.scrolled_text = None
        # 加入第一次按下的判断
        self.cliked_bool = False

        # 记录时间
        self.time = 0

        self.button_start = tk.Button(self.window, text="开始一个代办事项", command=self.get_input)
        self.button_ifclick = tk.Button(self.window, text="判断是否点击按钮", command=self.if_cliked)
        self.button_end = tk.Button(self.window, text="结束", command=self.window.quit)
        # 用户命令行输入
        self.user_input_label = tk.Label(self.window, text="请输入任务内容,时间:", font=("Arial", 14))
        self.user_input_buff = 0

        self.task_entry = tk.Entry(self.window, font=("Arial", 14), width=30)
        self.task_entry.pack(pady=5)

        self.user_input_label.pack(pady=(10,0))
        self.button_start.pack(pady=20)
        self.button_ifclick.pack(pady=20)
        self.button_end.pack(pady=20)
        # 启动主循环
        self.window.mainloop()  
    def get_input(self):
        # 获取从 "1.0" (第一行第0个字符) 到 tk.END (文本末尾) 的所有内容
        content = self.task_entry.get()
        if content.isdigit():  # 判断是否非负整数
            self.cliked_bool = True
            self.user_input_buff = int(content)
        else:
            self.scrolled_text.insert(tk.END, "请输入有效的整数秒数！\n")
            self.scrolled_text.see(tk.END)
            self.cliked_bool = False
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
    def if_cliked(self,scrolled_text=None):
        if self.cliked_bool == False:
            return
        if self.scrolled_text == None:
            self.scrolled_text = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, font=("Consolas", 100), width=40, height=10)
            self.scrolled_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.time_last()
        self.scrolled_text.insert(tk.END, "按钮被按下了！\n")
        self.scrolled_text.see(tk.END)


if __name__ == "__main__":
    app = ToDoListApp()