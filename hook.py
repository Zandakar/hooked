#https://stackoverflow.com/questions/67505554/python-keyboard-module-add-hotkey-is-not-working-after-you-lock-windows-once-he

import keyboard
import mouse
import time
from threading import Timer


import PySimpleGUI as sg


layout = [[sg.Text("Tom's super cool keyboard hook")], [sg.Button("Close")]]

# Create the window
window = sg.Window("Hooked", layout,size=(290, 300))



def onPressE():
    keyboard.send('enter')
    print('ctrl E')

def onCapsQ():
    keyboard.send('backspace')
    print('ctrl Q')

def onCapsW():
    keyboard.send('up')
    print('ctrl W')

def onCapsA():
    keyboard.send('left')
    print('ctrl A')

def onCapsS():
    keyboard.send('down')
    print('ctrl S')

def onCapsD():
    keyboard.send('right')
    print('ctrl D')

def onCapsC():
    keyboard.send('windows + ctrl + left')
    print('ctrl C')

def onCapsV():
    keyboard.send('windows + ctrl + right')
    print('ctrl V')

def suppressInput():
    # Stub to capture caps lock without fully blocking it
    # We can listen to shift caps this way
    print('Caps')

def onShiftCaps():
    keyboard.send('caps lock')
    print('Caps')

hasClickedRecently = False

def setHasClickedTimerFalse():
    global hasClickedRecently
    hasClickedRecently = False



t = Timer(1.0, setHasClickedTimerFalse)
def onCtrlR():
    global hasClickedRecently
    if (hasClickedRecently == False):
        hasClickedRecently = True
        mouse.double_click()
    else:
        hasClickedRecently = False
        mouse.click()

capsLockCombos = ['', 'w + d', 'w + e', 's + d', 's + w', 'a + d' ]

for otherKeys in capsLockCombos:
    fullKeyCombo = 'caps lock'
    if otherKeys != '':
        fullKeyCombo = fullKeyCombo + ' + ' + otherKeys
    keyboard.add_hotkey(fullKeyCombo, suppressInput, suppress=True)

# list of combinations of keys that should be supressed
# keyboard.add_hotkey('caps lock', suppressInput, suppress=True)
# keyboard.add_hotkey('caps lock + w + d', suppressInput, suppress=True)
# keyboard.add_hotkey('caps lock + w + e', suppressInput, suppress=True)
# keyboard.add_hotkey('caps lock + s + d', suppressInput, suppress=True)
# keyboard.add_hotkey('caps lock + s + w', suppressInput, suppress=True)
# keyboard.add_hotkey('caps lock + a + d', suppressInput, suppress=True)


keyboard.add_hotkey('caps lock + shift', onShiftCaps, suppress=True)
keyboard.add_hotkey('caps lock + e', onPressE, suppress=True)
keyboard.add_hotkey('caps lock + q', onCapsQ, suppress=True)
keyboard.add_hotkey('caps lock + w', onCapsW, suppress=True)
keyboard.add_hotkey('caps lock + a', onCapsA, suppress=True)
keyboard.add_hotkey('caps lock + s', onCapsS, suppress=True)
keyboard.add_hotkey('caps lock + d', onCapsD, suppress=True)
keyboard.add_hotkey('caps lock + c', onCapsC, suppress=True)
keyboard.add_hotkey('caps lock + v', onCapsV, suppress=True)

keyboard.add_hotkey('ctrl + r', onCtrlR, suppress=True)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Close" or event == sg.WIN_CLOSED:
        break

window.close()









