# โปรแกรมตัดเกรด (Tkinter)
# เกณฑ์ 80-100 = A, 75-79 = B+, 70-74 = B, 65-69 = C+
#      60-64 = C, 55-59 = D+, 50-54 = D, 0-49 = F
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

def grading(score):
    if score >= 80:
        return "A"
    elif score >= 75:
        return "B+"
    elif score >= 70:
        return "B"
    elif score >= 65:
        return "C+"
    elif score >= 60:
        return "C"
    elif score >= 55:
        return "D+"
    elif score >= 50:
        return "D"
    else:
        return "F"

def button_click():
    try:
        score = float(entry_score.get())
    except ValueError:
        messagebox.showerror("ผิดพลาด","กรุณากรอกคะแนนเป็นตัวเลข")
        return
    if score < 0 or score > 100:
        messagebox.showwarning("คำเตือน","คะแนนต้องอยู่ระหว่าง 0 - 100")
        return

    grade = grading(score)
    # เปลี่ยนสีตามเกรด
    if grade == "F":
        color = "red"
    elif grade == "A":
        color = "green"
    else:
        color = "blue"
    name = entry_name.get()
    if name == "":
        name = "นักศึกษา"
    label_result.config(text=f"{name} ได้ {score:g} คะแนน\nได้เกรด {grade}",fg=color)

def clear_all():
    entry_name.delete(0,tk.END)
    entry_score.delete(0,tk.END)
    label_result.config(text="เกรด",fg="black")

# สร้างหน้าต่างหลัก (main window)
window = tk.Tk()
window.title("โปรแกรมตัดเกรด")
window.geometry(calculate_center_screen(window,320,250))
window.resizable(False,False)

window.columnconfigure(tuple(range(0,4)),weight=1)
window.rowconfigure(tuple(range(0,5)),weight=1)

label_title = tk.Label(window,text="โปรแกรมตัดเกรด",font=("Arial Bold",16))
label_title.grid(column=0,row=0,columnspan=4)

label_name = tk.Label(window,text="ชื่อ :")
label_name.grid(column=0,row=1)
entry_name = tk.Entry(window)
entry_name.grid(column=1,row=1,columnspan=3,sticky="EW",padx=(0,10))

label_score = tk.Label(window,text="คะแนน :")
label_score.grid(column=0,row=2)
entry_score = tk.Entry(window)
entry_score.grid(column=1,row=2,columnspan=3,sticky="EW",padx=(0,10))

btn_grade = tk.Button(window,text="ตัดเกรด",width=10,bg="lightblue",command=button_click)
btn_grade.grid(column=0,row=3,columnspan=2)
btn_clear = tk.Button(window,text="ล้างค่า",width=10,command=clear_all)
btn_clear.grid(column=2,row=3,columnspan=2)

label_result = tk.Label(window,text="เกรด",borderwidth=1,relief="solid",font=("Arial Bold",14))
label_result.grid(column=0,row=4,columnspan=4,sticky="NSEW",padx=10,pady=10)

window.mainloop()
