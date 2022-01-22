#2020010849 이도연

from tkinter import *

def do_convert():
    inch_val = float(e_cvt_from.get())
    cm_val = inch_val * 2.54
    l_cvt_to.config(text=str(cm_val)+" 센미터")

window = Tk()
window.title("2020010849 이도연")

l_title = Label(window, text="인치를 센치미터로 변환하는 프로그램")
l_detail = Label(window, text="인치를 입력하시오:")
l_result = Label(window, text="변환 결과:")
b_convert = Button(window, text="변환", command=do_convert)
e_cvt_from = Entry(window)
l_cvt_to = Label(window, text=" ")

l_title.grid(row=0, columnspan=2)
l_detail.grid(row=1, column=0)
e_cvt_from.grid(row=1, column=1)
l_result.grid(row=2, column=0)
l_cvt_to.grid(row=2, column=1)
b_convert.grid(row=3, column=1)

window.mainloop()