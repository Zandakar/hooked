# https://pynput.readthedocs.io/en/latest/keyboard.html

from pynput.keyboard import Key, Controller, Listener

keyboard = Controller()
# listener = Listener()


keyActionMap =  {
    'w': Key.up,
    'a': Key.left,
    'd': Key.right,
    's': Key.down
}

def on_press(key):
    try:
        print(key)
        if keyActionMap.get(key.char):
            keyboard.press(keyActionMap.get(key.char))

    except AttributeError:
        if key == Key.esc:
            exit()

# def on_release(key):
#     print('{0} released'.format(
#         key))
#     if key == keyboard.Key.esc:
#         # Stop listener
#         return False

# Collect events until released
with Listener(
        on_press=on_press,
        suppress=True) as listener:
    listener.join()




