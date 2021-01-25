import tkinter as tk

def translate():
    text_new = text.get().upper()
    text_translated = ""
    for character in text_new:
        text_translated += MORSE[character] + ' '
    text_box.delete('1.0', tk.END)
    text_box.insert(tk.END, text_translated) 


MORSE = {'A': '.-',    'B': '-...',  'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.', ' ': ' ' 
        }

root = tk.Tk()
root.geometry('400x300')
title = "Tranlate text to Morse"
tk.Label(root, bg='red', font=('times', 20), text=title).grid(row=0, column=0)
text = tk.StringVar()
tk.Entry(root, textvariable=text, font=('times', 20)).grid(row=1, column=0)
text_box = tk.Text(root, bg='yellow', height = 5, width = 52)
text_box.grid(row=2, column=0) 
text_box.insert(tk.END, 'Your translated text hrer...') 
tk.Button(root, text="Translate", font=('times', 20), command=translate).grid(row=4, column=0)

root.mainloop()