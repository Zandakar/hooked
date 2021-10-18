import keyboard

# https://github.com/boppreh/keyboard

def onPress(e):
    print('onPress ' + e.name)

# keyboard.on_press_key('caps lock', onPress, suppress=True)
keyboard.on_press(onPress)

while True:
    import time
    time.sleep(1000)
w