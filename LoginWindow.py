"""
@version: 1.0
@author: WowGz
@blog: https://wowgz.com.cn
@file: LoginWindow
@time: 2020/4/24/024 21:05
"""

import tkinter as tk
from tkinter import messagebox  # 引入messagebox避免出现相关报错
import pymysql


# 登录后台逻辑
def student_login():
    student_number = var_student_number.get()
    student_password = var_student_password.get()
    sql = "select * from stu_info where stu_number = '%s'" % student_number
    conn = pymysql.connect('localhost', 'root', '123456', 'attendance_system_springboot')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql)
    result_student_info = cursor.fetchall()
    if len(result_student_info) == 0:
        tk.messagebox.showerror(message='学号不存在，请重新输入！')
        var_student_password.set('')
        var_student_number.set('')
    elif result_student_info[0].get('stu_password') != student_password:
        tk.messagebox.showerror(message='密码错误，请重新输入！')
        var_student_password.set('')
    else:
        tk.messagebox.showinfo(title='Welcome', message='欢迎你！' + result_student_info[0].get('stu_name'))


# 注册后台逻辑
def student_sign_up():
    pass


# 登录界面窗口基本设置
loginWindow = tk.Tk()
loginWindow.title('WowGz 人脸识别考勤客户端')
loginWindow.geometry('505x300')

# welcome image
canvas = tk.Canvas(loginWindow, height=200, width=500)
welcome_image_file = tk.PhotoImage(file='welcome.gif')
image = canvas.create_image(0, 0, anchor='nw', image=welcome_image_file)
canvas.pack(side='top')

# 用户信息
tk.Label(loginWindow, text='学  号: ').place(x=160, y=150)
tk.Label(loginWindow, text='密  码: ').place(x=160, y=190)

var_student_number = tk.StringVar()
entry_student_number = tk.Entry(loginWindow, textvariable=var_student_number)
entry_student_number.place(x=210, y=150)
var_student_password = tk.StringVar()
entry_student_password = tk.Entry(loginWindow, textvariable=var_student_password, show="*")
entry_student_password.place(x=210, y=190)

# 登录和注册按钮
button_login = tk.Button(loginWindow, text=' 登  录 ', command=student_login)
button_login.place(x=180, y=230)
button_sign_up = tk.Button(loginWindow, text=' 注  册 ', command=student_sign_up)
button_sign_up.place(x=280, y=230)

loginWindow.mainloop()
