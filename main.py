import tkinter as tk
import matlab.engine


def calculate(t, e, At, F1, F2):
    o = 5.67032 * 10 ** -12
    c1 = 3.741832 * 10 ** 4
    c2_1 = 1.438786 * 10 ** 4
    c2_2 = 1.4388 * 10 ** 4

    T = (t + 273)
    if T > 1337.58:
        c2 = c2_2
    else:
        c2 = c2_1
    M = e * o * T ** 4

    B = M * At

    M_F12 = (F1 - F2) * o * T ** 4

    V_m = 2898 / T
    return M, B, M_F12, V_m, c1, c2,T



def matlab_engine(c1,c2,F1,F2,T,At):
    engine=matlab.engine.start_matlab()
    engine.fun1(matlab.double([c1]),matlab.double([c2]),matlab.double([F1]),matlab.double([F2]),matlab.double([T]),matlab.double([At]))
    res=tk.Tk()
    res.title('Design by DHU ZbigBoom')
    res.geometry('100x100')

    def quit():
        res.destroy()
    exit=tk.Button(res,text='结束图像',command=quit)
    exit.pack()
    res.mainloop()


def get_data():
    t = float(text1.get())
    e = float(text2.get())
    At = float(text3.get())
    F1 = float(text4.get())
    F2 = float(text5.get())
    M, B, M_F12, V_m, c1, c2 ,T= calculate(t, e, At, F1, F2)

    text6 = tk.Label(window, text='全辐射度：', font=('Arial', 14))
    text7 = tk.Label(window, text='辐射能通量：', font=('Arial', 14))
    text8 = tk.Label(window, text='幅出度：', font=('Arial', 14))
    text9 = tk.Label(window, text='最大辐射波长：', font=('Arial', 14))

    text6_1 = tk.Label(window, text=M, font=('Arial', 14))
    text7_1 = tk.Label(window, text=B, font=('Arial', 14))
    text8_1 = tk.Label(window, text=M_F12, font=('Arial', 14))
    text9_1 = tk.Label(window, text=V_m, font=('Arial', 14))

    text6.place(x=500, y=100)
    text7.place(x=500, y=200)
    text8.place(x=500, y=300)
    text9.place(x=500, y=400)

    text6_1.place(x=600, y=100)
    text7_1.place(x=600, y=200)
    text8_1.place(x=600, y=300)
    text9_1.place(x=600, y=400)

    matlab_engine(c1,c2,F1,F2,T,At)


window = tk.Tk()
window.title('Design by DHU ZbigBoom')
window.geometry('1000x600')

text1_1 = tk.Label(window, text='t=', font=('Arial', 14))
text2_1 = tk.Label(window, text='e=', font=('Arial', 14))
text3_1 = tk.Label(window, text='At=', font=('Arial', 14))
text4_1 = tk.Label(window, text='F1=', font=('Arial', 14))
text5_1 = tk.Label(window, text='F2=', font=('Arial', 14))

text1 = tk.Entry(window, show=None, font=('Arial', 14))
text2 = tk.Entry(window, show=None, font=('Arial', 14))
text3 = tk.Entry(window, show=None, font=('Arial', 14))
text4 = tk.Entry(window, show=None, font=('Arial', 14))
text5 = tk.Entry(window, show=None, font=('Arial', 14))

text1_1.place(x=50, y=100)
text2_1.place(x=50, y=150)
text3_1.place(x=50, y=200)
text4_1.place(x=50, y=250)
text5_1.place(x=50, y=300)

text1.place(x=100, y=100)
text2.place(x=100, y=150)
text3.place(x=100, y=200)
text4.place(x=100, y=250)
text5.place(x=100, y=300)

button = tk.Button(window, text='开始', font=('Arial', 14), command=get_data)
button.place(x=200, y=500)

window.mainloop()
