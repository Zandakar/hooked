import keyboard

# https://github.com/boppreh/keyboard

def onPress(e):
    print('onPress ' + e)

def onCapsLock(e):
    print('caps')

# keyboard.on_press_key('caps lock', onPress, suppress=True)
# keyboard.on_press(onPress)
keyboard.block_key('caps lock')
keyboard.add_hotkey('caps lock + e', onPress, args=['ctrl + e was pressed'], suppress=True, trigger_on_release=True)
while True:
    import time
    time.sleep(1000)

eEEEeeeeEEEEeeWWWQWEEEEDD