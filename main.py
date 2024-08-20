import pyautogui as pag
import tkinter as tk
import time as t
import playsound as ps

black_color , mint_color , num = "#262626" , '#3fcb98' , 0
_list = ["msg_box_image_blue.png",
         "msg_box_image_dark.png",
         "msg_box_image_light.png"]

root = tk.Tk()
root.title("ربات شاد") 
root.geometry("230x190")
root.resizable(False, False)
root.configure(bg=black_color)
root.iconbitmap(r"image/shad_icon.ico")

for test in range(3):    
    try:pag.click(f"image/{_list[num]}")
    except:
        num += 1

def msg_typer():
    information_of_msg = msg_info.get()
    number_of_msg = msg_num.get()
    print(information_of_msg)
    print(number_of_msg)
    for _ in range(int(number_of_msg)):
        
        pag.click(_list[num])
        pag.write(information_of_msg)
        pag.press('enter')    
        t.sleep(.6)
    
    ps.playsound("/audio/alarm.wav")
    
# -------------- #
label_1 = tk.Label(root, text=":پیام خود را وارد کنید" , bg=black_color , fg=mint_color)
label_1.pack(pady=5)

msg_info = tk.Entry(root, width=30 , bg=mint_color , fg=black_color)
msg_info.pack(pady=4)
# -------------- #
label_2 = tk.Label(root, text=":پیام شما به چه مقدار ارسال شود" , bg=black_color , fg=mint_color)
label_2.pack(pady=5)

msg_num = tk.Entry(root, width=30 , bg=mint_color , fg=black_color)
msg_num.pack(pady=4)
# -------------- #  
    
button = tk.Button(root, text="شروع", command=msg_typer, width=12 , bg=mint_color , fg=black_color)
button.pack(pady=10)

label = tk.Label(root, text="○ سازنده: آرمان جباری ○", bg=black_color , fg=mint_color)
label.pack(pady=2)
    
root.mainloop()