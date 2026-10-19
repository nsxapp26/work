# โปรแกรมคำนวณพื้นที่สามเหลี่ยม และสี่เหลี่ยม (Tkinter)
import tkinter as tk
from tkinter import messagebox

# ฟังก์ชันสำหรับคำนวณตำแหน่งกึ่งกลางจอภาพ
def calculate_center_screen(window,app_width,app_height):
    scr_width = window.winfo_screenwidth()
    scr_height = window.winfo_screenheight()
    offset_x = (scr_width - app_width) / 2
    offset_y = (scr_height - app_height) / 2
    result = f'{app_width}x{app_height}+{int(offset_x)}+{int(offset_y)}'
    return result

# ฟังก์ชันคำนวณพื้นที่สามเหลี่ยม
def calculate_triangle():
    try:
        base = float(entry_base.get())
        height = float(entry_height.get())
    except ValueError:
        messagebox.showerror("ผิดพลาด","กรุณากรอกตัวเลขให้ถูกต้อง")
        return
    if base <= 0 or height <= 0:
        messagebox.showwarning("คำเตือน","ฐานและความสูงต้องมากกว่า 0")
        return
    area = 0.5 * base * height
    label_tri_result.config(text=f"พื้นที่ = 1/2 x {base:g} x {height:g} = {area:.2f} ตร.หน่วย")

# ฟังก์ชันคำนวณพื้นที่สี่เหลี่ยม
def calculate_rectangle():
    try:
        width = float(entry_width.get())
        length = float(entry_length.get())
    except ValueError:
        messagebox.showerror("ผิดพลาด","กรุณากรอกตัวเลขให้ถูกต้อง")
        return
    if width <= 0 or length <= 0:
        messagebox.showwarning("คำเตือน","ความกว้างและความยาวต้องมากกว่า 0")
        return
    area = width * length
    label_rec_result.config(text=f"พื้นที่ = {width:g} x {length:g} = {area:.2f} ตร.หน่วย")

# ฟังก์ชันล้างค่า
def clear_all():
    entry_base.delete(0,tk.END)
    entry_height.delete(0,tk.END)
    entry_width.delete(0,tk.END)
    entry_length.delete(0,tk.END)
    label_tri_result.config(text="ผลลัพธ์")
    label_rec_result.config(text="ผลลัพธ์")

# ฟังก์ชันสลับเฟรมตามตัวเลือก
def on_radio_select():
    if radio_var.get() == 'T':
        frame_tri.tkraise()
    else:
        frame_rec.tkraise()

# สร้างหน้าต่างหลัก (main window)
window = tk.Tk()
window.title("โปรแกรมคำนวณพื้นที่")
window.geometry(calculate_center_screen(window,350,300))
window.resizable(False,False)

# กำหนดค่าน้ำหนักให้กับกริด
window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)
window.rowconfigure(0,weight=1)
window.rowconfigure(1,weight=4)
window.rowconfigure(2,weight=1)

# หัวข้อโปรแกรม
label_title = tk.Label(window,text="คำนวณพื้นที่สามเหลี่ยม / สี่เหลี่ยม",font=("Arial Bold",14))
label_title.grid(column=0,row=0,columnspan=2)

# ---------------- เฟรมสามเหลี่ยม ----------------
frame_tri = tk.Frame(window,background='lightgreen',bd=2,relief='solid')
frame_tri.grid(column=0,row=1,columnspan=2,sticky="NSEW",padx=20,pady=5)
frame_tri.columnconfigure(tuple(range(0,4)),weight=1)
frame_tri.rowconfigure(tuple(range(0,4)),weight=1)

label_base = tk.Label(frame_tri,text="ฐาน :",background='lightgreen')
label_base.grid(column=0,row=0)
entry_base = tk.Entry(frame_tri)
entry_base.grid(column=1,row=0,columnspan=3,sticky="EW",padx=(0,10))

label_height = tk.Label(frame_tri,text="ความสูง :",background='lightgreen')
label_height.grid(column=0,row=1)
entry_height = tk.Entry(frame_tri)
entry_height.grid(column=1,row=1,columnspan=3,sticky="EW",padx=(0,10))

btn_tri = tk.Button(frame_tri,text="คำนวณพื้นที่สามเหลี่ยม",command=calculate_triangle)
btn_tri.grid(column=0,row=2,columnspan=4)

label_tri_result = tk.Label(frame_tri,text="ผลลัพธ์",borderwidth=1,relief='solid')
label_tri_result.grid(column=0,row=3,columnspan=4,sticky="EW",padx=5,pady=5)

# ---------------- เฟรมสี่เหลี่ยม ----------------
frame_rec = tk.Frame(window,background='lightblue',bd=2,relief='solid')
frame_rec.grid(column=0,row=1,columnspan=2,sticky="NSEW",padx=20,pady=5)
frame_rec.columnconfigure(tuple(range(0,4)),weight=1)
frame_rec.rowconfigure(tuple(range(0,4)),weight=1)

label_width = tk.Label(frame_rec,text="กว้าง :",background='lightblue')
label_width.grid(column=0,row=0)
entry_width = tk.Entry(frame_rec)
entry_width.grid(column=1,row=0,columnspan=3,sticky="EW",padx=(0,10))

label_length = tk.Label(frame_rec,text="ยาว :",background='lightblue')
label_length.grid(column=0,row=1)
entry_length = tk.Entry(frame_rec)
entry_length.grid(column=1,row=1,columnspan=3,sticky="EW",padx=(0,10))

btn_rec = tk.Button(frame_rec,text="คำนวณพื้นที่สี่เหลี่ยม",command=calculate_rectangle)
btn_rec.grid(column=0,row=2,columnspan=4)

label_rec_result = tk.Label(frame_rec,text="ผลลัพธ์",borderwidth=1,relief='solid')
label_rec_result.grid(column=0,row=3,columnspan=4,sticky="EW",padx=5,pady=5)

# ---------------- ตัวเลือกรูปทรง ----------------
radio_var = tk.StringVar()
radio1 = tk.Radiobutton(window,text="สามเหลี่ยม",variable=radio_var,value='T',command=on_radio_select)
radio1.grid(column=0,row=2)
radio2 = tk.Radiobutton(window,text="สี่เหลี่ยม",variable=radio_var,value='R',command=on_radio_select)
radio2.grid(column=1,row=2)

# ปุ่มล้างค่า
btn_clear = tk.Button(window,text="ล้างค่า",width=10,command=clear_all)
btn_clear.grid(column=0,row=3,columnspan=2,pady=(0,10))

# เริ่มต้นให้แสดงเฟรมสามเหลี่ยม
radio1.select()
frame_tri.tkraise()

# ให้ Tkinter วนรอบตรวจสอบเหตุการณ์
window.mainloop()
