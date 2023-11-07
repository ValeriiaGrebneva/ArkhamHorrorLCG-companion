import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw, ImageFont
from class_bag import bag
from PIL import Image, ImageDraw, ImageOps
from tkinter import filedialog
from tkinter.filedialog import askopenfile

window = tk.Tk()
window.geometry("390x670")
window.title('Arkham Horror 0.3')

initial_bag = [["+1",3], [0,4], [-1,5], [-2,4], [-3,3], [-4,2], [-5,2],
[-6,1], [-7,1], [-8,1], ["Auto-fail",1], ["Elder-Sign",1], ["Elder Thing",4],
["Tablet",4], ["Cultist",4], ["Skull",4], ["Bless",10], ["Curse",10],
["Frost",8]]
max_bag = [3,4,5,4,3,2,2,1,1,1,1,1,4,4,4,4,10,10,8]

window['bg'] = '#e4e2bb'

s=ttk.Style()
s.theme_use('clam')
s.configure("TCombobox", fieldbackground= "#cdb094", background= "#cdb094")

current_bag = bag()

def get_var_1(event):
    value = cb1_var.get()
    cb2_var.set(options[value][0])
    cb2.config(values=options[value])

def get_info():
    if cb1_var.get() == 'NIGHT OF THE ZEALOT':
        if cb2_var.get() == 'Easy':
            current_bag.NIGHT_OF_THE_ZEALOT_easy()
        if cb2_var.get() == 'Standart':
            current_bag.NIGHT_OF_THE_ZEALOT_standart()
        if cb2_var.get() == 'Hard':
            current_bag.NIGHT_OF_THE_ZEALOT_hard()
        if cb2_var.get() == 'Expert':
            current_bag.NIGHT_OF_THE_ZEALOT_expert()
            
    if cb1_var.get() == 'THE DUNWICH LEGACY':
        if cb2_var.get() == 'Easy':
            current_bag.THE_DUNWICH_LEGACY_easy()
        if cb2_var.get() == 'Standart':
            current_bag.THE_DUNWICH_LEGACY_standart()
        if cb2_var.get() == 'Hard':
            current_bag.THE_DUNWICH_LEGACY_hard()
        if cb2_var.get() == 'Expert':
            current_bag.THE_DUNWICH_LEGACY_expert()

    if cb1_var.get() == 'THE PATH TO CARCOSA':
        if cb2_var.get() == 'Easy':
            current_bag.THE_PATH_TO_CARCOSA_easy()
        if cb2_var.get() == 'Standart':
            current_bag.THE_PATH_TO_CARCOSA_standart()
        if cb2_var.get() == 'Hard':
            current_bag.THE_PATH_TO_CARCOSA_hard()
        if cb2_var.get() == 'Expert':
            current_bag.THE_PATH_TO_CARCOSA_expert()

    if cb1_var.get() == 'THE FORGOTTEN AGE':
        if cb2_var.get() == 'Easy':
            current_bag.THE_FORGOTTEN_AGE_easy()
        if cb2_var.get() == 'Standart':
            current_bag.THE_FORGOTTEN_AGE_standart()
        if cb2_var.get() == 'Hard':
            current_bag.THE_FORGOTTEN_AGE_hard()
        if cb2_var.get() == 'Expert':
            current_bag.THE_FORGOTTEN_AGE_expert()

    if cb1_var.get() == 'THE CIRCLE UNDONE':
        if cb2_var.get() == 'Easy':
            current_bag.THE_CIRCLE_UNDONE_easy()
        if cb2_var.get() == 'Standart':
            current_bag.THE_CIRCLE_UNDONE_standart()
        if cb2_var.get() == 'Hard':
            current_bag.THE_CIRCLE_UNDONE_hard()
        if cb2_var.get() == 'Expert':
            current_bag.THE_CIRCLE_UNDONE_expert()

    if cb1_var.get() == 'THE DREAM-EATERS A':
        if cb2_var.get() == 'Easy':
            current_bag.THE_DREAM_EATERS_A_easy()
        if cb2_var.get() == 'Standart':
            current_bag.THE_DREAM_EATERS_A_standart()
        if cb2_var.get() == 'Hard':
            current_bag.THE_DREAM_EATERS_A_hard()
        if cb2_var.get() == 'Expert':
            current_bag.THE_DREAM_EATERS_A_expert()

    if cb1_var.get() == 'THE DREAM-EATERS B':
        if cb2_var.get() == 'Easy':
            current_bag.THE_DREAM_EATERS_B_easy()
        if cb2_var.get() == 'Standart':
            current_bag.THE_DREAM_EATERS_B_standart()
        if cb2_var.get() == 'Hard':
            current_bag.THE_DREAM_EATERS_B_hard()
        if cb2_var.get() == 'Expert':
            current_bag.THE_DREAM_EATERS_B_expert()

    if cb1_var.get() == 'THE INNSMOUTH CONSPIRACY':
        if cb2_var.get() == 'Easy':
            current_bag.THE_INNSMOUTH_CONSPIRACY_easy()
        if cb2_var.get() == 'Standart':
            current_bag.THE_INNSMOUTH_CONSPIRACY_standart()
        if cb2_var.get() == 'Hard':
            current_bag.THE_INNSMOUTH_CONSPIRACY_hard()
        if cb2_var.get() == 'Expert':
            current_bag.THE_INNSMOUTH_CONSPIRACY_expert()

    if cb1_var.get() == 'EDGE OF THE EARTH':
        if cb2_var.get() == 'Easy':
            current_bag.EDGE_OF_THE_EARTH_easy()
        if cb2_var.get() == 'Standart':
            current_bag.EDGE_OF_THE_EARTH_standart()
        if cb2_var.get() == 'Hard':
            current_bag.EDGE_OF_THE_EARTH_hard()
        if cb2_var.get() == 'Expert':
            current_bag.EDGE_OF_THE_EARTH_expert()

    if cb1_var.get() == 'THE SCARLET KEYS':
        if cb2_var.get() == 'Easy':
            current_bag.THE_SCARLET_KEYS_easy()
        if cb2_var.get() == 'Standart':
            current_bag.THE_SCARLET_KEYS_standart()
        if cb2_var.get() == 'Hard':
            current_bag.THE_SCARLET_KEYS_hard()
        if cb2_var.get() == 'Expert':
            current_bag.THE_SCARLET_KEYS_expert()
            
    for i in range(0,19):
        quantity[i].config(text=current_bag.content[i])

