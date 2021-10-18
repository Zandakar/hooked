import keyboard

# https://github.com/boppreh/keyboard

def onPress(e):
    print('onPress ' + e.name)

# keyboard.on_press_key('caps lock', onPress, suppress=True)
# keyboard.on_press(onPress)
keyboard.add_hotkey('caps lock + e', print, args=['ctrl + e was pressed'])
while True:
    import time
    time.sleep(1000)
