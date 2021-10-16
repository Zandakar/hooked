import keyboard

# https://github.com/boppreh/keyboard
# https://github.com/boppreh/keyboard/blob/master/keyboard/_winkeyboard.py

def onRelease(e):
    print("Released: " + e.name)

def onPress(e):
    print('captured caps lock')

keyboard.on_press_key('caps lock', onPress, suppress=True)
keyboard.on_press(onPress)
keyboard.on_release(onRelease)

while True:
    import time
    time.sleep(1000)