add = tk.Label(window, text= "Choose your scenario:",width = 20,
               fg='#660000', bg = '#e4e2bb')
add.grid(row=2,column=0)

options = {'NIGHT OF THE ZEALOT': ['Easy', 'Standart', 'Hard', 'Expert'],
           'THE DUNWICH LEGACY': ['Easy', 'Standart', 'Hard', 'Expert'],
           'THE PATH TO CARCOSA': ['Easy', 'Standart', 'Hard', 'Expert'],
           'THE FORGOTTEN AGE': ['Easy', 'Standart', 'Hard', 'Expert'],
           'THE CIRCLE UNDONE': ['Easy', 'Standart', 'Hard', 'Expert'],
           'THE DREAM-EATERS A': ['Easy', 'Standart', 'Hard', 'Expert'],
           'THE DREAM-EATERS B': ['Easy', 'Standart', 'Hard', 'Expert'],
           'THE INNSMOUTH CONSPIRACY': ['Easy', 'Standart', 'Hard', 'Expert'],
           'EDGE OF THE EARTH': ['Easy', 'Standart', 'Hard', 'Expert'],
           'THE SCARLET KEYS': ['Easy', 'Standart', 'Hard', 'Expert']}

cb_frame1 = tk.Frame(window)
cb_frame1.grid(row=3,column=0)

cb1_values = list(options.keys())
cb1_var = tk.StringVar()
cb1_var.set(cb1_values[0])
cb1 = ttk.Combobox(cb_frame1, values=list(options.keys()), textvariable=cb1_var,
                   width = 30, justify='center')
cb1.grid()
cb1.bind('<<ComboboxSelected>>', get_var_1)

cb_frame2 = tk.Frame(window)
cb_frame2.grid(row=4,column=0)

cb2_var = tk.StringVar()
cb2_var.set(options[cb1_values[0]][0])
cb2 = ttk.Combobox(cb_frame2, values=options[cb1_values[0]],
                   textvariable=cb2_var, width = 30, justify='center')
cb2.grid()

btn_frame = tk.Frame(window)
btn_frame.grid()
tk.Button(btn_frame, text='Confirm',
          command=get_info,bg = '#a28566').grid(row=2,column=0)

welcome = tk.Label(window, text= "Random Token:", width = 15,
                   fg='#660000', bg = '#e4e2bb')
