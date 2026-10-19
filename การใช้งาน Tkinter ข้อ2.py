# โปรแกรมคำนวณค่าไฟฟ้า (Tkinter)
# อัตราค่าไฟ
#   หน่วยที่ 1 - 50     หน่วยละ 2 บาท
#   หน่วยที่ 51 - 100   หน่วยละ 3 บาท
#   หน่วยที่ 101 - 500  หน่วยละ 5 บาท
#   หน่วยที่ 501 ขึ้นไป  หน่วยละ 7 บาท
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

# ฟังก์ชันคำนวณค่าไฟ
def calculate_bill(unit):
    if unit <= 50:
        bill = unit * 2
    elif unit <= 100:
        bill = (50 * 2) + ((unit - 50) * 3)
    elif unit <= 500:
        bill = (50 * 2) + (50 * 3) + ((unit - 100) * 5)
    else:
        bill = (50 * 2) + (50 * 3) + (400 * 5) + ((unit - 500) * 7)
    return bill

def button_click():
    try:
        unit = float(entry_unit.get())
    except ValueError:
        messagebox.showerror("ผิดพลาด","กรุณากรอกจำนวนหน่วยเป็นตัวเลข")
        return
    if unit < 0:
        messagebox.showwarning("คำเตือน","จำนวนหน่วยต้องไม่ติดลบ")
        return

    bill = calculate_bill(unit)
    # ถ้าเลือกคิด VAT 7% ให้บวกเพิ่ม
    if vat_var.get():
        vat = bill * 0.07
        total = bill + vat
        label_result.config(text=f"ค่าไฟ {bill:,.2f} บาท\nVAT 7% = {vat:,.2f} บาท\nรวมทั้งสิ้น {total:,.2f} บาท")
    else:
        label_result.config(text=f"ใช้ไฟ {unit:g} หน่วย\nค่าไฟ {bill:,.2f} บาท")

def clear_all():
    entry_unit.delete(0,tk.END)
    label_result.config(text="ผลลัพธ์")

# สร้างหน้าต่างหลัก (main window)
window = tk.Tk()
window.title("โปรแกรมคำนวณค่าไฟฟ้า")
window.geometry(calculate_center_screen(window,320,260))
window.resizable(False,False)

window.columnconfigure(tuple(range(0,4)),weight=1)
window.rowconfigure(tuple(range(0,5)),weight=1)

label_title = tk.Label(window,text="คำนวณค่าไฟฟ้า",font=("Arial Bold",16))
label_title.grid(column=0,row=0,columnspan=4)

label_unit = tk.Label(window,text="หน่วยไฟฟ้า :")
label_unit.grid(column=0,row=1)
entry_unit = tk.Entry(window)
entry_unit.grid(column=1,row=1,columnspan=3,sticky="EW",padx=(0,10))

# Checkbutton สำหรับเลือกคิด VAT
vat_var = tk.BooleanVar()
check_vat = tk.Checkbutton(window,text="คิด VAT 7%",variable=vat_var)
check_vat.grid(column=0,row=2,columnspan=2)

btn_calc = tk.Button(window,text="คำนวณ",width=10,bg="orange",command=button_click)
btn_calc.grid(column=2,row=2)
btn_clear = tk.Button(window,text="ล้างค่า",width=8,command=clear_all)
btn_clear.grid(column=3,row=2)

label_result = tk.Label(window,text="ผลลัพธ์",borderwidth=1,relief="solid",font=("Arial",12))
label_result.grid(column=0,row=3,columnspan=4,rowspan=2,sticky="NSEW",padx=10,pady=10)

window.mainloop()
