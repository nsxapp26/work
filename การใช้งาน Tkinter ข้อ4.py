# โปรแกรมแปลงหน่วยอุณหภูมิ (Tkinter)
# แปลงได้ระหว่าง เซลเซียส (C), ฟาเรนไฮน์ (F) และ เคลวิน (K)
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# ฟังก์ชันสำหรับคำนวณตำแหน่งกึ่งกลางจอภาพ
def calculate_center_screen(window,app_width,app_height):
    scr_width = window.winfo_screenwidth()
    scr_height = window.winfo_screenheight()
    offset_x = (scr_width - app_width) / 2
    offset_y = (scr_height - app_height) / 2
    result = f'{app_width}x{app_height}+{int(offset_x)}+{int(offset_y)}'
    return result

# แปลงค่าที่รับมาให้เป็นเซลเซียสก่อน
def to_celsius(temp,unit):
    if unit == "C":
        return temp
    elif unit == "F":
        return (temp - 32) * 5 / 9
    else:
        return temp - 273.15

# แปลงจากเซลเซียสไปเป็นหน่วยที่ต้องการ
def from_celsius(temp_c,unit):
    if unit == "C":
        return temp_c
    elif unit == "F":
        return (temp_c * 9 / 5) + 32
    else:
        return temp_c + 273.15

def convert():
    try:
        temp = float(entry_temp.get())
    except ValueError:
        messagebox.showerror("ผิดพลาด","กรุณากรอกอุณหภูมิเป็นตัวเลข")
        return
    unit_from = combo_from.get()[0]   # เอาแค่ตัวอักษรแรก C/F/K
    unit_to = combo_to.get()[0]

    temp_c = to_celsius(temp,unit_from)
    if temp_c < -273.15:
        messagebox.showwarning("คำเตือน","อุณหภูมิต่ำกว่าศูนย์สัมบูรณ์ไม่ได้")
        return
    result = from_celsius(temp_c,unit_to)
    label_result.config(text=f"{temp:g} °{unit_from} = {result:.2f} °{unit_to}")

# ปุ่มสลับหน่วย
def swap_unit():
    a = combo_from.current()
    b = combo_to.current()
    combo_from.current(b)
    combo_to.current(a)

# สร้างหน้าต่างหลัก (main window)
window = tk.Tk()
window.title("โปรแกรมแปลงหน่วยอุณหภูมิ")
window.geometry(calculate_center_screen(window,340,250))
window.resizable(False,False)

window.columnconfigure(tuple(range(0,4)),weight=1)
window.rowconfigure(tuple(range(0,5)),weight=1)

label_title = tk.Label(window,text="แปลงหน่วยอุณหภูมิ",font=("Arial Bold",16))
label_title.grid(column=0,row=0,columnspan=4)

label_temp = tk.Label(window,text="อุณหภูมิ :")
label_temp.grid(column=0,row=1)
entry_temp = tk.Entry(window)
entry_temp.grid(column=1,row=1,columnspan=3,sticky="EW",padx=(0,10))

unit_list = ["C (เซลเซียส)","F (ฟาเรนไฮน์)","K (เคลวิน)"]

label_from = tk.Label(window,text="จาก :")
label_from.grid(column=0,row=2)
combo_from = ttk.Combobox(window,values=unit_list,state="readonly",width=13)
combo_from.current(0)
combo_from.grid(column=1,row=2)

btn_swap = tk.Button(window,text="<->",command=swap_unit)
btn_swap.grid(column=2,row=2)

combo_to = ttk.Combobox(window,values=unit_list,state="readonly",width=13)
combo_to.current(1)
combo_to.grid(column=3,row=2,padx=(0,10))

btn_convert = tk.Button(window,text="แปลงค่า",width=12,bg="lightgreen",command=convert)
btn_convert.grid(column=0,row=3,columnspan=4)

label_result = tk.Label(window,text="ผลลัพธ์",borderwidth=1,relief="solid",font=("Arial",13))
label_result.grid(column=0,row=4,columnspan=4,sticky="NSEW",padx=10,pady=10)

window.mainloop()