welcome.grid(row=9,column=0)
r_token = tk.Label(window, text= "-", width = 15, bg='#cdb094')
r_token.grid(row=10,column=0)



add = tk.Label(window, text= "Tokens",wraplength=300, width = 10,
               fg='#660000', bg = '#e4e2bb')
add.grid(row=0,column=2)
remove = tk.Label(window, text= "Quantity", wraplength=300,
                  fg='#660000', bg = '#e4e2bb')
remove.grid(row=0,column=3)

def choose_token():
    random_token = current_bag.random()
    r_token.config(text=random_token)
    if random_token == '-':
        label_1.grid_forget()
        return

    label_1.grid(row=14, column = 0,rowspan=5)
    path = str(random_token)+".png"
    image2 = Image.open(path)
    resized_image= image2.resize((110,110))
    img2 = ImageTk.PhotoImage(resized_image)
    label_1.configure(image=img2)
    label_1.image = img2

butn_frame = tk.Frame(window)
butn_frame.grid()
tk.Button(butn_frame, text='Choose another token',
          command=choose_token, bg = '#a28566').grid(row=11,column=0)

top = tk.Frame(window)
top.grid()

quantity = list()
for i in range(0,19):
    quantity.append(0)
    quantity[i] = tk.Label(window, text='0', bg = '#e4e2bb')
    quantity[i].grid(row=i+1,column=3)
    
def plus(i):
    if current_bag.content[i] + 1 > max_bag[i]:
        return
    current_bag.content[i] += 1
    quantity[i].config(text=current_bag.content[i])
    current_bag.quantity += 1

def minus(i):
    if current_bag.content[i] == 0:
        return
    current_bag.content[i] -= 1
    quantity[i].config(text=current_bag.content[i])
    current_bag.quantity -= 1

p = list()
m = list()
for i in range(0,19):
    p.append(0)
    m.append(0)

p[0] = tk.Button(window, text="+", command=lambda:plus(0), bg = '#a28566') 
m[0] = tk.Button(window, text="-", command=lambda:minus(0), bg = '#a28566')
p[1] = tk.Button(window, text="+", command=lambda:plus(1), bg = '#a28566') 
m[1] = tk.Button(window, text="-", command=lambda:minus(1), bg = '#a28566')
p[2] = tk.Button(window, text="+", command=lambda:plus(2), bg = '#a28566') 
m[2] = tk.Button(window, text="-", command=lambda:minus(2), bg = '#a28566')
p[3] = tk.Button(window, text="+", command=lambda:plus(3), bg = '#a28566') 
m[3] = tk.Button(window, text="-", command=lambda:minus(3), bg = '#a28566')
p[4] = tk.Button(window, text="+", command=lambda:plus(4), bg = '#a28566') 
m[4] = tk.Button(window, text="-", command=lambda:minus(4), bg = '#a28566')
p[5] = tk.Button(window, text="+", command=lambda:plus(5), bg = '#a28566') 
m[5] = tk.Button(window, text="-", command=lambda:minus(5), bg = '#a28566')
p[6] = tk.Button(window, text="+", command=lambda:plus(6), bg = '#a28566') 
m[6] = tk.Button(window, text="-", command=lambda:minus(6), bg = '#a28566')
p[7] = tk.Button(window, text="+", command=lambda:plus(7), bg = '#a28566') 
m[7] = tk.Button(window, text="-", command=lambda:minus(7), bg = '#a28566')
p[8] = tk.Button(window, text="+", command=lambda:plus(8), bg = '#a28566') 
m[8] = tk.Button(window, text="-", command=lambda:minus(8), bg = '#a28566')
p[9] = tk.Button(window, text="+", command=lambda:plus(9), bg = '#a28566') 
m[9] = tk.Button(window, text="-", command=lambda:minus(9), bg = '#a28566')
p[10] = tk.Button(window, text="+", command=lambda:plus(10), bg = '#a28566') 
m[10] = tk.Button(window, text="-", command=lambda:minus(10), bg = '#a28566')
p[11] = tk.Button(window, text="+", command=lambda:plus(11), bg = '#a28566') 
m[11] = tk.Button(window, text="-", command=lambda:minus(11), bg = '#a28566')
p[12] = tk.Button(window, text="+", command=lambda:plus(12), bg = '#a28566') 
m[12] = tk.Button(window, text="-", command=lambda:minus(12), bg = '#a28566')
p[13] = tk.Button(window, text="+", command=lambda:plus(13), bg = '#a28566') 
m[13] = tk.Button(window, text="-", command=lambda:minus(13), bg = '#a28566')
p[14] = tk.Button(window, text="+", command=lambda:plus(14), bg = '#a28566') 
m[14] = tk.Button(window, text="-", command=lambda:minus(14), bg = '#a28566')
p[15] = tk.Button(window, text="+", command=lambda:plus(15), bg = '#a28566') 
m[15] = tk.Button(window, text="-", command=lambda:minus(15), bg = '#a28566')
p[16] = tk.Button(window, text="+", command=lambda:plus(16), bg = '#a28566') 
m[16] = tk.Button(window, text="-", command=lambda:minus(16), bg = '#a28566')
p[17] = tk.Button(window, text="+", command=lambda:plus(17), bg = '#a28566') 
m[17] = tk.Button(window, text="-", command=lambda:minus(17), bg = '#a28566')
p[18] = tk.Button(window, text="+", command=lambda:plus(18), bg = '#a28566') 
m[18] = tk.Button(window, text="-", command=lambda:minus(18), bg = '#a28566')

