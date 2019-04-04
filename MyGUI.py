# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.messagebox as msg

import DataLevel

class MyGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        size = 500
        self.width = size*0.618+80
        self.height = size*0.382
        self.title("每小时记录")


        #组件
        hint = tk.Label(self,text="Q10Viking: 忙碌一个小时了，记录一下.", bg="lightgrey",fg="black", pady=20,padx=5,font=(None,11))

        row = tk.Frame(self)
        row_2 = tk.Frame(self)
        self.content = tk.Entry(row,font=(None,10))
        content = self.content
        b1 = tk.Button(row_2, text='确定',height = 1, width = 5,command=self.commit_message)
        b2 = tk.Button(row_2, text='重置',height = 1, width = 5,command=self.clear_text)

        hint.pack(side=tk.TOP, fill=tk.X)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        content.pack(side=tk.TOP, fill=tk.X,ipady=10)
        row_2.pack(side=tk.TOP, fill=tk.X, padx=self.width/4+10, pady=10)
        b1.pack(side=tk.LEFT,padx=10, pady=0)
        b2.pack(side=tk.LEFT,padx=10, pady=0)

        self.center_window()

        # handle 关闭事件
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bind('<Return>',self.commit_message)
        # 两分钟后关闭
        self.after(120000,lambda : self.destroy())

    def center_window(self):
        '''
        将窗口放置到屏幕中间
        '''
        # get windows width and height
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        #print(width,height)
        # 计算 x, y 位置
        x = (width/2) - (self.width/2)
        y = (height/2) - (self.height/2)
        self.geometry("%dx%d+%d+%d" % (self.width,self.height,x,y))

    def commit_message(self,event=None):
        str_con = self.content.get()
        if len(str_con) == 0:
            msg.showerror("错误","内容提交不能为空!")
            return

        if msg.askyesno("确定提交？",self.content.get()):
            DataLevel.store_date(self.content.get())
            self.content.delete(0,tk.END)
            msg.showinfo("Exit","保存成功")
            self.destroy()


    def clear_text(self):
        if msg.askyesno("重置","希望重新输入记录?"):
            self.content.delete(0,tk.END)


    def on_closing(self):
        if msg.askokcancel("不要偷懒哦!","确定这一小时不记录任何内容?"):
            self.destroy()



