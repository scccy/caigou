from tkinter import *
import tkinter.filedialog
from tkinter.filedialog import askdirectory
import tkinter.messagebox
from Primary.Processing.data_processing import Data


class Gui(object):
    window = Tk()
    window.title('采购excel转换')
    window.geometry('250x150')

    choose_excel_path = StringVar()
    download_path_path = StringVar()

    # excel选择弹窗
    def choose_excel(self):
        filename = tkinter.filedialog.askopenfilename()
        self.choose_excel_path.set(filename)

    # 转换文件位置
    def download_path(self):
        path_ = askdirectory()
        self.download_path_path.set(path_)

    # 点击跳转
    def hit_me(self):
        tkinter.messagebox.showinfo(title='Hi', message='转换完成！')

    # 转换按钮桉树
    def confirm(self):
        self.hit_me()
        Data(self.choose_excel_path.get(),self.download_path_path.get()).main()

    def main(self):

        # excel选择控件
        Label(self.window, text="excel选择:").grid(row=0, column=0)
        Button(self.window, text="选择", command=self.choose_excel).grid(row=0, column=2)
        Entry(self.window, textvariable=self.choose_excel_path).grid(row=0, column=1)

        # 转换文件选择控件
        Label(self.window, text="下载路径:").grid(row=1, column=0)
        Button(self.window, text="选择", command=self.download_path).grid(row=1, column=2)
        Entry(self.window, textvariable=self.download_path_path).grid(row=1, column=1)

        # 确认转换
        Button(self.window, text="转换", command=self.confirm).grid(row=2, column=1)
        self.window.mainloop()
