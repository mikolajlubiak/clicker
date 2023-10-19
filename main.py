import ctypes
import time
import psutil

app_name = 'app.exe'

VK_1 = 0x31
VK_2 = 0x32

MOUSE_LEFTDOWN = 0x0002
MOUSE_LEFTUP = 0x0004
MOUSE_RIGHTDOWN = 0x0008
MOUSE_RIGHTUP = 0x0010

user32 = ctypes.windll.user32

def is_app_running(app_name):
    for process in psutil.process_iter(attrs=['name']):
        if process.info['name'] == app_name:
            return True
    return False

def send_mouse_input(x, y, mouse_event):
    extra = ctypes.c_ulong(0)
    ii_ = ctypes.c_ulong(0)

    struct_input = ctypes.Structure(
        [("type", ctypes.c_ulong), ("ii", ctypes.c_ulong)]

    )
    x = int(x * (65536 / ctypes.windll.user32.GetSystemMetrics(0)) + 1)
    y = int(y * (65536 / ctypes.windll.user32.GetSystemMetrics(1)) + 1)

    struct_input.type = 0x0000
    struct_input.ii = (
        (x & 0xFFFF) | ((y & 0xFFFF) << 16) | mouse_event
    )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(struct_input), ctypes.sizeof(struct_input))

while True:
    if is_app_running(app_name):
        if ctypes.windll.user32.GetKeyState(VK_1) < 0:
            send_mouse_input(115, 297, MOUSE_LEFTDOWN | MOUSE_LEFTUP)
            time.sleep(0.1)
        elif ctypes.windll.user32.GetKeyState(VK_2) < 0:
            send_mouse_input(1183, 123, MOUSE_RIGHTDOWN | MOUSE_RIGHTUP)
            time.sleep(0.1)
