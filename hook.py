#https://stackoverflow.com/questions/67505554/python-keyboard-module-add-hotkey-is-not-working-after-you-lock-windows-once-he

import keyboard
import mouse
from threading import Timer


import PySimpleGUI as sg


layout = [[sg.Text("Tom's super cool keyboard hook")], [sg.Button("Close")]]

# Create the window
window = sg.Window("Hooked", layout,size=(290, 300))

def suppressInput():
    print()

def onKeyPress(val):
    keyboard.press(val)
    print(val)

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

suppressCombos = ['', 'w + d', 'w + e', 's + d', 's + w', 'a + d' ]

for otherKeys in suppressCombos:
    fullKeyCombo = 'caps lock'
    if otherKeys != '':
        fullKeyCombo = fullKeyCombo + ' + ' + otherKeys
    keyboard.add_hotkey(fullKeyCombo, suppressInput, suppress=True)


combos = {
'e': 'enter',
'q': 'backspace',
'w': 'up',
'a': 'left', 
's':'down',
'd': 'right',
'c': 'windows + ctrl + left', 
'v': 'windows + ctrl + right',
'shift': 'caps lock',
}

for x in combos:
    withCaps = 'caps lock + ' + x 
    print("combox")
    print(combos[x])
    keyboard.add_hotkey(withCaps, lambda: keyboard.press(combos[x]), suppress=True)

# keyboard.add_hotkey('capslock + shift', onShiftCaps, suppress=True)
# keyboard.add_hotkey('capslock + e', onPressE, suppress=True)
# keyboard.add_hotkey('caps lock + q', onCapsQ, suppress=True)
# keyboard.add_hotkey('caps lock + w', onCapsW, suppress=True)
# keyboard.add_hotkey('caps lock + a', onCapsA, suppress=True)
# keyboard.add_hotkey('caps lock + s', onCapsS, suppress=True)
# keyboard.add_hotkey('caps lock + d', onCapsD, suppress=True)
# keyboard.add_hotkey('caps lock + c', onCapsC, suppress=True)
# keyboard.add_hotkey('caps lock + v', onCapsV, suppress=True)

keyboard.add_hotkey('ctrl + r', onCtrlR, suppress=True)


while True:
    event, values = window.read()

    if event == "Close" or event == sg.WIN_CLOSED:
        break

window.close()


