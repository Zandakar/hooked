import keyboard

import time
import PySimpleGUI as sg

# hello_psg.py


layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]

# Create the window
window = sg.Window("Demo", layout)



def onPressE():
    keyboard.send('enter')
    print('ctrl E')

def onCapsQ():
    keyboard.press('backspace')
    print('ctrl Q')

def onCapsW():
    keyboard.press('up')
    print('ctrl W')

def onCapsA():
    keyboard.press('left')
    print('ctrl A')

def onCapsS():
    keyboard.press('down')
    print('ctrl S')

def onCapsD():
    keyboard.press('right')
    print('ctrl D')

def onCapsC():
    keyboard.send('windows + ctrl + left')
    print('ctrl C')

def onCapsV():
    keyboard.send('windows + ctrl + right')
    print('ctrl V')
  


keyboard.block_key('caps lock')
keyboard.add_hotkey('caps lock + e', onPressE, suppress=True)
keyboard.add_hotkey('caps lock + q', onCapsQ, suppress=True)
keyboard.add_hotkey('caps lock + w', onCapsW, suppress=True)
keyboard.add_hotkey('caps lock + a', onCapsA, suppress=True)
keyboard.add_hotkey('caps lock + s', onCapsS, suppress=True)
keyboard.add_hotkey('caps lock + d', onCapsD, suppress=True)
keyboard.add_hotkey('caps lock + c', onCapsC, suppress=True)
keyboard.add_hotkey('caps lock + v', onCapsV, suppress=True)


# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()




