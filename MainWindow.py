"""
@version: 1.0
@author: WowGz
@blog: https://wowgz.com.cn
@file: MainWindow
@time: 2020/4/24/024 16:41
"""

import tkinter as tk
from tkinter import messagebox  # import this to fix messagebox error
import pickle

window = tk.Tk()
window.title('Welcome to WowGz Face Attendance System Client')
window.geometry('400x300')

# welcome image
canvas = tk.Canvas(window, height=300, width=500)
image_file = tk.PhotoImage(file='')
image = canvas.create_image(0, 0, anchor='n', image=image_file)
canvas.pack(side='top')

# user information
tk.Label(window, text='User name: ').place(x=120, y=150)
tk.Label(window, text='Password: ').place(x=120, y=190)

var_user_name = tk.StringVar()
var_user_name.set('example@python.com')
entry_user_name = tk.Entry(window, textvariable=var_user_name)
entry_user_name.place(x=220, y=150)
var_user_pwd = tk.StringVar()
entry_user_pwd = tk.Entry(window, textvariable=var_user_pwd, show='*')
entry_user_pwd.place(x=220, y=190)

# login and sign up button
btn_login = tk.Button(window, text='  Login  ', command=usr_login)
btn_login.place(x=170, y=230)
btn_sign_up = tk.Button(window, text=' Sign up', command=user_sign_up)
btn_sign_up.place(x=270, y=230)


def usr_login():
    user_name = var_user_name.get()
    user_pwd = var_user_pwd.get()
    try:
        with open('users_info.pickle', 'rb') as user_file:
            users_info = pickle.load(user_file)
    except FileNotFoundError:
        with open('users_info.pickle', 'wb') as user_file:
            users_info = {'admin': 'admin'}
            pickle.dump(users_info, user_file)
    if user_name in users_info:
        if user_pwd == users_info[user_name]:
            tk.messagebox.showinfo(title='Welcome', message='How are you? ' + user_name)
        else:
            tk.messagebox.showerror(message='Error, your password is wrong, try again.')
    else:
        is_sign_up = tk.messagebox.askyesno('Welcome', 'You have not signed up yet. Sign up today?')
        if is_sign_up:
            user_sign_up()


def user_sign_up():
    def sign_to_WowGz_Face_Attendance_System_Client():
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
        with open('users_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        if np != npf:
            tk.messagebox.showerror('Error', 'Password and confirm password must be the same!')
        elif nn in exist_usr_info:
            tk.messagebox.showerror('Error', 'The user has already signed up!')
        else:
            exist_usr_info[nn] = np
            with open('users_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk.messagebox.showinfo('Welcome', 'You have successfully signed up!')
            window_sign_up.destroy()

    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('Sign up window')

    new_name = tk.StringVar()
    new_name.set('example@python.com')
    tk.Label(window_sign_up, text='User name: ').place(x=10, y=10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=150, y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Password: ').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=150, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Confirm password: ').place(x=10, y=90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=150, y=90)

    btn_confirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_WowGz_Face_Attendance_System_Client)
    btn_confirm_sign_up.place(x=150, y=130)




window.mainloop()
