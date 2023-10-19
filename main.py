from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode
import psutil

app_name = 'metin2.exe'

mouse = Controller()

keys = ((KeyCode.from_char('1'), (115, 297), Button.left), (KeyCode.from_char('2'), (1183, 123), Button.right))

def is_app_running(app_name):
    for process in psutil.process_iter(attrs=['name']):
        if process.info['name'] == app_name:
            return True
    return False

def on_key_press(key):
    for i in range(len(keys)):
        if key == keys[i][0]:
            if is_app_running(app_name):
                mouse.position = keys[i][1]
                mouse.click(keys[i][2], 1)

with Listener(on_press=on_key_press) as listener:
    listener.join()
