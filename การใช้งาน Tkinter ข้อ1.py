# โปรแกรมสูตรคูณ (Tkinter)
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

# ฟังก์ชันแสดงสูตรคูณ
def show_table():
    try:
        number = int(entry_number.get())
        end = int(combo_end.get())
    except ValueError:
        messagebox.showerror("ผิดพลาด","กรุณากรอกแม่สูตรคูณเป็นตัวเลขจำนวนเต็ม")
        return

    # เคลียร์พื้นที่แสดงผลก่อน
    text_result.config(state="normal")
    text_result.delete("1.0",tk.END)

    text_result.insert(tk.END,f"===== สูตรคูณแม่ {number} =====\n")
    for i in range(1,end+1):
        text_result.insert(tk.END,f"{number} x {i} = {number * i}\n")

    # ป้องกันการแก้ไขข้อความ
    text_result.config(state="disabled")

# ฟังก์ชันล้างค่า
def clear_all():
    entry_number.delete(0,tk.END)
    text_result.config(state="normal")
    text_result.delete("1.0",tk.END)
    text_result.config(state="disabled")

# สร้างหน้าต่างหลัก (main window)
window = tk.Tk()
window.title("โปรแกรมสูตรคูณ")
window.geometry(calculate_center_screen(window,320,380))

window.columnconfigure(tuple(range(0,4)),weight=1)
window.rowconfigure(3,weight=1)

# หัวข้อ
label_title = tk.Label(window,text="โปรแกรมสูตรคูณ",font=("Arial Bold",16))
label_title.grid(column=0,row=0,columnspan=4,pady=10)

# ช่องกรอกแม่สูตรคูณ
label_number = tk.Label(window,text="แม่สูตรคูณ :")
label_number.grid(column=0,row=1)
entry_number = tk.Entry(window,width=10)
entry_number.grid(column=1,row=1,sticky="EW")

# เลือกว่าจะคูณถึงเท่าไหร่
label_end = tk.Label(window,text="คูณถึง :")
label_end.grid(column=2,row=1)
combo_end = ttk.Combobox(window,values=["12","15","20","25"],width=5,state="readonly")
combo_end.current(0)
combo_end.grid(column=3,row=1,padx=(0,10))

# ปุ่ม
btn_show = tk.Button(window,text="แสดงสูตรคูณ",bg="lightgreen",command=show_table)
btn_show.grid(column=0,row=2,columnspan=2,pady=10)
btn_clear = tk.Button(window,text="ล้างค่า",command=clear_all)
btn_clear.grid(column=2,row=2,columnspan=2,pady=10)

# Frame สำหรับ Text และ Scrollbar
frame_text = tk.Frame(window)
frame_text.grid(column=0,row=3,columnspan=4,sticky="NSEW",padx=10,pady=(0,10))

text_result = tk.Text(frame_text,height=10,width=25,font=("Arial",12),state="disabled")
text_result.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)

scrollbar_y = ttk.Scrollbar(frame_text,orient="vertical",command=text_result.yview)
scrollbar_y.pack(side=tk.RIGHT,fill=tk.Y)
text_result.config(yscrollcommand=scrollbar_y.set)

# ให้ Tkinter วนรอบตรวจสอบเหตุการณ์
window.mainloop()
