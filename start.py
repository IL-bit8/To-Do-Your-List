import os
import tkinter as tk
from tkinter import scrolledtext



class ToDoListApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("To-Do Your List")
        self.window.geometry("1000x800")
        # 加入标签
        self.label = tk.Label(self.window, text="Welcome to To-Do Your List!", font=("Arial", 32))
        self.label.pack(pady=20)
        # 加入按钮就开始生成日志文本框
        def if_cliked(self):
            self.scrolled_text = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, font=("Consolas", 100), width=40, height=10)
            self.scrolled_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
            self.scrolled_text.insert(tk.END, "按钮被按下了！\n")
            self.scrolled_text.see(tk.END)

        self.button = tk.Button(self.window, text="开始一个代办事项", command=lambda: if_cliked(self))
        self.button_end = tk.Button(self.window, text="结束", command=self.window.quit)
        self.button.pack(pady=20)
        self.button_end.pack(pady=20)
        # 启动主循环
        self.window.mainloop()  
        # print("Welcome to To-Do Your List!")

if __name__ == "__main__":
    app = ToDoListApp()