for i in range(0,19):
    p[i].grid(row=i+1,column=4)
    m[i].grid(row=i+1,column=5)

for i in range(19):
    token = tk.Label(window, text= initial_bag[i][0], width = 10,
                     bg = '#e4e2bb')
    token.grid(row=i+1,column=2)

def clear_all():
    for i in range(19):
        current_bag.content[i] = 0
        quantity[i].config(text='0')
    current_bag.quantity = 0

btn_frame = tk.Frame(window)
btn_frame.grid(row=22,column=2,columnspan=2)
tk.Button(btn_frame, text='Clear all',command=clear_all, bg = '#a28566').grid()

r23 = tk.Label(window, height=3, bg = '#e4e2bb')
r23.grid(column=0, row=23)

version = tk.Label(window, text='Version 1.0 by Valeriia Grebneva',
                   fg='#660000', bg = '#e4e2bb', wraplength = 100, pady = 15)
version.grid(row=25,column=0)

cover = Image.open("cream_cover.png")

resized_cover= cover.resize((125,125))
cvr = ImageTk.PhotoImage(resized_cover)

label_cover = tk.Label(image=cvr)
label_cover.image = cvr

label_cover.grid(row=14, column = 0,rowspan=5)

image1 = Image.open("1.png")

resized_image= image1.resize((100,100))
img1 = ImageTk.PhotoImage(resized_image)

label_1 = tk.Label(image=img1)
label_1.image = img1

label_1.grid(row=14, column = 0,rowspan=5)
label_1.grid_forget()

Download_frame = tk.Frame(window)
Download_frame.grid(row=22,column=2,columnspan=2)
tk.Button(Download_frame, text='Clear all',command=clear_all, bg = '#a28566').grid()

btn_frame = tk.Frame(window)
btn_frame.grid(row=22,column=2,columnspan=2)
tk.Button(btn_frame, text='Clear all',command=clear_all, bg = '#a28566').grid()


def upload_bag():
    text_file = filedialog.askopenfilename(initialdir="D:\Programs\Python-2023\Arkham_Horror_files",
                                           title="Open Text File",
                                           filetypes=(("Text Files", "*.txt"), ))
    file = open(text_file, 'r')
    i = 0
    current_bag.quantity = 0
    for line in file:
        if int(line) <= max_bag[i]:
            current_bag.content[i] = int(line)
        else:
            current_bag.content[i] = max_bag[i]
        quantity[i].config(text=current_bag.content[i])
        current_bag.quantity += current_bag.content[i]
        i += 1
    file.close()
 
btn_upload = tk.Button(window, text ='Upload Bag', command = lambda:upload_bag(),
                       bg = '#a28566')
btn_upload.grid(row=23,column=2,columnspan=2)


def save_bag():
    text_file = filedialog.askopenfilename(initialdir="D:\Programs\Python-2023\Arkham_Horror_files",
                                           title="Open Text File",
                                           filetypes=(("Text Files", "*.txt"), ))
    file = open(text_file, 'w')
    file.seek(0)
    for i in range(19):
        file.write(str(current_bag.content[i])+"\n")
    file.truncate()
    file.close()
 
btn_save = tk.Button(window, text ='Save Bag', command = lambda:save_bag(),
                     bg = '#a28566')
btn_save.grid(row=24,column=2,columnspan=2)



window.mainloop()
