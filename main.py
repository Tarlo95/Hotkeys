from pixelfeld import Pixelfeld
from pynput.mouse import Button, Controller, Listener
from win32api import GetSystemMetrics
import win32gui, win32ui, win32api, win32con

dc = win32gui.GetDC(0)
dcObj = win32ui.CreateDCFromHandle(dc)
hwnd = win32gui.WindowFromPoint((0,0))
monitor = (0, 0, GetSystemMetrics(0), GetSystemMetrics(1))

red = win32api.RGB(255, 0, 0) # Red

past_coordinates = monitor
while True:
    m = win32gui.GetCursorPos()

    rect = win32gui.CreateRoundRectRgn(*past_coordinates, 2 , 2)
    win32gui.RedrawWindow(hwnd, past_coordinates, rect, win32con.RDW_INVALIDATE)

    for x in range(10):
        win32gui.SetPixel(dc, m[0]+x, m[1], red)
        win32gui.SetPixel(dc, m[0]+x, m[1]+10, red)
        for y in range(10):
            win32gui.SetPixel(dc, m[0], m[1]+y, red)
            win32gui.SetPixel(dc, m[0]+10, m[1]+y, red)

    past_coordinates = (m[0]-20, m[1]-20, m[0]+20, m[1]+20)



"""
dc = win32gui.GetDC(0)
dcObj = win32ui.CreateDCFromHandle(dc)
hwnd = win32gui.WindowFromPoint((0,0))
monitor = (0, 0, GetSystemMetrics(0), GetSystemMetrics(1))

m = win32gui.GetCursorPos()

while True:
    Maus = win32gui.GetCursorPos()
    unterschiedx = Maus[0]-m[0]
    unterschiedy = Maus[1]- m[1]
    dcObj.DrawFocusRect((m[0], m[1], m[0]+unterschiedx, m[1]+unterschiedy))
    win32gui.InvalidateRect(hwnd, monitor, True) # Refresh the entire monitor
    """

"""
def on_move(x, y):
    
    print('Pointer moved to {0}'.format(
        (x, y)))
    

def on_click(x, y, button, pressed):
    print('{0} at {1} '.format(
        'Pressed' if pressed else 'Released',
        (x, y))+str(button))

def on_scroll(x, y, dx, dy):
    
    print('Scrolled {0}'.format(
        (x, y)))


# Collect events until released
with Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()

"""



